import os
import psycopg2
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
def get_db_connection():
    # Get database credentials from environment variables
    dbname = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    # Add host as environment variable
    host = os.getenv('DB_HOST')
    # Default port for PostgreSQL
    port = os.getenv('DB_PORT', 5432) 
    # Set connection using psycopg2
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    return connection