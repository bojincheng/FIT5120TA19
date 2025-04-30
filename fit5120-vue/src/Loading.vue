<template>
  <div class="loading-container">
    <transition name="fade" mode="out-in">
      <div v-if="!showFact" class="tv-container">
        <div class="tv-frame">
          <div class="tv-screen">
            <video class="background-video" autoplay playsinline ref="video">
              <source src="../src/News.mp4" type="video/mp4">
            </video>
          </div>
          <div class="tv-knobs">
            <div class="tv-knob"></div>
            <div class="tv-knob"></div>
          </div>
          <div class="tv-base"></div>
        </div>
        <div class="progress-container">
          <div class="progress-bar" :style="{ width: progress + '%' }"></div>
        </div>
      </div>
      
      <div v-else class="warning-screen">
        <p class="warning-text fade-up">Drowning happens silently — protect your child before it's too late</p>
        <div class="navigate-indicator" v-if="showNavigateIndicator">
          <span class="navigate-text">Continuing to homepage</span>
          <div class="loading-dots">
            <span></span>
            <span></span>
            <span></span>
          </div>
        </div>
      </div>
    </transition>

    <div class="controls" v-if="!showFact">
      <button class="control-button" @click="toggleMute">
        <span v-if="isMuted">🔇</span>
        <span v-else>🔊</span>
      </button>
    </div>

    <button class="skip-button" @click="skipSequence" v-show="!isSkipped && !showFact">
      Skip <span class="skip-icon">→</span>
    </button>
    
    <div class="page-transition" :class="{ 'active': isNavigating }"></div>
  </div>
</template>

<script>
export default {
  name: 'LoadingPage',
  data() {
    return {
      showFact: false,
      isSkipped: false,
      videoDuration: 0,
      isMuted: false,
      progress: 0,
      progressInterval: null,
      isNavigating: false,
      showNavigateIndicator: false
    }
  },
  mounted() {
    const video = this.$refs.video;
    
    // Ensure video starts with volume
    video.muted = false;
    
    video.addEventListener('loadedmetadata', () => {
      this.videoDuration = video.duration;
    });

    video.addEventListener('ended', () => {
      if (!this.isSkipped) {
        this.showFact = true;
        clearInterval(this.progressInterval);
        
        // Show navigation indicator after a brief moment
        setTimeout(() => {
          this.showNavigateIndicator = true;
        }, 1500);
        
        // Automatically navigate to home after a brief display of the warning text
        this.navigateToHome();
      }
    });
    
    // Set up progress tracking
    this.progressInterval = setInterval(() => {
      if (video && !video.paused && !video.ended && this.videoDuration > 0) {
        this.progress = (video.currentTime / this.videoDuration) * 100;
      }
    }, 100);
  },
  beforeUnmount() {
    clearInterval(this.progressInterval);
  },
  methods: {
    toggleMute() {
      const video = this.$refs.video;
      video.muted = !video.muted;
      this.isMuted = video.muted;
    },
    skipSequence() {
      this.isSkipped = true;
      clearInterval(this.progressInterval);
      this.navigateToHome();
    },
    navigateToHome() {
      // First delay to read the warning message
      setTimeout(() => {
        // Trigger the transition animation
        this.isNavigating = true;
        
        // Wait for the transition to complete before navigating
        setTimeout(() => {
          this.$router.push('/home');
        }, 1800); // Matches the transition duration
      }, 4000); // Increased from 3000ms to 4000ms
    }
  }
}
</script>

<style scoped>
.loading-container {
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  overflow: hidden;
  color: white;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background-color: #121212;
}

.warning-screen {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #000;
  padding: 2rem;
  text-align: center;
}

.warning-text {
  font-size: clamp(1.8rem, 4vw, 2.8rem);
  font-weight: 600;
  line-height: 1.4;
  color: white;
  margin-bottom: 2rem;
  text-align: center;
  max-width: 900px;
  letter-spacing: 0.02em;
}

.fade-up {
  animation: fadeUpAnimation 0.8s ease forwards;
}

@keyframes fadeUpAnimation {
  from { 
    opacity: 0;
    transform: translateY(30px);
  }
  to { 
    opacity: 1;
    transform: translateY(0);
  }
}

.navigate-indicator {
  display: flex;
  flex-direction: column;
  align-items: center;
  animation: fadeIn 0.5s ease forwards;
}

.navigate-text {
  font-size: 1.2rem;
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 0.5rem;
}

.loading-dots {
  display: flex;
  gap: 0.5rem;
}

.loading-dots span {
  width: 10px;
  height: 10px;
  background-color: #ff4444;
  border-radius: 50%;
  display: inline-block;
  animation: dotPulse 1.4s infinite ease-in-out;
}

.loading-dots span:nth-child(2) {
  animation-delay: 0.2s;
}

.loading-dots span:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes dotPulse {
  0%, 100% { transform: scale(0.7); opacity: 0.5; }
  50% { transform: scale(1); opacity: 1; }
}

.page-transition {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #000;
  z-index: 9999;
  transform: translateY(100%);
  transition: transform 1.8s cubic-bezier(0.65, 0, 0.35, 1);
  pointer-events: none;
}

.page-transition.active {
  transform: translateY(0);
}

.tv-container {
  position: relative;
  width: 90%;
  max-width: 1200px;
  height: 80%;
  z-index: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.tv-frame {
  position: relative;
  width: 100%;
  height: 100%;
  background-color: #222;
  border-radius: 20px;
  padding: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.tv-screen {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  border-radius: 10px;
  border: 8px solid #111;
  box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.8);
  background-color: black;
}

.tv-knobs {
  position: absolute;
  bottom: 15px;
  right: 30px;
  display: flex;
  gap: 15px;
}

.tv-knob {
  width: 20px;
  height: 20px;
  background-color: #444;
  border-radius: 50%;
  border: 2px solid #333;
}

.tv-base {
  position: absolute;
  bottom: -40px;
  width: 50%;
  height: 40px;
  background-color: #222;
  border-radius: 0 0 20px 20px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.5);
}

.background-video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 0;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 1s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.skip-button {
  position: fixed;
  top: 2rem;
  right: 2rem;
  background: rgba(255, 68, 68, 0.9);
  border: 2px solid rgba(255, 255, 255, 0.3);
  color: white;
  padding: 0.8rem 1.5rem;
  border-radius: 2rem;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
  backdrop-filter: blur(5px);
  z-index: 1000;
  opacity: 0;
  animation: fadeInSkip 1s ease 2s forwards;
  box-shadow: 0 4px 15px rgba(255, 68, 68, 0.3);
}

@keyframes fadeInSkip {
  to { opacity: 1; }
}

.skip-button:hover {
  background: rgba(255, 68, 68, 1);
  transform: translateX(5px);
  box-shadow: 0 6px 20px rgba(255, 68, 68, 0.4);
}

.skip-icon {
  font-size: 1.2rem;
  transition: transform 0.3s ease;
}

.skip-button:hover .skip-icon {
  transform: translateX(3px);
}

@media (max-width: 768px) {
  .skip-button {
    top: 1rem;
    right: 1rem;
    padding: 0.6rem 1.2rem;
    font-size: 1rem;
  }
}

.controls {
  position: fixed;
  bottom: 2rem;
  left: 2rem;
  z-index: 1000;
}

.control-button {
  background: rgba(255, 68, 68, 0.9);
  border: 2px solid rgba(255, 255, 255, 0.3);
  color: white;
  padding: 0.8rem;
  border-radius: 50%;
  font-size: 1.2rem;
  cursor: pointer;
  transition: all 0.3s ease;
  backdrop-filter: blur(5px);
  width: 3.2rem;
  height: 3.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 15px rgba(255, 68, 68, 0.3);
}

.control-button:hover {
  background: rgba(255, 68, 68, 1);
  transform: scale(1.1);
  box-shadow: 0 6px 20px rgba(255, 68, 68, 0.4);
}

@media (max-width: 768px) {
  .controls {
    bottom: 1rem;
    left: 1rem;
  }
  
  .control-button {
    width: 2.8rem;
    height: 2.8rem;
    font-size: 1.1rem;
  }
}

.progress-container {
  width: 80%;
  height: 6px;
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 3px;
  margin-top: 20px;
  overflow: hidden;
  position: relative;
}

.progress-bar {
  height: 100%;
  background-color: #ff4444;
  width: 0%;
  border-radius: 3px;
  transition: width 0.1s linear;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
</style>
