<template>
  <div class="rip-safety-page">
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
            <div class="progress-step">
              <router-link to="/understanding-danger" class="step-link">
                <div class="step-number">2</div>
                <div class="step-label">Understanding Rip Currents</div>
              </router-link>
            </div>
            <div class="progress-connector"></div>
            <div class="progress-step active">
              <div class="step-number">3</div>
              <div class="step-label">Avoiding Rip Currents</div>
            </div>
          </div>
        </div>
        
        <div class="title-section">
          <h1>Avoiding Rip Currents</h1>
        </div>

        <div class="content-section">
          <h2 class="section-title">🌊 Identifying rip currents <span class="highlight">before</span> entering the water can save your life</h2>
          
          <div class="section-body">
            <p>Different types of rip currents can occur at beaches and may look and behave differently. Select a type below to learn about its characteristics:</p>
            
            <div class="rip-tabs">
              <div 
                class="rip-tab" 
                :class="{ active: activeRipTab === 'channelized' }"
                @click="setActiveRipTab('channelized')"
              >
                <div class="tab-icon">🌊</div>
                <div class="tab-label">Channelized Rips</div>
              </div>
              
              <div 
                class="rip-tab" 
                :class="{ active: activeRipTab === 'boundary' }"
                @click="setActiveRipTab('boundary')"
              >
                <div class="tab-icon">🏗️</div>
                <div class="tab-label">Boundary Rips</div>
              </div>
              
              <div 
                class="rip-tab" 
                :class="{ active: activeRipTab === 'flash' }"
                @click="setActiveRipTab('flash')"
              >
                <div class="tab-icon">⚡</div>
                <div class="tab-label">Flash Rips</div>
              </div>
            </div>
            
            <!-- Channelized Rips Content -->
            <div class="rip-content" v-if="activeRipTab === 'channelized'">
              <div class="rip-type-card">
                <h3 class="rip-type-title">Channelized Rips: Deep Water Channels Flowing Out to Sea</h3>
                
                <!-- Combined Impact Warning Box -->
                <div class="personal-impact-box">
                  <div class="impact-icon">⚠️</div>
                  <div class="impact-content">
                    <h4>Why It Matters</h4>
                    <p>Channelized rips are deep channels between sandbars that pull water away from shore at speeds up to 9 km/h—faster than Olympic swimmers. They look deceptively calm, but this apparent "safe water" is actually the most dangerous spot, responsible for more drownings than any other beach hazard.</p>
                  </div>
                </div>
                
                <div class="rip-overview">
                  <div class="rip-type-image">
                    <img src="./assets/Channelised-Rips-A.jpg" alt="Channelized rip current" @error="handleImageError">
                    <div class="image-overlay">
                      <div class="overlay-point" style="top: 55%; left: 30%;">
                        <span class="point-marker">1</span>
                        <div class="point-tooltip">Darker patches in the water (deeper water absorbs more light)</div>
                      </div>
                      <div class="overlay-point" style="top: 45%; left: 50%;">
                        <span class="point-marker">2</span>
                        <div class="point-tooltip">Gaps in the waves (no breaking waves = hidden rip)</div>
                      </div>
                      <div class="overlay-point" style="top: 60%; left: 70%;">
                        <span class="point-marker">3</span>
                        <div class="point-tooltip">Calmer water between rougher areas (deceptively safer-looking)</div>
                      </div>
                    </div>
                  </div>
                  <p class="image-caption">Hover over numbered points to see how to spot a channelized rip current</p>
                  
                  <div class="rip-characteristics">
                    <h4 class="characteristics-title">Key Characteristics <span class="hover-instruction">(Hover cards to flip)</span></h4>
                    <div class="flip-cards-container">
                      <!-- Duration Card -->
                      <div class="flip-card characteristic-card">
                        <div class="flip-card-inner">
                          <div class="flip-card-front">
                            <img src="./assets/duration.png" alt="Duration" class="characteristic-image">
                            <h4 class="card-title">Duration</h4>
                          </div>
                          <div class="flip-card-back">
                            <h4>Duration</h4>
                            <p>Days to months</p>
                            <p class="impact-note">Same spot might be dangerous for weeks!</p>
                          </div>
                        </div>
                      </div>
                      
                      <!-- Speed Card -->
                      <div class="flip-card characteristic-card">
                        <div class="flip-card-inner">
                          <div class="flip-card-front">
                            <img src="./assets/speed.png" alt="Speed" class="characteristic-image">
                            <h4 class="card-title">Speed</h4>
                          </div>
                          <div class="flip-card-back">
                            <h4>Speed</h4>
                            <p>Up to 9 km/h</p>
                            <p class="impact-note">1.5x faster than Olympic swimmers</p>
                          </div>
                        </div>
                      </div>
                      
                      <!-- Width Card -->
                      <div class="flip-card characteristic-card">
                        <div class="flip-card-inner">
                          <div class="flip-card-front">
                            <img src="./assets/width.jpeg" alt="Width" class="characteristic-image">
                            <h4 class="card-title">Width</h4>
                          </div>
                          <div class="flip-card-back">
                            <h4>Width</h4>
                            <p>10-30 meters</p>
                            <p class="impact-note">Wide enough to catch a group or family</p>
                          </div>
                        </div>
                      </div>
                      
                      <!-- Visibility Card -->
                      <div class="flip-card characteristic-card">
                        <div class="flip-card-inner">
                          <div class="flip-card-front">
                            <img src="./assets/visiblity.jpeg" alt="Visibility" class="characteristic-image">
                            <h4 class="card-title">Visibility</h4>
                          </div>
                          <div class="flip-card-back">
                            <h4>Visibility</h4>
                            <p>High</p>
                            <p class="impact-note">Easy to spot once you know how</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            
            <!-- Boundary Rips Content -->
            <div class="rip-content" v-if="activeRipTab === 'boundary'">
              <div class="rip-type-card">
                <h3 class="rip-type-title">Boundary Rips: Strong Currents Next to Structures</h3>
                
                <!-- Combined Impact Warning Box -->
                <div class="personal-impact-box">
                  <div class="impact-icon">⚠️</div>
                  <div class="impact-content">
                    <h4>Why It Matters</h4>
                    <p>Swimming near piers or jetties puts your family at double risk: a powerful current that can sweep a child 50 meters offshore in just 20 seconds, plus the danger of being slammed against the hard structure. These permanent rip currents reach speeds of 10.8 km/h—three times stronger than other rips and completely impossible to swim against, even for strong adult swimmers.</p>
                  </div>
                </div>
                
                <div class="rip-overview">
                  <div class="rip-type-image boundary-image">
                    <img src="./assets/Boundary-Rips-A.jpg" alt="Boundary rip current" @error="handleImageError">
                    <div class="image-overlay">
                      <div class="overlay-point" style="top: 30%; left: 45%;">
                        <span class="point-marker">1</span>
                        <div class="point-tooltip">Structure danger zone: Never swim within 50m of a pier, jetty, or rocky outcrop - the strongest rips form here</div>
                      </div>
                      <div class="overlay-point" style="top: 52%; left: 50%;">
                        <span class="point-marker">2</span>
                        <div class="point-tooltip">Dark water channel: Deeper, calmer-looking water alongside structures is a powerful outward current</div>
                      </div>
                      <div class="overlay-point" style="top: 65%; left: 35%;">
                        <span class="point-marker">3</span>
                        <div class="point-tooltip">Water movement: Watch for debris or foam moving away from shore - a key indicator of a dangerous rip</div>
                      </div>
                    </div>
                  </div>
                  <p class="image-caption">Hover over numbered points to learn how to identify dangerous boundary rips</p>
                  
                  <div class="rip-characteristics">
                    <h4 class="characteristics-title">Key Characteristics <span class="hover-instruction">(Hover cards to flip)</span></h4>
                    <div class="flip-cards-container">
                      <!-- Duration Card -->
                      <div class="flip-card characteristic-card">
                        <div class="flip-card-inner">
                          <div class="flip-card-front">
                            <img src="./assets/duration.png" alt="Duration" class="characteristic-image">
                            <h4 class="card-title">Duration</h4>
                          </div>
                          <div class="flip-card-back">
                            <h4>Duration</h4>
                            <p>Permanent</p>
                            <p class="impact-note">Present anytime waves are breaking</p>
                          </div>
                        </div>
                      </div>
                      
                      <!-- Speed Card -->
                      <div class="flip-card characteristic-card">
                        <div class="flip-card-inner">
                          <div class="flip-card-front">
                            <img src="./assets/speed.png" alt="Speed" class="characteristic-image">
                            <h4 class="card-title">Speed</h4>
                          </div>
                          <div class="flip-card-back">
                            <h4>Speed</h4>
                            <p>Up to 10.8 km/h</p>
                            <p class="impact-note">Twice as fast as Olympic swimmers</p>
                          </div>
                        </div>
                      </div>
                      
                      <!-- Location Card -->
                      <div class="flip-card characteristic-card">
                        <div class="flip-card-inner">
                          <div class="flip-card-front">
                            <img src="./assets/location.jpeg" alt="Location" class="characteristic-image">
                            <h4 class="card-title">Location</h4>
                          </div>
                          <div class="flip-card-back">
                            <h4>Location</h4>
                            <p>Next to structures</p>
                            <p class="impact-note">Always in the same predictable spot</p>
                          </div>
                        </div>
                      </div>
                      
                      <!-- Danger Level Card -->
                      <div class="flip-card characteristic-card">
                        <div class="flip-card-inner">
                          <div class="flip-card-front">
                            <img src="./assets/danger.avif" alt="Danger Level" class="characteristic-image">
                            <h4 class="card-title">Danger Level</h4>
                          </div>
                          <div class="flip-card-back">
                            <h4>Danger Level</h4>
                            <p>Very High</p>
                            <p class="impact-note">Combined hazard of rip and structure</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            
            <!-- Flash Rips Content -->
            <div class="rip-content" v-if="activeRipTab === 'flash'">
              <div class="rip-type-card">
                <h3 class="rip-type-title">Flash Rips: Sudden, Short-Lived Currents</h3>
                
                <!-- Combined Impact Warning Box -->
                <div class="personal-impact-box">
                  <div class="impact-icon">⚠️</div>
                  <div class="impact-content">
                    <h4>Why It Matters</h4>
                    <p>Flash rips are the most unpredictable beach danger because they appear without warning in water that was safe just moments before, catching families off guard. Even experienced beachgoers who monitor conditions closely can be surprised when a sudden set of large waves creates a powerful rip current in previously calm water, which is why constant supervision of children is essential.</p>
                  </div>
                </div>
                
                <div class="rip-overview">
                  <div class="rip-type-image flash-image">
                    <img src="./assets/Flash-Rip.jpg" alt="Flash rip current" @error="handleImageError">
                    <div class="image-overlay">
                      <div class="overlay-point" style="top: 30%; left: 45%;">
                        <span class="point-marker">1</span>
                        <div class="point-tooltip">Sudden disrupted water pattern: Watch for unexpected churning that appears after a set of large waves breaks</div>
                      </div>
                      <div class="overlay-point" style="top: 52%; left: 35%;">
                        <span class="point-marker">2</span>
                        <div class="point-tooltip">Discolored water: Murky, sandy or foamy water extending outward indicates water rushing back to sea</div>
                      </div>
                      <div class="overlay-point" style="top: 65%; left: 48%;">
                        <span class="point-marker">3</span>
                        <div class="point-tooltip">Safety zone: Keep children in shallow water where their feet touch bottom when large waves approach</div>
                      </div>
                    </div>
                  </div>
                  <p class="image-caption">Hover over numbered points to learn how to spot sudden flash rips</p>
                  
                  <div class="rip-characteristics">
                    <h4 class="characteristics-title">Key Characteristics <span class="hover-instruction">(Hover cards to flip)</span></h4>
                    <div class="flip-cards-container">
                      <!-- Duration Card -->
                      <div class="flip-card characteristic-card">
                        <div class="flip-card-inner">
                          <div class="flip-card-front">
                            <img src="./assets/duration.png" alt="Duration" class="characteristic-image">
                            <h4 class="card-title">Duration</h4>
                          </div>
                          <div class="flip-card-back">
                            <h4>Duration</h4>
                            <p>Minutes only</p>
                            <p class="impact-note">Can appear and vanish in moments</p>
                          </div>
                        </div>
                      </div>
                      
                      <!-- Speed Card -->
                      <div class="flip-card characteristic-card">
                        <div class="flip-card-inner">
                          <div class="flip-card-front">
                            <img src="./assets/speed.png" alt="Speed" class="characteristic-image">
                            <h4 class="card-title">Speed</h4>
                          </div>
                          <div class="flip-card-back">
                            <h4>Speed</h4>
                            <p>Up to 7.2 km/h</p>
                            <p class="impact-note">Can pull you 50m offshore in seconds</p>
                          </div>
                        </div>
                      </div>
                      
                      <!-- Predictability Card -->
                      <div class="flip-card characteristic-card">
                        <div class="flip-card-inner">
                          <div class="flip-card-front">
                            <img src="./assets/predicitablity.jpeg" alt="Predictability" class="characteristic-image">
                            <h4 class="card-title">Predictability</h4>
                          </div>
                          <div class="flip-card-back">
                            <h4>Predictability</h4>
                            <p>Very Low</p>
                            <p class="impact-note">Can form at any beach, any time</p>
                          </div>
                        </div>
                      </div>
                      
                      <!-- Trigger Card -->
                      <div class="flip-card characteristic-card">
                        <div class="flip-card-inner">
                          <div class="flip-card-front">
                            <img src="./assets/trigger.png" alt="Trigger" class="characteristic-image">
                            <h4 class="card-title">Trigger</h4>
                          </div>
                          <div class="flip-card-back">
                            <h4>Trigger</h4>
                            <p>Large wave sets</p>
                            <p class="impact-note">Watch for incoming larger waves</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <div class="next-section-arrow" v-if="showNavigationArrow" @click="navigateToNextSection">
      <div class="arrow-label">Return to Beach Safety</div>
      <div class="arrow-icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M8 12h8"/><path d="m12 8 4 4-4 4"/></svg>
      </div>
    </div>
  </div>
</template>

<script>
import BeachMenu from './components/BeachMenu.vue'

export default {
  name: 'SpotRipCurrents',
  components: {
    BeachMenu
  },
  data() {
    return {
      menuOpen: false,
      showNavigationArrow: false,
      activeRipTab: 'channelized' // Default active tab
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
    setActiveNavLink() {
      // Remove active class from all nav links
      document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
      });
      document.querySelectorAll('.mobile-nav-link').forEach(link => {
        link.classList.remove('active');
      });
      
      // Add active class to beach safety practices links ("Prevent the Risk")
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
      // Navigate back to the beach safety practices page
      this.$router.push({ 
        path: '/beach-safety-practices',
        // Adding this option ensures the page is scrolled to the top
        query: { _: Date.now() } 
      }).then(() => {
        // Ensure we're at the top of the page after navigation completes
        window.scrollTo(0, 0);
      });
    },
    setActiveRipTab(tabName) {
      this.activeRipTab = tabName;
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

/* Rip Tabs Styles */
.rip-tabs {
  display: flex;
  justify-content: space-between;
  margin: 1.5rem 0;
  gap: 1rem;
  flex-wrap: wrap;
}

.rip-tab {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: rgba(1, 54, 92, 0.6);
  border-radius: 0.75rem;
  padding: 1.25rem 0.75rem;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease;
  border-bottom: 3px solid transparent;
  min-width: 120px;
  text-align: center;
}

.rip-tab:hover {
  background: rgba(1, 54, 92, 0.8);
  transform: translateY(-3px);
}

.rip-tab.active {
  background: rgba(1, 54, 92, 0.9);
  border-bottom: 3px solid #f39c12;
}

.tab-icon {
  font-size: 2rem;
  margin-bottom: 0.75rem;
}

.tab-label {
  font-weight: 600;
  font-size: 1rem;
}

.rip-tab.active .tab-label {
  color: #f39c12;
}

.rip-content {
  animation: fadeInContent 0.4s ease-out;
}

@keyframes fadeInContent {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.rip-type-card {
  background: rgba(1, 54, 92, 0.7);
  border-radius: 0.75rem;
  padding: 1.5rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  border-left: 3px solid #f39c12;
  margin-bottom: 2rem;
}

.rip-type-title {
  font-size: clamp(1.1rem, 2vw, 1.4rem);
  margin: 0 0 1rem;
  color: #f39c12;
  font-weight: 700;
}

.rip-type-content {
  margin-top: 1rem;
}

.rip-type-content p {
  margin-bottom: 0.75rem;
}

.rip-type-content strong {
  color: #f39c12;
}

.rip-type-image {
  width: 100%;
  border-radius: 0.5rem;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  position: relative;
}

.rip-type-image img {
  width: 100%;
  height: 250px;
  object-fit: cover;
  display: block;
  background-color: rgba(1, 54, 92, 0.5); /* Fallback color if image is not available */
}

.image-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

.overlay-point {
  position: absolute;
  transform: translate(-50%, -50%);
}

.point-marker {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  background-color: #f39c12;
  color: white;
  border-radius: 50%;
  font-weight: bold;
  font-size: 0.8rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  transition: all 0.3s ease;
  cursor: pointer;
  pointer-events: auto;
  z-index: 2;
  border: 2px solid transparent;
  animation: pulse-marker 2s infinite;
  position: relative;
}

.point-marker::after {
  content: "Hover me";
  position: absolute;
  bottom: -25px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 3px 8px;
  border-radius: 4px;
  font-size: 0.7rem;
  white-space: nowrap;
  font-weight: normal;
  opacity: 0.9;
  transition: opacity 0.3s ease;
}

.overlay-point:hover .point-marker::after {
  opacity: 0;
}

@keyframes pulse-marker {
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

.point-tooltip {
  position: absolute;
  bottom: calc(100% + 10px);
  left: 50%;
  transform: translateX(-50%);
  background-color: rgba(0, 0, 0, 0.95);
  color: white;
  padding: 0.5rem 0.75rem;
  border-radius: 0.5rem;
  font-size: 0.8rem;
  white-space: normal;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s ease, transform 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  max-width: 250px;
  width: max-content;
  border-left: 3px solid #f39c12;
  backdrop-filter: blur(5px);
  z-index: 10;
}

.point-tooltip:after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border-width: 6px;
  border-style: solid;
  border-color: rgba(0, 0, 0, 0.95) transparent transparent transparent;
}

.overlay-point:hover .point-marker {
  transform: scale(1.2);
  background-color: #e67e22;
  border: 2px solid white;
  box-shadow: 0 4px 12px rgba(243, 156, 18, 0.6);
}

.overlay-point:hover .point-tooltip {
  opacity: 1;
  transform: translateX(-50%) translateY(-5px);
}

.image-caption {
  text-align: center;
  margin: 8px 0 15px;
  font-size: 0.95rem;
  font-style: italic;
  color: rgba(255, 255, 255, 0.85);
}

.rip-snapshot {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-top: 1.5rem;
}

.snapshot-item {
  flex: 1;
  min-width: 120px;
  border-radius: 0.5rem;
  padding: 1rem;
  display: flex;
  align-items: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.snapshot-item:nth-child(1) {
  background: rgba(52, 152, 219, 0.5); /* Blue */
}

.snapshot-item:nth-child(2) {
  background: rgba(46, 204, 113, 0.5); /* Green */
}

.snapshot-item:nth-child(3) {
  background: rgba(243, 156, 18, 0.5); /* Orange */
}

.snapshot-item:nth-child(4) {
  background: rgba(155, 89, 182, 0.5); /* Purple */
}

.snapshot-item:nth-child(1) .snapshot-content h5,
.snapshot-item:nth-child(2) .snapshot-content h5,
.snapshot-item:nth-child(4) .snapshot-content h5 {
  color: white;
}

.snapshot-item:nth-child(3) .snapshot-content h5 {
  color: #f8f9fa;
}

.snapshot-item:nth-child(1) .snapshot-content p,
.snapshot-item:nth-child(2) .snapshot-content p,
.snapshot-item:nth-child(4) .snapshot-content p {
  color: #f8f9fa;
}

.snapshot-item:nth-child(1) .snapshot-impact,
.snapshot-item:nth-child(2) .snapshot-impact,
.snapshot-item:nth-child(4) .snapshot-impact {
  color: white;
  font-weight: 700;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}

.snapshot-item:nth-child(3) .snapshot-impact {
  color: white;
  font-weight: 700;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.snapshot-icon {
  font-size: 1.75rem;
  margin-right: 0.75rem;
}

.snapshot-content h5 {
  margin: 0 0 0.25rem;
  font-size: 1.2rem;
  font-weight: 600;
  text-decoration: underline;
  padding-bottom: 0.25rem;
}

.snapshot-content p:not(.snapshot-impact) {
  margin: 0;
  font-size: 1rem;
}

.snapshot-impact {
  display: block;
  font-size: 1.05rem;
  margin-top: 0.5rem;
  line-height: 1.3;
}

.rip-info-container {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}

.rip-info-column {
  flex: 1;
  min-width: 280px;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.rip-info-column.full-width {
  width: 100%;
}

.info-card {
  background: rgba(1, 54, 92, 0.6);
  border-radius: 0.75rem;
  padding: 1.25rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  border-left: 3px solid #3498db;
  height: 100%;
}

.info-card.danger {
  border-left: 3px solid #e74c3c;
}

.info-icon {
  margin-right: 0.5rem;
  font-size: 1.2rem;
}

.info-card h4 {
  display: flex;
  align-items: center;
  color: white;
  margin: 0 0 0.75rem;
  font-size: 1.1rem;
  font-weight: 600;
}

.info-card p {
  margin: 0;
  line-height: 1.5;
}

.rip-overview {
  margin-bottom: 1.5rem;
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
  
  .rip-tab {
    padding: 1rem 0.5rem;
    min-width: 100px;
  }
  
  .tab-icon {
    font-size: 1.75rem;
    margin-bottom: 0.5rem;
  }
  
  .tab-label {
    font-size: 0.9rem;
  }
  
  .rip-type-card {
    padding: 1.25rem;
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
  
  .next-section-arrow {
    bottom: 1.5rem;
    right: 1.5rem;
    padding: 0.6rem 1rem;
  }
  
  .arrow-label {
    font-size: 0.9rem;
  }
  
  .rip-info-container {
    flex-direction: column;
  }
  
  .snapshot-item {
    min-width: 100px;
  }
  
  .point-marker::after {
    font-size: 0.65rem;
    padding: 2px 6px;
    bottom: -22px;
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
  
  .rip-tabs {
    flex-direction: column;
    gap: 0.75rem;
  }
  
  .rip-tab {
    flex-direction: row;
    justify-content: flex-start;
    padding: 0.75rem 1rem;
  }
  
  .tab-icon {
    margin-bottom: 0;
    margin-right: 1rem;
    font-size: 1.5rem;
  }
  
  .rip-type-card {
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
  
  .point-marker::after {
    display: none;
  }
  
  .image-caption {
    font-size: 0.85rem;
  }
}

.rip-type-content h4 {
  color: #f39c12;
  margin: 1.25rem 0 0.5rem;
  font-size: 1.1rem;
  font-weight: 600;
}

.rip-type-content h4:first-child {
  margin-top: 0;
}

.key-facts {
  background: rgba(1, 54, 92, 0.5);
  border-radius: 0.75rem;
  padding: 1rem 1.25rem;
  margin: 1.25rem 0;
  border-left: 3px solid #f39c12;
}

.key-facts h4 {
  margin-top: 0;
}

.key-facts ul {
  margin: 0.5rem 0 0 1.25rem;
  padding: 0;
}

.key-facts li {
  margin-bottom: 0.5rem;
  line-height: 1.4;
}

.safety-tip {
  font-style: italic;
  background: rgba(243, 156, 18, 0.15);
  padding: 0.75rem 1rem;
  border-radius: 0.5rem;
  border-left: 3px solid #f39c12;
  margin-top: 1.25rem;
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

.personal-impact-box {
  background: rgba(231, 76, 60, 0.15);
  border-radius: 0.75rem;
  padding: 1rem 1.25rem;
  margin: 0 0 1.5rem;
  border-left: 3px solid #e74c3c;
  display: flex;
  align-items: flex-start;
}

.impact-icon {
  font-size: 1.75rem;
  margin-right: 1rem;
  color: #e74c3c;
  flex-shrink: 0;
}

.impact-content h4 {
  color: #e74c3c;
  margin: 0 0 0.5rem;
  font-size: 1.1rem;
  font-weight: 600;
}

.impact-content p {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.5;
}

.spotting-card .spot-checklist {
  margin-top: 0.5rem;
}

.spotting-card li {
  margin-bottom: 0.75rem;
}

.real-risk-section {
  background: rgba(1, 54, 92, 0.5);
  border-radius: 0.75rem;
  padding: 1.25rem;
  margin: 0 0 1.5rem;
  border-left: 3px solid #f39c12;
}

.real-risk-section h4 {
  color: #f39c12;
  margin: 0 0 0.75rem;
  font-size: 1.1rem;
  font-weight: 600;
}

.spot-checklist {
  list-style: none;
  padding: 0;
  margin: 0;
}

.spot-checklist li {
  display: flex;
  align-items: flex-start;
  margin-bottom: 0.75rem;
  line-height: 1.4;
}

.spot-checklist li:last-child {
  margin-bottom: 0;
}

.checklist-content {
  flex: 1;
}

.check-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  background-color: rgba(243, 156, 18, 0.2);
  color: #f39c12;
  border-radius: 50%;
  margin-right: 0.75rem;
  margin-top: 0.2rem;
  font-weight: bold;
  flex-shrink: 0;
}

.checklist-content strong {
  color: #f39c12;
  font-weight: 700;
  font-size: 1.05em;
}

.boundary-image {
  width: 100%;
  height: auto;
  margin-bottom: 1.5rem;
  overflow: hidden;
  border-radius: 0.5rem;
}

.boundary-image img {
  width: 100%;
  height: 380px;
  object-fit: cover;
  object-position: center 75%;
}

.flash-image {
  width: 100%;
  height: auto;
  margin-bottom: 1.5rem;
  overflow: hidden;
  border-radius: 0.5rem;
}

.flash-image img {
  width: 100%;
  height: 400px;
  object-fit: cover;
  object-position: center 40%;
}

/* Make the tooltips larger for the more detailed content */
.boundary-image .point-tooltip,
.flash-image .point-tooltip {
  max-width: 280px;
  padding: 10px 15px;
  font-size: 0.85rem;
  line-height: 1.4;
}

@media (max-width: 768px) {
  .boundary-image .point-tooltip,
  .flash-image .point-tooltip {
    max-width: 220px;
    padding: 8px 12px;
    font-size: 0.75rem;
  }
}

.rip-characteristics {
  margin: 1.5rem 0;
  width: 100%;
}

.characteristics-title {
  font-size: 1.2rem;
  color: #ffffff;
  margin-bottom: 1rem;
  text-align: center;
  font-weight: 600;
}

.hover-instruction {
  font-size: 0.9rem;
  color: #f39c12;
  font-weight: normal;
  font-style: italic;
  margin-left: 5px;
  animation: pulse-text 2s infinite;
}

@keyframes pulse-text {
  0% { opacity: 0.7; }
  50% { opacity: 1; }
  100% { opacity: 0.7; }
}

.flip-cards-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 20px;
  width: 100%;
}

/* Flip Card Styles */
.characteristic-card {
  height: 250px;
  perspective: 1000px;
  background-color: transparent;
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.6s;
  transform-style: preserve-3d;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  border-radius: 10px;
}

.characteristic-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

.flip-card-front, .flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  border-radius: 10px;
  overflow: hidden;
}

.flip-card-front {
  background-color: rgba(1, 54, 92, 0.7);
  display: flex;
  flex-direction: column;
}

.flip-card-back {
  background-color: rgba(1, 54, 92, 0.9);
  transform: rotateY(180deg);
  padding: 1rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  border-left: 3px solid #f39c12;
}

.characteristic-image {
  width: 100%;
  height: 180px;
  object-fit: cover;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}

.card-title {
  margin: 0;
  padding: 15px 10px;
  font-size: 1.1rem;
  color: #ffffff;
  background-color: rgba(1, 54, 92, 0.85);
  flex-grow: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.flip-card-back h4 {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
  text-align: center;
  color: #f39c12;
  font-weight: 700;
}

.flip-card-back p {
  margin: 0.5rem 0;
  font-size: 1.1rem;
  text-align: center;
}

.impact-note {
  font-weight: 600;
  color: #f39c12;
  margin-top: 0.75rem;
}

.flip-card-front::after {
  content: "↻ Hover to flip";
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(243, 156, 18, 0.8);
  color: white;
  padding: 5px 10px;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 500;
  pointer-events: none;
  opacity: 0.9;
  transition: opacity 0.3s ease;
  z-index: 5;
}

.characteristic-card:hover .flip-card-front::after {
  opacity: 0;
}

@media (max-width: 768px) {
  .flip-cards-container {
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 15px;
  }
  
  .characteristic-card {
    height: 220px;
  }
  
  .characteristic-image {
    height: 150px;
  }
  
  .flip-card-back h4 {
    font-size: 1.1rem;
  }
  
  .flip-card-back p {
    font-size: 0.95rem;
  }
  
  .hover-instruction {
    font-size: 0.8rem;
    display: block;
    margin-left: 0;
    margin-top: 5px;
  }
  
  .flip-card-front::after {
    top: 5px;
    right: 5px;
    padding: 3px 8px;
    font-size: 0.7rem;
  }
}

@media (max-width: 480px) {
  .flip-cards-container {
    grid-template-columns: 1fr;
  }
  
  .hover-instruction {
    font-size: 0.75rem;
  }
}
</style> 