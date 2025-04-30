<template>
  <div class="backyard-pool-page">
    <div class="bg-image"></div>
    <div class="bg-overlay"></div>
    
    <!-- Pool Menu Component -->
    <PoolMenu :menuOpen="menuOpen" @toggle-menu="toggleMenu" />
    
    <div class="content-wrapper">
      <div class="main-content">
        <!-- Progress Bar (moved above title) -->
        <div class="progress-section">
          <div class="progress-container">
            <div class="progress-track danger-active">
              <div class="progress-step" @click="navigateToPage('/pool-supervision')">
                <div class="step-number">1</div>
                <div class="step-label">Understanding Danger</div>
              </div>
              <div class="progress-step active">
                <div class="step-number">2</div>
                <div class="step-label">Backyard Pool Safety</div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="title-section">
          <h1>Backyard Pool Safety</h1>
          <div class="statistic-banner">
            <h2 class="headline">Over <span class="highlight">50%</span> of child drownings occur in backyard pools</h2>
            <p class="subheadline">— Where families least expect the danger</p>
          </div>
        </div>

        <!-- Backyard Pool Danger Section -->
        <div class="content-section">
          <div class="danger-card">
            <div class="card-header">
              <h3 class="danger-title">The Hidden Risks of Backyard Pools</h3>
            </div>
            
            <div class="card-body">
              <div class="danger-stats">
                <div class="stat-card">
                  <div class="stat-header">
                    <span class="stat-icon">⚠️</span>
                    <h4>False Security</h4>
                  </div>
                  <p>Backyard settings create a dangerous illusion of safety where parents assume they'll notice if something goes wrong</p>
                </div>
                
                <div class="stat-card">
                  <div class="stat-header">
                    <span class="stat-icon">🔍</span>
                    <h4>Lack of Supervision</h4>
                  </div>
                  <p>63% of drownings occur when children are thought to be safely inside the house or under supervision</p>
                </div>
                
                <div class="stat-card">
                  <div class="stat-header">
                    <span class="stat-icon">⏱️</span>
                    <h4>Critical Window</h4>
                  </div>
                  <p>Most victims are found within 5 minutes, but resuscitation attempts are often unsuccessful</p>
                </div>
              </div>
              
              <div class="barrier-importance">
                <h4 class="section-subtitle">Pool Barriers Save Lives</h4>
                <p>Properly installed and maintained pool barriers reduce drowning risk by 83%. Yet many Australian pool fences fail safety checks, with non-compliant gates being the most common issue.</p>
              </div>
              
              <!-- Australian Fencing Regulations Section -->
              <div class="regulations-section">
                <h4 class="section-subtitle">Australian State Fencing Regulations</h4>
                
                <!-- Location-based finder -->
                <div class="location-finder">
                  <div class="search-container">
                    <h4 class="section-subtitle">Find Your Local Regulations</h4>
                    <div class="search-input-container">
                      <span class="search-icon">🔍</span>
                      <input 
                        v-model="userLocation" 
                        type="text" 
                        placeholder="Enter your city or postcode..." 
                        class="search-input"
                        @input="fetchLocationSuggestions"
                      />
                      <button 
                        v-if="userLocation" 
                        @click="clearLocation" 
                        class="clear-button"
                      >
                        ✕
                      </button>
                    </div>
                  </div>
                  
                  <!-- Error Message -->
                  <div v-if="errorMessage" class="error-message">
                    <span class="error-icon">⚠️</span> {{ errorMessage }}
                  </div>
                  
                  <!-- Suggestions Dropdown -->
                  <ul v-if="locationSuggestions.length" class="location-suggestions">
                    <li 
                      v-for="(suggestion, index) in locationSuggestions" 
                      :key="index" 
                      @click="selectLocation(suggestion)" 
                      class="suggestion-item"
                    >
                      <span class="location-icon">📍</span>
                      {{ suggestion.display_name }}
                    </li>
                  </ul>

                  <!-- Selected Location Info -->
                  <div v-if="selectedLocation" class="selected-location-info">
                    <div class="location-header">
                      <span class="location-pin">📌</span>
                      <h5>Selected Location</h5>
                    </div>
                    <p class="location-name">{{ selectedLocation.display_name }}</p>
                    <div v-if="autoDetectedState" class="state-detected">
                      <span class="check-icon">✓</span> We detected you're in <strong>{{ getStateFullName(autoDetectedState) }}</strong>
                    </div>
                    <p v-else class="error-message no-margin">Could not detect state from location. Please select manually below.</p>
                  </div>
                </div>
                
                <!-- Manual state selection -->
                <div class="state-selector-container">
                  <h4 class="section-subtitle">Australian Fencing Regulations by State</h4>
                  
                  <p v-if="!selectedState" class="select-prompt">
                    <span class="prompt-icon">👇</span> Select your state to view regulations
                  </p>
                  
                  <div class="state-selector">
                    <button 
                      v-for="state in australianStates" 
                      :key="state.code" 
                      :class="['state-button', { active: selectedState === state.code }]"
                      @click="selectState(state.code)"
                    >
                      {{ state.name }}
                    </button>
                  </div>
                </div>
                
                <!-- Regulation content area -->
                <div v-if="selectedState" class="regulation-content">
                  <div class="state-header">
                    <div class="state-icon">
                      <span v-if="selectedState === 'nsw'">🏙️</span>
                      <span v-else-if="selectedState === 'vic'">🏛️</span>
                      <span v-else-if="selectedState === 'qld'">🌴</span>
                      <span v-else-if="selectedState === 'wa'">🌅</span>
                      <span v-else-if="selectedState === 'sa'">🍇</span>
                      <span v-else-if="selectedState === 'tas'">🏝️</span>
                      <span v-else-if="selectedState === 'nt'">🏜️</span>
                      <span v-else-if="selectedState === 'act'">🏛️</span>
                      <span v-else>🇦🇺</span>
                    </div>
                    <h5>{{ getStateFullName(selectedState) }} Pool Fencing Requirements</h5>
                  </div>
                  
                  <div class="regulation-details">
                    <div class="regulation-item">
                      <h6><span class="requirement-icon">📏</span> Barrier Requirements</h6>
                      <ul>
                        <li v-if="selectedState === 'nsw'">Minimum fence height: 1.2 meters</li>
                        <li v-if="selectedState === 'nsw'">Maximum gap from ground: 100mm</li>
                        <li v-if="selectedState === 'nsw'">No climbable objects within 900mm of fence</li>
                        <li v-if="selectedState === 'nsw'">Gates must open outwards, away from pool area</li>
                        <li v-if="selectedState === 'nsw'">Gates must be self-closing and self-latching</li>
                        
                        <li v-if="selectedState === 'vic'">Minimum fence height: 1.2 meters</li>
                        <li v-if="selectedState === 'vic'">Maximum gap from ground: 100mm</li>
                        <li v-if="selectedState === 'vic'">No climbable objects within 900mm of fence</li>
                        <li v-if="selectedState === 'vic'">Self-closing and self-latching gates that open outward</li>
                        <li v-if="selectedState === 'vic'">Different requirements based on pool construction date</li>
                        
                        <!-- Similar pattern for other states -->
                      </ul>
                    </div>
                    
                    <div class="regulation-item">
                      <h6><span class="requirement-icon">📜</span> Legal Requirements</h6>
                      <ul>
                        <li v-if="selectedState === 'nsw'">All pools must be registered on the NSW Swimming Pool Register</li>
                        <li v-if="selectedState === 'nsw'">Mandatory pool barrier certification required when selling or leasing property</li>
                        <li v-if="selectedState === 'nsw'">Compliance certificate valid for 3 years</li>
                        <li v-if="selectedState === 'nsw'">Penalties of up to $5,500 for non-compliance</li>
                        
                        <li v-if="selectedState === 'vic'">All pools and spas must be registered with local council</li>
                        <li v-if="selectedState === 'vic'">Mandatory safety barrier inspections every 4 years</li>
                        <li v-if="selectedState === 'vic'">Certificate of compliance required</li>
                        <li v-if="selectedState === 'vic'">Penalties over $1,652 for individuals and $8,261 for companies</li>
                        
                        <!-- Similar pattern for other states -->
                      </ul>
                    </div>
                  </div>
                  
                  <div class="regulation-link">
                    <a :href="getOfficialLink()" target="_blank" class="resource-link">
                      <span class="link-icon">🔗</span> Official {{ selectedState.toUpperCase() }} Swimming Pool Safety Guidelines
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Disclaimer section -->
        <div class="disclaimer">
          <div class="disclaimer-icon">ℹ️</div>
          <div class="disclaimer-content">
            <p>
              These regulations are based on the latest available data. For the most accurate and up-to-date information, please consult your local council or refer to the official government resources.
            </p>
            <a href="https://www.royallifesaving.com.au/__data/assets/pdf_file/0014/74021/Royal-Life-Saving-Review-of-Pool-Fencing-Legistration-in-Australia.pdf" target="_blank" class="resource-link">
              <span class="pdf-icon">📄</span> Royal Life Saving Australia - Review of Pool Fencing Legislation
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PoolMenu from './components/PoolMenu.vue'

export default {
  name: 'BackyardPool',
  components: {
    PoolMenu
  },
  data() {
    return {
      menuOpen: false,
      selectedState: '',
      australianStates: [
        { code: 'nsw', name: 'NSW' },
        { code: 'vic', name: 'VIC' },
        { code: 'qld', name: 'QLD' },
        { code: 'wa', name: 'WA' },
        { code: 'sa', name: 'SA' },
        { code: 'tas', name: 'TAS' },
        { code: 'nt', name: 'NT' },
        { code: 'act', name: 'ACT' }
      ],
      // Location finder variables
      userLocation: '',
      locationSuggestions: [],
      selectedLocation: null,
      autoDetectedState: '',
      errorMessage: ''
    }
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
    navigateToPage(route) {
      // Ensure we're using router navigation, not page reload
      if (this.$router) {
        this.$router.push(route);
        // Scroll to top after navigation
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    },
    // State selection
    selectState(stateCode) {
      this.selectedState = stateCode;
    },
    // Get full state name from state code
    getStateFullName(stateCode) {
      const stateMap = {
        'nsw': 'New South Wales',
        'vic': 'Victoria',
        'qld': 'Queensland',
        'wa': 'Western Australia',
        'sa': 'South Australia',
        'tas': 'Tasmania',
        'nt': 'Northern Territory',
        'act': 'Australian Capital Territory'
      };
      return stateMap[stateCode.toLowerCase()] || stateCode;
    },
    // Location finder methods
    async fetchLocationSuggestions() {
      if (this.userLocation.length > 2) {
        try {
          const response = await fetch(`https://nominatim.openstreetmap.org/search?format=json&addressdetails=1&q=${this.userLocation}+Australia`);
          const data = await response.json();
          
          // Filter to show only Australian locations
          const australianLocations = data.filter(location => location.address && location.address.country === 'Australia');
          
          if (australianLocations.length === 0) {
            this.errorMessage = 'Location not found or not in Australia. Please enter a valid Australian location.';
            this.locationSuggestions = [];
          } else {
            this.errorMessage = '';
            this.locationSuggestions = australianLocations;
          }
        } catch (error) {
          this.errorMessage = 'Error fetching location data. Please try again.';
          this.locationSuggestions = [];
        }
      } else {
        this.locationSuggestions = [];
        this.errorMessage = '';
      }
    },
    // When user selects a location
    selectLocation(location) {
      this.userLocation = location.display_name;
      this.selectedLocation = location;
      this.locationSuggestions = [];

      // Extract state information from the location
      const stateName = location.address.state || location.address.state_district || '';
      
      // Map full state names to state codes
      const stateMap = {
        'Victoria': 'vic',
        'New South Wales': 'nsw',
        'Queensland': 'qld',
        'South Australia': 'sa',
        'Western Australia': 'wa',
        'Northern Territory': 'nt',
        'Tasmania': 'tas',
        'Australian Capital Territory': 'act'
      };

      // Set the detected state
      const stateCode = stateMap[stateName];
      this.autoDetectedState = stateCode || '';
      
      // Auto-select the state if detected
      if (stateCode) {
        this.selectedState = stateCode;
      }
    },
    // Clear the location input and suggestions
    clearLocation() {
      this.userLocation = '';
      this.locationSuggestions = [];
      this.errorMessage = '';
      this.selectedLocation = null;
      this.autoDetectedState = '';
    },
    // Get official link based on selected state
    getOfficialLink() {
      const linkMap = {
        'nsw': 'https://www.fairtrading.nsw.gov.au/housing-and-property/pool-safety',
        'vic': 'https://www.vba.vic.gov.au/consumers/swimming-pools',
        'qld': 'https://www.qbcc.qld.gov.au/home-building-owners/pool-safety',
        'wa': 'https://www.commerce.wa.gov.au/building-and-energy/swimming-pool-and-spa-pool-safety',
        'sa': 'https://www.sa.gov.au/topics/housing/safety-and-modifications/pool-safety',
        'tas': 'https://www.cbos.tas.gov.au/topics/housing/building-or-renovating/swimming-pool-safety',
        'nt': 'https://nt.gov.au/property/building/build-or-renovate-a-home/swimming-pool-safety',
        'act': 'https://www.accesscanberra.act.gov.au/s/article/building-approval-and-requirements-tab-swimming-pools'
      };
      return linkMap[this.selectedState] || '#';
    }
  }
}
</script>

<style scoped>
.backyard-pool-page {
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
  background-image: url('./assets/POOLHOME.png');
  background-size: cover;
  background-position: center;
  z-index: 0;
  opacity: 0.65;
}

.bg-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, rgba(0, 51, 71, 0.45), rgba(0, 51, 71, 0.55));
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
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
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
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.highlight {
  color: #ffcc00;
  font-weight: 700;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.subheadline {
  font-size: clamp(0.9rem, 1.8vw, 1.2rem);
  line-height: 1.4;
  margin: 0 0 1rem;
  color: #ffcc00;
  font-weight: 700;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.content-section {
  background: rgba(0, 41, 61, 0.75);
  backdrop-filter: blur(10px);
  border-radius: 1rem;
  padding: 1.5rem 2rem;
  animation: fadeUp 1s ease-out 0.7s both;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
  width: 90%;
  max-width: 1300px;
  margin: 0 auto 1.5rem;
  border-left: 3px solid rgba(0, 225, 255, 0.4);
}

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Progress Bar Styles */
.progress-section {
  background: rgba(0, 41, 61, 0.85);
  backdrop-filter: blur(10px);
  padding: 0.9rem 0.5rem 0.7rem;
  border-radius: 0.75rem;
  margin: 0 auto 1.5rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  border-left: 3px solid rgba(0, 225, 255, 0.4);
  width: auto;
  max-width: max-content;
  display: inline-block;
  position: relative;
  left: 50%;
  transform: translateX(-50%);
}

.progress-container {
  max-width: max-content;
  margin: 0 auto;
  padding: 0 1rem;
}

.progress-track {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  margin: 0;
  gap: 4.5rem;
}

.progress-track::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  right: 50%;
  width: 80%;
  height: 3px;
  background: rgba(255, 255, 255, 0.2);
  transform: translate(-50%, -50%);
  z-index: 1;
}

.progress-track::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 0;
  height: 3px;
  background: #00e1ff;
  transform: translateY(-50%);
  z-index: 1;
  transition: width 0.6s ease;
  width: 100%;
}

.progress-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  z-index: 2;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.progress-step:hover {
  transform: translateY(-5px);
}

.step-number {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: rgba(0, 225, 255, 0.2);
  border: 2px solid rgba(0, 225, 255, 0.4);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1rem;
  margin-bottom: 0.5rem;
  position: relative;
  transition: all 0.3s ease;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.2);
}

.step-label {
  font-size: 0.9rem;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.7);
  transition: all 0.3s ease;
  text-align: center;
  max-width: 100px;
}

.progress-step.active .step-number {
  background: #ffcc00;
  border-color: #ffcc00;
  transform: scale(1.1);
  box-shadow: 0 5px 15px rgba(255, 204, 0, 0.4);
}

.progress-step.active .step-label {
  color: white;
}

/* Danger Card Styles */
.danger-card {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
}

.card-header {
  background: linear-gradient(135deg, rgba(0, 123, 194, 0.8), rgba(0, 98, 155, 0.8));
  padding: 1.25rem 1.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  text-align: center;
}

.danger-title {
  margin: 0;
  color: white;
  font-size: 1.6rem;
  font-weight: 700;
  text-align: center;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.card-body {
  padding: 1.5rem;
}

/* Danger Stats Styling */
.danger-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
  padding: 1.5rem;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.stat-card:nth-child(1) {
  border-left: 3px solid rgba(231, 76, 60, 0.7);
}

.stat-card:nth-child(2) {
  border-left: 3px solid rgba(241, 196, 15, 0.7);
}

.stat-card:nth-child(3) {
  border-left: 3px solid rgba(52, 152, 219, 0.7);
}

.stat-header {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
}

.stat-icon {
  font-size: 2rem;
  margin-right: 1rem;
}

.stat-header h4 {
  margin: 0;
  font-size: 1.3rem;
  font-weight: 600;
  color: white;
}

.stat-card p {
  margin: 0;
  line-height: 1.5;
  font-size: 1.05rem;
}

/* Barrier Importance Section */
.barrier-importance {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
  padding: 1.5rem;
  margin-bottom: 2rem;
  border-left: 3px solid rgba(46, 204, 113, 0.7);
}

.section-subtitle {
  color: #00e1ff;
  font-size: 1.3rem;
  margin: 0 0 1rem;
  font-weight: 600;
}

.barrier-importance p {
  margin: 0;
  line-height: 1.6;
  font-size: 1.05rem;
}

/* Regulations Section */
.regulations-section {
  margin-bottom: 2rem;
}

/* Enhanced Location Finder Styles */
.location-finder {
  background: rgba(0, 41, 61, 0.6);
  border-radius: 1rem;
  padding: 1.8rem;
  margin-bottom: 1.8rem;
  border-left: 5px solid rgba(0, 225, 255, 0.7);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease;
}

.location-finder:hover {
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
  transform: translateY(-3px);
}

.search-container {
  margin-bottom: 1.25rem;
}

.search-icon {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  font-size: 1.2rem;
  color: rgba(0, 225, 255, 0.7);
}

.search-input-container {
  position: relative;
  display: flex;
  align-items: center;
  margin-top: 1rem;
}

.search-input {
  width: 100%;
  padding: 1rem 3rem 1rem 3rem;
  border-radius: 2rem;
  border: 2px solid rgba(0, 225, 255, 0.4);
  background: rgba(0, 0, 0, 0.3);
  color: white;
  font-size: 1.1rem;
  outline: none;
  transition: all 0.3s ease;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.search-input:focus {
  border-color: rgba(0, 225, 255, 0.8);
  box-shadow: 0 0 15px rgba(0, 225, 255, 0.3);
}

.search-input::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

.clear-button {
  position: absolute;
  right: 1.2rem;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(255, 255, 255, 0.1);
  border: none;
  color: rgba(255, 255, 255, 0.7);
  cursor: pointer;
  font-size: 0.9rem;
  height: 25px;
  width: 25px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.clear-button:hover {
  background-color: rgba(231, 76, 60, 0.3);
  color: #fff;
}

.error-message {
  color: #e74c3c;
  margin: 0.7rem 0;
  font-size: 0.95rem;
  padding: 0.5rem 1rem;
  background: rgba(231, 76, 60, 0.1);
  border-radius: 0.5rem;
  display: flex;
  align-items: center;
}

.error-icon {
  margin-right: 0.5rem;
}

.no-margin {
  margin: 0;
}

.location-suggestions {
  max-height: 250px;
  overflow-y: auto;
  background: rgba(0, 41, 61, 0.7);
  border-radius: 1rem;
  margin-top: 0.7rem;
  border: 1px solid rgba(0, 225, 255, 0.3);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
  z-index: 10;
  position: relative;
}

.suggestion-item {
  padding: 1rem 1.2rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
}

.suggestion-item:hover {
  background: rgba(0, 225, 255, 0.2);
}

.suggestion-item:last-child {
  border-bottom: none;
}

.location-icon {
  margin-right: 0.8rem;
  font-size: 1.1rem;
}

.selected-location-info {
  margin-top: 1.3rem;
  padding: 1.2rem;
  background: rgba(0, 225, 255, 0.1);
  border-radius: 1rem;
  border-left: 4px solid rgba(0, 225, 255, 0.6);
  animation: fadeIn 0.4s ease;
}

.location-header {
  display: flex;
  align-items: center;
  margin-bottom: 0.8rem;
}

.location-pin {
  font-size: 1.3rem;
  margin-right: 0.8rem;
}

.location-header h5 {
  margin: 0;
  font-size: 1.2rem;
  color: #00e1ff;
  font-weight: 600;
}

.location-name {
  margin: 0 0 0.8rem;
  padding: 0.5rem 0.8rem;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.5rem;
  font-size: 1rem;
}

.state-detected {
  display: flex;
  align-items: center;
  color: #2ecc71;
  font-size: 1rem;
  padding: 0.5rem 0.8rem;
  background: rgba(46, 204, 113, 0.1);
  border-radius: 0.5rem;
}

.check-icon {
  margin-right: 0.6rem;
}

/* State selector styles */
.state-selector-container {
  margin: 2rem 0;
}

.select-prompt {
  text-align: center;
  margin: 1rem 0 1.2rem;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
}

.prompt-icon {
  margin-right: 0.6rem;
  font-size: 1.2rem;
  animation: bounce 1s infinite alternate;
}

@keyframes bounce {
  from { transform: translateY(0); }
  to { transform: translateY(5px); }
}

.state-selector {
  display: flex;
  flex-wrap: wrap;
  gap: 0.7rem;
  justify-content: center;
  margin-bottom: 1.5rem;
}

.state-button {
  background: rgba(0, 41, 61, 0.7);
  border: 2px solid rgba(0, 225, 255, 0.3);
  border-radius: 2rem;
  padding: 0.6rem 1.2rem;
  font-size: 1rem;
  color: rgba(255, 255, 255, 0.8);
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  min-width: 70px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.state-button:hover {
  background: rgba(0, 123, 194, 0.5);
  border-color: rgba(0, 225, 255, 0.6);
  color: white;
  transform: translateY(-3px);
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
}

.state-button.active {
  background: linear-gradient(135deg, rgba(0, 123, 194, 0.8), rgba(0, 225, 255, 0.6));
  border-color: rgba(0, 225, 255, 0.8);
  color: white;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
}

/* Regulation Content Styles */
.regulation-content {
  background: rgba(0, 41, 61, 0.6);
  border-radius: 1rem;
  padding: 0;
  margin-bottom: 1.5rem;
  overflow: hidden;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
  animation: fadeIn 0.5s ease;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(15px); }
  to { opacity: 1; transform: translateY(0); }
}

.state-header {
  background: linear-gradient(to right, rgba(0, 123, 194, 0.8), rgba(0, 41, 61, 0.9));
  padding: 1.5rem;
  display: flex;
  align-items: center;
  border-bottom: 1px solid rgba(0, 225, 255, 0.3);
}

.state-icon {
  font-size: 2rem;
  margin-right: 1rem;
  background: rgba(255, 255, 255, 0.1);
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.state-header h5 {
  margin: 0;
  font-size: 1.5rem;
  color: white;
  font-weight: 700;
  text-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.regulation-details {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  padding: 1.5rem;
}

.regulation-item {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.regulation-item:hover {
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
  transform: translateY(-3px);
}

.regulation-item h6 {
  color: #00e1ff;
  font-size: 1.2rem;
  margin: 0 0 1rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  border-bottom: 1px solid rgba(0, 225, 255, 0.2);
  padding-bottom: 0.8rem;
}

.requirement-icon {
  margin-right: 0.7rem;
}

.regulation-item ul {
  margin: 0;
  padding-left: 1.5rem;
}

.regulation-item li {
  margin-bottom: 0.7rem;
  line-height: 1.5;
  position: relative;
  padding-left: 0.5rem;
}

.regulation-item li::before {
  content: '';
  position: absolute;
  left: -1rem;
  top: 0.6rem;
  width: 6px;
  height: 6px;
  background: rgba(0, 225, 255, 0.7);
  border-radius: 50%;
}

.regulation-link {
  padding: 1.2rem;
  text-align: center;
  background: rgba(0, 0, 0, 0.2);
  border-top: 1px solid rgba(0, 225, 255, 0.2);
}

.resource-link {
  display: inline-flex;
  align-items: center;
  color: #00e1ff;
  text-decoration: none;
  padding: 0.8rem 1.5rem;
  border: 1px solid rgba(0, 225, 255, 0.4);
  border-radius: 2rem;
  transition: all 0.3s ease;
  background: rgba(0, 41, 61, 0.6);
  font-weight: 600;
}

.resource-link:hover {
  background: rgba(0, 225, 255, 0.1);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
  transform: translateY(-2px);
}

.link-icon, .pdf-icon {
  margin-right: 0.7rem;
  font-size: 1.2rem;
}

/* Disclaimer Styles */
.disclaimer {
  margin-top: 2rem;
  padding: 1.8rem;
  background: linear-gradient(135deg, rgba(243, 156, 18, 0.3), rgba(231, 76, 60, 0.2));
  border-radius: 1rem;
  display: flex;
  align-items: flex-start;
  border-left: 6px solid rgba(243, 156, 18, 0.9);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.disclaimer::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(45deg, 
    rgba(243, 156, 18, 0) 0%,
    rgba(243, 156, 18, 0.1) 50%, 
    rgba(243, 156, 18, 0) 100%);
  animation: shine 3s infinite;
}

@keyframes shine {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(100%); }
}

.disclaimer:hover {
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
  transform: translateY(-4px);
}

.disclaimer-icon {
  font-size: 2.2rem;
  margin-right: 1.2rem;
  color: rgba(243, 156, 18, 1);
  background: rgba(243, 156, 18, 0.2);
  width: 60px;
  height: 60px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 15px rgba(243, 156, 18, 0.3);
  position: relative;
  z-index: 2;
}

.disclaimer-content {
  flex: 1;
  position: relative;
  z-index: 2;
}

.disclaimer-content p {
  margin-bottom: 1.2rem;
  color: white;
  line-height: 1.7;
  font-size: 1.05rem;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
  font-weight: 500;
}

.disclaimer .resource-link {
  background: rgba(243, 156, 18, 0.9);
  border: 2px solid rgba(243, 156, 18, 0.3);
  color: white;
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  padding: 0.9rem 1.8rem;
  border-radius: 2rem;
  transition: all 0.3s ease;
  text-decoration: none;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  letter-spacing: 0.5px;
  position: relative;
  overflow: hidden;
}

.disclaimer .resource-link::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to right, 
    rgba(255, 255, 255, 0.1) 0%, 
    rgba(255, 255, 255, 0.2) 50%, 
    rgba(255, 255, 255, 0.1) 100%);
  transform: translateX(-100%);
  transition: transform 0.6s ease;
}

.disclaimer .resource-link:hover {
  background: rgba(243, 156, 18, 1);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
  transform: translateY(-4px) scale(1.02);
}

.disclaimer .resource-link:hover::after {
  transform: translateX(100%);
}

.pdf-icon {
  margin-right: 0.8rem;
  font-size: 1.3rem;
  background: rgba(255, 255, 255, 0.2);
  padding: 7px;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.disclaimer .resource-link:hover .pdf-icon {
  background: rgba(255, 255, 255, 0.3);
  transform: scale(1.1);
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .location-finder, 
  .regulation-content,
  .regulation-item,
  .disclaimer {
    padding: 1.2rem;
  }
  
  .search-input {
    padding: 0.9rem 3rem 0.9rem 2.8rem;
    font-size: 1rem;
  }
  
  .state-header h5 {
    font-size: 1.3rem;
  }
  
  .regulation-details {
    grid-template-columns: 1fr;
    gap: 1.2rem;
  }
  
  .state-selector {
    gap: 0.6rem;
  }
  
  .state-button {
    padding: 0.5rem 1rem;
    font-size: 0.9rem;
  }
}

@media (max-width: 480px) {
  .location-finder, 
  .regulation-content,
  .regulation-item,
  .disclaimer {
    padding: 1rem;
  }
  
  .search-input {
    padding: 0.8rem 2.6rem 0.8rem 2.6rem;
    font-size: 0.95rem;
  }
  
  .search-icon {
    left: 0.8rem;
    font-size: 1rem;
  }
  
  .clear-button {
    right: 0.8rem;
  }
  
  .state-header {
    flex-direction: column;
    text-align: center;
    padding: 1rem;
  }
  
  .state-icon {
    margin-right: 0;
    margin-bottom: 0.8rem;
  }
  
  .state-header h5 {
    font-size: 1.2rem;
  }
  
  .disclaimer {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  
  .disclaimer-icon {
    margin-right: 0;
    margin-bottom: 0.8rem;
  }
  
  .resource-link {
    padding: 0.7rem 1.2rem;
    font-size: 0.9rem;
  }
}
</style> 