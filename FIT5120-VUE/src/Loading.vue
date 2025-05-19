<template>
  <div class="loading-container">
    <transition name="fade" mode="out-in">
      <div v-if="!showFact" class="tv-container">
        <div class="tv-frame">
          <div class="tv-screen">
            <div class="video-overlay"></div>
            <div class="tv-glare"></div>
            <div class="tv-static" :class="{ 'static-fading': progress > 80 }"></div>
            <video class="background-video" autoplay playsinline ref="video">
              <source src="/videos/News.mp4" type="video/mp4">
            </video>
            <div class="tv-power-light"></div>
          </div>
          <div class="tv-knobs">
            <div class="tv-knob"></div>
            <div class="tv-knob"></div>
            <div class="tv-knob"></div>
          </div>
          <div class="tv-base"></div>
          <div class="tv-antenna">
            <div class="antenna-left"></div>
            <div class="antenna-right"></div>
          </div>
        </div>
        <div class="progress-container">
          <div class="progress-bar" :style="{ width: progress + '%' }"></div>
        </div>
      </div>
      
      <div v-else class="warning-screen">
        <div class="warning-icon pulse-animation"></div>
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
      <button class="control-button" @click="toggleMute" aria-label="Toggle mute">
        <svg v-if="isMuted" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M11 5L6 9H2v6h4l5 4V5z" />
          <line x1="23" y1="9" x2="17" y2="15" />
          <line x1="17" y1="9" x2="23" y2="15" />
        </svg>
        <svg v-else xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5" />
          <path d="M15.54 8.46a5 5 0 0 1 0 7.07" />
          <path d="M19.07 4.93a10 10 0 0 1 0 14.14" />
        </svg>
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
    
    // Add accessibility attributes
    video.setAttribute('aria-hidden', 'true');
    
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
    
    // Handle keyboard shortcut for skip
    document.addEventListener('keydown', this.handleKeydown);
  },
  beforeUnmount() {
    clearInterval(this.progressInterval);
    document.removeEventListener('keydown', this.handleKeydown);
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
      
      // Add transition effect when skipping
      this.isNavigating = true;
      
      // Go to homepage after transition animation
      setTimeout(() => {
        this.$router.push('/home');
      }, 800);
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
      }, 4000);
    },
    handleKeydown(event) {
      // Allow skipping with ESC or Space key
      if ((event.key === 'Escape' || event.key === ' ') && !this.isSkipped && !this.showFact) {
        this.skipSequence();
      }
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

.warning-icon {
  width: 80px;
  height: 80px;
  background-color: #ff4444;
  border-radius: 50%;
  margin-bottom: 2rem;
  position: relative;
}

.warning-icon::before {
  content: "!";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 3rem;
  font-weight: bold;
  color: white;
}

.pulse-animation {
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(255, 68, 68, 0.7);
  }
  70% {
    box-shadow: 0 0 0 20px rgba(255, 68, 68, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(255, 68, 68, 0);
  }
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
  height: auto;
  aspect-ratio: 16 / 9;
  max-height: 80vh;
  z-index: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
}

.tv-frame {
  position: relative;
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, #444, #222);
  border-radius: 20px;
  padding: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7), 0 0 40px rgba(255, 68, 68, 0.2), inset 0 0 20px rgba(0, 0, 0, 0.8);
  display: flex;
  flex-direction: column;
  align-items: center;
  box-sizing: border-box;
  transition: all 0.3s ease;
  border: 1px solid #666;
}

.tv-frame:hover {
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.8), 0 0 60px rgba(255, 68, 68, 0.3);
  transform: scale(1.01);
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
  box-sizing: border-box;
}

.tv-glare {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(255,255,255,0.12) 0%, rgba(255,255,255,0) 50%);
  z-index: 2;
  pointer-events: none;
}

.tv-static {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMDAiIGhlaWdodD0iMzAwIj48ZmlsdGVyIGlkPSJhIiB4PSIwIiB5PSIwIj48ZmVUdXJidWxlbmNlIHR5cGU9ImZyYWN0YWxOb2lzZSIgYmFzZUZyZXF1ZW5jeT0iLjc1IiBzdGl0Y2hUaWxlcz0ic3RpdGNoIi8+PGZlQ29sb3JNYXRyaXggdHlwZT0ic2F0dXJhdGUiIHZhbHVlcz0iMCIvPjwvZmlsdGVyPjxwYXRoIGZpbHRlcj0idXJsKCNhKSIgb3BhY2l0eT0iLjA1IiBkPSJNMCAwaDMwMHYzMDBIMHoiLz48L3N2Zz4=');
  background-size: cover;
  opacity: 0.3;
  mix-blend-mode: overlay;
  z-index: 1;
  pointer-events: none;
  animation: staticAnimation 0.5s steps(2) infinite;
}

.static-fading {
  animation: fadeOutStatic 2s forwards;
}

@keyframes staticAnimation {
  0% { opacity: 0.3; }
  50% { opacity: 0.25; }
  100% { opacity: 0.3; }
}

@keyframes fadeOutStatic {
  from { opacity: 0.3; }
  to { opacity: 0; }
}

.video-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: repeating-linear-gradient(
    0deg,
    rgba(0, 0, 0, 0.03) 0px,
    rgba(0, 0, 0, 0.03) 1px,
    transparent 1px,
    transparent 2px
  );
  pointer-events: none;
  z-index: 1;
}

.tv-antenna {
  position: absolute;
  top: -40px;
  width: 40%;
  height: 40px;
  display: flex;
  justify-content: center;
  gap: 30px;
}

.antenna-left, .antenna-right {
  width: 4px;
  height: 40px;
  background-color: #222;
  position: relative;
}

.antenna-left:before, .antenna-right:before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: #444;
}

.tv-power-light {
  position: absolute;
  bottom: 10px;
  right: 10px;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #ff4444;
  box-shadow: 0 0 8px #ff4444;
  animation: blinkLight 4s infinite;
  z-index: 2;
}

@keyframes blinkLight {
  0% { opacity: 1; }
  95% { opacity: 1; }
  96% { opacity: 0.4; }
  97% { opacity: 1; }
  98% { opacity: 0.4; }
  100% { opacity: 1; }
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
  background: radial-gradient(circle at 40% 40%, #777, #333);
  border-radius: 50%;
  border: 2px solid #333;
  transition: transform 0.3s ease;
  position: relative;
}

.tv-knob:after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 8px;
  height: 2px;
  background-color: #222;
}

.tv-knob:hover {
  transform: rotate(45deg);
  cursor: pointer;
}

.tv-base {
  position: absolute;
  bottom: -40px;
  width: 50%;
  height: 40px;
  background: linear-gradient(to bottom, #333, #222);
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
  border: none;
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

.controls {
  position: fixed;
  bottom: 2rem;
  left: 2rem;
  z-index: 1000;
}

.control-button {
  background: rgba(255, 68, 68, 0.9);
  border: none;
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

.progress-container {
  width: 80%;
  height: 8px;
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 4px;
  margin-top: 20px;
  overflow: hidden;
  position: relative;
  display: flex;
  align-items: center;
}

.progress-bar {
  height: 100%;
  background: linear-gradient(90deg, #ff4444, #ff7676);
  width: 0%;
  border-radius: 4px;
  transition: width 0.2s linear;
  box-shadow: 0 0 10px rgba(255, 68, 68, 0.5);
}

.progress-text {
  display: none;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@media (max-aspect-ratio: 16/9) {
  .tv-container {
    width: 90%;
    height: auto;
    aspect-ratio: 16 / 9;
    max-height: 80vh;
  }
}

@media (min-aspect-ratio: 16/9) {
  .tv-container {
    height: 80vh;
    width: auto;
    aspect-ratio: 16 / 9;
    max-width: 90%;
  }
}

@media (max-width: 768px) {
  .tv-container {
    width: 95%;
    max-height: 75vh;
  }
  
  .tv-frame {
    padding: 12px;
    border-radius: 15px;
  }
  
  .tv-screen {
    border-width: 6px;
    border-radius: 8px;
  }
  
  .tv-knobs {
    right: 20px;
    gap: 10px;
  }
  
  .tv-knob {
    width: 15px;
    height: 15px;
  }
  
  .tv-base {
    bottom: -30px;
    height: 30px;
  }
  
  .skip-button {
    top: 1rem;
    right: 1rem;
    padding: 0.6rem 1.2rem;
    font-size: 1rem;
  }
  
  .controls {
    bottom: 1rem;
    left: 1rem;
  }
  
  .control-button {
    width: 2.8rem;
    height: 2.8rem;
    font-size: 1.1rem;
  }
  
  .warning-icon {
    width: 60px;
    height: 60px;
  }
  
  .warning-icon::before {
    font-size: 2.5rem;
  }
  
  .tv-antenna {
    top: -30px;
    height: 30px;
    gap: 20px;
  }
  
  .antenna-left, .antenna-right {
    height: 30px;
    width: 3px;
  }
}

@media (max-width: 480px) {
  .tv-container {
    width: 98%;
    max-height: 70vh;
  }
  
  .tv-frame {
    padding: 8px;
    border-radius: 10px;
  }
  
  .tv-screen {
    border-width: 4px;
    border-radius: 6px;
  }
  
  .tv-knobs {
    bottom: 10px;
    right: 15px;
    gap: 8px;
  }
  
  .tv-knob {
    width: 12px;
    height: 12px;
  }
  
  .tv-base {
    bottom: -20px;
    height: 20px;
    width: 60%;
  }
  
  .progress-container {
    height: 6px;
    width: 90%;
  }
  
  .progress-text {
    font-size: 0.7rem;
  }
  
  .warning-icon {
    width: 50px;
    height: 50px;
    margin-bottom: 1.5rem;
  }
  
  .warning-icon::before {
    font-size: 2rem;
  }
  
  .warning-text {
    font-size: clamp(1.5rem, 4vw, 2rem);
    margin-bottom: 1.5rem;
  }
  
  .tv-antenna {
    top: -20px;
    height: 20px;
    gap: 15px;
  }
  
  .antenna-left, .antenna-right {
    height: 20px;
    width: 2px;
  }
  
  .tv-power-light {
    width: 6px;
    height: 6px;
  }
}
</style>
