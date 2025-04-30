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
            <div class="progress-step active">
              <div class="step-number">1</div>
              <div class="step-label">What Are Rips</div>
            </div>
            <div class="progress-connector"></div>
            <div class="progress-step">
              <router-link to="/spot-rip-currents" class="step-link">
                <div class="step-number">2</div>
                <div class="step-label">Spot Rip Currents</div>
              </router-link>
            </div>
            <div class="progress-connector"></div>
            <div class="progress-step">
              <router-link to="/survive-rip-currents" class="step-link">
                <div class="step-number">3</div>
                <div class="step-label">Survive Rip Currents</div>
              </router-link>
            </div>
            <div class="progress-connector"></div>
            <div class="progress-step">
              <router-link to="/safety-tool" class="step-link">
                <div class="step-number">4</div>
                <div class="step-label">Safety Tools</div>
              </router-link>
            </div>
          </div>
        </div>
        
        <div class="title-section">
          <h1>Rip Current Safety Guide</h1>
          <div class="statistic-banner">
            <h2 class="headline">Rip currents: Australia's <span class="highlight">#1</span> beach danger causing <span class="highlight">80%</span> of rescues</h2>
            <p class="subheadline">— Learn how to identify, avoid, and escape these dangerous water channels</p>
          </div>
        </div>

        <div class="content-section">
          <h2 class="section-title">🌊 What Are Rip Currents?</h2>
          
          <div class="section-body">
            <p>Rip currents are powerful, narrow channels of fast-moving water that flow away from the shore. They can move at speeds up to 2.5 meters per second — faster than an Olympic swimmer — and can quickly pull swimmers hundreds of meters offshore.</p>
            
            <div class="rip-video-container">
              <video controls class="rip-video" @error="handleVideoError">
                <source src="/videos/how_rips_form.mp4" type="video/mp4">
                Your browser does not support the video tag.
              </video>
              <p class="video-caption">Video: How rip currents form and flow out to sea</p>
            </div>
            
            <div class="rip-explanation">
              <h4 class="explanation-title">How Rip Currents Form and Their Dangers</h4>
              <p>Rip currents form when waves break unevenly along the shoreline, often due to sandbars, piers, jetties, or other underwater structures. When waves travel from deep to shallow water, they eventually break near the shore, creating a flow of water onto the beach. This water needs to return to the ocean, and the path of least resistance is often through channels between sandbars, creating a concentrated stream of water flowing back out to sea.</p>
              
              <p>What makes rip currents particularly dangerous:</p>
              
              <div class="danger-cards">
                <div class="danger-card" :class="{ active: activeDanger === 'appearance' }">
                  <div class="card-header" @click="setActiveDanger('appearance')">
                    <div class="danger-icon">👁️</div>
                    <h4>Deceptive Appearance</h4>
                    <div class="expand-icon">
                      <span>{{ activeDanger === 'appearance' ? '−' : '+' }}</span>
                    </div>
                  </div>
                  <div class="card-body" :class="{ expanded: activeDanger === 'appearance' }">
                    <div class="card-content">
                      <p>Rips can appear as relatively calm areas between breaking waves, misleading swimmers into thinking they're safe zones when they're actually the most dangerous part of the water.</p>
                    </div>
                  </div>
                </div>
                
                <div class="danger-card" :class="{ active: activeDanger === 'speed' }">
                  <div class="card-header" @click="setActiveDanger('speed')">
                    <div class="danger-icon">⚡</div>
                    <h4>Rapid Acceleration</h4>
                    <div class="expand-icon">
                      <span>{{ activeDanger === 'speed' ? '−' : '+' }}</span>
                    </div>
                  </div>
                  <div class="card-body" :class="{ expanded: activeDanger === 'speed' }">
                    <div class="card-content">
                      <p>They can quickly accelerate from walking speed to speeds no human can swim against, even Olympic swimmers can't outpace a strong rip current.</p>
                    </div>
                  </div>
                </div>
                
                <div class="danger-card" :class="{ active: activeDanger === 'variable' }">
                  <div class="card-header" @click="setActiveDanger('variable')">
                    <div class="danger-icon">📈</div>
                    <h4>Strength Variability</h4>
                    <div class="expand-icon">
                      <span>{{ activeDanger === 'variable' ? '−' : '+' }}</span>
                    </div>
                  </div>
                  <div class="card-body" :class="{ expanded: activeDanger === 'variable' }">
                    <div class="card-content">
                      <p>Rip current strength can suddenly increase with changing wave conditions, catching swimmers off-guard when conditions worsen unexpectedly.</p>
                    </div>
                  </div>
                </div>
                
                <div class="danger-card" :class="{ active: activeDanger === 'panic' }">
                  <div class="card-header" @click="setActiveDanger('panic')">
                    <div class="danger-icon">😨</div>
                    <h4>Psychological Impact</h4>
                    <div class="expand-icon">
                      <span>{{ activeDanger === 'panic' ? '−' : '+' }}</span>
                    </div>
                  </div>
                  <div class="card-body" :class="{ expanded: activeDanger === 'panic' }">
                    <div class="card-content">
                      <p>Being pulled away from shore causes panic, which leads to exhaustion and increases drowning risk. Most fatalities occur due to exhaustion from fighting the current rather than from the current itself.</p>
                    </div>
                  </div>
                </div>
                
                <div class="danger-card" :class="{ active: activeDanger === 'locations' }">
                  <div class="card-header" @click="setActiveDanger('locations')">
                    <div class="danger-icon">🗺️</div>
                    <h4>Unexpected Locations</h4>
                    <div class="expand-icon">
                      <span>{{ activeDanger === 'locations' ? '−' : '+' }}</span>
                    </div>
                  </div>
                  <div class="card-body" :class="{ expanded: activeDanger === 'locations' }">
                    <div class="card-content">
                      <p>They can form suddenly and in locations where they weren't present earlier in the day as tides, wave patterns, and sandbar shapes change.</p>
                    </div>
                  </div>
                </div>
              </div>
              
              <p class="conclusion-note">Understanding rip current safety and escape techniques is crucial for all beachgoers, especially for families with children and those unfamiliar with Australian beaches.</p>
            </div>
            
            <div class="alert-box">
              <div class="alert-icon">⚠️</div>
              <div class="alert-content">
                <h4>Myth vs. Reality</h4>
                <p>Rip currents are often incorrectly called "rip tides" or "undertow." Unlike tides, rip currents don't pull people under water—they pull people away from shore. Drowning occurs when people can't stay afloat due to panic, exhaustion, or inability to swim.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <div class="next-section-arrow" v-if="showNavigationArrow" @click="navigateToNextSection">
      <div class="arrow-label">Spot Rip Currents</div>
      <div class="arrow-icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M8 12h8"/><path d="m12 8 4 4-4 4"/></svg>
      </div>
    </div>
  </div>
</template>

<script>
import BeachMenu from './components/BeachMenu.vue'

export default {
  name: 'RipSafety',
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
    handleImageError(e) {
      // Add a placeholder class to show a styled error state
      e.target.classList.add('image-error');
      // Set the src to a data URI of a placeholder image or leave empty
      e.target.src = '';
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
      
      // Add active class to rip current safety links
      const desktopRipLink = document.querySelector('.nav-link[href="/rip-safety"]');
      const mobileRipLink = document.querySelector('.mobile-nav-link[href="/rip-safety"]');
      
      if (desktopRipLink) desktopRipLink.classList.add('active');
      if (mobileRipLink) mobileRipLink.classList.add('active');
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

.rip-video-container {
  margin: 1.5rem 0;
  text-align: center;
  width: 100%;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

.rip-video {
  width: 100%;
  max-width: 100%;
  background-color: transparent;
  border-radius: 0;
  box-shadow: none;
  filter: none;
}

.rip-video::-webkit-media-controls {
  background-color: transparent;
  border-radius: 0;
}

.rip-video::-webkit-media-controls-panel {
  padding: 0;
}

.video-caption {
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

.rip-explanation {
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
  
  .rip-video-container {
    max-width: 100%;
  }
  
  .rip-video {
    max-height: 300px;
  }
  
  .alert-box {
    flex-direction: column;
  }
  
  .alert-icon {
    margin-right: 0;
    margin-bottom: 0.75rem;
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

@media (max-width: 768px) {
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
}

@media (max-width: 480px) {
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
  .next-section-arrow {
    bottom: 1rem;
    right: 1rem;
  }
}
</style> 