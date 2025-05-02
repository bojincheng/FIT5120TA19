<template>
  <div class="rip-safety-page">
    <div class="bg-image"></div>
    <div class="overlay"></div>
    
    <!-- Beach Menu Component -->
    <BeachMenu :menuOpen="menuOpen" @toggle-menu="toggleMenu" />
    
    <div class="content-wrapper">
      <div class="main-content">
        <div class="rip-progress-nav">
          <div class="progress-bar">
            <div class="progress-step">
              <router-link to="/beach-safety-rescue" class="step-link">
                <div class="step-number">1</div>
                <div class="step-label">Signs of Trouble</div>
              </router-link>
            </div>
            <div class="progress-connector"></div>
            <div class="progress-step active">
              <div class="step-number">2</div>
              <div class="step-label">Survive Rip Currents</div>
            </div>
            <div class="progress-connector"></div>
            <div class="progress-step">
              <router-link to="/safety-tool" class="step-link">
                <div class="step-number">3</div>
                <div class="step-label">Safety Tools</div>
              </router-link>
            </div>
          </div>
        </div>
        
        <div class="title-section">
          <h1>How to Survive a Rip Current</h1>
          <div class="statistic-banner">
          </div>
        </div>

        <div class="content-section">
          <h2 class="section-title">🆘 Rip Current Survival Steps</h2>
          
          <div class="section-body">
            <div class="escape-diagram">
              <h3 class="video-title">Rip Current Survival: Surf Life Saving Victoria</h3>
              <video controls preload="metadata" class="escape-video" @error="handleVideoError">
                <source src="/videos/How to Survive a Rip Current.mp4" type="video/mp4">
                Your browser does not support the video tag.
              </video>
              <p class="image-caption">Video: How to escape a rip current by swimming parallel to shore</p>
            </div>
            
            <div class="survival-steps-compact">
              <div class="step-card-compact">
                <div class="step-number">1</div>
                <h4>Stay Calm</h4>
                <p>Don't panic. Conserve energy.</p>
              </div>
              
              <div class="step-card-compact">
                <div class="step-number">2</div>
                <h4>Float</h4>
                <p>Rip currents pull out, not under. Stay afloat.</p>
              </div>
              
              <div class="step-card-compact">
                <div class="step-number">3</div>
                <h4>Swim Parallel</h4>
                <p>Swim along shore until free, then angle back.</p>
              </div>
              
              <div class="step-card-compact">
                <div class="step-number">4</div>
                <h4>Signal for Help</h4>
                <p>Raise one arm and call out if needed.</p>
              </div>
            </div>
            
            <div class="alert-box warning">
              <div class="alert-icon">🚫</div>
              <div class="alert-content">
                <h4>Never Try to Swim Against the Current</h4>
                <p>Even strong swimmers can become exhausted quickly fighting against a rip current. Swimming directly back to shore against the current is dangerous and can lead to drowning.</p>
              </div>
            </div>
          </div>
        </div>
        
        <div class="content-section">
          <h2 class="section-title">👨‍👩‍👧‍👦 Helping Your Child in a Rip Current</h2>
          
          <div class="section-body">
            <div class="child-danger-container">
              <img src="./assets/child_drwoning.jpg" alt="Parent helping child in rip current" class="child-danger-image" @error="handleImageError">
              <div class="image-overlay"></div>
              
              <!-- Interactive Hotspots - 3 key steps -->
              <div class="interactive-hotspots">
                <div class="hotspot hotspot-stay-calm">
                  <div class="hotspot-number">1</div>
                  <div class="hotspot-content">
                    <h4>Stay Calm & Guide</h4>
                    <p>Remain calm and keep your eyes on your child. Call out clear instructions: "Float on your back!" and "Swim sideways along the shore!"</p>
                  </div>
                </div>
                
                <div class="hotspot hotspot-throw">
                  <div class="hotspot-number">2</div>
                  <div class="hotspot-content">
                    <h4>Throw, Don't Go</h4>
                    <p>Throw anything that floats—beach balls, coolers, boogie boards. Never enter the water yourself unless you're trained in water rescue.</p>
                  </div>
                </div>
                
                <div class="hotspot hotspot-get-help">
                  <div class="hotspot-number">3</div>
                  <div class="hotspot-content">
                    <h4>Get Professional Help</h4>
                    <p>Alert lifeguards immediately or call 000. While waiting, keep visual contact with your child and continue guiding them from shore.</p>
                  </div>
                </div>
              </div>
              
              <div class="image-caption">Hover over numbers to learn how to help a child caught in a rip current</div>
            </div>
            
            <div class="alert-box warning parent-warning">
              <div class="alert-icon">❗</div>
              <div class="alert-content">
                <h4>Parents: Never Rush In</h4>
                <p>The most dangerous decision is to enter the water yourself without proper training or equipment. Up to 70% of rescuer drownings occur when parents try to save their children.</p>
              </div>
            </div>
            
            <p class="emphasis">Remember: In emergency situations, call 000 (Australian emergency services) immediately.</p>
          </div>
        </div>
      </div>
    </div>
    
    <div class="next-section-arrow" v-if="showNavigationArrow" @click="navigateToNextSection">
      <div class="arrow-label">Safety Tools</div>
      <div class="arrow-icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M8 12h8"/><path d="m12 8 4 4-4 4"/></svg>
      </div>
    </div>
  </div>
</template>

<script>
import BeachMenu from './components/BeachMenu.vue'

export default {
  name: 'SurviveRipCurrents',
  components: {
    BeachMenu
  },
  data() {
    return {
      menuOpen: false,
      showNavigationArrow: false
    }
  },
  mounted() {
    // Set the active navigation link for this page
    this.setActiveNavLink();
    
    // Add scroll event listener to check if user has reached bottom of page
    window.addEventListener('scroll', this.checkScrollPosition);
  },
  beforeDestroy() {
    // Remove scroll event listener
    window.removeEventListener('scroll', this.checkScrollPosition);
  },
  methods: {
    toggleMenu() {
      this.menuOpen = !this.menuOpen;
      // Prevent body scrolling when menu is open
      if (this.menuOpen) {
        document.body.style.overflow = 'hidden';
      } else {
        document.body.style.overflow = '';
      }
    },
    handleImageError(e) {
      // Add a placeholder class to show a styled error state
      e.target.classList.add('image-error');
      // Set the src to a data URI of a placeholder image or leave empty
      e.target.src = '';
    },
    handleVideoError(e) {
      // Log the error for debugging
      console.error('Video error:', e);
      
      // Add a placeholder class to show a styled error state
      e.target.classList.add('video-error');
      
      // Set a fallback message
      const errorContainer = e.target.parentNode;
      if (errorContainer) {
        // Remove any existing error messages
        const existingError = errorContainer.querySelector('.video-error-message');
        if (existingError) {
          errorContainer.removeChild(existingError);
        }
        
        const errorMsg = document.createElement('div');
        errorMsg.className = 'video-error-message';
        errorMsg.textContent = 'Video could not be loaded. Please refresh the page or try again later.';
        errorContainer.appendChild(errorMsg);
        
        // Add a fallback button to retry loading
        const retryButton = document.createElement('button');
        retryButton.className = 'retry-button';
        retryButton.textContent = 'Retry';
        retryButton.onclick = () => {
          const video = errorContainer.querySelector('video');
          if (video) {
            const src = video.querySelector('source').src;
            video.querySelector('source').src = '';
            setTimeout(() => {
              video.querySelector('source').src = src;
              video.load();
              video.play().catch(err => console.error('Play error:', err));
            }, 100);
          }
        };
        errorMsg.appendChild(retryButton);
      }
    },
    setActiveNavLink() {
      // Remove active class from all nav links
      document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
      });
      document.querySelectorAll('.mobile-nav-link').forEach(link => {
        link.classList.remove('active');
      });
      
      // Add active class to Beach Safety links
      const desktopBeachLink = document.querySelector('.nav-link[href="/beach-safety-rescue"]');
      const mobileBeachLink = document.querySelector('.mobile-nav-link[href="/beach-safety-rescue"]');
      
      if (desktopBeachLink) desktopBeachLink.classList.add('active');
      if (mobileBeachLink) mobileBeachLink.classList.add('active');
    },
    checkScrollPosition() {
      // Show navigation arrow when user is near the bottom of the page
      const scrollPosition = window.scrollY + window.innerHeight;
      const pageHeight = document.documentElement.scrollHeight;
      
      // Show arrow when user has scrolled past 90% of the page
      this.showNavigationArrow = scrollPosition > pageHeight * 0.9;
    },
    navigateToNextSection() {
      // Navigate to the next section and ensure we start at the top of that page
      this.$router.push({ 
        path: '/safety-tool',
        // Adding this option ensures the page is scrolled to the top
        query: { _: Date.now() } 
      }).then(() => {
        // Ensure we're at the top of the page after navigation completes
        window.scrollTo(0, 0);
      });
    }
  }
}
</script>

<style scoped>
.rip-safety-page {
  min-height: 100vh;
  width: 100%;
  color: #ffffff;
  position: relative;
  overflow-x: hidden;
}

.bg-image {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('./assets/Aussie_beachhome.jpg');
  background-size: cover;
  background-position: center;
  background-color: #01365c; /* Fallback color if image is not available */
  z-index: 0;
}

.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, rgba(1, 54, 92, 0.85), rgba(1, 54, 92, 0.7));
  z-index: 1;
}

.content-wrapper {
  position: relative;
  z-index: 2;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  padding-top: 5rem;
}

.main-content {
  flex: 1;
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 2rem 2rem;
}

.title-section {
  text-align: center;
  margin-bottom: 1.5rem;
  background: transparent;
  padding: 1rem 0 0;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}

h1 {
  font-size: clamp(1.8rem, 4vw, 2.5rem);
  margin: 0 0 1rem;
  color: #ffffff;
  font-weight: 800;
  letter-spacing: -0.02em;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
}

.statistic-banner {
  max-width: 1100px;
  margin: 0 auto;
  animation: fadeIn 1s ease-out 0.3s both;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-20px); }
  to { opacity: 1; transform: translateY(0); }
}

.headline {
  font-size: clamp(1.2rem, 2.5vw, 1.6rem);
  line-height: 1.3;
  margin: 0 0 0.5rem;
  color: #ffffff;
  font-weight: 600;
  text-shadow: 0 1px 4px rgba(0, 0, 0, 0.3);
}

.highlight {
  color: #f39c12;
  font-weight: 700;
}

.subheadline {
  font-size: clamp(0.9rem, 1.8vw, 1.2rem);
  line-height: 1.4;
  margin: 0 0 1rem;
  color: #f39c12;
  font-weight: 700;
  text-shadow: 0 1px 4px rgba(0, 0, 0, 0.3);
}

.content-section {
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(10px);
  border-radius: 1rem;
  padding: 1.5rem 2rem;
  animation: fadeUp 1s ease-out 0.7s both;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
  width: 90%;
  max-width: 1300px;
  margin: 0 auto 1.5rem;
}

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.section-title {
  font-size: clamp(1.2rem, 2.5vw, 1.6rem);
  margin: 0 0 1rem;
  color: #ffffff;
  font-weight: 700;
  letter-spacing: 0.01em;
}

.section-body {
  font-size: clamp(0.95rem, 1.5vw, 1.05rem);
  line-height: 1.6;
  width: 100%;
  margin: 0 auto;
}

.section-body p {
  margin-bottom: 1rem;
}

.rip-progress-nav {
  width: 100%;
  max-width: 800px;
  margin: 0 auto 2rem;
  padding: 0 1rem;
}

.progress-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: rgba(1, 54, 92, 0.5);
  border-radius: 1rem;
  padding: 1rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
}

.progress-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  position: relative;
  z-index: 2;
  flex: 1;
}

.progress-step.active .step-number {
  background-color: #f39c12;
  color: white;
}

.progress-step.active .step-label {
  color: #f39c12;
  font-weight: 700;
}

.step-link {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-decoration: none;
  color: inherit;
  transition: transform 0.2s ease;
}

.step-link:hover {
  transform: translateY(-3px);
}

.step-link:hover .step-number {
  background-color: rgba(243, 156, 18, 0.7);
}

.step-number {
  width: 35px;
  height: 35px;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  margin-bottom: 0.5rem;
  transition: background-color 0.3s ease;
}

.step-label {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.9);
  transition: color 0.3s ease;
}

.progress-connector {
  width: 100%;
  height: 2px;
  background: rgba(255, 255, 255, 0.3);
  margin: 0 0.5rem;
  position: relative;
  top: -8px;
  flex: 1;
  max-width: 100px;
}

.survival-steps {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0;
}

.step-card {
  background: rgba(1, 54, 92, 0.7);
  border-radius: 0.75rem;
  padding: 1.25rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  text-align: center;
  position: relative;
}

.step-card .step-number {
  background: #f39c12;
  color: white;
  font-weight: 700;
  font-size: 1.2rem;
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 0.75rem;
}

.step-card h4 {
  margin: 0 0 0.75rem;
  font-size: 1.1rem;
  font-weight: 600;
  color: white;
}

.survival-steps-compact {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1.5rem;
  margin: 2rem 0;
}

.step-card-compact {
  background: rgba(1, 54, 92, 0.7);
  border-radius: 0.75rem;
  padding: 1rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  text-align: center;
  position: relative;
  width: 180px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.step-card-compact .step-number {
  background: #f39c12;
  color: white;
  font-weight: 700;
  font-size: 1.2rem;
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 0.5rem;
}

.step-card-compact h4 {
  margin: 0 0 0.5rem;
  font-size: 1rem;
  font-weight: 600;
  color: white;
}

.step-card-compact p {
  margin: 0;
  font-size: 0.9rem;
  line-height: 1.4;
}

.escape-diagram {
  margin: 2rem 0;
  text-align: center;
}

.video-importance {
  text-align: center;
  margin: 2rem 0 1rem;
  font-weight: 600;
  color: #f39c12;
  font-size: 1.05rem;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

.video-title {
  font-size: 1.3rem;
  color: #f39c12;
  margin-bottom: 1rem;
  font-weight: 600;
}

.escape-video {
  max-width: 100%;
  border-radius: 0.75rem;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
  min-height: 300px; /* Slightly taller for video content */
  background-color: rgba(1, 54, 92, 0.5); /* Fallback color if video is not available */
  width: 100%;
  max-height: 400px;
  object-fit: cover;
}

.video-error {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(1, 54, 92, 0.7) !important;
  min-height: 300px;
}

.video-error-message {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: rgba(255, 255, 255, 0.8);
  font-style: italic;
  background: rgba(0, 0, 0, 0.5);
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  text-align: center;
}

.retry-button {
  display: block;
  margin: 0.75rem auto 0;
  background: #f39c12;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.2s ease;
}

.retry-button:hover {
  background: #e67e22;
  transform: translateY(-2px);
}

.image-caption {
  margin-top: 0.75rem;
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.8);
  text-align: center;
}

.alert-box {
  display: flex;
  background: rgba(243, 156, 18, 0.15);
  border-radius: 0.75rem;
  padding: 1rem;
  margin: 1.5rem 0;
  border-left: 4px solid #f39c12;
}

.alert-box.warning {
  background: rgba(231, 76, 60, 0.15);
  border-left: 4px solid #e74c3c;
}

.alert-icon {
  font-size: 2rem;
  margin-right: 1rem;
  display: flex;
  align-items: center;
}

.alert-content {
  flex: 1;
}

.alert-content h4 {
  margin: 0 0 0.5rem;
  color: #f39c12;
  font-weight: 600;
}

.alert-box.warning .alert-content h4 {
  color: #e74c3c;
}

.emphasis {
  font-weight: 600;
  font-size: 1.05em;
  color: #f39c12;
  padding: 0.8rem;
  border-left: 3px solid #f39c12;
  background: rgba(243, 156, 18, 0.1);
  border-radius: 0 0.5rem 0.5rem 0;
}

.parent-rescue-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.25rem;
  margin: 1.5rem 0;
}

.parent-rescue-card {
  background: rgba(1, 54, 92, 0.7);
  border-radius: 0.75rem;
  padding: 1.5rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  text-align: center;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.parent-rescue-card .step-number {
  position: absolute;
  top: -10px;
  left: -10px;
  background: #f39c12;
  color: white;
  font-weight: 700;
  font-size: 1.2rem;
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid rgba(255, 255, 255, 0.8);
}

.parent-rescue-card .rescue-icon {
  font-size: 2.2rem;
  margin-bottom: 1rem;
  color: #f39c12;
}

.parent-rescue-card h4 {
  margin: 0 0 0.75rem;
  font-size: 1.1rem;
  font-weight: 600;
  color: white;
}

.parent-rescue-card p {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.5;
}

.parent-warning {
  margin-top: 2.5rem;
  background: rgba(231, 76, 60, 0.2);
  border-left: 5px solid #e74c3c;
}

.child-danger-image {
  text-align: center;
  margin-bottom: 1.5rem;
}

.drowning-image {
  max-width: 100%;
  border-radius: 0.75rem;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
}

.image-error {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(1, 54, 92, 0.7) !important;
  min-height: 200px;
}

.image-error::after {
  content: "Image coming soon";
  color: rgba(255, 255, 255, 0.8);
  font-style: italic;
}

.next-section-arrow {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  display: flex;
  align-items: center;
  background: #f39c12;
  color: white;
  padding: 0.8rem 1.2rem;
  border-radius: 2rem;
  cursor: pointer;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  z-index: 10;
  transition: all 0.3s ease;
  animation: pulse 2s infinite;
}

.next-section-arrow:hover {
  background: #e67e22;
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
  animation: none;
}

.arrow-label {
  font-weight: 600;
  margin-right: 0.5rem;
  font-size: 1rem;
}

.arrow-icon {
  display: flex;
  align-items: center;
  justify-content: center;
}

@keyframes pulse {
  0% {
    transform: translateY(0) scale(1);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  }
  50% {
    transform: translateY(-5px) scale(1.05);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
  }
  100% {
    transform: translateY(0) scale(1);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  }
}

@media (max-width: 768px) {
  .content-wrapper {
    padding-top: 3.5rem;
  }
  
  .main-content {
    padding: 0 1rem 2rem;
  }
  
  .content-section {
    padding: 1.25rem 1.5rem;
    width: 95%;
  }
  
  .survival-steps {
    grid-template-columns: 1fr;
  }
  
  .rip-progress-nav {
    padding: 0;
    margin-bottom: 1.5rem;
  }
  
  .progress-bar {
    padding: 0.75rem;
  }
  
  .step-number {
    width: 30px;
    height: 30px;
    font-size: 0.9rem;
  }
  
  .step-label {
    font-size: 0.8rem;
  }
  
  .rescue-step {
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 1rem;
  }
  
  .rescue-icon {
    margin-bottom: 0.5rem;
  }
  
  .alert-box {
    flex-direction: column;
  }
  
  .alert-icon {
    margin-right: 0;
    margin-bottom: 0.75rem;
  }
  
  .escape-video {
    min-height: 220px;
    max-height: 300px;
  }
  
  .video-error {
    min-height: 220px;
  }
  
  .parent-rescue-grid {
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
  }
  
  .parent-rescue-card {
    padding: 1.25rem 1rem;
  }
  
  .parent-rescue-card .rescue-icon {
    font-size: 1.8rem;
    margin-bottom: 0.75rem;
  }
  
  .drowning-image {
    max-height: 250px;
  }
  
  .video-title {
    font-size: 1.2rem;
  }
  
  .next-section-arrow {
    bottom: 1.5rem;
    right: 1.5rem;
    padding: 0.6rem 1rem;
  }
  
  .arrow-label {
    font-size: 0.9rem;
  }
  
  .survival-steps-compact {
    gap: 1rem;
  }
  
  .step-card-compact {
    width: 160px;
    padding: 0.8rem;
  }
  
  .step-card-compact h4 {
    font-size: 0.95rem;
  }
  
  .step-card-compact p {
    font-size: 0.85rem;
  }
}

@media (max-width: 480px) {
  .content-wrapper {
    padding-top: 3rem;
  }
  
  .main-content {
    padding: 0 0.75rem 1rem;
  }
  
  .content-section {
    padding: 1rem;
  }
  
  .step-card {
    padding: 1rem;
  }
  
  .step-label {
    font-size: 0.7rem;
  }
  
  .step-number {
    width: 25px;
    height: 25px;
    font-size: 0.8rem;
    margin-bottom: 0.3rem;
  }
  
  .progress-connector {
    top: -5px;
  }
  
  .escape-video {
    min-height: 180px;
    max-height: 240px;
  }
  
  .video-error {
    min-height: 180px;
  }
  
  .parent-rescue-grid {
    grid-template-columns: 1fr;
  }
  
  .parent-rescue-card {
    padding: 1.25rem 0.75rem;
  }
  
  .drowning-image {
    max-height: 200px;
  }
  
  .video-title {
    font-size: 1.1rem;
  }
  
  .next-section-arrow {
    bottom: 1rem;
    right: 1rem;
  }
}

@media (max-width: 576px) {
  .survival-steps-compact {
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
  }
  
  .step-card-compact {
    width: 140px;
    padding: 0.7rem;
  }
}

/* Bystander image hotspots */
.hotspot-reach {
  top: 35%;
  right: 15%;
}

.hotspot-throw {
  top: 45%;
  right: 30%;
}

.hotspot-wade {
  bottom: 25%;
  right: 40%;
}

/* Child in danger hotspots */
.hotspot-stay-calm {
  top: 10%;
  left: 20%;
}

.hotspot-throw {
  top: 25%;
  right: 25%;
}

.hotspot-get-help {
  bottom: 40%;
  right: 55%;
}

.child-danger-container {
  position: relative;
  width: 100%;
  max-width: 800px;
  margin: 1rem auto 1.5rem;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
  height: 450px;
}

.child-danger-image {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
  object-position: center;
}

.image-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.3);
  pointer-events: none;
}

/* Interactive hotspots styles */
.interactive-hotspots {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 5;
}

.hotspot {
  position: absolute;
  width: 40px;
  height: 40px;
  cursor: pointer;
  z-index: 6;
}

.hotspot .hotspot-number {
  position: relative;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: #f39c12;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  font-weight: 700;
  border: 2px solid white;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.3);
  transition: all 0.3s ease;
  z-index: 7;
}

.hotspot:hover .hotspot-number {
  transform: scale(1.1);
  background-color: #e67e22;
}

.hotspot-content {
  position: absolute;
  width: 250px;
  background: rgba(0, 0, 0, 0.8);
  border-radius: 0.5rem;
  padding: 1rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
  color: white;
  font-size: 0.9rem;
  z-index: 8;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
  pointer-events: none;
}

.hotspot-stay-calm .hotspot-content {
  left: 0;
  top: 50px;
}

.hotspot-throw .hotspot-content {
  right: 0;
  top: 50px;
}

.hotspot-get-help .hotspot-content {
  right: 0;
  top: 50px;
}

.hotspot-content h4 {
  color: #f39c12;
  margin: 0 0 0.5rem;
  font-size: 1rem;
  font-weight: 600;
}

.hotspot-content p {
  margin: 0;
  line-height: 1.4;
}

.hotspot:hover .hotspot-content {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

/* Hotspot pulse animation */
.hotspot .hotspot-number:after {
  content: '';
  position: absolute;
  top: -8px;
  left: -8px;
  width: calc(100% + 16px);
  height: calc(100% + 16px);
  border-radius: 50%;
  border: 2px solid #f39c12;
  opacity: 0;
  animation: pulse-ring 2s infinite ease-out;
  z-index: 6;
}

@keyframes pulse-ring {
  0% {
    transform: scale(0.8);
    opacity: 0.8;
  }
  70% {
    opacity: 0.2;
  }
  100% {
    transform: scale(1.3);
    opacity: 0;
  }
}

@media (max-width: 768px) {
  .child-danger-container {
    height: 350px;
  }
  
  .hotspot .hotspot-number {
    width: 35px;
    height: 35px;
    font-size: 1rem;
  }
  
  .hotspot-content {
    width: 200px;
    padding: 0.75rem;
    font-size: 0.85rem;
  }
}

@media (max-width: 480px) {
  .child-danger-container {
    height: 300px;
  }
  
  .hotspot .hotspot-number {
    width: 30px;
    height: 30px;
    font-size: 0.9rem;
  }
  
  .hotspot-content {
    width: 180px;
    padding: 0.75rem;
    font-size: 0.8rem;
  }
  
  .hotspot-content h4 {
    font-size: 0.9rem;
  }
}
</style> 