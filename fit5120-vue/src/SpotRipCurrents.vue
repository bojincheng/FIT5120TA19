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
              <router-link to="/rip-safety" class="step-link">
                <div class="step-number">1</div>
                <div class="step-label">What Are Rips</div>
              </router-link>
            </div>
            <div class="progress-connector"></div>
            <div class="progress-step active">
              <div class="step-number">2</div>
              <div class="step-label">Spot Rip Currents</div>
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
          <h1>How to Spot Rip Currents</h1>
          <div class="statistic-banner">
            <h2 class="headline">Identifying rip currents <span class="highlight">before</span> entering the water can save your life</h2>
            <p class="subheadline">— Learn to recognize the telltale signs of these dangerous water channels</p>
          </div>
        </div>

        <div class="content-section">
          <h2 class="section-title">🌊 Common Types of Rip Currents</h2>
          
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
                <h3 class="rip-type-title">Channelized Rips</h3>
                
                <!-- Personal Impact Warning Box -->
                <div class="personal-impact-box">
                  <div class="impact-icon">⚠️</div>
                  <div class="impact-content">
                    <h4>Why It Matters to You:</h4>
                    <p>Channelized rips cause more drownings than any other beach hazard in Australia. If you or your child are caught, you can be pulled hundreds of meters out in less than a minute. Knowing what to look for can save lives.</p>
                  </div>
                </div>
                
                <div class="rip-overview">
                  <div class="rip-type-image">
                    <img src="./assets/Channelised-Rips-A.jpg" alt="Channelized rip current" @error="handleImageError">
                    <div class="image-overlay">
                      <div class="overlay-point" style="top: 40%; left: 30%;">
                        <span class="point-marker">1</span>
                        <div class="point-tooltip">Deep channel between sandbars</div>
                      </div>
                      <div class="overlay-point" style="top: 25%; left: 50%;">
                        <span class="point-marker">2</span>
                        <div class="point-tooltip">Breaking waves on sandbars</div>
                      </div>
                      <div class="overlay-point" style="top: 60%; left: 70%;">
                        <span class="point-marker">3</span>
                        <div class="point-tooltip">Gap in breaking waves</div>
                      </div>
                    </div>
                  </div>
                  
                  <div class="rip-snapshot">
                    <div class="snapshot-item">
                      <div class="snapshot-icon">⏱️</div>
                      <div class="snapshot-content">
                        <h5>Duration</h5>
                        <p>Days to months</p>
                        <p class="snapshot-impact">Same spot might be dangerous for weeks!</p>
                      </div>
                    </div>
                    <div class="snapshot-item">
                      <div class="snapshot-icon">🌊</div>
                      <div class="snapshot-content">
                        <h5>Speed</h5>
                        <p>0.5-2.5 m/s (up to 9 km/h)</p>
                        <p class="snapshot-impact">1.5x faster than Olympic swimmers</p>
                      </div>
                    </div>
                    <div class="snapshot-item">
                      <div class="snapshot-icon">📏</div>
                      <div class="snapshot-content">
                        <h5>Width</h5>
                        <p>10-30 meters</p>
                        <p class="snapshot-impact">Wide enough to catch a group or family</p>
                      </div>
                    </div>
                    <div class="snapshot-item">
                      <div class="snapshot-icon">🔍</div>
                      <div class="snapshot-content">
                        <h5>Visibility</h5>
                        <p>High</p>
                        <p class="snapshot-impact">Easy to spot once you know how</p>
                      </div>
                    </div>
                  </div>
                </div>
                
                <div class="rip-info-container">
                  <div class="rip-info-column">
                    <div class="info-card">
                      <h4><span class="info-icon">ℹ️</span> What Is It?</h4>
                      <p>Channelized rips form in deeper channels that cut through sandbars parallel to the shore. These natural pathways allow water pushed toward shore by breaking waves to flow back to the ocean.</p>
                    </div>
                    
                    <div class="info-card spotting-card">
                      <h4><span class="info-icon">👁️</span> How To Spot It</h4>
                      <ul class="spot-checklist">
                        <li>
                          <span class="check-icon">✓</span> 
                          <div class="checklist-content">
                            <strong>Darker patches</strong> in the water (deeper water absorbs more light)
                          </div>
                        </li>
                        <li>
                          <span class="check-icon">✓</span> 
                          <div class="checklist-content">
                            <strong>Gaps in the waves</strong> (no breaking waves = hidden rip)
                          </div>
                        </li>
                        <li>
                          <span class="check-icon">✓</span> 
                          <div class="checklist-content">
                            <strong>Calmer water</strong> between rougher areas (deceptively safer-looking)
                          </div>
                        </li>
                      </ul>
                    </div>
                  </div>
                  
                  <div class="rip-info-column">
                    <div class="info-card danger">
                      <h4><span class="info-icon">⚠️</span> Danger Factor</h4>
                      <p>These channels might look inviting because they appear calmer than surrounding water, but this apparent calmness indicates a strong current flowing seaward that can quickly carry swimmers hundreds of meters offshore.</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            
            <!-- Boundary Rips Content -->
            <div class="rip-content" v-if="activeRipTab === 'boundary'">
              <div class="rip-type-card">
                <h3 class="rip-type-title">Boundary/Structural Rips</h3>
                
                <!-- Personal Impact Warning Box -->
                <div class="personal-impact-box">
                  <div class="impact-icon">⚠️</div>
                  <div class="impact-content">
                    <h4>Why It Matters to You:</h4>
                    <p>Swimming near piers or jetties is like stepping into a powerful underwater vacuum. Boundary rips can sweep your child 50 meters offshore in just 20 seconds — faster than you can sprint there to help. These currents can reach speeds of 10.8 km/h, making them 3x stronger than other rip types and impossible to swim against, even for Olympic athletes.</p>
                  </div>
                </div>
                
                <div class="rip-overview">
                  <div class="rip-type-image boundary-image">
                    <img src="./assets/Boundary-Rips-A.jpg" alt="Boundary rip current" @error="handleImageError">
                    <div class="image-overlay">
                      <div class="overlay-point" style="top: 30%; left: 45%;">
                        <span class="point-marker">1</span>
                        <div class="point-tooltip">Pier structure creating boundary</div>
                      </div>
                      <div class="overlay-point" style="top: 52%; left: 50%;">
                        <span class="point-marker">2</span>
                        <div class="point-tooltip">Rip current flowing alongside structure</div>
                      </div>
                      <div class="overlay-point" style="top: 75%; left: 30%;">
                        <span class="point-marker">3</span>
                        <div class="point-tooltip">Darker water indicating deeper channel</div>
                      </div>
                    </div>
                  </div>
                  
                  <div class="rip-snapshot">
                    <div class="snapshot-item">
                      <div class="snapshot-icon">⏱️</div>
                      <div class="snapshot-content">
                        <h5>Duration</h5>
                        <p>Permanent</p>
                        <p class="snapshot-impact">Present anytime waves are breaking</p>
                      </div>
                    </div>
                    <div class="snapshot-item">
                      <div class="snapshot-icon">🌊</div>
                      <div class="snapshot-content">
                        <h5>Speed</h5>
                        <p>0.5-3.0 m/s (up to 10.8 km/h)</p>
                        <p class="snapshot-impact">Twice as fast as Olympic swimmers</p>
                      </div>
                    </div>
                    <div class="snapshot-item">
                      <div class="snapshot-icon">📍</div>
                      <div class="snapshot-content">
                        <h5>Location</h5>
                        <p>Next to structures</p>
                        <p class="snapshot-impact">Always in the same predictable spot</p>
                      </div>
                    </div>
                    <div class="snapshot-item">
                      <div class="snapshot-icon">⚠️</div>
                      <div class="snapshot-content">
                        <h5>Danger Level</h5>
                        <p>Very High</p>
                        <p class="snapshot-impact">Combined hazard of rip and structure</p>
                      </div>
                    </div>
                  </div>
                </div>
                
                <div class="rip-info-container">
                  <div class="rip-info-column">
                    <div class="info-card">
                      <h4><span class="info-icon">ℹ️</span> What Is It?</h4>
                      <p>Boundary rips form alongside physical structures like piers, jetties, groins, and rocky headlands. These structures block the natural flow of water along the beach, forcing it to flow seaward in a concentrated channel.</p>
                    </div>
                    
                    <div class="info-card spotting-card">
                      <h4><span class="info-icon">👁️</span> How To Spot It</h4>
                      <ul class="spot-checklist">
                        <li>
                          <span class="check-icon">✓</span> 
                          <div class="checklist-content">
                            <strong>Always near structures</strong> - look for any pier, jetty, or rocky outcrop
                          </div>
                        </li>
                        <li>
                          <span class="check-icon">✓</span> 
                          <div class="checklist-content">
                            <strong>Darker water</strong> next to the structure
                          </div>
                        </li>
                        <li>
                          <span class="check-icon">✓</span> 
                          <div class="checklist-content">
                            <strong>Disturbed or choppy water</strong> flowing away from shore
                          </div>
                        </li>
                      </ul>
                    </div>
                  </div>
                  
                  <div class="rip-info-column">
                    <div class="info-card danger">
                      <h4><span class="info-icon">⚠️</span> Danger Factor</h4>
                      <p>Boundary rips present a double danger: the powerful current that can pull you away from shore, plus the risk of being slammed into the structure itself, causing injuries. Always stay at least 50 meters (150 feet) away from any structure on a beach.</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            
            <!-- Flash Rips Content -->
            <div class="rip-content" v-if="activeRipTab === 'flash'">
              <div class="rip-type-card">
                <h3 class="rip-type-title">Flash Rips</h3>
                
                <!-- Personal Impact Warning Box -->
                <div class="personal-impact-box">
                  <div class="impact-icon">⚠️</div>
                  <div class="impact-content">
                    <h4>Why It Matters to You:</h4>
                    <p>Flash rips are the most unpredictable type - they can form suddenly with no warning, even at beaches that seemed safe moments before. They account for many rescues of families who were swimming in "safe" water.</p>
                  </div>
                </div>
                
                <div class="rip-overview">
                  <div class="rip-type-image flash-image">
                    <img src="./assets/Flash-Rip.jpg" alt="Flash rip current" @error="handleImageError">
                    <div class="image-overlay">
                      <div class="overlay-point" style="top: 30%; left: 50%;">
                        <span class="point-marker">1</span>
                        <div class="point-tooltip">Darker water showing the rip channel</div>
                      </div>
                      <div class="overlay-point" style="top: 45%; left: 52%;">
                        <span class="point-marker">2</span>
                        <div class="point-tooltip">Flow direction of the rip current</div>
                      </div>
                      <div class="overlay-point" style="top: 65%; left: 48%;">
                        <span class="point-marker">3</span>
                        <div class="point-tooltip">Rip current extending beyond breaking waves</div>
                      </div>
                    </div>
                  </div>
                  
                  <div class="rip-snapshot">
                    <div class="snapshot-item">
                      <div class="snapshot-icon">⏱️</div>
                      <div class="snapshot-content">
                        <h5>Duration</h5>
                        <p>Minutes only</p>
                        <p class="snapshot-impact">Can appear and vanish in moments</p>
                      </div>
                    </div>
                    <div class="snapshot-item">
                      <div class="snapshot-icon">⚡</div>
                      <div class="snapshot-content">
                        <h5>Speed</h5>
                        <p>0.5-2.0 m/s (up to 7.2 km/h)</p>
                        <p class="snapshot-impact">Can pull you 50m offshore in seconds</p>
                      </div>
                    </div>
                    <div class="snapshot-item">
                      <div class="snapshot-icon">🔮</div>
                      <div class="snapshot-content">
                        <h5>Predictability</h5>
                        <p>Very Low</p>
                        <p class="snapshot-impact">Can form at any beach, any time</p>
                      </div>
                    </div>
                    <div class="snapshot-item">
                      <div class="snapshot-icon">🌊</div>
                      <div class="snapshot-content">
                        <h5>Trigger</h5>
                        <p>Large wave sets</p>
                        <p class="snapshot-impact">Watch for incoming larger waves</p>
                      </div>
                    </div>
                  </div>
                </div>
                
                <div class="rip-info-container">
                  <div class="rip-info-column">
                    <div class="info-card">
                      <h4><span class="info-icon">ℹ️</span> What Is It?</h4>
                      <p>Flash rips are sudden, short-lived rip currents that form quickly and disappear just as fast. Unlike channelized rips, they aren't bound to fixed locations and can appear on any beach when conditions are right.</p>
                    </div>
                    
                    <div class="info-card spotting-card">
                      <h4><span class="info-icon">👁️</span> How To Spot It</h4>
                      <ul class="spot-checklist">
                        <li>
                          <span class="check-icon">✓</span> 
                          <div class="checklist-content">
                            <strong>Turbulent, foamy water</strong> moving away from shore
                          </div>
                        </li>
                        <li>
                          <span class="check-icon">✓</span> 
                          <div class="checklist-content">
                            <strong>Suddenly appearing</strong> after a set of large waves breaks
                          </div>
                        </li>
                        <li>
                          <span class="check-icon">✓</span> 
                          <div class="checklist-content">
                            <strong>Sandy, discolored water</strong> extending beyond the break zone
                          </div>
                        </li>
                      </ul>
                    </div>
                  </div>
                  
                  <div class="rip-info-column">
                    <div class="info-card danger">
                      <h4><span class="info-icon">⚠️</span> Danger Factor</h4>
                      <p>Flash rips are especially dangerous because they can form in previously safe water. Always watch for large sets of incoming waves - these can trigger flash rips. If waves suddenly get bigger, move to shallower water until conditions stabilize.</p>
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
        path: '/survive-rip-currents',
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
  transition: all 0.2s ease;
  cursor: pointer;
  pointer-events: auto;
  z-index: 2;
}

.point-tooltip {
  position: absolute;
  bottom: calc(100% + 10px);
  left: 50%;
  transform: translateX(-50%);
  background-color: rgba(0, 0, 0, 0.8);
  color: white;
  padding: 0.5rem 0.75rem;
  border-radius: 0.5rem;
  font-size: 0.8rem;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.point-tooltip:after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border-width: 5px;
  border-style: solid;
  border-color: rgba(0, 0, 0, 0.8) transparent transparent transparent;
}

.overlay-point:hover .point-marker {
  transform: scale(1.2);
  background-color: #e67e22;
}

.overlay-point:hover .point-tooltip {
  opacity: 1;
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
</style> 