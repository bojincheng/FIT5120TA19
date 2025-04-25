const express = require('express');
const multer = require('multer');
const fs = require('fs');
const path = require('path');
const cors = require('cors');
const axios = require('axios');

const app = express();
const port = 3000;

// Enable CORS
app.use(cors());

// Parse JSON body for API requests
app.use(express.json({limit: '50mb'}));
app.use(express.urlencoded({extended: true, limit: '50mb'}));

// Root endpoint
app.get('/', (req, res) => {
  res.send('Rip Current Detection API Server is running');
});

// Set up storage for uploaded files
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    const uploadDir = path.join(__dirname, './uploads');
    if (!fs.existsSync(uploadDir)) {
      fs.mkdirSync(uploadDir, { recursive: true });
    }
    cb(null, uploadDir);
  },
  filename: function (req, file, cb) {
    cb(null, Date.now() + '-' + file.originalname);
  }
});

const upload = multer({ storage: storage });

// API endpoint for processing uploaded image
app.post('/process-image', upload.single('image'), async (req, res) => {
  try {
    const imagePath = req.file.path;
    const imageBuffer = fs.readFileSync(imagePath);
    const imageBase64 = imageBuffer.toString('base64');
    
    console.log('Processing image:', path.basename(imagePath));
    console.log('Image size:', imageBuffer.length, 'bytes');
    
    // Call Roboflow API with ultra-low confidence threshold (5%)
    const response = await axios({
      method: "POST",
      url: "https://detect.roboflow.com/rip-currents/3",
      params: {
        api_key: "loM8Ah5tC5BPZbTZsVyR",
        confidence: 5,    // Extremely low threshold to catch all possible detections
        overlap: 50,      // Increased overlap threshold to allow more overlapping detections
        format: "json",   // Ensure we get JSON response
        stroke: 5         // Thicker stroke for visibility
      },
      data: imageBase64,
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      }
    });
    
    console.log('API Response structure:', JSON.stringify(response.data, null, 2));
    
    // Return both the raw API response and our processed version
    res.json({
      original: `/uploads/${path.basename(imagePath)}`,
      predictions: response.data.predictions || [],
      rawResponse: response.data  // Return the raw response for debugging
    });
  } catch (error) {
    console.error('Error processing image:', error.message);
    if (error.response) {
      console.error('API Response Error:', error.response.data);
      console.error('API Response Status:', error.response.status);
    }
    res.status(500).json({ error: error.message });
  }
});

// API endpoint for processing image from URL (using camera)
app.post('/process-camera-image', express.json({limit: '50mb'}), async (req, res) => {
  try {
    const imageDataUrl = req.body.image;
    
    if (!imageDataUrl || !imageDataUrl.startsWith('data:image')) {
      throw new Error('Invalid image data URL');
    }
    
    // Extract base64 image data from the data URL
    const base64Data = imageDataUrl.replace(/^data:image\/\w+;base64,/, '');
    
    // Save the image to a file for debugging
    const uploadDir = path.join(__dirname, './uploads');
    if (!fs.existsSync(uploadDir)) {
      fs.mkdirSync(uploadDir, { recursive: true });
    }
    
    const timestamp = Date.now();
    const imagePath = path.join(uploadDir, `${timestamp}-camera.jpg`);
    fs.writeFileSync(imagePath, Buffer.from(base64Data, 'base64'));
    
    console.log('Processing camera image, saved to:', path.basename(imagePath));
    
    // Call Roboflow API with ultra-low confidence threshold
    const response = await axios({
      method: "POST",
      url: "https://detect.roboflow.com/rip-currents/3",
      params: {
        api_key: "loM8Ah5tC5BPZbTZsVyR",
        confidence: 5,    // Extremely low threshold to catch all possible detections
        overlap: 50,      // Increased overlap threshold to allow more overlapping detections
        format: "json",   // Ensure we get JSON response
        stroke: 5         // Thicker stroke for visibility
      },
      data: base64Data,
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      }
    });
    
    console.log('API Response structure:', JSON.stringify(response.data, null, 2));
    
    // Return the results
    res.json({
      original: `/uploads/${path.basename(imagePath)}`,
      predictions: response.data.predictions || [],
      rawResponse: response.data
    });
  } catch (error) {
    console.error('Error processing camera image:', error.message);
    if (error.response) {
      console.error('API Response Error:', error.response.data);
    }
    res.status(500).json({ error: error.message });
  }
});

// Serve files from uploads directory
app.use('/uploads', express.static(path.join(__dirname, './uploads')));

// Create uploads directory if it doesn't exist
const uploadsDir = path.join(__dirname, './uploads');
if (!fs.existsSync(uploadsDir)) {
  fs.mkdirSync(uploadsDir, { recursive: true });
}

app.listen(port, () => {
  console.log(`Rip Current Detection server listening at http://localhost:${port}`);
});