<template>
  <div class="container">
    <h1 class="rip-header">Rip Current Detection</h1>

    <div class="upload-container">
      <h2>Upload Image</h2>

      <div class="upload-methods">
        <!-- Upload from file -->
        <div class="upload-method">
          <h3>Option 1: Upload File</h3>
          <div class="file-input">
            <input type="file" id="fileInput" ref="fileInput" @change="handleFileChange" accept="image/*" />
            <label for="fileInput" class="btn">Select Image</label>
          </div>
        </div>

        <!-- Capture from camera -->
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

      <!-- Image Preview Section -->
<div class="preview-container" v-if="!processedPreview && (imagePreview || capturedImage)">
  <h3>Image Preview</h3>
  <div class="image-preview">
    <img :src="imagePreview" alt="Preview" />
  </div>
  <button
    class="btn primary-btn"
    @click="processImage"
  >
    Detect Rip Currents
  </button>
</div>
</div>

    <!-- Detection Results -->
    <div class="results-container" v-show="showResults">
      <h2>Detection Results</h2>
      <div class="results-content">
        <div class="result-image-container" v-if="processedPreview">
          <img :src="processedPreview" alt="Detection Result" />
        </div>
        <p v-if="noRipMessage" class="no-rip-msg">{{ noRipMessage }}</p>
      </div>

      <div class="disclaimer">
        <p>
          <strong>SAFETY NOTICE:</strong>
          This tool uses artificial intelligence to detect potential rip currents.
          It may not detect all hazards and should not replace proper beach safety practices.
          Always follow lifeguard instructions and local beach warnings.
        </p>
      </div>
    </div>

    <!-- Loading overlay -->
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
      imagePreview: null,
      processedPreview: null,
      isCameraActive: false,
      capturedImage: null,
      imageFile: null,
      stream: null,
      loading: false,
      showResults: false,
      noRipMessage: ''
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
          this.processedPreview = null;
          this.showResults = false;
          this.noRipMessage = '';
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
        this.showResults = false;
        this.noRipMessage = '';
        this.processedPreview = null;
        this.closeCamera();
      }
    },
    async processImage() {
      this.loading = true;
      this.noRipMessage = '';
      try {
        let response;
        if (this.imageFile) {
          const formData = new FormData();
          formData.append('image', this.imageFile);
          response = await axios.post('https://fit5120ta19.onrender.com/process-image', formData);
        } else if (this.capturedImage) {
          response = await axios.post('https://fit5120ta19.onrender.com/process-camera-image', {
            image: this.capturedImage
          });
        } else {
          throw new Error('No image to process');
        }

        this.loadAndDisplayDetection(response.data);
      } catch (error) {
        alert('Processing error: ' + error.message);
        this.loading = false;
      }
    },
    loadAndDisplayDetection(result) {
      const img = new Image();
      img.crossOrigin = "Anonymous";

      img.onload = () => {
        const predictions = result.rawResponse?.predictions || result.predictions || [];

        // Scale and draw to preview canvas
        const MAX_WIDTH = 600;
        const scale = Math.min(1, MAX_WIDTH / img.width);

        const previewCanvas = document.createElement('canvas');
        previewCanvas.width = img.width * scale;
        previewCanvas.height = img.height * scale;

        const ctx = previewCanvas.getContext('2d');
        ctx.drawImage(img, 0, 0, previewCanvas.width, previewCanvas.height);

        if (predictions.length > 0) {
          const best = predictions[0];
          const scaleX = previewCanvas.width / img.width;
          const scaleY = previewCanvas.height / img.height;

          const x = (best.x - best.width / 2) * scaleX;
          const y = (best.y - best.height / 2) * scaleY;
          const width = best.width * scaleX;
          const height = best.height * scaleY;

          ctx.strokeStyle = 'rgba(255, 0, 0, 0.9)';
          ctx.lineWidth = 4;
          ctx.strokeRect(x, y, width, height);

          ctx.fillStyle = 'rgba(255, 0, 0, 0.8)';
          ctx.fillRect(x, y - 25, 120, 25);
          ctx.fillStyle = 'white';
          ctx.font = 'bold 16px Arial';
          ctx.fillText("RIP CURRENT", x + 5, y - 5);

          this.noRipMessage = '';
        } else {
          this.noRipMessage = 'No rip current detected.';
        }

        this.processedPreview = previewCanvas.toDataURL('image/jpeg', 0.8);
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
    }
  }
};
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
  max-height: 320px;
  overflow: auto;
}
.image-preview img {
  max-width: 100%;
  height: auto;
  display: block;
  margin: auto;
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
.no-rip-msg {
  color: #b00020;
  font-weight: bold;
  margin-top: 1rem;
}
</style>
