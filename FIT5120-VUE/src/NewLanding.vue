<template>
  <div class="app-container" ref="appContainer">
    <!-- Video Background -->
    <video class="video-background" autoplay loop muted playsinline ref="videoBackground">
      <source src="/videos/3192100-hd_1920_1080_30fps.mp4" type="video/mp4">
    </video>
    
    <!-- Danger Points Overlay -->
    <div class="danger-points-overlay">
      <!-- Rip Current -->
      <div class="danger-point" style="top: 20%; left: 20%;" ref="ripPoint">
        <div class="danger-marker"></div>
        <div class="danger-tooltip">
          <h3>Rip Current</h3>
          <p>Powerful water channel pulling swimmers away from shore</p>
        </div>
      </div>
      
      <!-- Large Waves -->
      <div class="danger-point" style="top: 35%; left: 75%;" ref="wavesPoint">
        <div class="danger-marker"></div>
        <div class="danger-tooltip">
          <h3>Powerful Waves</h3>
          <p>Unusually strong waves that can knock swimmers over</p>
        </div>
      </div>
      
      <!-- No Flags Zone -->
      <div class="danger-point" style="top: 70%; left: 60%;" ref="flagsPoint">
        <div class="danger-marker"></div>
        <div class="danger-tooltip">
          <h3>Swimming Outside Flags</h3>
          <p>Unpatrolled waters - high drowning risk</p>
        </div>
      </div>
    </div>
    
    <!-- Navigation Bar -->
    <NavigationBar />
    
    <!-- Tools Button with External Hover Hint -->
    <div class="tools-button-container">
      <div class="hover-hint-external">HOVER ME</div>
      <div class="tools-button" @mouseenter="openToolsPopup" @mouseleave="startCloseTimer">
        <span>TOOLS</span>
      </div>
    </div>
    
    <!-- Tools Popup -->
    <div v-if="showToolsPopup" class="tools-popup-overlay" @mouseenter="cancelCloseTimer" @mouseleave="startCloseTimer">
      <div class="tools-popup-container">
        <button class="close-tools-popup" @click.stop="closeToolsPopup">×</button>
        <BeachComparisonTool :isPopup="true" />
      </div>
    </div>
    
    <!-- Content -->
    <div class="content-section" ref="contentSection">
      <div class="text-content">
        <div class="message-container">
          <div class="message-line first-line" ref="topContent">
            <span class="highlight">Drowning is the second leading cause of accidental death among children in Australia</span>
          </div>
          <div class="message-line second-line" ref="bottomContent">
            <span class="appear-text delay-1">— but with simple, informed choices, it's a tragedy we can prevent.</span>
          </div>
        </div>
      </div>
      
      <!-- Scroll Circle -->
      <div class="scroll-indicator" @click="scrollDown">
        <div class="scroll-circle">
          <div class="scroll-text">SCROLL TO<br>DISCOVER HOW</div>
        </div>
      </div>
    </div>
    
    <!-- Sand color overlay for transition -->
    <div class="sand-overlay" ref="sandOverlay"></div>
    
    <!-- Split effect elements -->
    <div class="split-top" ref="splitTop">
      <div class="sand-background"></div>
      <video class="video-background-split top-video" autoplay loop muted playsinline ref="topVideo">
        <source src="/videos/3192100-hd_1920_1080_30fps.mp4" type="video/mp4">
      </video>
    </div>
    <div class="split-bottom" ref="splitBottom">
      <div class="sand-background"></div>
      <video class="video-background-split bottom-video" autoplay loop muted playsinline ref="bottomVideo">
        <source src="/videos/3192100-hd_1920_1080_30fps.mp4" type="video/mp4">
      </video>
    </div>
  </div>
</template>

<script>
import NavigationBar from './components/NavigationBar.vue';
import BeachComparisonTool from './components/BeachComparisonTool.vue';

export default {
  name: 'NewLanding',
  components: {
    NavigationBar,
    BeachComparisonTool
  },
  data() {
    return {
      isScrolling: false,
      scrollStarted: false,
      showToolsPopup: false,
      closeTimer: null
    }
  },
  mounted() {
    window.addEventListener('wheel', this.handleScroll);
    window.addEventListener('touchstart', this.handleTouchStart, { passive: false });
    window.addEventListener('touchmove', this.handleTouchMove, { passive: false });
    
    // Preload the videos to ensure they're ready for the transition
    this.preloadVideos();
    
    // Preload the BeachHomePage to ensure instant transition
    this.preloadBeachHomePage();
    
    // Initialize the danger points with staggered appearance
    this.initDangerPoints();
  },
  beforeUnmount() {
    window.removeEventListener('wheel', this.handleScroll);
    window.removeEventListener('touchstart', this.handleTouchStart);
    window.removeEventListener('touchmove', this.handleTouchMove);
  },
  methods: {
    startCloseTimer() {
      // Set a small delay before closing to make interaction smoother
      this.closeTimer = setTimeout(() => {
        this.closeToolsPopup();
      }, 300);
    },
    
    cancelCloseTimer() {
      // Cancel the close timer when user hovers back into the popup
      if (this.closeTimer) {
        clearTimeout(this.closeTimer);
        this.closeTimer = null;
      }
    },
    
    openToolsPopup() {
      this.showToolsPopup = true;
      document.body.style.overflow = 'hidden';
      // Temporarily disable scroll transition while popup is open
      this.isScrolling = true;
    },
    
    closeToolsPopup() {
      this.showToolsPopup = false;
      document.body.style.overflow = '';
      
      // Re-enable scroll transition after popup is closed with a slight delay
      setTimeout(() => {
        this.isScrolling = false;
      }, 100);
    },
    
    preloadVideos() {
      // Ensure top and bottom videos start at the same point as main video
      this.$refs.topVideo.currentTime = 0;
      this.$refs.bottomVideo.currentTime = 0;
    },
    
    preloadBeachHomePage() {
      // Preload the beach home page component to avoid any loading delay
      const img = new Image();
      img.src = '/images/beach-home-bg.jpg'; // Add this image to public folder if needed
      
      // Preload the component
      this.$router.options.routes.find(route => route.path === '/beach');
    },
    
    initDangerPoints() {
      // Add staggered appearance animation to danger points
      const dangerPoints = document.querySelectorAll('.danger-point');
      
      dangerPoints.forEach((point, index) => {
        // Initially hide all points
        point.style.opacity = '0';
        point.style.transform = 'scale(0.5)';
        point.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        
        // Show points with staggered delay after main content appears
        setTimeout(() => {
          point.style.opacity = '1';
          point.style.transform = 'scale(1)';
          
          // After points appear, automatically open tooltips in sequence
          if (index === 0) {
            setTimeout(() => this.showTooltip(point), 1000);
          }
        }, 3000 + (index * 300)); // Start after main content animation, then stagger by 300ms each
        
        // Add click event for manual interaction
        point.addEventListener('click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          this.showTooltip(point);
        });
        
        // Add touch event for mobile devices
        point.addEventListener('touchstart', (e) => {
          // Prevent scrolling when touching a danger point
          e.preventDefault();
          e.stopPropagation();
          this.showTooltip(point);
        });
      });
      
      // Close tooltips when clicking elsewhere
      document.addEventListener('click', (e) => {
        if (!e.target.closest('.danger-point')) {
          this.closeAllTooltips();
        }
      });
      
      document.addEventListener('touchstart', (e) => {
        if (!e.target.closest('.danger-point')) {
          this.closeAllTooltips();
        }
      });
    },
    
    showTooltip(point) {
      // Close all tooltips first
      this.closeAllTooltips();
      
      // Get the tooltip and show it
      const tooltip = point.querySelector('.danger-tooltip');
      tooltip.classList.add('active');
      tooltip.style.opacity = '1';
      tooltip.style.visibility = 'visible';
      tooltip.style.transform = window.innerWidth <= 768 ? 'translateX(-50%) translateY(0)' : 'translateY(0)';
      
      // Mark the point as active
      point.classList.add('active');
      
      // Find the index of the current point
      const points = Array.from(document.querySelectorAll('.danger-point'));
      const currentIndex = points.indexOf(point);
      const nextIndex = (currentIndex + 1) % points.length;
      
      // Automatically open the next point after a delay, unless user has scrolled
      if (!this.scrollStarted) {
        setTimeout(() => {
          if (!this.scrollStarted) {
            this.showTooltip(points[nextIndex]);
          }
        }, 5000);
      }
    },
    
    closeAllTooltips() {
      document.querySelectorAll('.danger-tooltip').forEach(tip => {
        tip.classList.remove('active');
        tip.style.opacity = '0';
        tip.style.visibility = 'hidden';
      });
      
      document.querySelectorAll('.danger-point').forEach(point => {
        point.classList.remove('active');
      });
    },
    
    handleScroll(event) {
      if (this.isScrolling || this.scrollStarted) return;
      
      // Detect downward scroll
      if (event.deltaY > 0) {
        this.triggerSplitTransition();
      }
    },
    
    handleTouchStart(event) {
      this.touchStartY = event.touches[0].clientY;
    },
    
    handleTouchMove(event) {
      if (!this.touchStartY || this.isScrolling || this.scrollStarted) return;
      
      const touchY = event.touches[0].clientY;
      const diff = this.touchStartY - touchY;
      
      // Detect downward swipe
      if (diff > 50) {
        this.triggerSplitTransition();
        event.preventDefault();
      }
    },
    
    scrollDown() {
      this.triggerSplitTransition();
    },
    
    triggerSplitTransition() {
      if (this.scrollStarted) return;
      this.scrollStarted = true;
      this.isScrolling = true;
      
      // Hide danger points during transition
      const dangerPoints = document.querySelectorAll('.danger-point');
      dangerPoints.forEach(point => {
        point.style.opacity = '0';
        point.style.pointerEvents = 'none';
      });
      
      // Get references to elements
      const splitTop = this.$refs.splitTop;
      const splitBottom = this.$refs.splitBottom;
      const topContent = this.$refs.topContent;
      const bottomContent = this.$refs.bottomContent;
      const mainVideo = this.$refs.videoBackground;
      const topVideo = this.$refs.topVideo;
      const bottomVideo = this.$refs.bottomVideo;
      const appContainer = this.$refs.appContainer;
      const sandOverlay = this.$refs.sandOverlay;
      
      // Activate sand overlay to fade to sand color immediately
      sandOverlay.style.opacity = '0.9';
      
      // Sync videos to match the current time of the main video
      const currentTime = mainVideo.currentTime;
      topVideo.currentTime = currentTime;
      bottomVideo.currentTime = currentTime;
      
      // Create clones of content for the split elements
      const topHTML = document.createElement('div');
      topHTML.classList.add('split-content');
      topHTML.innerHTML = topContent.outerHTML;
      splitTop.appendChild(topHTML);
      
      const bottomHTML = document.createElement('div');
      bottomHTML.classList.add('split-content');
      bottomHTML.innerHTML = bottomContent.outerHTML;
      splitBottom.appendChild(bottomHTML);
      
      // Show the split elements
      splitTop.style.opacity = '1';
      splitBottom.style.opacity = '1';
      
      // Hide the main video and content
      mainVideo.style.opacity = '0';
      this.$refs.contentSection.style.opacity = '0';
      
      // Immediately show sand background in split elements
      splitTop.querySelector('.sand-background').style.opacity = '0.9';
      splitBottom.querySelector('.sand-background').style.opacity = '0.9';
      topVideo.style.opacity = '0.1';
      bottomVideo.style.opacity = '0.1';
      
      // Add the animation classes for a faster split
      splitTop.classList.add('split-animate-top');
      splitBottom.classList.add('split-animate-bottom');
      
      // Navigate to beach page immediately but keep displaying our animation
      // Use replaceState to avoid keeping this in history
      history.replaceState(null, null, '/beach');
      
      // Fully navigate after the animation has progressed enough
      // This is a very short timeout just to let the animation start
      setTimeout(() => {
        // Navigate to route without animation
        this.$router.replace({ 
          path: '/beach', 
          query: { direct: 'true' }
        });
      }, 250);
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;700&family=Montserrat:wght@300;400;500;600&display=swap');

/* Base Styles */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  margin: 0;
  padding: 0;
  overflow: hidden;
}

.app-container {
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;
  color: #FFFFFF;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  position: relative;
  animation: fadeIn 0.3s ease forwards;
  overflow: hidden;
  padding-top: 0;
}

.app-container.exiting {
  animation: none;
  transition: opacity 0.2s ease-out;
  opacity: 0;
}

/* Video background */
.video-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 0;
  transition: opacity 0.5s ease;
}

/* Sand overlay for transition */
.sand-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #f5f1e6; /* Sand color */
  z-index: 45;
  opacity: 0;
  transition: opacity 0.2s ease;
  pointer-events: none;
}

/* Content section */
.content-section {
  padding: 2rem;
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(to bottom, rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.6));
  padding-top: 80px;
  transition: opacity 0.5s ease;
}

.text-content {
  max-width: 1200px;
  width: 100%;
  text-align: center;
}

.message-container {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.message-line {
  font-family: 'Playfair Display', serif;
  line-height: 1.4;
  letter-spacing: -0.02em;
  text-shadow: 0 2px 15px rgba(0, 0, 0, 0.7);
  position: relative;
  z-index: 5;
}

.first-line {
  font-size: 2.8rem;
  max-width: 80%;
  margin: 0 auto;
  position: relative;
}

.second-line {
  font-size: 2.5rem;
  position: relative;
  font-weight: 600;
}

.highlight {
  font-weight: 700;
  color: #E1BC56;
  opacity: 0;
  transform: translateY(30px);
  display: inline-block;
  animation: fadeInScale 1.2s cubic-bezier(0.215, 0.61, 0.355, 1) forwards;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.9),
               0 2px 6px rgba(0, 0, 0, 0.8),
               0 4px 15px rgba(0, 0, 0, 0.7),
               0 8px 25px rgba(0, 0, 0, 0.6);
  padding: 0 3px;
}

.appear-text {
  opacity: 0;
  transform: translateY(20px);
  display: inline-block;
  animation: appear 0.8s ease forwards;
  animation-delay: 0.8s;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 1),
               0 2px 8px rgba(0, 0, 0, 0.9),
               0 4px 20px rgba(0, 0, 0, 0.8),
               0 8px 30px rgba(0, 0, 0, 0.7);
  padding: 0 3px;
  font-weight: 700;
  color: #ffffff;
  position: relative;
  z-index: 6;
}

.delay-1 {
  animation-delay: 1.5s;
}

/* Scroll Indicator */
.scroll-indicator {
  position: absolute;
  bottom: 40px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 10;
  opacity: 0;
  animation: fadeIn 0.8s ease forwards;
  animation-delay: 2.5s;
  cursor: pointer;
}

.scroll-circle {
  width: 130px;
  height: 130px;
  border-radius: 50%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(8px);
  transition: all 0.3s ease;
}

.scroll-text {
  font-size: 1rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 2px;
  text-align: center;
  line-height: 1.4;
  color: #ffffff;
}

.scroll-circle:hover {
  background-color: rgba(0, 0, 0, 0.7);
  transform: scale(1.05);
}

/* Split screen effect styles */
.split-top, .split-bottom {
  position: fixed;
  left: 0;
  width: 100%;
  height: 50vh;
  z-index: 50;
  overflow: hidden;
  opacity: 0;
  pointer-events: none;
}

.split-top {
  top: 0;
}

.split-bottom {
  bottom: 0;
}

.sand-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #f5f1e6; /* Sand color */
  opacity: 0;
  transition: opacity 0.3s ease;
  z-index: 2;
}

.split-content {
  position: absolute;
  width: 100%;
  text-align: center;
  padding: 0 2rem;
  z-index: 3;
}

.split-top .split-content {
  bottom: 1rem;
}

.split-bottom .split-content {
  top: 1rem;
}

.video-background-split {
  position: absolute;
  width: 100%;
  height: 200vh; /* Double height to cover either half */
  object-fit: cover;
  z-index: 1;
  transition: opacity 0.3s ease;
}

.top-video {
  top: 0;
  object-position: center top;
}

.bottom-video {
  bottom: 0;
  object-position: center bottom;
}

.split-animate-top {
  animation: splitTop 0.4s cubic-bezier(0.215, 0.61, 0.355, 1) forwards;
}

.split-animate-bottom {
  animation: splitBottom 0.4s cubic-bezier(0.215, 0.61, 0.355, 1) forwards;
}

@keyframes splitTop {
  0% {
    transform: translateY(0);
  }
  100% {
    transform: translateY(-100%);
  }
}

@keyframes splitBottom {
  0% {
    transform: translateY(0);
  }
  100% {
    transform: translateY(100%);
  }
}

@keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-10px);
  }
  60% {
    transform: translateY(-5px);
  }
}

/* Animation Keyframes */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes appear {
  0% { 
    opacity: 0;
    transform: translateY(20px);
  }
  100% { 
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeInScale {
  0% {
    opacity: 0;
    transform: translateY(30px);
  }
  50% {
    opacity: 1;
    transform: translateY(-5px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Danger Points Styles */
.danger-points-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  pointer-events: none;
}

.danger-point {
  position: absolute;
  width: 30px;
  height: 30px;
  z-index: 5;
  pointer-events: all;
  cursor: pointer;
}

.danger-marker {
  position: relative;
  width: 28px;
  height: 28px;
  background-color: rgba(255, 50, 50, 0.9);
  border: 3px solid #ffffff;
  border-radius: 50%;
  box-shadow: 0 0 10px rgba(255, 50, 50, 0.6), 0 0 0 rgba(255, 50, 50, 0.6);
  animation: pulse 2s infinite;
  transition: transform 0.3s ease;
}

.danger-point:hover .danger-marker,
.danger-point.active .danger-marker {
  transform: scale(1.3);
  background-color: rgb(255, 50, 50);
  box-shadow: 0 0 20px rgba(255, 50, 50, 0.8), 0 0 0 rgba(255, 50, 50, 0.6);
}

.danger-tooltip {
  position: absolute;
  width: 280px;
  background-color: rgba(0, 0, 0, 0.95);
  backdrop-filter: blur(10px);
  border-radius: 8px;
  padding: 18px;
  box-shadow: 0 5px 25px rgba(0, 0, 0, 0.7), 0 0 0 3px rgba(255, 255, 255, 0.5);
  color: white;
  opacity: 0;
  visibility: hidden;
  transition: all 0.4s ease;
  transform: translateY(10px);
  pointer-events: none;
  z-index: 6;
  border: 2px solid rgba(255, 255, 255, 0.7);
  left: 30px;
  top: -5px;
}

.danger-point:hover .danger-tooltip,
.danger-tooltip.active {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

.danger-tooltip h3 {
  margin: 0 0 10px 0;
  color: #FFE066;
  font-size: 1.4rem;
  font-weight: 800;
  letter-spacing: 0.01em;
}

.danger-tooltip p {
  margin: 0;
  font-size: 1.1rem;
  line-height: 1.5;
  color: #ffffff;
  font-weight: 600;
}

@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(255, 50, 50, 0.8);
  }
  70% {
    box-shadow: 0 0 0 20px rgba(255, 50, 50, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(255, 50, 50, 0);
  }
}

/* Tools Button */
.tools-button-container {
  position: fixed;
  bottom: 40px;
  right: 40px;
  z-index: 100;
  display: flex;
  flex-direction: column;
  align-items: center;
  animation: fadeIn 0.8s ease forwards;
  animation-delay: 3s;
  opacity: 0;
}

.tools-button {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background-color: rgba(243, 156, 18, 0.9);
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4), 0 0 0 4px rgba(255, 255, 255, 0.2);
  transition: all 0.3s ease;
  border: 2px solid rgba(255, 255, 255, 0.7);
  animation: glow 2s infinite alternate;
  animation-delay: 0.5s;
}

.tools-button span {
  font-weight: 700;
  font-size: 0.8rem;
  letter-spacing: 1px;
  text-transform: uppercase;
}

.hover-hint-external {
  background-color: rgba(0, 0, 0, 0.8);
  color: white;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 1px;
  padding: 6px 12px;
  border-radius: 20px;
  margin-bottom: 10px;
  text-transform: uppercase;
  position: relative;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  animation: bounce 1.5s infinite alternate, pulse-opacity 1.5s infinite alternate;
  border: 1px solid rgba(243, 156, 18, 0.9);
}

.hover-hint-external:after {
  content: '';
  position: absolute;
  bottom: -6px;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 0;
  border-left: 6px solid transparent;
  border-right: 6px solid transparent;
  border-top: 6px solid rgba(0, 0, 0, 0.8);
}

.tools-button:hover {
  transform: scale(1.1);
  background-color: rgba(243, 156, 18, 1);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5), 0 0 0 6px rgba(255, 255, 255, 0.4);
}

@keyframes pulse-opacity {
  0% {
    opacity: 0.6;
  }
  100% {
    opacity: 1;
  }
}

@keyframes glow {
  0% {
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4), 0 0 0 4px rgba(255, 255, 255, 0.2);
  }
  100% {
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4), 0 0 0 8px rgba(255, 255, 255, 0.4);
  }
}

/* Tools Popup */
.tools-popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(5px);
  z-index: 1000;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  animation: fadeIn 0.3s ease-out;
}

.tools-popup-container {
  position: relative;
  background: linear-gradient(135deg, rgba(15, 25, 40, 0.95), rgba(30, 40, 60, 0.95));
  border-radius: 16px;
  width: 95%;
  max-width: 1200px;
  height: auto;
  min-height: 200px;
  max-height: 95vh;
  overflow: auto;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(243, 156, 18, 0.4);
  animation: scaleIn 0.3s ease-out;
  padding: 15px;
  margin: 10px;
}

.close-tools-popup {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(0, 0, 0, 0.5);
  border: none;
  color: white;
  font-size: 24px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  z-index: 10;
  transition: all 0.2s ease;
}

.close-tools-popup:hover {
  background: rgba(231, 76, 60, 0.8);
  transform: rotate(90deg);
}

@keyframes scaleIn {
  from { transform: scale(0.9); opacity: 0; }
  to { transform: scale(1); opacity: 1; }
}

/* Responsive Styles */
@media (max-width: 992px) {
  .first-line {
    font-size: 2.4rem;
    max-width: 90%;
  }
  
  .second-line {
    font-size: 2rem;
  }
  
  .scroll-circle {
    width: 110px;
    height: 110px;
  }
  
  .danger-tooltip {
    width: 220px;
    padding: 12px;
  }
  
  .danger-tooltip h3 {
    font-size: 1.1rem;
  }
  
  .danger-tooltip p {
    font-size: 0.9rem;
  }
  
  .tools-button-container {
    bottom: 30px;
    right: 30px;
  }
  
  .tools-button {
    width: 70px;
    height: 70px;
  }
  
  .hover-hint-external {
    font-size: 0.7rem;
    padding: 5px 10px;
    margin-bottom: 8px;
  }
}

@media (max-width: 768px) {
  .first-line {
    font-size: 2rem;
    max-width: 95%;
  }
  
  .second-line {
    font-size: 1.8rem;
  }
  
  .message-container {
    gap: 1.5rem;
  }
  
  .scroll-circle {
    width: 110px;
    height: 110px;
  }
  
  .scroll-text {
    font-size: 0.85rem;
  }
  
  .danger-marker {
    width: 24px;
    height: 24px;
  }
  
  .danger-tooltip {
    width: 220px;
    padding: 15px;
    top: auto;
    bottom: 35px;
    left: 50%;
    transform: translateX(-50%) translateY(10px);
    background-color: rgba(0, 0, 0, 0.95);
    border: 2px solid rgba(255, 255, 255, 0.7);
  }
  
  .danger-tooltip h3 {
    font-size: 1.2rem;
    margin-bottom: 8px;
  }
  
  .danger-tooltip p {
    font-size: 1rem;
  }
  
  .danger-point:hover .danger-tooltip,
  .danger-tooltip.active {
    transform: translateX(-50%) translateY(0);
  }
  
  /* Reposition tooltip arrow for bottom positioning */
  .danger-tooltip::after {
    content: '';
    position: absolute;
    bottom: -10px;
    left: 50%;
    transform: translateX(-50%) rotate(45deg);
    width: 12px;
    height: 12px;
    background-color: rgba(0, 0, 0, 0.95);
    border-right: 2px solid rgba(255, 255, 255, 0.7);
    border-bottom: 2px solid rgba(255, 255, 255, 0.7);
  }
  
  .tools-button-container {
    bottom: 20px;
    right: 20px;
  }
  
  .tools-button {
    width: 60px;
    height: 60px;
  }
  
  .tools-button span {
    font-size: 0.7rem;
  }
  
  .hover-hint-external {
    font-size: 0.65rem;
    padding: 4px 8px;
    margin-bottom: 6px;
  }
  
  .tools-popup-container {
    width: 100%;
    height: 100%;
    border-radius: 0;
    max-height: 100%;
  }
}

@media (max-width: 480px) {
  .first-line {
    font-size: 1.6rem;
  }
  
  .second-line {
    font-size: 1.5rem;
  }
  
  .message-container {
    gap: 1.2rem;
  }
  
  .scroll-circle {
    width: 100px;
    height: 100px;
  }
  
  .scroll-text {
    font-size: 0.75rem;
  }
  
  .danger-marker {
    width: 16px;
    height: 16px;
  }
  
  .danger-tooltip {
    width: 180px;
    padding: 8px;
    bottom: 20px;
  }
  
  .danger-tooltip h3 {
    font-size: 0.9rem;
    margin-bottom: 5px;
  }
  
  .danger-tooltip p {
    font-size: 0.8rem;
    line-height: 1.3;
  }
  
  .tools-button-container {
    bottom: 15px;
    right: 15px;
  }
  
  .tools-button {
    width: 50px;
    height: 50px;
  }
  
  .tools-button span {
    font-size: 0.6rem;
  }
  
  .hover-hint-external {
    font-size: 0.6rem;
    padding: 3px 6px;
    margin-bottom: 4px;
  }
}
</style>
