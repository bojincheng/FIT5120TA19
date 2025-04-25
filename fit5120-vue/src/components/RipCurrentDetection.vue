<template>
  <div class="container">
    <h1 class="rip-header">Rip Current Detection</h1>
    
    <div class="upload-container">
      <h2>Upload Image</h2>
      
      <div class="upload-methods">
        <div class="upload-method">
          <h3>Option 1: Upload File</h3>
          <div class="file-input">
            <input type="file" id="fileInput" ref="fileInput" @change="handleFileChange" accept="image/*">
            <label for="fileInput" class="btn">Select Image</label>
          </div>
        </div>
        
        <div class="upload-method">
          <h3>Option 2: Use Camera</h3>
          <button id="openCameraBtn" class="btn" @click="openCamera">Open Camera</button>
          <div class="camera-container" :class="{ active: isCameraActive }" id="cameraContainer">
            <video id="cameraFeed" ref="cameraFeed" autoplay playsinline></video>
            <button id="captureCameraBtn" class="btn" @click="captureImage">Capture</button>
            <button id="closeCameraBtn" class="btn" @click="closeCamera">Close Camera</button>
          </div>
        </div>
      </div>
      
      <div class="preview-container">
        <h3>Image Preview</h3>
        <div class="image-preview">
          <img id="imagePreview" ref="imagePreview" alt="Preview" :style="{ display: imagePreview ? 'block' : 'none' }">
        </div>
        <button id="processImageBtn" class="btn primary-btn" @click="processImage" :disabled="!imagePreview">Detect Rip Currents</button>
      </div>
    </div>
    
    <div class="results-container" id="resultsContainer" v-show="showResults">
      <h2>Detection Results</h2>
      
      <div class="results-content">
        <div class="result-image-container">
          <canvas id="resultCanvas" ref="resultCanvas"></canvas>
        </div>
      </div>

      <div class="disclaimer">
        <p>SAFETY NOTICE: This tool uses artificial intelligence to detect potential rip currents. 
           It may not detect all hazards and should not replace proper beach safety practices. 
           Always follow lifeguard instructions and local beach warnings.</p>
      </div>
    </div>

    <div class="loading-overlay" v-show="loading">
      <div class="loading-spinner"></div>
      <p>Processing image...</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "RipCurrentDetection",
  data() {
    return {
      isCameraActive: false,
      imagePreview: null,
      capturedImage: null,
      imageFile: null,
      stream: null,
      loading: false,
      showResults: false
    };
  },
  methods: {
    handleFileChange(e) {
      if (e.target.files && e.target.files[0]) {
        this.imageFile = e.target.files[0];
        const reader = new FileReader();
        
        reader.onload = (e) => {
          this.imagePreview = e.target.result;
          this.capturedImage = null;
        };
        
        reader.readAsDataURL(this.imageFile);
      }
    },
    
    async openCamera() {
      try {
        this.stream = await navigator.mediaDevices.getUserMedia({ 
          video: { 
            facingMode: { ideal: 'environment' },
            width: { ideal: 1280 },
            height: { ideal: 720 } 
          } 
        });
        this.$refs.cameraFeed.srcObject = this.stream;
        this.isCameraActive = true;
      } catch (err) {
        alert('Error accessing camera: ' + err.message);
        console.error('Error accessing camera:', err);
      }
    },
    
    closeCamera() {
      if (this.stream) {
        const tracks = this.stream.getTracks();
        tracks.forEach(track => track.stop());
        this.stream = null;
        this.isCameraActive = false;
      }
    },
    
    captureImage() {
      if (this.stream) {
        // Create a canvas element to capture the frame
        const canvas = document.createElement('canvas');
        const video = this.$refs.cameraFeed;
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        
        // Convert to data URL
        const imageDataUrl = canvas.toDataURL('image/jpeg', 0.9);
        
        // Update preview
        this.imagePreview = imageDataUrl;
        
        // Save captured image data
        this.capturedImage = imageDataUrl;
        this.imageFile = null;
        
        // Close camera
        this.closeCamera();
      }
    },
    
    async processImage() {
      this.loading = true;
      
      try {
        let response;
        
        if (this.imageFile) {
          // If using file upload
          const formData = new FormData();
          formData.append('image', this.imageFile);
          
          response = await axios.post('http://localhost:3000/process-image', formData);
        } else if (this.capturedImage) {
          // If using captured image from camera
          response = await axios.post('http://localhost:3000/process-camera-image', { 
            image: this.capturedImage 
          });
        } else {
          throw new Error('No image available for processing');
        }
        
        // Load the original image and display the detection
        this.loadAndDisplayDetection(response.data);
        
      } catch (error) {
        console.error('Error processing image:', error);
        alert('Error processing image: ' + error.message);
        this.loading = false;
      }
    },
    
    loadAndDisplayDetection(result) {
      const img = new Image();
      img.crossOrigin = "Anonymous";
      img.onload = () => {
        // Set canvas dimensions to match the image
        const resultCanvas = this.$refs.resultCanvas;
        resultCanvas.width = img.width;
        resultCanvas.height = img.height;
        
        // Draw the original image on the canvas
        const ctx = resultCanvas.getContext('2d');
        ctx.clearRect(0, 0, resultCanvas.width, resultCanvas.height);
        ctx.drawImage(img, 0, 0);
        
        // Get predictions and find the most confident one
        let predictions = [];
        if (result.rawResponse && result.rawResponse.predictions) {
          predictions = result.rawResponse.predictions;
        } else if (Array.isArray(result.predictions)) {
          predictions = result.predictions;
        }
        
        // Sort predictions by confidence and get the most confident one
        if (predictions.length > 0) {
          predictions.sort((a, b) => b.confidence - a.confidence);
          const bestPrediction = predictions[0];
          
          // Draw the bounding box for the most confident prediction
          this.drawDetection(ctx, bestPrediction);
        }
        
        // Show results container
        this.showResults = true;
        
        // Hide loading overlay
        this.loading = false;
        
        // Scroll to results
        this.$nextTick(() => {
          document.getElementById('resultsContainer').scrollIntoView({ behavior: 'smooth' });
        });
      };
      
      img.onerror = () => {
        console.error("Failed to load the image:", result.original);
        alert('Error loading the processed image. Please try again.');
        this.loading = false;
      };
      
      // Use the full path for the image
      img.src = `http://localhost:3000${result.original}`;
    },
    
    drawDetection(ctx, prediction) {
      // Extract coordinates
      const x = prediction.x;
      const y = prediction.y;
      const width = prediction.width;
      const height = prediction.height;
      
      // Calculate box coordinates (handle Roboflow's center point format)
      const boxX = x - width / 2;
      const boxY = y - height / 2;
      
      // Draw rectangle with a noticeable red color
      ctx.strokeStyle = 'rgba(255, 0, 0, 0.9)';  // Bright red
      ctx.lineWidth = 4;
      ctx.strokeRect(boxX, boxY, width, height);
      
      // Draw "RIP CURRENT" label without percentage
      ctx.fillStyle = 'rgba(255, 0, 0, 0.8)';
      ctx.fillRect(boxX, boxY - 25, 120, 25);
      
      ctx.fillStyle = 'white';
      ctx.font = 'bold 16px Arial';
      ctx.fillText("RIP CURRENT", boxX + 5, boxY - 5);
    }
  }
}
</script>

<style scoped>
.container {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f5f5f5;
  padding: 20px;
  max-width: 900px;
  margin: 0 auto;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  padding: 30px;
}

h1 {
  text-align: center;
  margin-bottom: 30px;
  color: #2c3e50;
}

h2 {
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 2px solid #eee;
  color: #2c3e50;
}

h3 {
  margin-bottom: 15px;
  color: #3498db;
}

.rip-header {
  font-family: 'Arial', sans-serif;
  text-align: center;
  font-size: 48px;
  padding: 10px;
  border-radius: 10px;
  color: #01579b;
}

.upload-methods {
  display: flex;
  flex-wrap: wrap;
  gap: 30px;
  margin-bottom: 30px;
}

.upload-method {
  flex: 1;
  min-width: 250px;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
}

.btn {
  display: inline-block;
  padding: 10px 15px;
  background-color: #3498db;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
  font-size: 16px;
}

.btn:hover {
  background-color: #2980b9;
}

.btn:disabled {
  background-color: #bdc3c7;
  cursor: not-allowed;
}

.primary-btn {
  background-color: #2ecc71;
  font-size: 18px;
  padding: 12px 20px;
  margin-top: 15px;
}

.primary-btn:hover {
  background-color: #27ae60;
}

.file-input input[type="file"] {
  width: 0.1px;
  height: 0.1px;
  opacity: 0;
  overflow: hidden;
  position: absolute;
  z-index: -1;
}

.file-input label {
  display: inline-block;
  cursor: pointer;
}

.camera-container {
  margin-top: 15px;
  display: none;
}

.camera-container.active {
  display: block;
}

video {
  width: 100%;
  border: 2px solid #ddd;
  border-radius: 8px;
  margin-bottom: 10px;
}

.image-preview {
  margin: 20px 0;
  text-align: center;
  min-height: 200px;
  border: 2px dashed #ddd;
  border-radius: 8px;
  padding: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.image-preview img {
  max-width: 100%;
  max-height: 300px;
}

.preview-container {
  text-align: center;
}

.results-container {
  margin-top: 40px;
}

.results-content {
  display: flex;
  justify-content: center;
  margin-bottom: 30px;
}

.result-image-container {
  width: 100%;
  max-width: 800px;
  text-align: center;
}

canvas {
  max-width: 100%;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.9);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.loading-spinner {
  width: 50px;
  height: 50px;
  border: 5px solid #f3f3f3;
  border-top: 5px solid #3498db;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 20px;
}

/* Disclaimer styling */
.disclaimer {
  background-color: #fcf8e3;
  border: 1px solid #faebcc;
  color: #8a6d3b;
  padding: 15px;
  border-radius: 8px;
  margin-top: 20px;
  text-align: center;
  font-size: 14px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@media (max-width: 768px) {
  .upload-methods {
    flex-direction: column;
  }
  
  .container {
    padding: 15px;
  }
}
</style>