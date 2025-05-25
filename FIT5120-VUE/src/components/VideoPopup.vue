<template>
  <transition name="fade">
  <div v-if="show" class="video-popup-overlay" @click.self="closePopup">
    <div class="video-popup">
      <div class="video-popup-header">
          <h3>{{ displayTitle }}</h3>
          <button class="close-button" @click="closePopup" aria-label="Close">
            <span class="close-icon"></span>
          </button>
      </div>
      <div class="video-container">
          <div class="video-frame">
            <video ref="videoPlayer" controls autoplay @timeupdate="handleTimeUpdate">
          <source :src="videoSrc" type="video/mp4">
          Your browser does not support the video tag.
        </video>
            
            <!-- Annotation overlay -->
            <div class="annotation-overlay" v-if="showAnnotations">
              <transition-group name="annotation-fade">
                <div 
                  v-for="annotation in activeAnnotations" 
                  :key="annotation.id"
                  class="annotation-marker"
                  :style="{ 
                    left: `${annotation.position.x}%`, 
                    top: `${annotation.position.y}%` 
                  }"
                >
                  <div class="annotation-point"></div>
                  <div class="annotation-content" :class="annotation.position.align">
                    <div class="annotation-title">{{ annotation.title }}</div>
                    <div class="annotation-text">{{ annotation.text }}</div>
                  </div>
                </div>
              </transition-group>
            </div>
            
            <!-- Annotation controls -->
            <div class="annotation-controls" v-if="hasAnnotations">
              <button 
                class="annotation-toggle" 
                @click="toggleAnnotations"
                :class="{ active: showAnnotations }"
              >
                <span class="toggle-icon"></span>
                <span class="toggle-text">{{ showAnnotations ? 'Hide Annotations' : 'Show Annotations' }}</span>
              </button>
            </div>
          </div>
        </div>
        <div class="video-popup-footer">
          <span class="sls-tag">Surf Life Saving</span>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'VideoPopup',
  props: {
    show: {
      type: Boolean,
      default: false
    },
    videoSrc: {
      type: String,
      required: true
    },
    title: {
      type: String,
      default: 'Video'
    }
  },
  data() {
    return {
      currentTime: 0,
      showAnnotations: true,
      // Define annotations with timestamps, positions and content
      annotations: [
        {
          id: 1,
          startTime: 3, // in seconds
          endTime: 10,
          position: { x: 70, y: 30, align: 'right' },
          title: 'Deeper Channel',
          text: 'Notice the darker water - this indicates a deeper channel where rip currents form'
        },
        {
          id: 2,
          startTime: 8,
          endTime: 15,
          position: { x: 25, y: 45, align: 'left' },
          title: 'Calm Water Surface',
          text: 'Deceptively calm water between breaking waves is often a sign of a rip current'
        },
        {
          id: 3,
          startTime: 14,
          endTime: 22,
          position: { x: 60, y: 60, align: 'bottom' },
          title: 'Water Direction',
          text: 'Water flows away from shore through the rip channel'
        },
        {
          id: 4,
          startTime: 20,
          endTime: 30,
          position: { x: 40, y: 25, align: 'top' },
          title: 'Foam Pattern',
          text: 'Notice how foam and debris move seaward in the rip current'
        }
      ]
    };
  },
  computed: {
    displayTitle() {
      // Replace specific title for rip currents video with the new title
      if (this.videoSrc.includes('how_rips_form.mp4')) {
        return 'How Rips Can Look in Real Life';
      }
      return this.title;
    },
    // Returns true if the current video has annotations available
    hasAnnotations() {
      return this.videoSrc.includes('how_rips_form.mp4');
    },
    // Filter annotations to only show those active at the current time
    activeAnnotations() {
      if (!this.showAnnotations) return [];
      return this.annotations.filter(
        annotation => this.currentTime >= annotation.startTime && this.currentTime <= annotation.endTime
      );
    }
  },
  watch: {
    show(newVal) {
      // Control page scrolling when popup is open/closed
      if (newVal) {
        document.body.style.overflow = 'hidden';
        document.body.classList.add('video-popup-open');
        // Reset time tracking when opening
        this.currentTime = 0;
      } else {
        document.body.style.overflow = '';
        document.body.classList.remove('video-popup-open');
      }
    }
  },
  methods: {
    closePopup() {
      this.$emit('close');
    },
    handleTimeUpdate(event) {
      this.currentTime = event.target.currentTime;
    },
    toggleAnnotations() {
      this.showAnnotations = !this.showAnnotations;
    }
  }
}
</script>

<style scoped>
/* Fade transition with improved timings */
.fade-enter-active {
  transition: opacity 0.4s cubic-bezier(0.19, 1, 0.22, 1);
}
.fade-leave-active {
  transition: opacity 0.3s cubic-bezier(0.55, 0.055, 0.675, 0.19);
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

/* Annotation fade transition */
.annotation-fade-enter-active, .annotation-fade-leave-active {
  transition: all 0.5s cubic-bezier(0.19, 1, 0.22, 1);
}
.annotation-fade-enter, .annotation-fade-leave-to {
  opacity: 0;
  transform: scale(0.85);
}

/* Video popup styles */
.video-popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.85);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  backdrop-filter: blur(15px);
  -webkit-backdrop-filter: blur(15px);
}

.video-popup {
  width: 95%;
  max-width: 1300px;
  background-color: rgba(17, 17, 17, 0.95);
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 
    0 30px 60px rgba(0, 0, 0, 0.5), 
    0 0 0 1px rgba(255, 255, 255, 0.1),
    0 0 30px rgba(1, 79, 134, 0.3); /* Subtle blue glow */
  animation: popupIntro 0.7s cubic-bezier(0.16, 1, 0.3, 1);
  transform-origin: center;
  border: 1px solid rgba(255, 255, 255, 0.08);
}

@keyframes popupIntro {
  0% {
    opacity: 0;
    transform: scale(0.85);
  }
  40% {
    opacity: 1;
    transform: scale(1.03);
  }
  70% {
    transform: scale(0.99);
  }
  100% {
    transform: scale(1);
  }
}

.video-popup-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 22px 28px;
  background: linear-gradient(135deg, #013a63, #2a6f97);
  color: white;
  position: relative;
  overflow: hidden;
}

.video-popup-header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: 
    linear-gradient(90deg, 
      rgba(255, 255, 255, 0) 0%, 
      rgba(255, 255, 255, 0.1) 50%, 
      rgba(255, 255, 255, 0) 100%);
  transform: translateX(-100%);
  animation: headerShine 4s infinite ease-in-out;
}

@keyframes headerShine {
  0%, 100% {
    transform: translateX(-100%);
  }
  50% {
    transform: translateX(100%);
  }
}

.video-popup-header h3 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 600;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
  letter-spacing: 0.01em;
  display: flex;
  align-items: center;
}

.close-button {
  background: rgba(255, 255, 255, 0.1);
  border: none;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  position: relative;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.close-icon {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 16px;
  height: 16px;
}

.close-icon::before, 
.close-icon::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: white;
  border-radius: 1px;
}

.close-icon::before {
  transform: rotate(45deg);
}

.close-icon::after {
  transform: rotate(-45deg);
}

.close-button:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: scale(1.1);
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.3);
}

.video-container {
  width: 100%;
  padding: 28px;
  background-color: rgba(0, 0, 0, 0.6);
  position: relative;
}

.video-frame {
  width: 100%;
  height: 0;
  padding-bottom: 56.25%; /* 16:9 aspect ratio */
  position: relative;
  border-radius: 6px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.05);
}

.video-frame video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: contain;
  background-color: black;
}

/* Annotation Styles */
.annotation-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 10;
}

.annotation-marker {
  position: absolute;
  transform: translate(-50%, -50%);
  z-index: 15;
}

.annotation-point {
  width: 18px;
  height: 18px;
  background-color: rgba(231, 111, 81, 0.9);
  border-radius: 50%;
  box-shadow: 0 0 0 3px rgba(231, 111, 81, 0.3), 0 0 10px rgba(0, 0, 0, 0.5);
  animation: pulse 2s infinite;
  position: relative;
  z-index: 2;
}

@keyframes pulse {
  0% {
    transform: scale(1);
    box-shadow: 0 0 0 0 rgba(231, 111, 81, 0.7);
  }
  70% {
    transform: scale(1.1);
    box-shadow: 0 0 0 6px rgba(231, 111, 81, 0);
  }
  100% {
    transform: scale(1);
    box-shadow: 0 0 0 0 rgba(231, 111, 81, 0);
  }
}

.annotation-content {
  position: absolute;
  width: 240px;
  background-color: rgba(17, 17, 17, 0.9);
  border-radius: 8px;
  padding: 12px 16px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(231, 111, 81, 0.5);
  color: #fff;
  font-size: 14px;
  line-height: 1.4;
  z-index: 1;
  backdrop-filter: blur(4px);
  pointer-events: auto;
}

.annotation-content.right {
  left: 20px;
  transform: translateY(-50%);
}

.annotation-content.left {
  right: 20px;
  transform: translateY(-50%);
}

.annotation-content.top {
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
}

.annotation-content.bottom {
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
}

.annotation-title {
  font-weight: 700;
  font-size: 16px;
  margin-bottom: 6px;
  color: #e76f51;
}

.annotation-text {
  font-weight: 400;
  font-size: 15px;
  color: rgba(255, 255, 255, 0.9);
}

/* Annotation Controls */
.annotation-controls {
  position: absolute;
  top: 15px;
  right: 15px;
  z-index: 20;
}

.annotation-toggle {
  background-color: rgba(1, 79, 134, 0.85);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 30px;
  color: white;
  padding: 8px 16px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
}

.annotation-toggle:hover {
  background-color: rgba(1, 79, 134, 0.95);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
}

.annotation-toggle.active {
  background-color: rgba(231, 111, 81, 0.85);
}

.toggle-icon {
  width: 16px;
  height: 16px;
  background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-5-9h10v2H7z"/></svg>');
  background-repeat: no-repeat;
  background-position: center;
}

.annotation-toggle.active .toggle-icon {
  background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-5-9h4V7h2v4h4v2h-4v4h-2v-4H7z"/></svg>');
  transform: rotate(45deg);
}

/* Enhanced responsive styling */
@media (max-width: 1024px) {
  .video-popup {
    width: 96%;
    max-width: 95vw;
  }
  
  .video-popup-header {
    padding: 18px 24px;
  }
  
  .video-popup-header h3 {
    font-size: 1.3rem;
  }
  
  .video-container {
    padding: 20px;
  }
  
  .annotation-content {
    width: 220px;
    padding: 10px 14px;
  }
  
  .annotation-title {
    font-size: 15px;
  }
  
  .annotation-text {
    font-size: 14px;
  }
}

@media (max-width: 768px) {
  .video-popup {
    width: 98%;
    max-width: none;
    border-radius: 18px;
  }
  
  .video-popup-header {
    padding: 16px 20px;
  }
  
  .video-popup-header h3 {
    font-size: 1.2rem;
  }
  
  .video-container {
    padding: 15px;
  }
  
  .close-button {
    width: 32px;
    height: 32px;
  }
  
  .annotation-content {
    width: 180px;
    font-size: 13px;
  }
  
  .annotation-title {
    font-size: 14px;
  }
  
  .annotation-text {
    font-size: 13px;
  }
  
  .toggle-text {
    display: none;
  }
  
  .annotation-toggle {
    padding: 8px;
  }
}

@media (max-width: 480px) {
  .video-popup {
    border-radius: 14px;
  }
  
  .video-popup-header {
    padding: 14px 16px;
  }
  
  .video-popup-header h3 {
    font-size: 1.1rem;
  }
  
  .video-container {
    padding: 10px;
  }
  
  .close-button {
    width: 28px;
    height: 28px;
  }
  
  .close-icon {
    width: 14px;
    height: 14px;
  }
  
  .annotation-content {
    width: 160px;
    padding: 8px 12px;
  }
  
  .annotation-title {
    font-size: 13px;
    margin-bottom: 4px;
  }
  
  .annotation-text {
    font-size: 12px;
  }
  
  .annotation-point {
    width: 14px;
    height: 14px;
  }
}

/* Footer Styles */
.video-popup-footer {
  text-align: right;
  padding: 10px 20px 16px 0;
  background-color: rgba(0, 0, 0, 0.6);
}

.sls-tag {
  font-size: 8px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.5);
  letter-spacing: 0.05em;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}
</style> 