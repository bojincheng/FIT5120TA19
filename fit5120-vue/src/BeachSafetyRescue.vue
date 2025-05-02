<template>
  <div class="beach-safety-page">
    <div class="bg-image"></div>
    <div class="overlay"></div>
    
    <!-- Beach Menu Component -->
    <BeachMenu :menuOpen="menuOpen" @toggle-menu="toggleMenu" />
    
    <div class="content-wrapper">
      <div class="main-content">
        <!-- Progress Bar -->
        <div class="safety-progress-nav">
          <div class="progress-bar">
            <div class="progress-step active">
              <div class="step-number">1</div>
              <div class="step-label">Signs of Trouble</div>
            </div>
            <div class="progress-connector"></div>
            <div class="progress-step">
              <router-link to="/survive-rip-currents" class="step-link">
                <div class="step-number">2</div>
                <div class="step-label">Survive Rip Currents</div>
              </router-link>
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
          <h1>Near-Shore Rescue Techniques</h1>
          <div class="statistic-banner">
          </div>
        </div>

        <!-- Main Content Section -->
        <div class="content-section">
          <h2 class="section-title">🚨 Recognizing a Swimmer in Distress</h2>
          
          <div class="section-body">
            <p>Before attempting any rescue, you must first be able to identify when someone is truly in danger.</p>
            
            <div class="drowning-statistic">
              <div class="stat-number">Nearly 50%</div>
              <div class="stat-text">of adults cannot correctly identify when someone is drowning.</div>
            </div>
            
            <div class="drowning-image-container">
              <img src="./assets/drowning.jpeg" alt="Person drowning with hand raised above water" class="drowning-image">
              <div class="image-overlay"></div>
              
              <!-- Interactive Hotspots -->
              <div class="interactive-hotspots">
                <div class="hotspot hotspot-1">
                  <div class="hotspot-number">1</div>
                  <div class="hotspot-content">
                    <h4>Weak or No Wave</h4>
                    <p>Unable to wave properly - may only raise one arm briefly as they struggle to stay afloat</p>
                  </div>
                </div>
                
                <div class="hotspot hotspot-2">
                  <div class="hotspot-number">2</div>
                  <div class="hotspot-content">
                    <h4>Unable to Call for Help</h4>
                    <p>Too focused on breathing to shout - drowning is often silent</p>
                  </div>
                </div>
                
                <div class="hotspot hotspot-3">
                  <div class="hotspot-number">3</div>
                  <div class="hotspot-content">
                    <h4>Vertical Position</h4>
                    <p>Upright in water with little forward movement, head tilted back</p>
                  </div>
                </div>
              </div>
              
              <div class="image-caption">Hover over numbers to learn the signs of a drowning person</div>
            </div>
          </div>
        </div>
        
        <div class="content-section">
          <h2 class="section-title">🛟 Rescue Techniques for Near-Shore Emergencies</h2>
          
          <div class="section-body">
            <div class="rescue-tabs">
              <div class="tab-buttons">
                <button 
                  class="tab-button" 
                  :class="{ active: activeRescueTab === 'lifeguard' }"
                  @click="activeRescueTab = 'lifeguard'"
                >
                  <span class="tab-icon">🏊‍♂️</span>
                  <span class="tab-label">When Lifeguards Respond</span>
                </button>
                <button 
                  class="tab-button" 
                  :class="{ active: activeRescueTab === 'bystander' }"
                  @click="activeRescueTab = 'bystander'"
                >
                  <span class="tab-icon">🪃</span>
                  <span class="tab-label">Safe Bystander Response</span>
                </button>
              </div>
              
              <div class="tab-content">
                <!-- Lifeguard Response Tab -->
                <div v-if="activeRescueTab === 'lifeguard'" class="rescue-technique">
                  <div class="lifeguard-image-container">
                    <img src="./assets/lifeguard rescue.jpg" alt="Lifeguards with red and yellow flags and rescue board" class="lifeguard-image">
                    <div class="image-overlay"></div>
                    <div class="image-overlay-button">
                      <router-link to="/water-safety-simulation" class="simulation-button">
                        <div class="sim-icon">
                          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polygon points="5 3 19 12 5 21 5 3"></polygon>
                          </svg>
                        </div>
                        <span>Try the Rescue Simulation</span>
                      </router-link>
                    </div>
                    <div class="image-caption">Professional lifeguards on duty with rescue equipment between the flags</div>
                  </div>
                  
                  <div class="parent-actions">
                    <h4 class="parent-actions-title">What To Do While Waiting For Professional Help</h4>
                    
                    <div class="parent-action-card">
                      <div class="action-number">1</div>
                      <div class="action-content">
                        <h5>Call For Help</h5>
                        <p>Alert lifeguards immediately or call 000. Wave arms overhead and shout "HELP" to draw attention to the emergency.</p>
                      </div>
                    </div>
                    
                    <div class="parent-action-card">
                      <div class="action-number">2</div>
                      <div class="action-content">
                        <h5>Stay On Shore</h5>
                        <p><strong>DO NOT</strong> enter deep water yourself. Parents who enter water often become victims themselves, making the rescue more difficult.</p>
                      </div>
                    </div>
                    
                    <div class="parent-action-card">
                      <div class="action-number">3</div>
                      <div class="action-content">
                        <h5>Guide Rescuers</h5>
                        <p>Keep pointing to the person in trouble, maintain visual contact, and help direct lifeguards to their exact location.</p>
                      </div>
                    </div>
                  </div>
                </div>
                
                <!-- Bystander Response Tab -->
                <div v-if="activeRescueTab === 'bystander'" class="rescue-technique">
                  <div class="bystander-image-container">
                    <img src="./assets/bystander.jpg" alt="Person reaching from shore to help drowning victim" class="bystander-image">
                    <div class="image-overlay"></div>
                    
                    <!-- Interactive Hotspots -->
                    <div class="interactive-hotspots">
                      <div class="hotspot hotspot-reach">
                        <div class="hotspot-number">1</div>
                        <div class="hotspot-content">
                          <h4>REACH</h4>
                          <p>If the person is close to shore, use a pole, branch, or towel to reach them without entering the water.</p>
                        </div>
                      </div>
                      
                      <div class="hotspot hotspot-throw">
                        <div class="hotspot-number">2</div>
                        <div class="hotspot-content">
                          <h4>THROW</h4>
                          <p>If they're further out, throw a flotation device (life ring, bodyboard, esky lid) with a rope attached if possible.</p>
                        </div>
                      </div>
                      
                      <div class="hotspot hotspot-wade">
                        <div class="hotspot-number">3</div>
                        <div class="hotspot-content">
                          <h4>WADE</h4>
                          <p>If safe to do so, wade into shallow water (keeping your feet firmly on the bottom) to reach them with an extended device.</p>
                        </div>
                      </div>
                    </div>
                    
                    <div class="image-caption">Hover over numbers to learn safe rescue methods without entering deep water</div>
                  </div>
                  
                  <p class="technique-description">Methods that can be used by untrained rescuers without entering deep water</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="content-section">
          <h2 class="section-title">🩹 Post-Rescue Care</h2>
          
          <div class="section-body">
            <p class="post-rescue-intro">After a successful rescue, immediate care is crucial. Hover over cards to see details:</p>
            
            <div class="flip-cards-container">
              <div class="flip-card">
                <div class="flip-card-inner">
                  <div class="flip-card-front">
                    <img src="./assets/breathing.png" alt="Person administering breathing support" class="card-image">
                    <div class="card-overlay"></div>
                    <div class="card-title">Check Breathing</div>
                    <div class="flip-hint">Hover to flip</div>
                  </div>
                  <div class="flip-card-back">
                    <h4>Check Breathing</h4>
                    <p>Ensure their airway is clear and they're breathing normally. Begin CPR if necessary.</p>
                  </div>
                </div>
              </div>

              <div class="flip-card">
                <div class="flip-card-inner">
                  <div class="flip-card-front">
                    <img src="./assets/000.jpg" alt="000 Emergency number on red background" class="card-image">
                    <div class="card-overlay"></div>
                    <div class="card-title">Call 000</div>
                    <div class="flip-hint">Hover to flip</div>
                  </div>
                  <div class="flip-card-back">
                    <h4>Seek Medical Attention</h4>
                    <p>Always get medical help after a water rescue, even if they seem fine. Secondary drowning can occur hours later.</p>
                  </div>
                </div>
              </div>

              <div class="flip-card">
                <div class="flip-card-inner">
                  <div class="flip-card-front">
                    <img src="./assets/treat_shock.jpg" alt="Person in distress" class="card-image">
                    <div class="card-overlay"></div>
                    <div class="card-title">Treat for Shock</div>
                    <div class="flip-hint">Hover to flip</div>
                  </div>
                  <div class="flip-card-back">
                    <h4>Treat for Shock</h4>
                    <p>Keep them warm with towels or blankets, even on hot days.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <div class="next-section-arrow" v-if="showNavigationArrow" @click="navigateToNextSection">
      <div class="arrow-label">Survive Rip Currents</div>
      <div class="arrow-icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M8 12h8"/><path d="m12 8 4 4-4 4"/></svg>
      </div>
    </div>
  </div>
</template>

<script>
import BeachMenu from './components/BeachMenu.vue'

export default {
  name: 'BeachSafetyRescue',
  components: {
    BeachMenu
  },
  data() {
    return {
      menuOpen: false,
      showNavigationArrow: false,
      activeRescueTab: 'lifeguard' // Default active tab
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
    setActiveNavLink() {
      // Remove active class from all nav links
      document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
      });
      document.querySelectorAll('.mobile-nav-link').forEach(link => {
        link.classList.remove('active');
      });
      
      // Add active class to "Facing the Risk" links
      const desktopRipLink = document.querySelector('.nav-link[href="/beach-safety-rescue"]');
      const mobileRipLink = document.querySelector('.mobile-nav-link[href="/beach-safety-rescue"]');
      
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
      // Navigate to the next section in the sequence
      this.$router.push({ 
        path: '/survive-rip-currents',
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
.beach-safety-page {
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

/* Interactive Hotspots */
.interactive-hotspots {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

.drowning-statistic {
  background-color: rgba(243, 156, 18, 0.9);
  border-radius: 8px;
  padding: 1.5rem;
  margin: 1.5rem auto;
  max-width: 700px;
  text-align: center;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
  animation: pulse-stat 2.5s infinite;
}

.stat-number {
  font-size: 2rem;
  font-weight: 800;
  color: white;
  margin-bottom: 0.5rem;
}

.stat-text {
  font-size: 1.2rem;
  color: white;
  font-weight: 600;
}

@keyframes pulse-stat {
  0% {
    transform: scale(1);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
  }
  50% {
    transform: scale(1.02);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
  }
  100% {
    transform: scale(1);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
  }
}

@media (max-width: 768px) {
  .drowning-statistic {
    padding: 1.2rem;
    margin: 1.2rem auto;
  }
  
  .stat-number {
    font-size: 1.7rem;
  }
  
  .stat-text {
    font-size: 1.1rem;
  }
}

@media (max-width: 576px) {
  .drowning-statistic {
    padding: 1rem;
    margin: 1rem auto;
  }
  
  .stat-number {
    font-size: 1.5rem;
  }
  
  .stat-text {
    font-size: 1rem;
  }
}

.hotspot {
  position: absolute;
  pointer-events: auto;
}

.hotspot-1 {
  top: 45%;
  left: 60%;
}

.hotspot-2 {
  top: 35%;
  right: 30%;
}

.hotspot-3 {
  bottom: 30%;
  left: 40%;
}

/* Bystander image hotspots */
.hotspot-reach {
  top: 35%;
  right: 15%;
}

.hotspot-throw {
  bottom: 30%;
  left: 25%;
}

.hotspot-wade {
  bottom: 25%;
  right: 40%;
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
  content: "Hover me";
  position: absolute;
  top: -25px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 3px 8px;
  border-radius: 4px;
  font-size: 0.7rem;
  white-space: nowrap;
  opacity: 0.9;
  transition: opacity 0.3s ease;
  z-index: 5;
}

.hotspot:hover .hotspot-number::after {
  opacity: 0;
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

.hotspot-content {
  position: absolute;
  background: rgba(0, 0, 0, 0.95);
  backdrop-filter: blur(5px);
  padding: 12px 15px;
  border-radius: 8px;
  width: 250px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.4);
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.3s ease, transform 0.3s ease;
  z-index: 10;
  left: 50%;
  transform: translateX(-50%) translateY(10px);
  bottom: 100%;
  margin-bottom: 10px;
  pointer-events: none;
  border-left: 3px solid #f39c12;
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
  border-top: 8px solid rgba(0, 0, 0, 0.95);
}

.hotspot:hover .hotspot-number {
  transform: scale(1.2);
  background-color: #e67e22;
  border: 2px solid white;
  box-shadow: 0 4px 12px rgba(243, 156, 18, 0.6);
}

.hotspot:hover .hotspot-content {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(-5px);
}

.hotspot-content h4 {
  color: #f39c12;
  margin: 0 0 7px;
  font-size: 1rem;
  font-weight: 600;
}

.hotspot-content p {
  margin: 0;
  font-size: 0.9rem;
  line-height: 1.4;
}

/* Post-Rescue Styles */
.post-rescue-intro {
  font-size: 1.1rem;
  margin-bottom: 1.5rem;
  text-align: center;
  color: #f39c12;
  font-weight: 600;
}

.flip-cards-container {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  margin: 2rem 0;
  justify-content: center;
}

.flip-card {
  width: 280px;
  height: 350px;
  perspective: 1000px;
  margin-bottom: 1rem;
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.8s;
  transform-style: preserve-3d;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  border-radius: 12px;
}

.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

.flip-card-front, .flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  border-radius: 12px;
  overflow: hidden;
}

.flip-card-front {
  background-color: #01365c;
  color: white;
}

.card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  position: absolute;
  top: 0;
  left: 0;
}

.emergency-image {
  object-position: right center;
}

.card-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.7));
  z-index: 1;
}

.card-title {
  position: absolute;
  bottom: 50px;
  left: 0;
  width: 100%;
  padding: 0 1rem;
  font-size: 1.4rem;
  font-weight: 700;
  color: white;
  z-index: 2;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.6);
}

.flip-hint {
  position: absolute;
  bottom: 15px;
  left: 0;
  width: 100%;
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.9);
  z-index: 2;
  padding: 5px 0;
  background-color: rgba(0, 0, 0, 0.5);
}

.flip-card-back {
  background-color: #3498db;
  color: white;
  transform: rotateY(180deg);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 2rem;
}

.flip-card-back h4 {
  color: white;
  font-size: 1.5rem;
  margin-bottom: 1.5rem;
  text-align: center;
  font-weight: 700;
}

.flip-card-back p {
  font-size: 1.1rem;
  line-height: 1.6;
  text-align: center;
  margin: 0;
}

/* Navigation Arrow */
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

/* Responsive Styles */
@media (max-width: 992px) {
  .flip-cards-container {
    gap: 1.5rem;
  }
  
  .flip-card {
    width: 250px;
    height: 320px;
  }
  
  .card-title {
    font-size: 1.3rem;
    bottom: 45px;
  }
}

@media (max-width: 768px) {
  .flip-cards-container {
    gap: 1rem;
  }
  
  .flip-card {
    width: 220px;
    height: 300px;
  }
  
  .card-title {
    font-size: 1.2rem;
    bottom: 40px;
  }
  
  .flip-hint {
    font-size: 0.8rem;
  }
  
  .flip-card-back h4 {
    font-size: 1.3rem;
    margin-bottom: 1rem;
  }
  
  .flip-card-back p {
    font-size: 1rem;
  }
}

@media (max-width: 576px) {
  .flip-cards-container {
    flex-direction: column;
    align-items: center;
    gap: 2rem;
  }
  
  .flip-card {
    width: 280px;
    height: 350px;
    margin-bottom: 0;
  }
  
  .card-title {
    font-size: 1.4rem;
    bottom: 50px;
  }
  
  .flip-hint {
    font-size: 0.9rem;
  }
}

/* Update CSS for the drowning image to make it smaller */
.drowning-image-container {
  position: relative;
  width: 100%;
  max-width: 700px;
  margin: 1.5rem auto 2rem;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
  height: 400px;
}

.drowning-image {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
  object-position: center;
}

.image-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 40%;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.8), transparent);
}

.image-caption {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 1rem;
  color: white;
  font-size: 1.1rem;
  font-weight: 500;
  text-align: center;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

@media (max-width: 768px) {
  .hotspot-number {
    width: 30px;
    height: 30px;
    font-size: 1rem;
  }
  
  .hotspot-content {
    width: 220px;
    padding: 10px 12px;
  }
  
  .hotspot-number::after {
    font-size: 0.65rem;
    padding: 2px 6px;
  }
  
  .hotspot-content h4 {
    font-size: 0.9rem;
  }
  
 .hotspot-content p {
    font-size: 0.8rem;
  }
  
  .drowning-image-container {
    height: 350px;
  }
}

@media (max-width: 480px) {
  .hotspot-number {
    width: 24px;
    height: 24px;
    font-size: 0.9rem;
  }
  
  .hotspot-content {
    width: 180px;
  }
  
  .hotspot-number::after {
    display: none;
  }
  
  .drowning-image-container {
    height: 300px;
  }
}

/* Add CSS for the tabbed interface */
.rescue-tabs {
  margin: 1.5rem 0;
}

.tab-buttons {
  display: flex;
  border-bottom: 2px solid rgba(255, 255, 255, 0.1);
  margin-bottom: 1.5rem;
}

.tab-button {
  background: transparent;
  border: none;
  padding: 0.75rem 1.5rem;
  color: rgba(255, 255, 255, 0.7);
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  border-bottom: 3px solid transparent;
  display: flex;
  align-items: center;
  flex: 1;
  justify-content: center;
}

.tab-button.active {
  color: white;
  border-bottom-color: #3498db;
}

.tab-icon {
  font-size: 1.5rem;
  margin-right: 0.75rem;
}

.tab-label {
  white-space: nowrap;
}

.tab-content {
  position: relative;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .tab-buttons {
    flex-direction: column;
  }
  
  .tab-button {
    border-bottom: none;
    border-left: 3px solid transparent;
    justify-content: flex-start;
    padding: 0.75rem 1rem;
  }
  
  .tab-button.active {
    border-bottom-color: transparent;
    border-left-color: #3498db;
    background: rgba(52, 152, 219, 0.1);
  }
}

@media (max-width: 576px) {
  .tab-icon {
    font-size: 1.3rem;
    margin-right: 0.5rem;
  }
  
  .tab-label {
    font-size: 0.9rem;
  }
}

/* Add CSS for the lifeguard image */
.lifeguard-image-container {
  position: relative;
  width: 100%;
  max-width: 600px;
  margin: 1rem auto 1.5rem;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
  height: 300px;
}

.lifeguard-image {
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
  background: rgba(0, 0, 0, 0.4);
  transition: background 0.3s ease;
}

.lifeguard-image-container:hover .image-overlay {
  background: rgba(0, 0, 0, 0.6);
}

.image-overlay-button {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 5;
}

.image-overlay-button .simulation-button {
  transform: scale(1);
  transition: transform 0.3s ease, background-color 0.3s ease, box-shadow 0.3s ease;
}

.lifeguard-image-container:hover .simulation-button {
  transform: scale(1.1);
  background: #e67e22;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.5);
}

.image-caption {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 1rem;
  color: white;
  font-size: 1rem;
  font-weight: 500;
  text-align: center;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
  z-index: 2;
}

/* Keep existing simulation button styles */
.simulation-button {
  display: flex;
  align-items: center;
  background: #f39c12;
  color: white;
  text-decoration: none;
  padding: 0.8rem 1.5rem;
  border-radius: 2rem;
  font-weight: 600;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.sim-icon {
  margin-right: 0.75rem;
  display: flex;
  align-items: center;
}

/* Remove the old simulation button container */
.simulation-button-container {
  display: none;
}

@media (max-width: 768px) {
  .lifeguard-image-container {
    height: 250px;
    margin: 1rem auto 1.5rem;
  }
  
  .image-caption {
    font-size: 0.9rem;
    padding: 0.75rem;
  }
  
  .simulation-button {
    font-size: 0.95rem;
    padding: 0.7rem 1.3rem;
  }
  
  .sim-icon {
    margin-right: 0.6rem;
  }
  
  .sim-icon svg {
    width: 20px;
    height: 20px;
  }
}

@media (max-width: 480px) {
  .lifeguard-image-container {
    height: 200px;
  }
  
  .image-caption {
    font-size: 0.8rem;
    padding: 0.5rem;
  }
  
  .simulation-button {
    font-size: 0.9rem;
    padding: 0.6rem 1.1rem;
  }
  
  .sim-icon {
    margin-right: 0.5rem;
  }
  
  .sim-icon svg {
    width: 18px;
    height: 18px;
  }
}

/* Add CSS for the bystander image */
.bystander-image-container {
  position: relative;
  width: 100%;
  max-width: 800px;
  margin: 1rem auto 1.5rem;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
  height: 450px;
}

.bystander-image {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
  object-position: center;
}

@media (max-width: 768px) {
  .bystander-image-container {
    height: 350px;
    margin: 1rem auto 1.5rem;
  }
}

@media (max-width: 480px) {
  .bystander-image-container {
    height: 300px;
  }
}

/* Parent Actions CSS */
.parent-actions {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin: 1.5rem 0;
}

.parent-actions-title {
  font-size: 1.2rem;
  color: #ffffff;
  margin-bottom: 1rem;
  text-align: left;
  font-weight: 600;
}

.parent-action-card {
  display: flex;
  background: rgba(1, 54, 92, 0.6);
  border-radius: 0.75rem;
  padding: 1.25rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  border-left: 3px solid #3498db;
}

.action-number {
  font-size: 1.6rem;
  margin-right: 1.25rem;
  color: #ffffff;
  flex-shrink: 0;
  background-color: #3498db;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
}

.action-content h5 {
  color: #f39c12;
  margin: 0 0 0.5rem;
  font-size: 1.1rem;
  font-weight: 600;
}

.action-content p {
  margin: 0;
  font-size: 1rem;
  line-height: 1.5;
}

@media (max-width: 768px) {
  .parent-action-card {
    padding: 1rem;
  }
  
  .action-number {
    font-size: 1.4rem;
    margin-right: 1rem;
    width: 35px;
    height: 35px;
  }
  
  .action-content h5 {
    font-size: 1rem;
  }
  
  .action-content p {
    font-size: 0.95rem;
  }
}

@media (max-width: 480px) {
  .parent-action-card {
    padding: 0.8rem;
  }
  
  .action-number {
    font-size: 1.2rem;
    margin-right: 0.8rem;
    width: 30px;
    height: 30px;
  }
  
  .action-content h5 {
    font-size: 0.95rem;
  }
  
  .action-content p {
    font-size: 0.9rem;
  }
}

/* Bystander technique description */
.technique-description {
  text-align: center;
  font-size: 1.1rem;
  color: #f39c12;
  font-weight: 600;
  margin: 1.5rem 0;
}
</style> 