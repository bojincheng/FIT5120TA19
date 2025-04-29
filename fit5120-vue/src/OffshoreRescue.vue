<template>
  <div class="offshore-rescue-page">
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
            <div class="progress-step">
              <router-link to="/beach-safety-rescue" class="step-link">
                <div class="step-number">2</div>
                <div class="step-label">Near-Shore Rescue</div>
              </router-link>
            </div>
            <div class="progress-connector"></div>
            <div class="progress-step active">
              <div class="step-number">3</div>
              <div class="step-label">Offshore Rescue</div>
            </div>
          </div>
        </div>
        
        <div class="title-section">
          <h1>Offshore Rescue Techniques</h1>
          <div class="statistic-banner">
            <h2 class="headline">Advanced rescue methods for <span class="highlight">deep water</span> emergencies</h2>
            <p class="subheadline">— Essential knowledge for situations beyond the surf zone</p>
          </div>
        </div>

        <!-- Main Content Section -->
        <div class="content-section">
          <h2 class="section-title">🚨 Understanding Offshore Rescue in Australia</h2>
          
          <div class="section-body">
            <p>Australia's sophisticated maritime rescue system is strategically positioned along our 25,760 kilometers of coastline to respond to a variety of water emergencies—even in areas beyond the flags and patrolled beaches. These services are available to everyone, including visitors and new immigrants who may be unfamiliar with Australian waters.</p>
            
            <div class="safety-alert">
              <div class="alert-icon">ℹ️</div>
              <div class="alert-content">
                <h4>RESCUE BEYOND THE FLAGS</h4>
                <p>While swimming between the red and yellow flags is strongly recommended, Australian rescue services can and do respond to emergencies in unpatrolled areas. Response times may be longer, but help is available anywhere along the coast.</p>
              </div>
            </div>
            
            <div class="offshore-image-container">
              <img src="./Maratime.jpg" alt="Australian Maritime Rescue vessel" class="offshore-image">
              <div class="image-overlay"></div>
              <div class="image-caption">The Australian Maritime Rescue system operates year-round across the entire coastline</div>
            </div>
            
            <div class="immigrant-resources">
              <h3>Resources for New Australians and Visitors</h3>
              <p>If you're new to Australia or visiting our beaches and waterways, these resources are available in multiple languages:</p>
              <div class="resource-buttons">
                <a href="https://beachsafe.org.au/surf-safety/multilingual" target="_blank" class="resource-button">
                  <span class="resource-icon">🌐</span>
                  <span>Multilingual Beach Safety Guide</span>
                </a>
                <a href="https://www.royallifesaving.com.au/stay-safe-active/communities/multicultural-communities" target="_blank" class="resource-button">
                  <span class="resource-icon">🏊‍♂️</span>
                  <span>Swimming Resources</span>
                </a>
              </div>
            </div>
            
            <div class="rescue-scenario-tabs">
              <div class="tab-buttons">
                <button 
                  class="tab-button" 
                  :class="{ active: activeScenarioTab === 'metro' }"
                  @click="activeScenarioTab = 'metro'"
                >
                  <span class="tab-icon">🏙️</span>
                  <span class="tab-label">Metropolitan Beaches</span>
                </button>
                <button 
                  class="tab-button" 
                  :class="{ active: activeScenarioTab === 'regional' }"
                  @click="activeScenarioTab = 'regional'"
                >
                  <span class="tab-icon">🏝️</span>
                  <span class="tab-label">Regional Beaches</span>
                </button>
                <button 
                  class="tab-button" 
                  :class="{ active: activeScenarioTab === 'remote' }"
                  @click="activeScenarioTab = 'remote'"
                >
                  <span class="tab-icon">🚤</span>
                  <span class="tab-label">Offshore Waters</span>
                </button>
              </div>
              
              <div class="tab-content">
                <!-- Metropolitan Beaches Tab -->
                <div v-if="activeScenarioTab === 'metro'" class="rescue-scenario">
                  <h3>Metropolitan Beach Response</h3>
                  <p class="response-time"><strong>Average Response Time:</strong> 5-10 minutes</p>
                  
                  <div class="response-details">
                    <div class="response-item">
                      <div class="response-icon">👥</div>
                      <div class="response-content">
                        <h4>First Responders</h4>
                        <p>Surf Lifesavers on patrolled beaches can deploy immediately. All Australian metropolitan beaches have dedicated rescue teams within 10km range.</p>
                      </div>
                    </div>
                    
                    <div class="response-item">
                      <div class="response-icon">🛥️</div>
                      <div class="response-content">
                        <h4>Available Equipment</h4>
                        <p>Rescue boards, tubes, jetskis, IRBs (Inflatable Rescue Boats), and jet rescue boats are stationed directly at popular beaches during patrol hours (typically 9am-5pm).</p>
                      </div>
                    </div>
                    
                    <div class="response-item">
                      <div class="response-icon">⌚</div>
                      <div class="response-content">
                        <h4>Operational Hours</h4>
                        <p>Year-round coverage with full-time professional lifeguards at major city beaches. Volunteer surf lifesavers supplement coverage on weekends and holidays.</p>
                      </div>
                    </div>
                  </div>
                </div>
                
                <!-- Regional Beaches Tab -->
                <div v-if="activeScenarioTab === 'regional'" class="rescue-scenario">
                  <h3>Regional Beach Response</h3>
                  <p class="response-time"><strong>Average Response Time:</strong> 15-30 minutes</p>
                  
                  <div class="response-details">
                    <div class="response-item">
                      <div class="response-icon">🚑</div>
                      <div class="response-content">
                        <h4>First Responders</h4>
                        <p>Local volunteer lifesaving clubs with support from regional emergency services. Coverage varies by season with more resources during summer months.</p>
                      </div>
                    </div>
                    
                    <div class="response-item">
                      <div class="response-icon">🚁</div>
                      <div class="response-content">
                        <h4>Available Equipment</h4>
                        <p>Regional centers maintain IRBs, 4WD beach vehicles, and access to helicopter support from nearby bases. Rescue boats from Volunteer Marine Rescue can be deployed for nearshore incidents.</p>
                      </div>
                    </div>
                    
                    <div class="response-item">
                      <div class="response-icon">📆</div>
                      <div class="response-content">
                        <h4>Operational Coverage</h4>
                        <p>Most regional beaches have weekend patrols during summer (November-April). Year-round emergency response is coordinated via police with longer response times outside patrol hours.</p>
                      </div>
                    </div>
                  </div>
                </div>
                
                <!-- Offshore Waters Tab -->
                <div v-if="activeScenarioTab === 'remote'" class="rescue-scenario">
                  <h3>Offshore/Remote Areas Response</h3>
                  <p class="response-time"><strong>Average Response Time:</strong> 30-120+ minutes</p>
                  
                  <div class="response-details">
                    <div class="response-item">
                      <div class="response-icon">🛳️</div>
                      <div class="response-content">
                        <h4>First Responders</h4>
                        <p>Australian Maritime Safety Authority coordinates responses with Water Police and Volunteer Marine Rescue. Commercial vessels may be diverted to assist in remote ocean rescues.</p>
                      </div>
                    </div>
                    
                    <div class="response-item">
                      <div class="response-icon">✈️</div>
                      <div class="response-content">
                        <h4>Available Assets</h4>
                        <p>Long-range helicopters, fixed-wing search aircraft, and ocean-capable vessels. Offshore response often involves multiple assets working in coordination over longer periods.</p>
                      </div>
                    </div>
                    
                    <div class="response-item">
                      <div class="response-icon">📡</div>
                      <div class="response-content">
                        <h4>Communication Methods</h4>
                        <p>Satellite tracking of emergency beacons (EPIRBs and PLBs) is critical for remote rescues. VHF radio and satellite phones are monitored continuously for distress calls.</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="content-section">
          <h2 class="section-title">📞 Emergency Contact Information</h2>
          
          <div class="section-body">
            <div class="safety-alert important">
              <div class="alert-icon">⚠️</div>
              <div class="alert-content">
                <h4>WHEN TO CONTACT EMERGENCY SERVICES</h4>
                <p>Call immediately if you spot someone in distress in the water, a missing swimmer, or a vessel in trouble. Don't delay or assume someone else has already called.</p>
              </div>
            </div>
            
            <div class="emergency-tabs">
              <div class="tab-buttons">
                <button 
                  class="tab-button" 
                  :class="{ active: activeEmergencyTab === 'contacts' }"
                  @click="activeEmergencyTab = 'contacts'"
                >
                  <span class="tab-icon">📞</span>
                  <span class="tab-label">Emergency Contacts</span>
                </button>
                <button 
                  class="tab-button" 
                  :class="{ active: activeEmergencyTab === 'info' }"
                  @click="activeEmergencyTab = 'info'"
                >
                  <span class="tab-icon">ℹ️</span>
                  <span class="tab-label">Information to Provide</span>
                </button>
              </div>
              
              <div class="tab-content">
                <!-- Emergency Contacts Tab -->
                <div v-if="activeEmergencyTab === 'contacts'" class="emergency-tab-content">
                  <div class="emergency-contacts">
                    <div class="emergency-contact">
                      <div class="contact-icon">📞</div>
                      <div class="contact-content">
                        <h4>Triple Zero (000)</h4>
                        <p>Works nationwide, even with low mobile signal. Request "Police" for water emergencies.</p>
                      </div>
                    </div>
                    
                    <div class="emergency-contact">
                      <div class="contact-icon">📱</div>
                      <div class="contact-content">
                        <h4>Marine Rescue App</h4>
                        <p>Free app that sends your GPS coordinates directly to rescue services.</p>
                      </div>
                    </div>
                    
                    <div class="emergency-contact">
                      <div class="contact-icon">📻</div>
                      <div class="contact-content">
                        <h4>VHF Radio (Channel 16)</h4>
                        <p>Monitored 24/7 by coast stations and other vessels. Clear communication: "MAYDAY, MAYDAY, MAYDAY" for life-threatening emergencies.</p>
                      </div>
                    </div>
                    
                    <div class="emergency-contact">
                      <div class="contact-icon">🛰️</div>
                      <div class="contact-content">
                        <h4>Emergency Beacons</h4>
                        <p>EPIRB activation triggers immediate response and is tracked via satellite.</p>
                      </div>
                    </div>
                  </div>
                </div>
                
                <!-- Information to Provide Tab -->
                <div v-if="activeEmergencyTab === 'info'" class="emergency-tab-content">
                  <div class="emergency-info-box">
                    <h3>Critical Information to Provide When Calling</h3>
                    <div class="info-grid">
                      <div class="info-item">
                        <div class="info-number">1</div>
                        <div class="info-content">
                          <h4>EXACT LOCATION</h4>
                          <p>Beach name, nearby landmarks, or GPS coordinates</p>
                        </div>
                      </div>
                      
                      <div class="info-item">
                        <div class="info-number">2</div>
                        <div class="info-content">
                          <h4>EMERGENCY TYPE</h4>
                          <p>Missing swimmer, person struggling, capsized vessel</p>
                        </div>
                      </div>
                      
                      <div class="info-item">
                        <div class="info-number">3</div>
                        <div class="info-content">
                          <h4>NUMBER OF PEOPLE</h4>
                          <p>How many victims and their current condition</p>
                        </div>
                      </div>
                      
                      <div class="info-item">
                        <div class="info-number">4</div>
                        <div class="info-content">
                          <h4>VICTIM DESCRIPTION</h4>
                          <p>Age, clothing colors, distinctive features</p>
                        </div>
                      </div>
                      
                      <div class="info-item">
                        <div class="info-number">5</div>
                        <div class="info-content">
                          <h4>ENVIRONMENTAL CONDITIONS</h4>
                          <p>Current, waves, visibility, weather changes</p>
                        </div>
                      </div>
                      
                      <div class="info-item">
                        <div class="info-number">6</div>
                        <div class="info-content">
                          <h4>YOUR DETAILS</h4>
                          <p>Your name and callback number</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="content-section">
          <h2 class="section-title">🛟 Rescue Equipment & Response Capabilities</h2>
          
          <div class="section-body">
            <p>Understanding the specialized equipment used in Australian water rescues helps you recognize rescue assets when they arrive:</p>
            
            <div class="rescue-tabs">
              <div class="tab-buttons">
                <button 
                  class="tab-button" 
                  :class="{ active: activeRescueTab === 'nearshore' }"
                  @click="activeRescueTab = 'nearshore'"
                >
                  <span class="tab-icon">🏄‍♂️</span>
                  <span class="tab-label">Nearshore Equipment</span>
                </button>
                <button 
                  class="tab-button" 
                  :class="{ active: activeRescueTab === 'offshore' }"
                  @click="activeRescueTab = 'offshore'"
                >
                  <span class="tab-icon">🚢</span>
                  <span class="tab-label">Offshore Vessels</span>
                </button>
                <button 
                  class="tab-button" 
                  :class="{ active: activeRescueTab === 'aerial' }"
                  @click="activeRescueTab = 'aerial'"
                >
                  <span class="tab-icon">🚁</span>
                  <span class="tab-label">Aerial Assets</span>
                </button>
              </div>
              
              <div class="tab-content">
                <!-- Nearshore Tab -->
                <div v-if="activeRescueTab === 'nearshore'" class="rescue-technique">
                  <div class="technique-header">
                    <div class="technique-icon">🏄‍♂️</div>
                    <h3>Nearshore Rescue Equipment</h3>
                  </div>
                  
                  <p class="technique-description">Australian surf life savers use specialized equipment for rapid response to rescues within 1km of shoreline. These tools prioritize speed and maneuverability in challenging surf conditions:</p>
                  
                  <div class="equipment-grid">
                    <div class="equipment-item">
                      <div class="equipment-image-container">
                        <img src="./rescue_board.jpg" alt="Rescue board" class="equipment-image">
                      </div>
                      <h4>Rescue Boards</h4>
                      <p><strong>Response Time:</strong> Immediate</p>
                      <p><strong>Range:</strong> Up to 400m</p>
                      <p>Maneuverable in breaking waves and can support multiple people</p>
                    </div>
                    
                    <div class="equipment-item">
                      <div class="equipment-image-container">
                        <img src="./rescue_jetski.jpg" alt="Rescue jetski" class="equipment-image">
                      </div>
                      <h4>Rescue Jetskis</h4>
                      <p><strong>Response Time:</strong> 2-5 minutes</p>
                      <p><strong>Range:</strong> Up to 5km</p>
                      <p>Fast response in challenging surf with rescue sleds</p>
                    </div>
                    
                    <div class="equipment-item">
                      <div class="equipment-image-container">
                        <img src="./IRB.jpg" alt="Inflatable Rescue Boat" class="equipment-image">
                      </div>
                      <h4>IRBs</h4>
                      <p><strong>Response Time:</strong> 3-8 minutes</p>
                      <p><strong>Range:</strong> Up to 10km</p>
                      <p>Highly maneuverable inflatable craft with capacity for multiple rescues</p>
                    </div>
                  </div>
                </div>
                
                <!-- Offshore Tab -->
                <div v-if="activeRescueTab === 'offshore'" class="rescue-technique">
                  <div class="technique-header">
                    <div class="technique-icon">🚢</div>
                    <h3>Offshore Rescue Vessels</h3>
                  </div>
                  
                  <p class="technique-description">For emergencies beyond the surf zone, Australia deploys larger vessels with extended range and sophisticated equipment. These craft can operate in adverse weather conditions and provide medical support:</p>
                  
                  <div class="equipment-grid">
                    <div class="equipment-item">
                      <div class="equipment-image-container">
                        <img src="./RHIB.jpg" alt="Rigid Hull Inflatable Boat" class="equipment-image">
                      </div>
                      <h4>RHIBs</h4>
                      <p><strong>Response Time:</strong> 10-20 minutes</p>
                      <p><strong>Range:</strong> Up to 30km</p>
                      <p>Fast, stable platforms with navigation equipment and first aid capabilities</p>
                    </div>
                    
                    <div class="equipment-item">
                      <div class="equipment-image-container">
                        <img src="./VMR.png" alt="Volunteer Marine Rescue vessel" class="equipment-image">
                      </div>
                      <h4>VMR Vessels</h4>
                      <p><strong>Response Time:</strong> 20-45 minutes</p>
                      <p><strong>Range:</strong> Up to 100km</p>
                      <p>All-weather rescue capability with medical facilities and towing capacity</p>
                    </div>
                    
                    <div class="equipment-item">
                      <div class="equipment-image-container">
                        <img src="./police.jpg" alt="Water Police vessel" class="equipment-image">
                      </div>
                      <h4>Police Vessels</h4>
                      <p><strong>Response Time:</strong> 20-60 minutes</p>
                      <p><strong>Range:</strong> Up to 200km</p>
                      <p>Advanced communications, night operations capability, and extended search capacity</p>
                    </div>
                  </div>
                </div>
                
                <!-- Aerial Tab -->
                <div v-if="activeRescueTab === 'aerial'" class="rescue-technique">
                  <div class="technique-header">
                    <div class="technique-icon">🚁</div>
                    <h3>Aerial Rescue Assets</h3>
                  </div>
                  
                  <p class="technique-description">Air assets provide critical support for distant rescues and challenging terrain. They offer rapid deployment, extensive search capability, and can operate where vessels cannot reach:</p>
                  
                  <div class="equipment-grid">
                    <div class="equipment-item">
                      <div class="equipment-image-container">
                        <img src="./Westpac-50-Years.jpg" alt="Rescue helicopter" class="equipment-image">
                      </div>
                      <h4>Rescue Helicopters</h4>
                      <p><strong>Response Time:</strong> 15-30 minutes</p>
                      <p><strong>Range:</strong> Up to 250km</p>
                      <p>Winch capability for direct extraction from water with paramedic crews</p>
                    </div>
                    
                    <div class="equipment-item">
                      <div class="equipment-image-container">
                        <img src="./drones.jpg" alt="Rescue drone" class="equipment-image">
                      </div>
                      <h4>Rescue Drones</h4>
                      <p><strong>Response Time:</strong> 1-5 minutes</p>
                      <p><strong>Range:</strong> Up to 1.5km</p>
                      <p>Rapid deployment with life raft drop capability and shark spotting</p>
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
</template>

<script>
import BeachMenu from './components/BeachMenu.vue'

export default {
  name: 'OffshoreRescue',
  components: {
    BeachMenu
  },
  data() {
    return {
      menuOpen: false,
      showNavigationArrow: false,
      activeRescueTab: 'nearshore', // Default active tab for rescue equipment
      activeScenarioTab: 'metro', // Default active tab for rescue scenarios
      activeEmergencyTab: 'contacts' // Default active tab for emergency contacts
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
    }
  }
}
</script>

<style scoped>
.offshore-rescue-page {
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
  background-image: url('./Aussie_beachhome.jpg');
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

/* Emergency Contacts */
.emergency-tabs {
  margin: 1.5rem 0;
}

.emergency-tab-content {
  animation: fadeIn 0.5s ease;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.emergency-contacts {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  margin: 0;
}

.emergency-contact {
  display: flex;
  align-items: flex-start;
  background: rgba(1, 54, 92, 0.6);
  border-radius: 0.75rem;
  padding: 1.25rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  border-left: 3px solid #3498db;
}

.contact-icon {
  font-size: 2rem;
  margin-right: 1rem;
  color: #3498db;
  flex-shrink: 0;
}

.contact-content h4 {
  color: #3498db;
  margin: 0 0 0.5rem;
  font-size: 1.1rem;
  font-weight: 600;
}

.contact-content p {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.4;
}

.emergency-info-box {
  background: transparent;
  border-radius: 0.75rem;
  padding: 0;
  margin: 0;
  border: none;
}

.emergency-info-box h3 {
  color: #e74c3c;
  margin: 0 0 1.5rem;
  font-size: 1.3rem;
  text-align: center;
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

.safety-alert.important {
  background: rgba(231, 76, 60, 0.2);
  border-left: 4px solid #e74c3c;
}

.safety-alert.important .alert-icon {
  color: #e74c3c;
}

.safety-alert.important .alert-content h4 {
  color: #e74c3c;
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

/* Offshore Image Styles */
.offshore-image-container {
  position: relative;
  width: 100%;
  max-width: 900px;
  margin: 1.5rem auto 2rem;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
  height: 350px;
}

.watercraft-image-container, 
.helicopter-image-container {
  position: relative;
  width: 100%;
  max-width: 600px;
  margin: 1.5rem auto 2rem;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
  height: 350px;
}

.offshore-image {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: contain;
  object-position: center;
  background-color: rgba(1, 54, 92, 0.8);
}

.watercraft-image,
.helicopter-image {
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

/* Safety Simulator Section */
.safety-simulator {
  background: rgba(52, 152, 219, 0.15);
  border-radius: 0.75rem;
  padding: 1.5rem;
  margin-top: 2rem;
  text-align: center;
  border: 1px solid rgba(52, 152, 219, 0.3);
}

.safety-simulator h3 {
  font-size: 1.4rem;
  margin-bottom: 1rem;
  color: #3498db;
}

/* Simulation Button */
.simulation-button-container {
  width: 100%;
  display: flex;
  justify-content: center;
  margin: 1rem 0 0.5rem;
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

/* Responsive Styles */
@media (max-width: 992px) {
  .distress-signs, .post-rescue-steps, .emergency-contacts {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .progress-connector {
    width: 100px;
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
  
  .technique-header, .safety-alert {
    flex-direction: column;
    text-align: center;
  }
  
  .technique-icon, .alert-icon, .sign-icon, .contact-icon, .step-icon {
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
  
  .distress-signs, .post-rescue-steps, .emergency-contacts {
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
  
  .offshore-image-container, 
  .watercraft-image-container, 
  .helicopter-image-container {
    height: 250px;
    margin: 1rem auto 1.5rem;
  }
  
  .image-caption {
    font-size: 0.9rem;
    padding: 0.75rem;
  }
}

@media (max-width: 576px) {
  .content-wrapper {
    padding-top: 3rem;
  }
  
  .main-content {
    padding: 0 0.75rem 1rem;
  }
  
  .content-section, .distress-sign, .post-rescue-step {
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
  
  .tab-icon {
    font-size: 1.3rem;
    margin-right: 0.5rem;
  }
  
  .tab-label {
    font-size: 0.9rem;
  }
  
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
  
  .offshore-image-container, 
  .watercraft-image-container, 
  .helicopter-image-container {
    height: 200px;
  }
  
  .image-caption {
    font-size: 0.8rem;
    padding: 0.5rem;
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

.child-safety-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin: 1.5rem 0;
}

.child-safety-item {
  background: rgba(1, 54, 92, 0.6);
  border-radius: 0.75rem;
  padding: 1.5rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  border-left: 3px solid #2ecc71;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.child-safety-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
}

.safety-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
  color: #2ecc71;
}

.child-safety-item h4 {
  color: #2ecc71;
  margin: 0 0 0.75rem;
  font-size: 1.2rem;
  font-weight: 600;
}

.child-safety-item p {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.5;
}

.child-safety-resources {
  background: rgba(52, 152, 219, 0.15);
  border-radius: 0.75rem;
  padding: 1.5rem;
  margin-top: 2rem;
  text-align: center;
  border: 1px solid rgba(52, 152, 219, 0.3);
}

.child-safety-resources h3 {
  font-size: 1.4rem;
  margin-bottom: 1.5rem;
  color: #3498db;
}

.resources-grid {
  display: flex;
  justify-content: center;
  gap: 2rem;
  flex-wrap: wrap;
  margin-top: 1rem;
}

.resource-link {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-decoration: none;
  color: white;
  transition: transform 0.3s ease;
  width: 150px;
}

.resource-link:hover {
  transform: translateY(-5px);
}

.resource-icon {
  font-size: 3rem;
  margin-bottom: 0.75rem;
  color: #3498db;
}

.resource-link span {
  font-weight: 600;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.25rem;
  margin-top: 1.5rem;
}

.info-item {
  display: flex;
  align-items: flex-start;
  background: rgba(231, 76, 60, 0.15);
  border-radius: 0.75rem;
  padding: 1.25rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.info-number {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background: #e74c3c;
  color: white;
  font-weight: 700;
  font-size: 1.3rem;
  border-radius: 50%;
  margin-right: 1rem;
  flex-shrink: 0;
}

.info-content h4 {
  color: #e74c3c;
  margin: 0 0 0.5rem;
  font-size: 1rem;
  font-weight: 700;
}

.info-content p {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.4;
}

.equipment-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-top: 1.5rem;
}

.equipment-item {
  display: flex;
  flex-direction: column;
  background: rgba(1, 54, 92, 0.6);
  border-radius: 0.75rem;
  padding: 1.25rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  border-top: 3px solid #3498db;
  text-align: center;
  height: 100%;
}

.equipment-image-container {
  width: 100%;
  height: 150px;
  margin-bottom: 1rem;
  border-radius: 0.5rem;
  overflow: hidden;
}

.equipment-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.equipment-item h4 {
  color: #3498db;
  margin: 0 0 0.75rem;
  font-size: 1.2rem;
  font-weight: 600;
}

.equipment-item p {
  margin: 0 0 0.5rem;
  font-size: 0.95rem;
  line-height: 1.4;
}

.equipment-item p strong {
  color: #f39c12;
}

@media (max-width: 768px) {
  .response-details,
  .info-grid,
  .equipment-grid {
    grid-template-columns: 1fr;
  }
  
  .response-item,
  .info-item {
    padding: 1rem;
  }
  
  .info-number {
    width: 35px;
    height: 35px;
    font-size: 1.1rem;
  }
  
  .equipment-image-container {
    height: 130px;
  }
  
  .equipment-item {
    padding: 1rem;
  }
  
  .response-icon,
  .info-number {
    margin-right: 0.75rem;
  }
}

@media (max-width: 576px) {
  .response-icon {
    font-size: 1.6rem;
  }
  
  .info-number {
    width: 30px;
    height: 30px;
    font-size: 1rem;
  }
  
  .equipment-image-container {
    height: 120px;
  }
  
  .equipment-item h4 {
    font-size: 1.1rem;
  }
  
  .equipment-item p {
    font-size: 0.9rem;
  }
}

.immigrant-resources {
  background: rgba(52, 152, 219, 0.15);
  border-radius: 0.75rem;
  padding: 1.5rem;
  margin: 1.5rem 0;
  border: 1px solid rgba(52, 152, 219, 0.3);
}

.immigrant-resources h3 {
  color: #3498db;
  margin: 0 0 0.75rem;
  font-size: 1.3rem;
  text-align: center;
}

.immigrant-resources p {
  text-align: center;
  margin-bottom: 1.25rem;
}

.resource-buttons {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
}

.resource-button {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: rgba(1, 54, 92, 0.6);
  border-radius: 0.75rem;
  padding: 1.25rem;
  width: 180px;
  text-decoration: none;
  color: white;
  transition: transform 0.3s ease, background 0.3s ease;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.resource-button:hover {
  transform: translateY(-5px);
  background: rgba(52, 152, 219, 0.3);
}

.resource-button .resource-icon {
  font-size: 2.5rem;
  margin-bottom: 0.75rem;
  color: #3498db;
}

.resource-button span:last-child {
  text-align: center;
  font-weight: 600;
  font-size: 0.95rem;
}

@media (max-width: 768px) {
  .immigrant-resources {
    padding: 1.25rem;
  }
  
  .resource-button {
    width: 150px;
    padding: 1rem;
  }
  
  .resource-button .resource-icon {
    font-size: 2rem;
    margin-bottom: 0.5rem;
  }
  
  .resource-button span:last-child {
    font-size: 0.9rem;
  }
}

@media (max-width: 576px) {
  .resource-buttons {
    gap: 0.75rem;
  }
  
  .resource-button {
    width: 130px;
    padding: 0.75rem;
  }
  
  .resource-button .resource-icon {
    font-size: 1.75rem;
  }
  
  .resource-button span:last-child {
    font-size: 0.8rem;
  }
}

.rescue-scenario-tabs {
  margin: 1.5rem 0;
}

.rescue-scenario h3 {
  font-size: 1.4rem;
  color: #3498db;
  margin: 0 0 1rem;
  text-align: center;
}

.response-time {
  text-align: center;
  font-size: 1.1rem;
  margin-bottom: 1.5rem;
  background: rgba(52, 152, 219, 0.15);
  padding: 0.75rem;
  border-radius: 0.5rem;
}

.response-details {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.response-item {
  display: flex;
  align-items: flex-start;
  background: rgba(1, 54, 92, 0.6);
  border-radius: 0.75rem;
  padding: 1.25rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  border-left: 3px solid #3498db;
}

.response-icon {
  font-size: 2rem;
  margin-right: 1rem;
  color: #3498db;
  flex-shrink: 0;
}

.response-content h4 {
  color: #3498db;
  margin: 0 0 0.5rem;
  font-size: 1.1rem;
  font-weight: 600;
}

.response-content p {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.4;
}

@media (max-width: 768px) {
  .child-safety-grid {
    grid-template-columns: 1fr;
  }
  
  .child-safety-item {
    padding: 1.25rem;
  }
  
  .safety-icon {
    font-size: 2.5rem;
    margin-bottom: 0.75rem;
  }
  
  .resources-grid {
    gap: 1.5rem;
  }
  
  .resource-link {
    width: 120px;
  }
  
  .resource-icon {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
  }
  
  .response-details,
  .info-grid,
  .equipment-grid {
    grid-template-columns: 1fr;
  }
  
  .response-item,
  .info-item {
    padding: 1rem;
  }
}

@media (max-width: 576px) {
  .child-safety-item h4 {
    font-size: 1.1rem;
  }
  
  .child-safety-item p {
    font-size: 0.9rem;
  }
  
  .resource-link {
    width: 100px;
  }
  
  .resource-icon {
    font-size: 2rem;
  }
  
  .resource-link span {
    font-size: 0.9rem;
  }
  
  .response-icon {
    font-size: 1.6rem;
  }
}
</style> 