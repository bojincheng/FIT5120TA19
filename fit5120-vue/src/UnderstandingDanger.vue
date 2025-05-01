<template>
  <div class="understanding-danger-page">
    <div class="bg-image"></div>
    <div class="overlay"></div>
    
    <!-- Beach Menu Component -->
    <BeachMenu :menuOpen="menuOpen" @toggle-menu="toggleMenu" />
    
    <div class="content-wrapper">
      <div class="main-content">
        <div class="safety-progress-nav">
          <div class="progress-bar">
            <div class="progress-step">
              <router-link to="/beach-safety-practices" class="step-link">
                <div class="step-number">1</div>
                <div class="step-label">Picking the Right Spot</div>
              </router-link>
            </div>
            <div class="progress-connector"></div>
            <div class="progress-step active">
              <div class="step-number">2</div>
              <div class="step-label">Understanding Rip Currents</div>
            </div>
            <div class="progress-connector"></div>
            <div class="progress-step">
              <router-link to="/spot-rip-currents" class="step-link">
                <div class="step-number">3</div>
                <div class="step-label">Avoiding Rip Currents</div>
              </router-link>
            </div>
          </div>
        </div>
        
        <div class="title-section">
          <h1>Understanding Rip Currents</h1>
          <div class="statistic-banner">
          </div>
        </div>

        <div class="content-section">
          <h2 class="section-title">🌊 What Are Rip Currents & How To Spot Them</h2>
          
          <div class="section-body">
            <div class="key-stats-container">
              <div class="key-stat">
                <div class="stat-number">80%</div>
                <div class="stat-text">of beach rescues in Australia are due to rip currents</div>
              </div>
              <div class="key-stat">
                <div class="stat-number">9 km/h</div>
                <div class="stat-text">speed of rip currents, nearly twice as fast as Olympic swimmers</div>
              </div>
            </div>
            
            <p class="intro-text">Rip currents are powerful, narrow channels of fast-moving water that flow away from the shore.</p>
            
            <div class="rip-video-container">
              <div class="video-wrapper">
                <video controls class="rip-video" @error="handleVideoError">
                  <source src="/videos/how_rips_form.mp4" type="video/mp4">
                  Your browser does not support the video tag.
                </video>
                
                <!-- Interactive Hotspots -->
                <div class="interactive-hotspots">
                  <div class="hotspot hotspot-1">
                    <div class="hotspot-number">1</div>
                    <div class="hotspot-content">
                      <h4>Water Appearance</h4>
                      <p>Notice the darker, deeper looking water - this is a rip current channel</p>
                    </div>
                  </div>
                  
                  <div class="hotspot hotspot-2">
                    <div class="hotspot-number">2</div>
                    <div class="hotspot-content">
                      <h4>Disrupted Wave Pattern</h4>
                      <p>Waves break on either side but not in the rip channel</p>
                    </div>
                  </div>
                  
                  <div class="hotspot hotspot-3">
                    <div class="hotspot-number">3</div>
                    <div class="hotspot-content">
                      <h4>Moving Debris or Foam</h4>
                      <p>Foam and debris moving steadily away from shore</p>
                    </div>
                  </div>
                  
                  <div class="hotspot hotspot-4">
                    <div class="hotspot-number">4</div>
                    <div class="hotspot-content">
                      <h4>Surface Ripples</h4>
                      <p>Choppy, rippled surface extending beyond the surf zone</p>
                    </div>
                  </div>
                </div>
              </div>
              <p class="video-caption">Video: How rip currents form and flow out to sea. Hover over numbers to identify key features.</p>
            </div>
            
            <div class="danger-explanation">
              <div class="alert-box">
                <div class="alert-icon">⚠️</div>
                <div class="alert-content">
                  <h4>Rip Current Myth vs. Reality</h4>
                  <p>Rips don't pull you under—they pull you away from shore. Drowning happens from panic and exhaustion. <router-link to="/survive-rip-currents" class="text-link">Learn how to survive rip currents</router-link>.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <div class="next-section-arrow" v-if="showNavigationArrow" @click="navigateToNextSection">
      <div class="arrow-label">Avoiding Rip Currents</div>
      <div class="arrow-icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M8 12h8"/><path d="m12 8 4 4-4 4"/></svg>
      </div>
    </div>
  </div>
</template>

<script>
import BeachMenu from './components/BeachMenu.vue'

export default {
  name: 'UnderstandingDanger',
  components: {
    BeachMenu
  },
  data() {
    return {
      menuOpen: false,
      activeDanger: null,
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
    handleVideoError(e) {
      // Add a placeholder class to show a styled error state
      e.target.classList.add('video-error');
    },
    setActiveDanger(dangerId) {
      // If clicking the already active card, close it
      // Otherwise, set this card as the active one
      this.activeDanger = (this.activeDanger === dangerId) ? null : dangerId;
    },
    setActiveNavLink() {
      // Remove active class from all nav links
      document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
      });
      document.querySelectorAll('.mobile-nav-link').forEach(link => {
        link.classList.remove('active');
      });
      
      // Add active class to beach safety practices links
      const desktopPracticesLink = document.querySelector('.nav-link[href="/beach-safety-practices"]');
      const mobilePracticesLink = document.querySelector('.mobile-nav-link[href="/beach-safety-practices"]');
      
      if (desktopPracticesLink) desktopPracticesLink.classList.add('active');
      if (mobilePracticesLink) mobilePracticesLink.classList.add('active');
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
        path: '/spot-rip-currents',
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
.understanding-danger-page {
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

.alert-box {
  display: flex;
  background: rgba(243, 156, 18, 0.15);
  border-radius: 0.75rem;
  padding: 1rem;
  margin: 1.5rem 0;
  border-left: 4px solid #f39c12;
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
  margin: 0 0 0.6rem;
  color: #f39c12;
  font-weight: 600;
  font-size: 1.3rem;
}

.alert-content p {
  margin: 0;
  font-size: 1.15rem;
  line-height: 1.5;
}

.danger-explanation {
  margin: 1.5rem 0;
  background: rgba(1, 54, 92, 0.2);
  padding: 1.5rem;
  border-radius: 0.75rem;
  border-left: 3px solid #f39c12;
}

.explanation-title {
  color: #f39c12;
  font-size: 1.2rem;
  margin-top: 0;
  margin-bottom: 1rem;
  font-weight: 600;
}

.conclusion-note {
  font-weight: 600;
  font-style: italic;
  margin-top: 1.5rem;
  color: #f39c12;
}

.danger-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0;
}

.danger-card {
  background: rgba(1, 54, 92, 0.7);
  border-radius: 0.75rem;
  border-left: 3px solid #f39c12;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  margin-bottom: 0.5rem;
}

.danger-card.active {
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
  background: rgba(1, 54, 92, 0.8);
}

.card-header {
  display: flex;
  align-items: center;
  padding: 1rem;
  position: relative;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.card-header:hover {
  background: rgba(1, 54, 92, 0.9);
}

.danger-icon {
  font-size: 1.5rem;
  margin-right: 1rem;
  color: #f39c12;
}

.card-header h4 {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 600;
  color: white;
  flex: 1;
}

.expand-icon {
  font-size: 1.5rem;
  font-weight: 300;
  color: rgba(255, 255, 255, 0.7);
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-body {
  height: 0;
  overflow: hidden;
  transition: height 0.3s ease;
}

.card-body.expanded {
  height: auto;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.card-content {
  padding: 1rem;
}

.card-body p {
  margin: 0.7rem 0;
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.9);
}

.text-link {
  color: #f39c12;
  text-decoration: underline;
  font-weight: 600;
  transition: color 0.2s ease;
}

.text-link:hover {
  color: #e67e22;
}

/* Progress Bar Styles */
.safety-progress-nav {
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
  flex: 1;
  height: 2px;
  background: rgba(255, 255, 255, 0.3);
  margin: 0 0.5rem;
  position: relative;
  top: -8px;
}

/* Next Section Arrow Styles */
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

/* Responsive adjustments */
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
  
  .alert-box {
    flex-direction: column;
  }
  
  .alert-icon {
    margin-right: 0;
    margin-bottom: 0.75rem;
  }
  
  .safety-progress-nav {
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
  
  .next-section-arrow {
    bottom: 1.5rem;
    right: 1.5rem;
    padding: 0.6rem 1rem;
  }
  
  .arrow-label {
    font-size: 0.9rem;
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
  
  .next-section-arrow {
    bottom: 1rem;
    right: 1rem;
  }
}

.rip-video-container {
  margin: 2rem auto;
  text-align: center;
  width: 100%;
  max-width: 1000px;
}

.video-wrapper {
  position: relative;
  width: 100%;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
}

.rip-video {
  width: 100%;
  display: block;
  height: auto;
  min-height: 500px;
  object-fit: cover;
}

.interactive-hotspots {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 5;
}

.hotspot {
  position: absolute;
  pointer-events: auto;
}

.hotspot-1 {
  top: 40%;
  left: 30%;
}

.hotspot-2 {
  top: 25%;
  right: 35%;
}

.hotspot-3 {
  bottom: 35%;
  left: 20%;
}

.hotspot-4 {
  bottom: 30%;
  right: 25%;
}

.hotspot-number {
  width: 36px;
  height: 36px;
  background: #f39c12;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 1.1rem;
  cursor: pointer;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
  transition: all 0.3s ease;
  z-index: 5;
  position: relative;
  animation: pulse-hotspot 2s infinite;
  border: 2px solid #fff;
}

.hotspot-number::after {
  content: "Hover me!";
  position: absolute;
  bottom: -30px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.7rem;
  white-space: nowrap;
  opacity: 0.8;
  font-weight: normal;
}

.hotspot:hover .hotspot-number::after {
  opacity: 0;
}

.hotspot-content {
  position: absolute;
  background: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(5px);
  padding: 12px 15px;
  border-radius: 8px;
  width: 220px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.4);
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
  z-index: 6;
  left: 50%;
  transform: translateX(-50%) translateY(10px);
  bottom: 100%;
  margin-bottom: 10px;
  pointer-events: none;
  border-left: 3px solid #f39c12;
}

.hotspot:hover .hotspot-content {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
}

.hotspot-content:after {
  content: '';
  position: absolute;
  bottom: -8px;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 0;
  border-left: 8px solid transparent;
  border-right: 8px solid transparent;
  border-top: 8px solid rgba(0, 0, 0, 0.8);
}

.hotspot-content h4 {
  color: #f39c12;
  margin: 0 0 5px;
  font-size: 0.9rem;
  font-weight: 600;
}

.hotspot-content p {
  margin: 0;
  font-size: 0.85rem;
  line-height: 1.3;
}

@keyframes pulse-hotspot {
  0% {
    transform: scale(1);
    box-shadow: 0 0 0 0 rgba(243, 156, 18, 0.7);
  }
  
  70% {
    transform: scale(1.1);
    box-shadow: 0 0 0 10px rgba(243, 156, 18, 0);
  }
  
  100% {
    transform: scale(1);
    box-shadow: 0 0 0 0 rgba(243, 156, 18, 0);
  }
}

@media (max-width: 768px) {
  .hotspot-number {
    width: 30px;
    height: 30px;
    font-size: 1rem;
  }
  
  .hotspot-content {
    width: 180px;
    padding: 10px 12px;
  }
  
  .hotspot-number::after {
    font-size: 0.65rem;
    bottom: -25px;
  }
}

@media (max-width: 480px) {
  .hotspot-number {
    width: 24px;
    height: 24px;
    font-size: 0.9rem;
  }
  
  .hotspot-content {
    width: 150px;
  }
  
  .hotspot-content h4 {
    font-size: 0.8rem;
  }
  
  .hotspot-content p {
    font-size: 0.75rem;
  }
  
  .hotspot-number::after {
    display: none;
  }
}

.video-caption {
  margin-top: 0.75rem;
  font-size: 1.1rem;
  color: rgba(255, 255, 255, 0.9);
  text-align: center;
  font-weight: 500;
}

.video-error {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(1, 54, 92, 0.7) !important;
  min-height: 300px;
}

.video-error::after {
  content: "Video unavailable";
  color: rgba(255, 255, 255, 0.8);
  font-style: italic;
}

/* Add styles for key statistics */
.key-stats-container {
  display: flex;
  justify-content: center;
  gap: 2rem;
  margin: 0 0 2rem;
  flex-wrap: wrap;
  padding-top: 1rem;
}

.key-stat {
  background: rgba(243, 156, 18, 0.2);
  border-radius: 10px;
  padding: 1.5rem;
  text-align: center;
  flex: 1;
  min-width: 200px;
  max-width: 400px;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
  border-left: 4px solid #f39c12;
}

.key-stat:hover {
  /* Removed hover effect */
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 700;
  color: #f39c12;
  margin-bottom: 0.5rem;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.stat-text {
  font-size: 1rem;
  line-height: 1.4;
}

@media (max-width: 768px) {
  .key-stats-container {
    gap: 1rem;
  }

  .key-stat {
    padding: 1.25rem;
    min-width: 160px;
  }

  .stat-number {
    font-size: 2rem;
  }

  .stat-text {
    font-size: 0.9rem;
  }
}

.intro-text {
  text-align: center;
  width: 100%;
  margin: 0 auto 1.5rem;
  font-size: 1.3rem;
  font-weight: 500;
  color: #ffffff;
  line-height: 1.5;
  padding: 0 1rem;
}
</style> 