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
            <div class="progress-step">
              <router-link to="/beach-safety-practices" class="step-link">
                <div class="step-number">1</div>
                <div class="step-label">Beach Rules</div>
              </router-link>
            </div>
            <div class="progress-connector"></div>
            <div class="progress-step active">
              <div class="step-number">2</div>
              <div class="step-label">Near-Shore Rescue</div>
            </div>
            <div class="progress-connector"></div>
            <div class="progress-step">
              <router-link to="/offshore-rescue" class="step-link">
                <div class="step-number">3</div>
                <div class="step-label">Offshore Rescue</div>
              </router-link>
            </div>
          </div>
        </div>
        
        <div class="title-section">
          <h1>Near-Shore Rescue Techniques</h1>
          <div class="statistic-banner">
            <h2 class="headline">Swift, effective rescue methods for <span class="highlight">swimmers</span> in distress near the shore</h2>
            <p class="subheadline">— Learn to safely help others without putting yourself at risk</p>
          </div>
        </div>

        <!-- Main Content Section -->
        <div class="content-section">
          <h2 class="section-title">🚨 Recognizing a Swimmer in Distress</h2>
          
          <div class="section-body">
            <p>Before attempting any rescue, you must first be able to identify when someone is truly in danger. A swimmer in distress will often:</p>
            
            <div class="drowning-image-container">
              <img src="./assets/drowning.jpeg" alt="Person drowning with hand raised above water" class="drowning-image">
              <div class="image-overlay"></div>
              <div class="image-caption">A drowning person may only be able to raise one hand briefly above water</div>
            </div>
            
            <div class="distress-signs">
              <div class="distress-sign">
                <div class="sign-icon">👋</div>
                <div class="sign-content">
                  <h4>Weak or No Wave</h4>
                  <p>Unable to wave properly - may only raise one arm briefly as they struggle to stay afloat</p>
                </div>
              </div>
              
              <div class="distress-sign">
                <div class="sign-icon">🗣️</div>
                <div class="sign-content">
                  <h4>Unable to Call for Help</h4>
                  <p>Too focused on breathing to shout - drowning is often silent</p>
                </div>
              </div>
              
              <div class="distress-sign">
                <div class="sign-icon">🏊‍♂️</div>
                <div class="sign-content">
                  <h4>Vertical Position</h4>
                  <p>Upright in water with little forward movement, head tilted back</p>
                </div>
              </div>
              
              <div class="distress-sign">
                <div class="sign-icon">👀</div>
                <div class="sign-content">
                  <h4>Glassy Stare</h4>
                  <p>Unfocused eyes, possibly closed, or unable to fix on rescuer</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="content-section">
          <h2 class="section-title">🛟 Rescue Techniques for Near-Shore Emergencies</h2>
          
          <div class="section-body">
            <div class="safety-alert">
              <div class="alert-icon">⚠️</div>
              <div class="alert-content">
                <h4>Safety First!</h4>
                <p>Always call for help before attempting a rescue. Alert lifeguards if available, or have someone call emergency services (000).</p>
              </div>
            </div>
            
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
                  <div class="technique-header">
                    <div class="technique-icon">🏊‍♂️</div>
                    <h3>When Lifeguards Respond</h3>
                  </div>
                  
                  <div class="lifeguard-image-container">
                    <img src="./assets/lifeguard rescue.jpg" alt="Lifeguards with red and yellow flags and rescue board" class="lifeguard-image">
                    <div class="image-overlay"></div>
                    <div class="image-caption">Professional lifeguards on duty with rescue equipment between the flags</div>
                  </div>
                  
                  <div class="simulation-button-container">
                    <router-link to="/water-safety-simulation" class="simulation-button">
                      <div class="sim-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                          <polygon points="5 3 19 12 5 21 5 3"></polygon>
                        </svg>
                      </div>
                      <span>Try the Rescue Simulation</span>
                    </router-link>
                  </div>
                  
                  <p class="technique-description">What parents should do while waiting for professional help:</p>
                  <div class="technique-steps">
                    <div class="rescue-method">
                      <div class="method-header">
                        <div class="method-number">1</div>
                        <h4>CALL FOR HELP</h4>
                      </div>
                      <div class="method-content">
                        <p>Alert lifeguards immediately or call 000. Wave arms overhead and shout "HELP" to draw attention to the emergency.</p>
                      </div>
                    </div>
                    
                    <div class="rescue-method">
                      <div class="method-header">
                        <div class="method-number">2</div>
                        <h4>STAY ON SHORE</h4>
                      </div>
                      <div class="method-content">
                        <p><strong>DO NOT</strong> enter deep water yourself. Parents who enter water often become victims themselves, making the rescue more difficult.</p>
                      </div>
                    </div>
                    
                    <div class="rescue-method">
                      <div class="method-header">
                        <div class="method-number">3</div>
                        <h4>GUIDE RESCUERS</h4>
                      </div>
                      <div class="method-content">
                        <p>Keep pointing to the person in trouble, maintain visual contact, and help direct lifeguards to their exact location.</p>
                      </div>
                    </div>
                  </div>
                </div>
                
                <!-- Bystander Response Tab -->
                <div v-if="activeRescueTab === 'bystander'" class="rescue-technique">
                  <div class="technique-header">
                    <div class="technique-icon">🪃</div>
                    <h3>Safe Bystander Response</h3>
                  </div>
                  
                  <div class="bystander-image-container">
                    <img src="./assets/bystander.png" alt="Life ring floating in rough water" class="bystander-image">
                    <div class="image-overlay"></div>
                    <div class="image-caption">Life ring flotation device - a crucial tool for rescuing people without entering the water</div>
                  </div>
                  
                  <p class="technique-description">Methods that can be used by untrained rescuers without entering deep water:</p>
                  <div class="technique-steps">
                    <div class="rescue-method">
                      <div class="method-header">
                        <div class="method-number">1</div>
                        <h4>REACH</h4>
                      </div>
                      <div class="method-content">
                        <p>If the person is close to shore, use a pole, branch, or towel to reach them without entering the water.</p>
                      </div>
                    </div>
                    
                    <div class="rescue-method">
                      <div class="method-header">
                        <div class="method-number">2</div>
                        <h4>THROW</h4>
                      </div>
                      <div class="method-content">
                        <p>If they're further out, throw a flotation device (life ring, bodyboard, esky lid) with a rope attached if possible.</p>
                      </div>
                    </div>
                    
                    <div class="rescue-method">
                      <div class="method-header">
                        <div class="method-number">3</div>
                        <h4>WADE</h4>
                      </div>
                      <div class="method-content">
                        <p>If safe to do so, wade into shallow water (keeping your feet firmly on the bottom) to reach them with an extended device.</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="content-section">
          <h2 class="section-title">🩹 Post-Rescue Care</h2>
          
          <div class="section-body">
            <p>After a successful rescue, immediate care is crucial:</p>
            
            <div class="post-rescue-steps">
              <div class="post-rescue-step">
                <div class="step-icon">🫁</div>
                <div class="step-content">
                  <h4>Check Breathing</h4>
                  <p>Ensure their airway is clear and they're breathing normally. Begin CPR if necessary.</p>
                </div>
              </div>
              
              <div class="post-rescue-step">
                <div class="step-icon">🧣</div>
                <div class="step-content">
                  <h4>Treat for Shock</h4>
                  <p>Keep them warm with towels or blankets, even on hot days.</p>
                </div>
              </div>
              
              <div class="post-rescue-step">
                <div class="step-icon">👨‍⚕️</div>
                <div class="step-content">
                  <h4>Seek Medical Attention</h4>
                  <p>Always get medical help after a water rescue, even if they seem fine. Secondary drowning can occur hours later.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <div class="next-section-arrow" v-if="showNavigationArrow" @click="navigateToNextSection">
      <div class="arrow-label">Offshore Rescue</div>
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
        path: '/offshore-rescue',
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

/* Distress Signs Styles */
.distress-signs {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  margin: 1rem 0;
}

.distress-sign {
  display: flex;
  align-items: flex-start;
  background: rgba(1, 54, 92, 0.6);
  border-radius: 0.75rem;
  padding: 1.25rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  border-left: 3px solid #e74c3c;
}

.sign-icon {
  font-size: 2rem;
  margin-right: 1rem;
  flex-shrink: 0;
}

.sign-content h4 {
  color: #e74c3c;
  margin: 0 0 0.5rem;
  font-size: 1.1rem;
  font-weight: 600;
}

.sign-content p {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.4;
}

/* Rescue Techniques Styles */
.safety-alert {
  display: flex;
  background: rgba(241, 196, 15, 0.2);
  border-radius: 0.75rem;
  padding: 1.25rem;
  margin-bottom: 1.5rem;
  border-left: 4px solid #f1c40f;
  align-items: center;
}

.alert-icon {
  font-size: 2rem;
  margin-right: 1rem;
  color: #f1c40f;
  flex-shrink: 0;
}

.alert-content h4 {
  margin: 0 0 0.5rem;
  color: #f1c40f;
  font-weight: 600;
}

.rescue-types {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  margin: 1.5rem 0;
}

.rescue-technique {
  background: rgba(1, 54, 92, 0.6);
  border-radius: 0.75rem;
  padding: 1.5rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.technique-header {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
}

.technique-icon {
  font-size: 2.2rem;
  margin-right: 1rem;
  color: #3498db;
}

.technique-header h3 {
  font-size: 1.3rem;
  color: #3498db;
  margin: 0;
  font-weight: 700;
}

.technique-steps {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  margin-top: 1.5rem;
}

.rescue-method {
  background: rgba(52, 152, 219, 0.15);
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  border-left: 4px solid #3498db;
}

.method-header {
  display: flex;
  align-items: center;
  background: rgba(52, 152, 219, 0.3);
  padding: 0.8rem 1.25rem;
  border-bottom: 1px solid rgba(52, 152, 219, 0.3);
}

.method-number {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background: #3498db;
  color: white;
  font-weight: 700;
  font-size: 1.3rem;
  border-radius: 50%;
  margin-right: 1rem;
}

.method-header h4 {
  margin: 0;
  font-size: 1.2rem;
  color: white;
  font-weight: 700;
  letter-spacing: 0.05em;
}

.method-content {
  padding: 1.25rem;
}

.method-content p {
  margin: 0;
  line-height: 1.5;
}

.technique-description {
  margin: 0.5rem 0 1.5rem;
  color: rgba(255, 255, 255, 0.9);
  font-style: italic;
}

/* Post-Rescue Styles */
.post-rescue-steps {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 1rem 0;
}

.post-rescue-step {
  display: flex;
  align-items: flex-start;
  background: rgba(1, 54, 92, 0.6);
  border-radius: 0.75rem;
  padding: 1.25rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  border-left: 3px solid #2ecc71;
}

.step-icon {
  font-size: 2rem;
  margin-right: 1rem;
  color: #2ecc71;
  flex-shrink: 0;
}

.step-content h4 {
  color: #2ecc71;
  margin: 0 0 0.5rem;
  font-size: 1.1rem;
  font-weight: 600;
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

/* Hide old step styling elements that conflict with our new design */
.step {
  display: none;
}

/* Responsive Styles */
@media (max-width: 992px) {
  .distress-signs, .post-rescue-steps {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .progress-connector {
    width: 100px;
  }
  
  .rescue-types {
    grid-template-columns: 1fr;
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
  
  .technique-header, .safety-alert, .caution-box {
    flex-direction: column;
    text-align: center;
  }
  
  .technique-icon, .alert-icon, .caution-icon {
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
  
  .distress-signs, .post-rescue-steps {
    grid-template-columns: 1fr;
  }
  
  .progress-connector {
    width: 50px;
  }
  
  .method-header {
    padding: 0.7rem 1rem;
  }
  
  .method-number {
    width: 35px;
    height: 35px;
    font-size: 1.2rem;
    margin-right: 0.8rem;
  }
  
  .method-header h4 {
    font-size: 1.1rem;
  }
  
  .method-content {
    padding: 1rem;
  }
}

@media (max-width: 576px) {
  .content-wrapper {
    padding-top: 3rem;
  }
  
  .main-content {
    padding: 0 0.75rem 1rem;
  }
  
  .content-section, .distress-sign, .rescue-technique, .post-rescue-step {
    padding: 1rem;
  }
  
  .step-label {
    font-size: 0.75rem;
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
  
  .technique-icon, .sign-icon, .step-icon {
    font-size: 1.6rem;
  }
  
  .progress-connector {
    width: 30px;
  }
  
  .method-header {
    padding: 0.6rem 0.8rem;
  }
  
  .method-number {
    width: 30px;
    height: 30px;
    font-size: 1rem;
    margin-right: 0.7rem;
  }
  
  .method-header h4 {
    font-size: 1rem;
  }
  
  .method-content {
    padding: 0.8rem;
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

/* Update CSS for the drowning image to make it smaller */
.drowning-image-container {
  position: relative;
  width: 100%;
  max-width: 600px;
  margin: 1.5rem auto 2rem;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
  height: 350px;
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
  .drowning-image-container {
    margin: 1rem auto 1.5rem;
    max-width: 500px;
    height: 300px;
  }
  
  .image-caption {
    font-size: 1rem;
    padding: 0.75rem;
  }
}

@media (max-width: 480px) {
  .drowning-image-container {
    max-width: 100%;
    height: 250px;
  }
  
  .image-caption {
    font-size: 0.9rem;
    padding: 0.5rem;
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
  font-size: 1rem;
  font-weight: 500;
  text-align: center;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
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
}

@media (max-width: 480px) {
  .lifeguard-image-container {
    height: 200px;
  }
  
  .image-caption {
    font-size: 0.8rem;
    padding: 0.5rem;
  }
}

/* Add CSS for the simulation button */
.simulation-button-container {
  width: 100%;
  display: flex;
  justify-content: center;
  margin: 0.5rem 0 1.5rem;
}

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

.simulation-button:hover {
  background: #e67e22;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
}

.sim-icon {
  margin-right: 0.75rem;
  display: flex;
  align-items: center;
}

@media (max-width: 576px) {
  .simulation-button {
    font-size: 0.9rem;
    padding: 0.7rem 1.2rem;
  }
  
  .sim-icon {
    margin-right: 0.5rem;
  }
  
  .sim-icon svg {
    width: 20px;
    height: 20px;
  }
}

/* Add CSS for the bystander image */
.bystander-image-container {
  position: relative;
  width: 100%;
  max-width: 600px;
  margin: 1rem auto 1.5rem;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
  height: 300px;
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
    height: 250px;
    margin: 1rem auto 1.5rem;
  }
}

@media (max-width: 480px) {
  .bystander-image-container {
    height: 200px;
  }
}
</style> 