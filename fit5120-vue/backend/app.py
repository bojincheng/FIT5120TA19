import requests 
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import time
import base64
from werkzeug.utils import secure_filename
import psycopg2
from dotenv import load_dotenv
import os
import openmeteo_requests
import requests_cache
from retry_requests import retry
import pandas as pd
import imghdr
# Load environment variables from .env file
load_dotenv()
app = Flask(__name__)
# Enable the cross original resource sharing
CORS(app)

# Epic 1 backend function
# Call the database connection function in database.py
try:
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    cursor = conn.cursor()
    print("Database connection established.")
except Exception as e:
    print("Error connecting to the database:", e)
   
# Drowning Death Search 
@app.route('/DrowningDeathSearch', methods=['GET'])
def search_deaths():
    """Query the drowning_deaths table based on filters (age, location)."""
    try:
        conn.rollback()
        age_group = request.args.get('age_group', '').strip()
        location = request.args.get('location', '').strip()
        print(f"Received request - Age Group: {age_group}, Location: {location}")
        # Map age groups to correct database column names
        age_column_map = {
            "0-4": ("age_0_4_deaths", "age_0_4_rate"),
            "5-14": ("age_5_14_deaths", "age_5_14_rate"),
            "15-24": ("age_15_24_deaths", "age_15_24_rate"),
            "25-44": ("age_25_44_deaths", "age_25_44_rate"),
            "45-64": ("age_45_64_deaths", "age_45_64_rate"),
            "65+": ("age_65_plus_deaths", "age_65_plus_rate"),
        }
        # If a specific age group is selected, get deaths and rate
        if age_group:
            age_column, rate_column = age_column_map.get(age_group, ("total_deaths", "total_rate"))
        else:
            # If "All" is selected, sum deaths and calculate a weighted average for the rate
            age_column = ("age_0_4_deaths + age_5_14_deaths + age_15_24_deaths + "
                          "age_25_44_deaths + age_45_64_deaths + age_65_plus_deaths AS deaths")

            rate_column = ("(age_0_4_deaths * age_0_4_rate + age_5_14_deaths * age_5_14_rate + "
                           "age_15_24_deaths * age_15_24_rate + age_25_44_deaths * age_25_44_rate + "
                           "age_45_64_deaths * age_45_64_rate + age_65_plus_deaths * age_65_plus_rate) / "
                           "(age_0_4_deaths + age_5_14_deaths + age_15_24_deaths + "
                           "age_25_44_deaths + age_45_64_deaths + age_65_plus_deaths) AS rate")
        # Build SQL query
        query = f"""
            SELECT location, {age_column}, {rate_column}
            FROM drowning_deaths
            WHERE 1=1
        """
        params = []
        # Handle location filtering
        if location and location != "Total":
            query += " AND location = %s"
            params.append(location)
        # Print final query for debugging
        print("🔍 Final SQL Query:")
        print(cursor.mogrify(query, tuple(params)).decode())  # Show formatted query
        # Execute query
        cursor.execute(query, tuple(params))
        results = cursor.fetchall()
        conn.commit()
        print(f"✅ Query executed successfully. Found {len(results)} results.")
        # Return results as JSON
        return jsonify([
            {
                "location": row[0],
                "age_group": age_group if age_group else "All",
                "deaths": row[1],
                # Multiply rate by 100 and convert to integer, then ensure it's a whole number without decimals
                "rate": str(int(row[2] * 100)) if row[2] is not None else "N/A"  # Multiply by 100, then convert to string to avoid decimals
            }
            for row in results
        ])
    except psycopg2.Error as e:
        conn.rollback()
        print("⚠️ SQL Error:", e)
        return jsonify({"error": "Database query error", "message": str(e)}), 500
    except Exception as e:
        print("❌ General Error:", e)
        return jsonify({"error": "An unexpected error occurred", "message": str(e)}), 500

# Drowning Injury Search
@app.route('/DrowningInjurySearch', methods=['GET'])
def search_injury():
    """Query the drowning_injury table based on filters (age, location)."""
    try:
        # Rollback any failed transactions
        conn.rollback()
        # Fetch request parameters
        age_group = request.args.get('age_group', '').strip()
        location = request.args.get('location', '').strip()
        print(f"Received request - Age Group: {age_group}, Location: {location}")
        # Map age groups to the correct column names
        age_column_map = {
            "0-4": "age_0_4_cases",
            "5-14": "age_5_14_cases",
            "15-24": "age_15_24_cases",
            "25-44": "age_25_44_cases",
            "45-64": "age_45_64_cases",
            "65+": "age_65_plus_cases"
        }
        # Default to total cases if no specific age group is selected
        age_column = age_column_map.get(age_group, 'total_cases')
        # Build SQL query
        query = f"SELECT location, {age_column} as cases FROM drowning_injury WHERE 1=1"
        params = []
        # Handle location filtering (with case-insensitive matching)
        if location and location != "All Locations":
            query += " AND location ILIKE %s"
            params.append(f"%{location}%")  # Ensure partial matching with LIKE
        print(f"Executing SQL Query: {query}")
        print(f"Parameters: {params}")
        # Execute the query
        cursor.execute(query, tuple(params))
        results = cursor.fetchall()
        conn.commit()
        # If no results are found
        if not results:
            return jsonify({"message": "No injury data found based on your selection. Try adjusting the filters."}), 404
        print(f"Query executed successfully. Found {len(results)} results.")
        # Return results in JSON format (only location and cases)
        return jsonify([
            {"location": row[0], "age_group": age_group if age_group else "All", "cases": row[1]}
            for row in results
        ])
    except psycopg2.Error as e:
        conn.rollback()
        print("SQL Error:", e)
        return jsonify({"error": "Database query error", "message": str(e)}), 500
    except Exception as e:
        print("❌ General Error:", e)
        return jsonify({"error": "An unexpected error occurred", "message": str(e)}), 500

# Epic 2 Search Beach Infomation
# Open-Meteo set-up
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# Marine api
@app.route("/marine", methods=["GET"])
def get_marine_data():
    latitude = request.args.get("latitude", type=float)
    longitude = request.args.get("longitude", type=float)
    if latitude is None or longitude is None:
        return jsonify({"error": "Missing latitude or longitude"}), 400
    try:
        url = "https://marine-api.open-meteo.com/v1/marine"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": [
                "wave_height",
                "swell_wave_height",
                "ocean_current_velocity",
                "sea_surface_temperature",
                "sea_level_height_msl"
            ]
        }
        responses = openmeteo.weather_api(url, params=params)
        response = responses[0]
        current = response.Current()
        result = {
            "latitude": response.Latitude(),
            "longitude": response.Longitude(),
            "elevation": response.Elevation(),
            "timezone": response.Timezone(),
            "utc_offset_seconds": response.UtcOffsetSeconds(),
            "current_time": current.Time(),
            "wave_height": current.Variables(0).Value(),
            "swell_wave_height": current.Variables(1).Value(),
            "ocean_current_velocity": current.Variables(2).Value(),
            "sea_surface_temperature": current.Variables(3).Value(),
            "sea_level_height_msl": current.Variables(4).Value()
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Weather Api    
@app.route("/weather", methods=["GET"])
def get_weather_data():
    latitude = request.args.get("latitude", type=float)
    longitude = request.args.get("longitude", type=float)
    if latitude is None or longitude is None:
        return jsonify({"error": "Missing latitude or longitude"}), 400
    try:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "daily": "uv_index_max",
            "current": [
                "pressure_msl",
                "weather_code",
                "temperature_2m",
                "wind_speed_10m"
            ]
        }
        responses = openmeteo.weather_api(url, params=params)
        response = responses[0]
        current = response.Current()
        current_data = {
            "time": current.Time(),
            "pressure_msl": float(current.Variables(0).Value()),
            "weather_code": int(current.Variables(1).Value()),
            "temperature_2m": float(current.Variables(2).Value()),
            "wind_speed_10m": float(current.Variables(3).Value())
        }
        daily = response.Daily()
        uv_index_max = daily.Variables(0).ValuesAsNumpy()
        time_range = pd.date_range(
            start=pd.to_datetime(daily.Time(), unit="s", utc=True),
            end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=daily.Interval()),
            inclusive="left"
        )
        uv_list = []
        for t, val in zip(time_range, uv_index_max):
            uv_list.append({
                "date": t.strftime("%Y-%m-%d"),
                "uv_index_max": float(val)
            })
        return jsonify({
            "latitude": response.Latitude(),
            "longitude": response.Longitude(),
            "elevation": response.Elevation(),
            "timezone": response.Timezone(),
            "utc_offset_seconds": response.UtcOffsetSeconds(),
            "current": current_data,
            "daily_uv_index_max": uv_list
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Epic 7 Rip Current Detection
# Set up config for file uploads
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # Max upload size 50 MB
# Ensure uploads directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
# Helper function to check allowed extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# Content check
def is_valid_image(file_stream):
    file_stream.seek(0)
    file_type = imghdr.what(None, file_stream.read())
    file_stream.seek(0)
    return file_type in ALLOWED_IMGHDR_TYPES
# Process image upload
@app.route('/process-image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename) and is_valid_image(file.stream):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        # Read the image as base64
        with open(file_path, 'rb') as f:
            image_base64 = base64.b64encode(f.read()).decode('utf-8')
        try:
            # Retrieve the API key from environment variables
            api_key = os.getenv('ROBOFLOW_API_KEY')
            
            # Get confidence and overlap parameters from request or use defaults
            confidence = request.args.get('confidence', '0.5')
            overlap = request.args.get('overlap', '0.5')
            
            # Convert string to float if needed
            confidence = float(confidence) if isinstance(confidence, str) else confidence
            overlap = float(overlap) if isinstance(overlap, str) else overlap
            
            # Ensure minimum confidence threshold for API call
            confidence = max(confidence, 0.01)  # Ensure minimum 1% confidence
            
            # Call the Roboflow API with the uploaded image
            response = requests.post(
                'https://detect.roboflow.com/rip-currents/3',
                params={
                    'api_key': api_key,
                    'confidence': confidence,
                    'overlap': overlap,
                    'format': 'json',
                    'stroke': 5
                },
                data=image_base64,
                headers={"Content-Type": "application/x-www-form-urlencoded"}
            )
            if response.status_code == 200:
                return jsonify({
                    'original': f'/uploads/{filename}',
                    'predictions': response.json().get('predictions', []),
                    'rawResponse': response.json()
                })
            else:
                return jsonify({'error': 'Error from Roboflow API', 'details': response.text}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid file type'}), 400

# Process image from camera using URL
@app.route('/process-camera-image', methods=['POST'])
def process_camera_image():
    data = request.get_json()
    if 'image' not in data:
        return jsonify({'error': 'No image data URL provided'}), 400
    image_data_url = data['image']
    if not image_data_url.startswith('data:image'):
        return jsonify({'error': 'Invalid image data URL'}), 400
    # Extract base64 image data
    base64_data = image_data_url.replace('data:image/jpeg;base64,', '').replace('data:image/png;base64,', '')
    # Save the image to a file
    timestamp = str(int(time.time()))
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], f'{timestamp}-camera.jpg')
    with open(file_path, 'wb') as f:
        f.write(base64.b64decode(base64_data))
    try:
        # Retrieve the API key from environment variables
        api_key = os.getenv('ROBOFLOW_API_KEY')
        
        # Get confidence and overlap parameters from request or use defaults
        confidence = request.args.get('confidence', '0.5')
        overlap = request.args.get('overlap', '0.5')
        
        # Convert string to float if needed
        confidence = float(confidence) if isinstance(confidence, str) else confidence
        overlap = float(overlap) if isinstance(overlap, str) else overlap
        
        # Ensure minimum confidence threshold for API call
        confidence = max(confidence, 0.01)  # Ensure minimum 1% confidence
        
        # Call the Roboflow API with the camera image data
        response = requests.post(
            'https://detect.roboflow.com/rip-currents/3',
            params={
                'api_key': api_key,
                'confidence': confidence,
                'overlap': overlap,
                'format': 'json',
                'stroke': 5
            },
            data=base64_data,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        if response.status_code == 200:
            return jsonify({
                'original': f'/uploads/{timestamp}-camera.jpg',
                'predictions': response.json().get('predictions', []),
                'rawResponse': response.json()
            })
        else:
            return jsonify({'error': 'Error from Roboflow API', 'details': response.text}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
# Serve uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
        
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port, debug=True)