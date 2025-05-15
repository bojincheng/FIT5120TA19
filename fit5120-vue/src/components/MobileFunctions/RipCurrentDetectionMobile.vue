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
            <button class="btn" @click="openCamera">Open Camera</button>
            <div class="camera-container" :class="{ active: isCameraActive }">
              <video ref="cameraFeed" autoplay playsinline></video>
              <button class="btn" @click="captureImage">Capture</button>
              <button class="btn" @click="closeCamera">Close Camera</button>
            </div>
          </div>
        </div>
        
        <!-- Add model settings section -->
        <div class="model-settings">
          <h3 @click="showSettings = !showSettings" class="settings-toggle">
            Model Settings <span>{{ showSettings ? '▼' : '►' }}</span>
          </h3>
          <div class="settings-panel" v-if="showSettings">
            <div class="model-info">
              <div class="metric">
                <span class="metric-label">mAP@50:</span>
                <span class="metric-value">{{ modelInfo.mAP }}%</span>
              </div>
              <div class="metric">
                <span class="metric-label">Precision:</span>
                <span class="metric-value">{{ modelInfo.precision }}%</span>
              </div>
              <div class="metric">
                <span class="metric-label">Recall:</span>
                <span class="metric-value">{{ modelInfo.recall }}%</span>
              </div>
            </div>
            
            <div class="setting-item">
              <label>Confidence Threshold: <span class="threshold-value">{{ modelSettings.confidenceThreshold }}%</span></label>
              <div class="range-control">
                <input type="range" v-model.number="modelSettings.confidenceThreshold" min="0" max="100" step="1">
                <div class="range-track">
                  <div class="range-fill" :style="{width: `${modelSettings.confidenceThreshold}%`}"></div>
                </div>
              </div>
              <div class="range-labels">
                <span>0%</span>
                <span>100%</span>
              </div>
            </div>
            
            <div class="setting-item">
              <label>Overlap Threshold: {{ modelSettings.overlapThreshold }}%</label>
              <input type="range" v-model="modelSettings.overlapThreshold" min="0" max="100" step="1">
              <div class="range-labels">
                <span>0%</span>
                <span>100%</span>
              </div>
            </div>
            
            <div class="setting-item">
              <label>Label Display Mode:</label>
              <div class="checkbox-group">
                <label>
                  <input type="checkbox" v-model="modelSettings.displayOptions.drawConfidence">
                  Draw Confidence
                </label>
                <label>
                  <input type="checkbox" v-model="modelSettings.displayOptions.drawLabels">
                  Draw Labels
                </label>
                <label>
                  <input type="checkbox" v-model="modelSettings.displayOptions.drawBoxes">
                  Draw Boxes
                </label>
                <label>
                  <input type="checkbox" v-model="modelSettings.displayOptions.censorPredictions">
                  Censor Predictions
                </label>
              </div>
            </div>
          </div>
        </div>
  
        <div class="preview-container" v-if="imagePreview" :key="imagePreview">
          <h3>Image Preview</h3>
          <div class="image-preview">
            <img :src="imagePreview" alt="Preview" />
          </div>
          <button class="btn primary-btn" @click="processImage">Detect Rip Currents</button>
        </div>
      </div>
  
      <div class="results-container" v-show="showResults">
        <h2>Detection Results</h2>
        <div class="results-content">
          <div class="detection-status" ref="detectionStatus"></div>
          <div class="result-image-container">
            <canvas ref="resultCanvas"></canvas>
          </div>
        </div>
        <div class="disclaimer">
          <p><strong>SAFETY NOTICE:</strong> This tool uses artificial intelligence to detect potential rip currents. It may not detect all hazards and should not replace proper beach safety practices. Always follow lifeguard instructions and local beach warnings.</p>
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
    name: "RipCurrentDetectionMobile",
    data() {
      return {
        isCameraActive: false,
        imagePreview: null,
        capturedImage: null,
        imageFile: null,
        stream: null,
        loading: false,
        showResults: false,
        // Store original predictions and processed image for threshold adjustments
        originalPredictions: [],
        processedImage: null,
        // Model settings
        modelSettings: {
          confidenceThreshold: 50,  // Default confidence threshold set to 50%
          overlapThreshold: 50,
          displayOptions: {
            drawConfidence: true,
            drawLabels: true,
            drawBoxes: true,
            censorPredictions: false
          }
        },
        modelInfo: {
          mAP: 92.0,
          precision: 91.0,
          recall: 87.8
        },
        showSettings: false
      };
    },
    watch: {
      // Watch for changes to the confidence threshold
      'modelSettings.confidenceThreshold': function(newThreshold) {
        // Only update if we have results to display
        if (this.showResults && this.originalPredictions.length > 0 && this.processedImage) {
          this.updateDetectionDisplay();
        }
      },
      // Watch for changes to the display options
      'modelSettings.displayOptions': {
        handler: function(newOptions) {
          if (this.showResults && this.originalPredictions.length > 0 && this.processedImage) {
            this.updateDetectionDisplay();
          }
        },
        deep: true
      }
    },
    methods: {
      handleFileChange(e) {
        if (e.target.files && e.target.files[0]) {
          this.imageFile = e.target.files[0];
          const reader = new FileReader();
          reader.onload = (e) => {
            this.imagePreview = e.target.result;
            this.capturedImage = null;
            this.showResults = false; // Hide previous result
          };
          reader.readAsDataURL(this.imageFile);
        }
      },
      async openCamera() {
        try {
          this.stream = await navigator.mediaDevices.getUserMedia({
            video: { facingMode: { ideal: 'environment' } }
          });
          this.$refs.cameraFeed.srcObject = this.stream;
          this.isCameraActive = true;
        } catch (err) {
          alert('Camera error: ' + err.message);
        }
      },
      closeCamera() {
        if (this.stream) {
          this.stream.getTracks().forEach(track => track.stop());
          this.stream = null;
          this.isCameraActive = false;
        }
      },
      captureImage() {
        if (this.stream) {
          const canvas = document.createElement('canvas');
          const video = this.$refs.cameraFeed;
          canvas.width = video.videoWidth;
          canvas.height = video.videoHeight;
          const ctx = canvas.getContext('2d');
          ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
          this.imagePreview = canvas.toDataURL('image/jpeg', 0.9);
          this.capturedImage = this.imagePreview;
          this.imageFile = null;
          this.showResults = false; // Hide previous result
          this.closeCamera();
        }
      },
      async processImage() {
        this.loading = true;
        try {
          let response;
          if (this.imageFile) {
            const formData = new FormData();
            formData.append('image', this.imageFile);
            
            // Pass the threshold settings to the backend API
            const config = {
              params: {
                confidence: this.modelSettings.confidenceThreshold / 100,
                overlap: this.modelSettings.overlapThreshold / 100
              }
            };
            
            response = await axios.post('https://fit5120ta19.onrender.com/process-image', formData, config);
          } else if (this.capturedImage) {
            response = await axios.post('https://fit5120ta19.onrender.com/process-camera-image', {
              image: this.capturedImage
            }, {
              params: {
                confidence: this.modelSettings.confidenceThreshold / 100,
                overlap: this.modelSettings.overlapThreshold / 100
              }
            });
          } else {
            throw new Error('No image to process');
          }
  
          this.loadAndDisplayDetection(response.data);
        } catch (error) {
          console.error('Processing error:', error);
          alert('Processing error: ' + (error.response?.data?.message || error.message));
          this.loading = false;
        }
      },
      loadAndDisplayDetection(result) {
        const predictions = result.rawResponse?.predictions || result.predictions || [];
        
        // Store the original predictions for threshold adjustments
        this.originalPredictions = predictions;
        
        const img = new Image();
        img.crossOrigin = "Anonymous";
        
        img.onload = () => {
          // Store the processed image for reuse when threshold changes
          this.processedImage = img;
          
          // Update the detection display with current settings
          this.updateDetectionDisplay();
          
          this.showResults = true;
          this.loading = false;
          this.$nextTick(() => {
            document.querySelector('.results-container').scrollIntoView({ behavior: 'smooth' });
          });
        };
  
        img.onerror = () => {
          alert('Image failed to load');
          this.loading = false;
        };
  
        img.src = `https://fit5120ta19.onrender.com${result.original}`;
      },
      
      updateDetectionDisplay() {
        if (!this.processedImage || !this.$refs.resultCanvas) return;
        
        const canvas = this.$refs.resultCanvas;
        const ctx = canvas.getContext('2d');
        
        // Set canvas dimensions if not already set
        if (canvas.width !== this.processedImage.width) {
          canvas.width = this.processedImage.width;
          canvas.height = this.processedImage.height;
        }
        
        // Clear and redraw the original image
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(this.processedImage, 0, 0);

        // Filter predictions based on current confidence threshold
        const filteredPredictions = this.originalPredictions.filter(
          pred => pred.confidence >= (this.modelSettings.confidenceThreshold / 100)
        );
        
        // Update the detection status text
        const detectionStatus = this.$refs.detectionStatus;
        
        // Draw all predictions that meet the threshold
        if (filteredPredictions.length > 0) {
          // Show danger message
          const detectionCount = filteredPredictions.length;
          detectionStatus.innerHTML = `
            <div class="danger-alert">
              <i class="alert-icon">⚠️</i>
              <span><strong>${detectionCount} RIP CURRENT${detectionCount > 1 ? 'S' : ''} DETECTED!</strong> Use caution and avoid this area.</span>
            </div>
          `;
          detectionStatus.className = "detection-status danger";
          
          filteredPredictions.forEach(prediction => {
            this.drawDetection(ctx, prediction);
          });
        } else {
          // Show safe message
          detectionStatus.innerHTML = `
            <div class="safe-alert">
              <i class="alert-icon">✓</i>
              <span><strong>NO RIP CURRENTS DETECTED</strong> in this image.</span>
            </div>
          `;
          detectionStatus.className = "detection-status safe";
          
          // No rip currents detected - show message on canvas
          this.drawNoDetectionMessage(ctx, canvas.width, canvas.height);
        }
      },
      
      drawDetection(ctx, prediction) {
        // Roboflow format: x, y are the center, width and height are dimensions
        // Convert to top-left coordinate for drawing
        const x = prediction.x - prediction.width / 2;
        const y = prediction.y - prediction.height / 2;
        const width = prediction.width;
        const height = prediction.height;
  
        // Draw bounding box if enabled
        if (this.modelSettings.displayOptions.drawBoxes) {
          ctx.strokeStyle = 'rgba(255, 0, 0, 0.9)';
          ctx.lineWidth = 4;
          ctx.strokeRect(x, y, width, height);
        }
  
        // Draw label background and text if enabled
        if (this.modelSettings.displayOptions.drawLabels) {
          ctx.fillStyle = 'rgba(255, 0, 0, 0.8)';
          ctx.fillRect(x, y - 25, 120, 25);
          ctx.fillStyle = 'white';
          ctx.font = 'bold 16px Arial';
          ctx.fillText("RIP CURRENT", x + 5, y - 5);
        }
  
        // Draw confidence if enabled
        if (this.modelSettings.displayOptions.drawConfidence) {
          const confidence = Math.round(prediction.confidence * 100);
          const confidenceText = `${confidence}%`;
          
          if (!this.modelSettings.displayOptions.drawLabels) {
            // If we're not drawing labels, draw confidence directly above the box
            ctx.fillStyle = 'rgba(255, 0, 0, 0.8)';
            ctx.fillRect(x, y - 25, 60, 25);
          }
          
          ctx.fillStyle = 'white';
          ctx.font = 'bold 14px Arial';
          
          if (this.modelSettings.displayOptions.drawLabels) {
            // If drawing labels, put confidence after the label
            ctx.fillText(confidenceText, x + 90, y - 5);
          } else {
            // Otherwise put it at the top of the box
            ctx.fillText(confidenceText, x + 5, y - 5);
          }
        }
        
        // Apply censoring if enabled
        if (this.modelSettings.displayOptions.censorPredictions) {
          // Apply pixelation/blur effect to the detected area
          const pixelSize = 15;  // Size of the pixelation effect
          
          // Get the image data for the detection area
          const imageData = ctx.getImageData(x, y, width, height);
          const data = imageData.data;
          
          // Apply pixelation effect
          for (let cy = 0; cy < height; cy += pixelSize) {
            for (let cx = 0; cx < width; cx += pixelSize) {
              // Get the color of the first pixel in this block
              const pixelIndex = (cy * width + cx) * 4;
              const r = data[pixelIndex];
              const g = data[pixelIndex + 1];
              const b = data[pixelIndex + 2];
              
              // Apply this color to all pixels in the block
              for (let py = 0; py < pixelSize && cy + py < height; py++) {
                for (let px = 0; px < pixelSize && cx + px < width; px++) {
                  const index = ((cy + py) * width + (cx + px)) * 4;
                  data[index] = r;
                  data[index + 1] = g;
                  data[index + 2] = b;
                }
              }
            }
          }
          
          // Put the pixelated image data back
          ctx.putImageData(imageData, x, y);
        }
      },
      
      drawNoDetectionMessage(ctx, width, height) {
        // Add a semi-transparent overlay with a "No Rip Currents Detected" message
        
        // Add a semi-transparent banner across the image
        const bannerHeight = 60;
        const y = (height / 2) - (bannerHeight / 2);
        
        // Green background banner
        ctx.fillStyle = 'rgba(0, 150, 0, 0.7)';  // Green background with some transparency
        ctx.fillRect(0, y, width, bannerHeight);
        
        // White text
        ctx.fillStyle = 'white';
        ctx.font = 'bold 24px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText('NO RIP CURRENTS DETECTED', width / 2, y + (bannerHeight / 2));
        
        // Add a checkmark or safety symbol
        const safetyCircleRadius = 30;
        const circleX = 60;
        const circleY = y + (bannerHeight / 2);
        
        // White circle
        ctx.beginPath();
        ctx.arc(circleX, circleY, safetyCircleRadius, 0, 2 * Math.PI);
        ctx.fillStyle = 'white';
        ctx.fill();
        
        // Green checkmark inside the circle
        ctx.beginPath();
        ctx.moveTo(circleX - 15, circleY);
        ctx.lineTo(circleX - 5, circleY + 10);
        ctx.lineTo(circleX + 15, circleY - 10);
        ctx.lineWidth = 4;
        ctx.strokeStyle = '#00aa00';
        ctx.stroke();
      }
    }
  }
  </script>
  
  <style scoped>
  .container {
    font-family: Arial, sans-serif;
    padding: 30px;
    max-width: 900px;
    margin: 0 auto;
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(0,0,0,0.1);
  }
  .rip-header {
    text-align: center;
    font-size: 48px;
    color: #01579b;
  }
  .upload-methods {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
  }
  .upload-method {
    flex: 1;
    min-width: 250px;
    padding: 20px;
    background: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0,0,0,0.05);
  }
  .btn {
    padding: 10px 15px;
    background: #3498db;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  .btn:hover {
    background: #2980b9;
  }
  .primary-btn {
    background: #2ecc71;
    font-size: 18px;
    margin-top: 15px;
  }
  .primary-btn:hover {
    background: #27ae60;
  }
  .file-input input[type="file"] {
    opacity: 0;
    position: absolute;
    z-index: -1;
  }
  .file-input label {
    cursor: pointer;
  }
  .camera-container {
    margin-top: 10px;
    display: none;
  }
  .camera-container.active {
    display: block;
  }
  video {
    width: 100%;
    border: 2px solid #ccc;
    border-radius: 8px;
  }
  .image-preview {
    text-align: center;
    border: 2px dashed #ccc;
    padding: 15px;
    border-radius: 8px;
    margin-top: 20px;
  }
  .image-preview img {
    max-width: 100%;
    max-height: 300px;
  }
  .results-container {
    margin-top: 40px;
  }
  .result-image-container {
    text-align: center;
  }
  canvas {
    max-width: 100%;
    border: 1px solid #ccc;
    border-radius: 8px;
  }
  .loading-overlay {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: rgba(255,255,255,0.9);
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
  @keyframes spin {
    to { transform: rotate(360deg); }
  }
  .disclaimer {
    background: #fcf8e3;
    border: 1px solid #fbeed5;
    padding: 15px;
    border-radius: 5px;
    font-size: 14px;
    color: #8a6d3b;
  }
  
  /* Model Settings Styles */
  .model-settings {
    margin-top: 20px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    overflow: hidden;
  }
  
  .settings-toggle {
    background: #f5f5f5;
    padding: 10px 15px;
    margin: 0;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 18px;
  }
  
  .settings-panel {
    padding: 15px;
    background: #fafafa;
  }
  
  .model-info {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
    background: #f0f8ff;
    padding: 10px;
    border-radius: 5px;
  }
  
  .metric {
    text-align: center;
  }
  
  .metric-label {
    font-size: 14px;
    color: #666;
    display: block;
  }
  
  .metric-value {
    font-size: 18px;
    font-weight: bold;
    color: #01579b;
  }
  
  .setting-item {
    margin-bottom: 15px;
  }
  
  .setting-item label {
    display: block;
    margin-bottom: 5px;
  }
  
  .setting-item input[type="range"] {
    width: 100%;
  }
  
  .range-labels {
    display: flex;
    justify-content: space-between;
    margin-top: 5px;
    font-size: 12px;
    color: #666;
  }
  
  .checkbox-group {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
  }
  
  .checkbox-group label {
    display: flex;
    align-items: center;
    margin-bottom: 0;
  }
  
  .checkbox-group input[type="checkbox"] {
    margin-right: 5px;
  }
  
  /* Detection Status Styles */
  .detection-status {
    margin-bottom: 20px;
    padding: 15px;
    border-radius: 5px;
    text-align: center;
    font-size: 18px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .detection-status.danger {
    background-color: #ffebee;
    border: 2px solid #f44336;
    color: #c62828;
  }
  
  .detection-status.safe {
    background-color: #e8f5e9;
    border: 2px solid #4caf50;
    color: #2e7d32;
  }
  
  .alert-icon {
    font-size: 24px;
    margin-right: 10px;
  }
  
  .danger-alert, .safe-alert {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  /* Advanced Range Slider Styles */
  .threshold-value {
    font-weight: bold;
    color: #01579b;
    transition: color 0.3s ease;
  }
  
  .range-control {
    position: relative;
    height: 30px;
  }
  
  .range-track {
    position: absolute;
    top: 50%;
    left: 0;
    width: 100%;
    height: 6px;
    background: #e0e0e0;
    border-radius: 3px;
    transform: translateY(-50%);
    pointer-events: none;
  }
  
  .range-fill {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    background: linear-gradient(to right, #4caf50, #ffc107, #f44336);
    border-radius: 3px;
    pointer-events: none;
    transition: width 0.2s ease;
  }
  
  input[type="range"] {
    -webkit-appearance: none;
    width: 100%;
    height: 30px;
    background: transparent;
    position: relative;
    z-index: 2;
    cursor: pointer;
  }
  
  input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 20px;
    height: 20px;
    background: #2196f3;
    border-radius: 50%;
    cursor: pointer;
    border: 2px solid white;
    box-shadow: 0 0 5px rgba(0,0,0,0.3);
  }
  
  input[type="range"]::-moz-range-thumb {
    width: 20px;
    height: 20px;
    background: #2196f3;
    border-radius: 50%;
    cursor: pointer;
    border: 2px solid white;
    box-shadow: 0 0 5px rgba(0,0,0,0.3);
  }
  </style>
  