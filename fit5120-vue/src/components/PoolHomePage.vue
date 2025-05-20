<template>
  <div id="poolTop" class="beach-home-container" :class="{ 'immediate-display': isDirectTransition }">
    <!-- Custom Navigation Bar -->
    <div class="navbar-wrapper" :class="{ 'scrolled': isScrolled && navbarDynamicEnabled, 'hidden': isNavbarHidden }">
      <nav class="navbar">
        <div class="navbar-content">
          <!-- Logo on left -->
          <div class="navbar-logo">
            <router-link to="/" class="logo-link">
              <span class="logo-water">Water</span><span class="logo-wise">Wise</span><span class="logo-family">Family</span>
            </router-link>
          </div>
          
          <!-- Navigation tabs in middle -->          
          <div class="navbar-tabs">
            <!-- Beach tab with dropdown -->
            <div class="navbar-tab-dropdown">
              <router-link 
                to="/beach" 
                class="navbar-tab" 
                active-class="active"
              >
                <span class="tab-text">BEACH</span>
                <span class="dropdown-arrow">▼</span>
              </router-link>
              <div class="dropdown-menu">
                <div class="menu-section">
                  <div class="menu-section-header">Interactive Features</div>
                  <a href="#" @click.prevent="showRipIdentifierPopup = true; document.body.style.overflow = 'hidden';" class="dropdown-item highlight-item">
                    <span class="highlight-icon">✹</span>
                    Rip Current Identifier
                  </a>
                  <a href="#" @click.prevent="showRipCurrentQuiz" class="dropdown-item highlight-item">
                    <span class="highlight-icon">✹</span>
                    Rip Safety Quiz
                  </a>
                </div>
                
                <div class="menu-divider"></div>
                
                <div class="menu-section">
                  <div class="menu-section-header">Safety Information</div>
                  <router-link to="/beach#sandy-content-section" class="dropdown-item">
                    Lowering Your Risk
                  </router-link>
                  <router-link to="/beach#rescue-content-section" class="dropdown-item">
                    Emergency Response
                  </router-link>
                </div>
              </div>
            </div>
            
            <!-- Pool tab with dropdown -->
            <div class="navbar-tab-dropdown">
              <router-link 
                to="/pool" 
                class="navbar-tab" 
                active-class="active"
              >
                <span class="tab-text">POOL</span>
                <span class="dropdown-arrow">▼</span>
              </router-link>
              <div class="dropdown-menu">
                <div class="menu-section">
                  <div class="menu-section-header">Interactive Features</div>
                  <a href="#" @click.prevent="openQuizPopup" class="dropdown-item highlight-item">
                    <span class="highlight-icon">✹</span>
                    Pool Safety Quiz
                  </a>
                </div>
                
                <div class="menu-divider"></div>
                
                                  <div class="menu-section">
                  <div class="menu-section-header">Safety Information</div>
                  <router-link to="/pool#heroSection" class="dropdown-item highlight-item">
                    <span class="highlight-icon">✹</span>
                    Fence Regulations
                  </router-link>
                  <a href="#" @click.prevent="navigateToSection('keySteps')" class="dropdown-item">
                    Steps to a Safer Pool
                  </a>
                </div>
              </div>
            </div>
            
            <!-- River tab with dropdown -->
            <div class="navbar-tab-dropdown">
              <router-link 
                to="/river" 
                class="navbar-tab" 
                active-class="active"
              >
                <span class="tab-text">RIVER</span>
                <span class="dropdown-arrow">▼</span>
              </router-link>
              <div class="dropdown-menu">
                <div class="menu-section">
                  <div class="menu-section-header">Interactive Features</div>
                  <a href="#" @click.prevent="showRiverSafetyQuiz" class="dropdown-item highlight-item">
                    <span class="highlight-icon">✹</span>
                    River Simulation
                  </a>
                </div>
                
                <div class="menu-divider"></div>
                
                <div class="menu-section">
                  <div class="menu-section-header">Safety Information</div>
                  <router-link to="/river#criticalPrecautions" class="dropdown-item">
                    Critical Precautions
                  </router-link>
                                <router-link to="/river?section=rescue#rescueResponse" class="dropdown-item">
                Rescue Response
              </router-link>
                </div>
              </div>
            </div>
          </div>
          
                <!-- Right side space -->
      <div class="navbar-right">
        <!-- Can be used for search, user menu, etc. -->
      </div>
        </div>
      </nav>
      
      <!-- Search bar that appears in navbar only when scrolled - temporarily disabled -->
      <div v-if="isScrolled && navbarDynamicEnabled" class="navbar-integrated-search" :class="{ 'expanded': compactToolOpen }">
        <div class="search-bar-compact">
          <!-- Compact search options -->
          <div class="search-options-compact">
            <button 
              v-for="(option, index) in searchOptions" 
              :key="index" 
              class="search-option-compact" 
              :class="{ active: compactToolOpen && selectedCompactOption === index }"
              @click="toggleCompactTool(index)"
            >
              <span class="option-emoji">{{ searchOptionsEmojis[index] }}</span>
              <span class="option-label" v-if="compactToolOpen">{{ option }}</span>
            </button>
          </div>
          
          <!-- Active Tool Input Area - Only shows when a specific tool is selected -->
          <div v-if="compactToolOpen" class="compact-tool-container">
            <!-- Rip Identifier -->
            <div v-if="selectedCompactOption === 0" class="compact-tool-content">
              <button class="compact-upload-btn" @click="triggerFileUpload">
                <span class="upload-icon">📸</span> Upload Beach Image
              </button>
              <input type="file" ref="fileInput" class="hidden-file-input" accept="image/*" @change="handleImageUpload" />
            </div>
            
            <!-- Search Beach -->
            <div v-if="selectedCompactOption === 1" class="compact-tool-content">
              <div class="compact-search-input">
                <input type="text" placeholder="Enter Australian beach name..." v-model="beachSearchQuery">
                <button @click="searchBeach">Find</button>
              </div>
            </div>
            
            <!-- Compare Beaches -->
            <div v-if="selectedCompactOption === 2" class="compact-tool-content">
              <div class="compact-compare-inputs">
                <div class="compact-input-group">
                  <input type="text" placeholder="Home Beach" v-model="homeBeach">
                </div>
                <div class="compact-input-group">
                  <input type="text" placeholder="Beach to Compare" v-model="compareBeach">
                </div>
                <button @click="compareBeaches">Compare</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Hero Content with Dynamic Text -->
    <div class="hero-content" :class="{ 'suggestions-active-padding': isPostcodeFinderActive }">
      <!-- Main flex container for vertical layout -->
      <div class="hero-flex-container">
        <!-- Left side - Dynamic Hero Text -->
        <div class="hero-left-column">
          <div id="heroSection" class="hero-section">
            <h1 class="dynamic-headline">
              <span class="text-line">IT ONLY TAKES</span>
              <span class="text-line"><span class="highlight">20 SILENT SECONDS</span></span>
              <span class="text-line">FOR A TODDLER</span>
              <span class="text-line">TO DROWN</span>
            </h1>
            
            <div class="hero-connector">
              <p class="connector-text">Learn to safeguard your pool and keep your family safe</p>
            </div>
            
            <!-- Pool Safety Standards Finder - added from BackyardPool.vue -->
            <div class="safety-standards-container" :class="{ 'suggestions-active': isPostcodeFinderActive }">
              <div class="section-top">
                <h4 class="section-subtitle">Does Your Pool Meet Local Safety Standards?</h4>
                <div class="option-toggle">
                  <button 
                    @click="activeOption = 'postcode'" 
                    :class="['toggle-btn', activeOption === 'postcode' ? 'active' : '']"
                  >
                    <span class="toggle-icon">📍</span> Enter Postcode
                  </button>
                  <button 
                    @click="activeOption = 'state'" 
                    :class="['toggle-btn', activeOption === 'state' ? 'active' : '']"
                  >
                    <span class="toggle-icon">🇦🇺</span> Select State
                  </button>
                </div>
              </div>
              
              <!-- Postcode/location search option -->
              <div v-if="activeOption === 'postcode'" class="option-content location-finder">
                <div class="search-container">
                  <div class="search-input-container">
                    <span class="search-icon">🔍</span>
                    <input 
                      v-model="userLocation" 
                      type="text" 
                      placeholder="Enter your city or postcode..." 
                      class="search-input"
                      @input="fetchLocationSuggestions"
                    />
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
                  <p v-if="!autoDetectedState && activeOption === 'postcode'" class="error-message no-margin">Could not detect state from location. Please select manually below.</p>
                </div>
              </div>
              
              <!-- Manual state selection -->
              <div v-if="activeOption === 'state'" class="state-selector-container">
                <h4 class="section-subtitle">Australian Fencing Regulations by State</h4>
                
                <p v-if="!selectedState" class="select-prompt">
                  <span class="prompt-icon">👇</span> Select your state to view regulations
                </p>
                
                <div class="select-wrapper">
                  <select 
                    v-model="selectedState"
                    class="state-dropdown"
                    @change="handleStateChange"
                  >
                    <option value="" disabled selected>Select a state</option>
                    <option 
                      v-for="state in australianStates" 
                      :key="state.code" 
                      :value="state.code"
                    >
                      {{ state.name }}
                    </option>
                  </select>
                  <div class="select-arrow">▼</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Large scroll down indicator -->
      <div class="large-scroll-indicator">
        <svg class="large-chevron-down" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M4 8L12 16L20 8" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
    </div>
  </div>
  
  <!-- White content section completely separate from container -->
  <div class="elegant-content-section" :class="{ 'pushed-down-by-suggestions': isPostcodeFinderActive }">
    <!-- Left-aligned heading about Australian beach conditions -->
    <div class="section-heading">
      <span class="section-label">Backyard Pools in Australia</span>
      <h2 class="section-title">The Hidden Dangers<br>in Your Backyard</h2>
      <div class="section-tagline-container">
                  <p class="section-tagline">
          Drowning is a leading cause of accidental death for toddlers in Australia, with backyard pools being <br>a major risk factor.
        </p>
        

      </div>
    </div>
    
    <!-- Beach images comparison container -->
    <div class="beach-images-comparison">
      <div class="comparison-container">
        <div class="image-container">
          <!-- After image - will be revealed -->
          <img src="../assets/backyard_pool.jpg" alt="Backyard Pool" class="comparison-image">
          <!-- Hotspots for Pool Safety -->
          <div class="hotspot-container pool-hotspots">
            <div class="hotspot" style="top: 25%; left: 20%;">
              <div class="hotspot-dot"></div>
              <div class="hotspot-pulse"></div>
              <div class="hotspot-info right">
                <h4>Secure Fencing</h4>
                <p>1.2m+ fence with self-closing, self-latching gate. Check for gaps and climbable objects.</p>
              </div>
            </div>
            <div class="hotspot" style="top: 55%; left: 65%;">
              <div class="hotspot-dot"></div>
              <div class="hotspot-pulse"></div>
              <div class="hotspot-info left">
                <h4>Active Supervision</h4>
                <p>Always watch toddlers near water. Keep them in arm's reach</p>
              </div>
            </div>
          </div>
          <!-- Australian beach hotspots -->
          <!-- Hotspots removed as they are not relevant to a single pool image -->
          <!-- Slider handle -->
          <!-- Slider handle removed -->
          <!-- Before image - shown by default -->
          <!-- Comparison 'before' (Asian beach) image and its hotspots removed -->
                </div>
        <!-- Comparison labels removed -->
              </div>
                </div>
              </div>
  
  <!-- Sandy colored content section -->  <div id="keySteps" class="sandy-content-section pool-key-steps">    <!-- Left-aligned heading for sandy section -->    <div class="section-heading">      <span class="section-label">Pool Safety Essentials</span>      <h2 class="section-title">Key Steps to a Safer Pool</h2>            </div>
    
    <!-- Content placeholder for the sandy section -->
    <div class="sandy-content-placeholder">
      <!-- Horizontal bar layout with scroll-triggered images -->
      <div class="safety-items-container">
        <!-- Item about Pool Fencing -->
        <div class="safety-item">
          <div class="safety-image-container">
            <div class="image-mask">
              <img src="../assets/barrier.jpg" alt="Secure Pool Fencing" class="safety-image">
          </div>
        </div>
          <div class="safety-content">
            <h3 class="safety-content-title">WHY THIS MATTERS</h3>
                          <div class="safety-stat-container">              <div class="stat-row">                <span class="safety-stat-number"><span class="counter" ref="poolFenceCounter">0</span>%</span>                <p class="safety-stat-text">of toddler drownings occur in pools with non-compliant fencing.</p>              </div>            </div>            <div class="safety-content-wrapper">
              <p class="safety-content-text">Proper pool fencing is required by law in Australia. Make sure your pool fence meets regulations for your state.</p>
            </div>
          </div>          <div class="safety-flag-text">
            SECURE POOL FENCING
          </div>
                      <!-- Priority label removed -->
          <div class="safety-item-info"></div>
  </div>
  
        <!-- Item about Active Supervision & CPR -->
        <div class="safety-item">
          <div class="safety-image-container">
            <div class="image-mask">
              <img src="../assets/pexels-freestockpro-12615996.jpg" alt="Active Pool Supervision and CPR" class="safety-image">
              </div>
              <button @click="openQuizPopup" class="image-overlay-button">
                <span>Take Pool Safety Quiz</span>
                <span class="quiz-icon">❓</span>
              </button>
            </div>
          <div class="safety-content">
            <h3 class="safety-content-title">WHY THIS MATTERS</h3>
            <div class="safety-stat-container">
              <div class="stat-row">
                <span class="safety-stat-number"><span class="counter" ref="poolSupervisionCounter">0</span>%</span>
                <p class="safety-stat-text">of child drownings are preventable with constant adult supervision.</p>
              </div>
            </div>
            <p class="safety-content-text">Always stay within arm's reach of toddlers & be prepared. Knowing CPR can save a life before help arrives. </p>
          </div>
          <div class="safety-flag-text">
            CONSTANT SUPERVISION
          </div>
          <div class="safety-item-info">
            <span class="safety-priority"><span class="icon-marker">■</span> HIGH PRIORITY</span>
          </div>
        </div>
        
        <!-- Item about Pool Area Safety -->
        <div class="safety-item">
          <div class="safety-image-container">
            <div class="image-mask">
              <img src="../assets/memorial-day_pool-rules.jpg" alt="Pool Area Safety and Hazard Removal" class="safety-image">
            </div>
          </div>
          <div class="safety-content">
            <h3 class="safety-content-title">WHY THIS MATTERS</h3>
            <div class="safety-stat-container">
              <div class="stat-row">
                <span class="safety-stat-number"><span class="counter" ref="poolHazardCounter">0</span>%</span>
                <p class="safety-stat-text">of pool safety issues involve climbable objects or propped gates.</p>
              </div>
            </div>
            <p class="safety-content-text">Simple habits like putting away toys & checking gates can prevent accidents.</p>
          </div>
          <div class="safety-flag-text">
            REMOVE POOL HAZARDS
          </div>
          <div class="safety-item-info">
            <span class="safety-priority"><span class="icon-marker">■</span> HIGH PRIORITY</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  
  <!-- Video popup component -->
  <VideoPopup 
    :show="showVideoPopup" 
    :video-src="videoSrc" 
    :title="videoTitle" 
    @close="closeVideoPopup"
  />
  
  <!-- Rip Escape Simulation popup -->
  <div v-if="showRipSimulation" class="rip-simulation-overlay" @click.self="closeRipSimulation">
    <div class="rip-simulation-container">
      <div class="rip-simulation-header">
        <h3>How to Escape a Rip Current</h3>
        <button class="close-button" @click="closeRipSimulation" aria-label="Close">
          <span class="close-icon"></span>
        </button>
      </div>
      <div class="rip-simulation-content">
        <RipEscapeSimulation />
      </div>
    </div>
  </div>

  <!-- Rip Current Quiz popup -->
  <div v-if="showRipCurrentQuizPopup" class="rip-simulation-overlay" @click.self="closeRipCurrentQuiz">
    <div class="rip-simulation-container quiz-container">
      <div class="rip-simulation-header">
        <h3>Rip Current Safety Quiz</h3>
        <button class="close-button" @click="closeRipCurrentQuiz" aria-label="Close">
          <span class="close-icon"></span>
        </button>
      </div>
      <div class="rip-simulation-content">
        <RipCurrentQuiz />
      </div>
    </div>
  </div>

  <!-- Rip Identifier Results popup -->
  <div v-if="showRipIdentifierPopup" class="rip-simulation-overlay" @click.self="closeRipIdentifier">
    <div class="rip-simulation-container rip-identifier-container">
      <div class="rip-simulation-header">
        <h3>Rip Current Identification</h3>
        <button class="close-button" @click="closeRipIdentifier" aria-label="Close">
          <span class="close-icon"></span>
        </button>
      </div>
      <div class="rip-simulation-content">
        <BeachComparisonTool 
          ref="ripIdentifierPopup" 
          :initialTab="'ripIdentifier'" 
          :initialSearchValue="beachSearchQuery" 
          :initialHomeBeach="homeBeach" 
          :initialCompareBeach="compareBeach"
          :ripImage="uploadedImage"
          :isPopup="true" />
      </div>
    </div>
  </div>

  <!-- Regulation Popup Component -->
  <RegulationPopup
    :show="showRegulationPopup"
    :selected-state="selectedState"
    :australian-states="australianStates"
    @close="closeRegulationPopup"
  />

  <!-- Pool Safety Quiz Popup -->
  <div v-if="showQuizPopup" class="rip-simulation-overlay" @click.self="closeQuizPopup">
    <div class="rip-simulation-container">
      <div class="rip-simulation-header">
        <h3>Pool Safety Quiz</h3>
        <button class="close-button" @click="closeQuizPopup" aria-label="Close">
          <span class="close-icon"></span>
        </button>
      </div>
      <div class="rip-simulation-content">
        <PoolSafetyQuiz />
      </div>
    </div>
  </div>

  <!-- River Safety Quiz Popup -->
  <div v-if="showRiverSafetyQuizPopup" class="rip-simulation-overlay" @click.self="closeRiverSafetyQuiz">
    <div class="rip-simulation-container quiz-container">
      <div class="rip-simulation-header">
        <h3>River Safety for Teens</h3>
        <button class="close-button" @click="closeRiverSafetyQuiz" aria-label="Close">
          <span class="close-icon"></span>
        </button>
      </div>
      <div class="rip-simulation-content">
        <RiverSafetyQuiz />
      </div>
    </div>
  </div>
</template>

<script>
import VideoPopup from './VideoPopup.vue';
import RipEscapeSimulation from '../RipEscapeSimulation.vue';
import RegulationPopup from './RegulationPopup.vue'; // Import the new popup component
import PoolSafetyQuiz from '../PoolSafetyQuiz.vue'; // Import the pool safety quiz component
import RipCurrentQuiz from '../components/RipCurrentQuiz.vue';
import BeachComparisonTool from './BeachComparisonTool.vue';
import RiverSafetyQuiz from '../components/RiverSafetyQuiz.vue'; // Import river safety quiz component
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

// Register the ScrollTrigger plugin
gsap.registerPlugin(ScrollTrigger);

export default {
  name: 'BeachHomePage',
  components: {
    VideoPopup,
    RipEscapeSimulation,
    RegulationPopup, // Register the new popup component
    PoolSafetyQuiz,
    RipCurrentQuiz,
    BeachComparisonTool,
    RiverSafetyQuiz
  },
    data() {    return {      isDirectTransition: false,      isScrolled: false,      isNavbarHidden: false,      lastScrollPosition: 0,      // Toddler stat hover state      showToddlerStat: false,      // Properties for compact tool management      compactToolOpen: false,      selectedCompactOption: 0,      searchOptions: ['Rip Identifier', 'Search Beach', 'Compare Beaches'],      searchOptionsEmojis: ['🌊', '🔍', '⚖️'],
      // Rip identifier popup
      showRipIdentifierPopup: false,
      // Rip current quiz popup
      showRipCurrentQuizPopup: false,
      // River safety quiz popup
      showRiverSafetyQuizPopup: false,
      // Data properties for beach tool
      uploadedImage: null,
      beachSearchQuery: '',
      homeBeach: '',
      compareBeach: '',
      // Flag to enable navbar dynamic behavior
      navbarDynamicEnabled: true, // Enable dynamic navbar
      // ScrollTrigger references
      scrollTriggers: [],
      // Video popup properties
      showVideoPopup: false,
      videoSrc: '',
      videoTitle: '',
      // Rip escape simulation popup
      showRipSimulation: false,
      // Pool safety quiz popup
      showQuizPopup: false,
      quizCompleted: false, // Add this line
      // Beach tool initial tab
      beachToolTab: 'search',
      // Pool drowning stats
      poolDrowningStats: {
        age0to4Percentage: 0,
        age5to14Percentage: 0
      },
      // Pool safety standards finder properties
      userLocation: '',
      locationSuggestions: [],
      selectedLocation: null,
      autoDetectedState: '',
      selectedState: '', // This will now primarily be used to pass to the popup
      errorMessage: '',
      activeOption: 'postcode', // Default active option for pool safety standards
      showRegulationPopup: false, // Data property to control regulation popup
      errorMessageTimeoutId: null, // For delaying the error message
      australianStates: [
        { code: 'nsw', name: 'NSW' },
        { code: 'vic', name: 'VIC' },
        { code: 'qld', name: 'QLD' },
        { code: 'wa', name: 'WA' },
        { code: 'sa', name: 'SA' },
        { code: 'tas', name: 'TAS' },
        { code: 'nt', name: 'NT' },
        { code: 'act', name: 'ACT' }
      ]
    }
  },
  computed: {
    isPostcodeFinderActive() {
      return this.activeOption === 'postcode' && this.locationSuggestions.length > 0;
    }
  },
  beforeCreate() {
    // Check for direct transition parameter
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('direct') === 'true') {
      window.__beachDirectTransition = true;
    }
  },
    created() {    // Set transition flag    this.isDirectTransition = window.__beachDirectTransition ||                               this.$route.query.direct === 'true';        // Clean up global flag    if (window.__beachDirectTransition) {      delete window.__beachDirectTransition;    }        // Add smooth scrolling behavior to document if needed    if (!('scrollBehavior' in document.documentElement.style)) {      this.addSmoothScrollPolyfill();    }        // Watch for route changes to handle hash navigation    this.$watch(      () => this.$route.hash,      (newHash) => {        if (newHash) {          this.scrollToElement(newHash);        }      },      { immediate: true } // Run immediately for the initial route    );        // Set values based on correct statistics from DrowningSearch data    const validatedStats = this.validatePoolDrowningStatistics();    this.poolDrowningStats.age0to4Percentage = validatedStats.age0to4Percentage;    this.poolDrowningStats.age5to14Percentage = validatedStats.age5to14Percentage;      },    mounted() {    // Check if the showQuiz query parameter is present    if (this.$route.query.showQuiz) {      // Open the quiz popup      this.openQuizPopup();      // Remove the query parameter without reloading      this.$router.replace({ path: '/pool' });    }        // Remove direct query parameter without reloading    if (this.$route.query.direct) {      this.$router.replace({ path: '/pool' });    }        // Check if there's a hash in the URL and scroll to that element
    if (this.$route.hash) {
      this.scrollToElement(this.$route.hash);
    } else {
      // If no hash, ensure page is at the top
      // Using nextTick to ensure the DOM is fully ready before scrolling
      this.$nextTick(() => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
        console.log('No hash, scrolled to top of PoolHomePage.');
      });
    }
    
    // Initialize toddler stat hover effect
    this.$nextTick(() => {
      this.initToddlerStatHover();
    });
    
    // Add scroll event listener for navbar transformation
    window.addEventListener('scroll', this.handleScroll);
    
    // Initial adjustment of container height
    this.$nextTick(() => {
      this.adjustFirstPageHeight();
    });
    
    // Add resize listener to adjust height on window resize
    window.addEventListener('resize', this.adjustFirstPageHeight);
    
    // Initialize animation state
    setTimeout(() => {
      this.animationReady = true;
    }, 100);
    
    // Apply initial styles to elegant content section for smooth edges
    this.applyRoundedCorners();
    window.addEventListener('resize', this.applyRoundedCorners);
    
    // Initialize the scroll-triggered animations for safety items
    this.$nextTick(() => {
      this.initScrollAnimations();
    });
    
    // Initialize emergency steps animations
    this.$nextTick(() => {
      this.initEmergencyStepsAnimation();
    });
    
    // Add event listener for messages from the quiz iframe
    window.addEventListener('message', this.handleMessage);
  },
  beforeDestroy() {
    // Clean up event listeners
    window.removeEventListener('scroll', this.handleScroll);
    window.removeEventListener('resize', this.applyRoundedCorners);
    window.removeEventListener('resize', this.adjustFirstPageHeight);
    window.removeEventListener('resize', this.updateArrowPosition);
    
    // Clean up ScrollTrigger instances
    this.scrollTriggers.forEach(trigger => {
      if (trigger) {
        trigger.kill();
      }
    });
    ScrollTrigger.getAll().forEach(st => st.kill());
    // Clear any pending error message timeout
    if (this.errorMessageTimeoutId) {
      clearTimeout(this.errorMessageTimeoutId);
    }
    
    // Remove the event listener when component is unmounted
    window.removeEventListener('message', this.handleMessage);
  },
  methods: {
    // Validate pool drowning statistics based on actual data from DrowningSearch
    validatePoolDrowningStatistics() {
      // These values come directly from the DrowningSearch.vue calculations
      // For age0to4: 7 pool deaths out of 18 total deaths = 38.89%, rounded to 40%
      // For age5to14: 3 pool deaths out of 12 total deaths = 25%
      return {
        age0to4Percentage: 40, // Validated from DrowningSearch.vue
        age5to14Percentage: 25  // Validated from DrowningSearch.vue
      };
    },
    
    // Initialize the toddler stat hover effect
    initToddlerStatHover() {
      // Adding a small delay to ensure DOM elements are fully rendered
      setTimeout(() => {
        const trigger = document.querySelector('.toddler-stat-trigger');
        const popup = document.querySelector('.toddler-stat-popup');
        const arrow = document.querySelector('.hand-drawn-arrow');
        
        if (trigger && popup && arrow) {
          // Update arrow path to point from the toddlers word position
          this.updateArrowPosition();
          console.log('Toddler stat hover initialized with dynamic arrow positioning');
        }
      }, 500);
      
      // Add window resize handler for responsive designs
      window.addEventListener('resize', this.updateArrowPosition);
    },
    
    // Update arrow position to always start from toddlers word
    updateArrowPosition() {
      // Simple positioning is more reliable in this case
      // No dynamic path manipulation needed
      console.log('Using fixed positioning for arrow to match design');
    },
    
    handleCardClick(type) {
      console.log(`Clicked on ${type} card`);
      if (type === 'rips') {
        // Show the rip escape simulation popup
        this.showRipSimulation = true;
        
        // Prevent page scrolling when popup is open
        document.body.style.overflow = 'hidden';
      }
    },
    
    // Add a method to close the simulation popup
    closeRipSimulation() {
      this.showRipSimulation = false;
      
      // Re-enable page scrolling
      document.body.style.overflow = '';
    },
    // Method to open the pool safety quiz popup
    openQuizPopup() {
      this.showQuizPopup = true;
      
      // Prevent page scrolling when popup is open
      document.body.style.overflow = 'hidden';
    },
    // Method to close the pool safety quiz popup
    closeQuizPopup() {
      this.showQuizPopup = false;
      this.quizCompleted = false; // Reset the completion state
      
      // Re-enable page scrolling
      document.body.style.overflow = '';
    },
    triggerVideoAnimation(event, videoSrc, videoTitle) {
      // Get the parent image container
      const imageContainer = event.target.closest('.image-mask');
      
      if (imageContainer) {
        const image = imageContainer.querySelector('img');
        
        if (image) {
          // Save original styles for restoration
          const originalTransform = image.style.transform;
          const originalTransition = image.style.transition;
          
          // Apply squeeze animation
          image.style.transition = 'transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
          image.style.transform = 'scale(0.85)';
          
          // After a short delay, start expanding and open the popup
          setTimeout(() => {
            image.style.transform = 'scale(1.05)';
            
            // Open the popup when animation is midway
            this.openVideoPopup(videoSrc, videoTitle);
            
            // Reset the image after animation completes
            setTimeout(() => {
              image.style.transition = originalTransition;
              image.style.transform = originalTransform;
            }, 300);
          }, 300);
        } else {
          // Fallback if image not found
          this.openVideoPopup(videoSrc, videoTitle);
        }
      } else {
        // Fallback if container not found
        this.openVideoPopup(videoSrc, videoTitle);
      }
    },
    openVideoPopup(videoSrc, videoTitle) {
      this.videoSrc = videoSrc;
      this.videoTitle = videoTitle;
      this.showVideoPopup = true;
      
      // Prevent page scrolling when popup is open
      document.body.style.overflow = 'hidden';
    },
    closeVideoPopup() {
      this.showVideoPopup = false;
      this.videoSrc = '';
      
      // Re-enable page scrolling
      document.body.style.overflow = '';
    },
    
    // Method to scroll to element by ID
    scrollToElement(hash) {
      // Remove the '#' character from the hash
      const targetId = hash.substring(1);
      console.log(`Attempting to scroll to element with ID: ${targetId}`);
      
      // Function to attempt scrolling with retries
      const attemptScroll = (attempts = 0, maxAttempts = 5) => {
        const targetElement = document.getElementById(targetId);
        
        if (targetElement) {
          // Use requestAnimationFrame for smoother scrolling
          requestAnimationFrame(() => {
            targetElement.scrollIntoView({
              behavior: 'smooth',
              block: 'start'
            });
            console.log(`Successfully scrolled to element with ID: ${targetId}`);
          });
        } else if (attempts < maxAttempts) {
          // Retry with exponential backoff
          console.log(`Element with ID ${targetId} not found, retrying... (${attempts + 1}/${maxAttempts})`);
          setTimeout(() => attemptScroll(attempts + 1, maxAttempts), 100 * Math.pow(2, attempts));
        } else {
          console.error(`Failed to find element with ID ${targetId} after ${maxAttempts} attempts`);
        }
      };
      
      // Wait for next tick to ensure DOM is updated, then start attempts
      this.$nextTick(() => {
        attemptScroll();
      });
    },
    
    // Method to navigate to a specific section
    navigateToSection(sectionId) {
      // First update the URL hash (for bookmarking purposes)
      this.$router.push({ path: '/beach', hash: '#' + sectionId });
      
      // Then scroll to the element
      this.scrollToElement('#' + sectionId);
    },
    
    // Initialize animations for emergency steps
    initEmergencyStepsAnimation() {
      // Use Intersection Observer to detect when the steps are in viewport
      if ('IntersectionObserver' in window) {
        const emergencySection = this.$refs.emergencySteps;
        if (!emergencySection) return;
        
        const animateElements = emergencySection.querySelectorAll('.animate-element');
        
        const options = {
          root: null,
          rootMargin: '0px',
          threshold: 0.1
        };
        
        const observer = new IntersectionObserver((entries) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              // Reset animations by removing animated class
              animateElements.forEach(el => {
                el.classList.remove('animated');
                // Force reflow to ensure animation restarts
                void el.offsetWidth;
              });
              
              // When the section is in view, animate each element with its delay
              animateElements.forEach(el => {
                const delay = el.getAttribute('data-delay') || 0;
                setTimeout(() => {
                  el.classList.add('animated');
                }, delay * 1000);
              });
            } else {
              // When section is out of view, remove animation classes
              animateElements.forEach(el => {
                el.classList.remove('animated');
              });
            }
          });
        }, options);
        
        observer.observe(emergencySection);
      } else {
        // Fallback for browsers that don't support Intersection Observer
        const animateElements = document.querySelectorAll('.animate-element');
        animateElements.forEach(el => el.classList.add('animated'));
      }
      
      // Initialize escape steps animations 
      this.initEscapeStepsAnimation();
    },
    
    // Method to initialize escape steps animations - using exact same code as emergency steps
    initEscapeStepsAnimation() {
      // Use Intersection Observer to detect when the steps are in viewport
      if ('IntersectionObserver' in window) {
        // Get the escape steps container
        const escapeStepsContainer = document.querySelector('.escape-steps');
        if (!escapeStepsContainer) {
          console.error('Escape steps container not found');
          return;
        }
        
        // Get all escape animate elements
        const escapeElements = escapeStepsContainer.querySelectorAll('.escape-animate');
        
        const options = {
          root: null,
          rootMargin: '0px',
          threshold: 0.1
        };
        
        const observer = new IntersectionObserver((entries) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              console.log('Escape steps entering viewport, animating...');
              
              // Reset animations by removing animated class
              escapeElements.forEach(el => {
                el.classList.remove('animated');
                // Force reflow to ensure animation restarts
                void el.offsetWidth;
              });
              
              // When the section is in view, animate each element with its delay
              escapeElements.forEach(el => {
                const delay = el.getAttribute('data-delay') || 0;
                setTimeout(() => {
                  el.classList.add('animated');
                }, delay * 1000);
              });
            } else {
              console.log('Escape steps leaving viewport, resetting...');
              
              // When section is out of view, remove animation classes
              escapeElements.forEach(el => {
                el.classList.remove('animated');
              });
            }
          });
        }, options);
        
        observer.observe(escapeStepsContainer);
      } else {
        // Fallback for browsers that don't support Intersection Observer
        const escapeElements = document.querySelectorAll('.escape-animate');
        escapeElements.forEach(el => el.classList.add('animated'));
      }
    },
        handleScroll() {
      // Get current scroll position
      const currentScrollPosition = window.scrollY;
      const scrollThreshold = 150;
      
      // Determine scroll direction
      if (currentScrollPosition < 0) {
        return;
      }
      
      // Always keep isScrolled as false to maintain the dark transparent navbar
      const wasScrolled = this.isScrolled;
      this.isScrolled = false;
      
      // Determine if the navbar should be shown or hidden based on scroll direction
      // Show navbar when scrolling up, hide when scrolling down (beyond threshold)
      if (currentScrollPosition > this.lastScrollPosition && !this.isNavbarHidden && currentScrollPosition > 200) {
        // Scrolling down and navbar is visible - hide it
        this.isNavbarHidden = true;
      } else if (currentScrollPosition < this.lastScrollPosition && this.isNavbarHidden) {
        // Scrolling up and navbar is hidden - show it
        this.isNavbarHidden = false;
      }
      
      // Only reset compact tool state if dynamic navbar is enabled
      if (this.navbarDynamicEnabled && wasScrolled && !this.isScrolled) {
        this.resetCompactToolState();
      }
      
      // Remember current scroll position for next comparison
      this.lastScrollPosition = currentScrollPosition;
    },
    applyRoundedCorners() {
      // Ensure the rounded corners are applied consistently across all sections
      const elegantSection = document.querySelector('.elegant-content-section');
      const sandySection = document.querySelector('.sandy-content-section');
      const rescueSection = document.querySelector('.rescue-content-section');
      
      // Get all sections that need rounded corners
      const allSections = [elegantSection, sandySection, rescueSection].filter(Boolean);
      
      // Apply the same border radius to all sections, with increased roundness
      // These values should match the media queries in the CSS
      const largeRadius = '50px';
      const mediumRadius = '35px';
      const smallRadius = '30px';
      
      allSections.forEach(section => {
        // Ensure consistent border radius for both CSS and inline styles
        if (window.innerWidth < 480) {
          section.style.borderTopLeftRadius = smallRadius;
          section.style.borderTopRightRadius = smallRadius;
        } else if (window.innerWidth < 768) {
          section.style.borderTopLeftRadius = mediumRadius;
          section.style.borderTopRightRadius = mediumRadius;
        } else {
          section.style.borderTopLeftRadius = largeRadius;
          section.style.borderTopRightRadius = largeRadius;
        }
        
        // Ensure overflow is hidden to maintain the curved appearance
        section.style.overflow = 'hidden';
      });
      
      console.log('Applied rounded corners to content sections');
    },
    addSmoothScrollPolyfill() {
      // Very simple smooth scroll polyfill for browsers that don't support scroll-behavior
      document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
          e.preventDefault();
          document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
          });
        });
      });
    },
    resetCompactToolState() {
      // Close any open compact tool
      this.compactToolOpen = false;
    },
    toggleCompactTool(index) {
      // Toggle tool state
      if (this.compactToolOpen && this.selectedCompactOption === index) {
        this.compactToolOpen = false;
      } else {
        this.selectedCompactOption = index;
        this.compactToolOpen = true;
      }
    },

    
    adjustFirstPageHeight() {
      // Calculate height of the hero section
      const heroSection = document.querySelector('.hero-section');
      
      if (heroSection) {
        // Get content height
        const contentHeight = heroSection.offsetHeight + 150; // Add padding
        
        // If content is taller than viewport, make sure container can expand
        if (contentHeight > window.innerHeight) {
          const container = document.querySelector('.beach-home-container');
          if (container) {
            container.style.minHeight = `${contentHeight}px`;
          }
        }
      }
    },
    triggerFileUpload() {
      // Trigger file input click
      this.$refs.fileInput.click();
    },
    handleImageUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.uploadedImage = URL.createObjectURL(file);
        
        // Set the tab to ripIdentifier and pass data to the integrated tool
        this.beachToolTab = 'ripIdentifier';
        
        // Use nextTick to ensure the component is rendered before calling its methods
        this.$nextTick(() => {
          if (this.$refs.beachTool) {
            // Pass the image to the BeachComparisonTool for analysis
            this.$refs.beachTool.ripImage = this.uploadedImage;
          }
        });
        
        // Adjust container height when image is added
        this.$nextTick(() => {
          this.adjustFirstPageHeight();
        });
      }
    },
    analyzeImage() {
      console.log('Analyzing image for rips');
      // Pass control to the BeachComparisonTool's analyze function
      if (this.$refs.beachTool && this.uploadedImage) {
        this.beachToolTab = 'ripIdentifier';
        this.$nextTick(() => {
          this.$refs.beachTool.analyzeRipImage();
        });
      }
    },
    searchBeach() {
      console.log('Searching for beach:', this.beachSearchQuery);
      // Set the tab to search and pass data to the integrated tool
      this.beachToolTab = 'search';
      
      // Use nextTick to ensure the component is rendered before calling its methods
      this.$nextTick(() => {
        if (this.$refs.beachTool && this.beachSearchQuery) {
          // Use the BeachComparisonTool's search functionality
          this.$refs.beachTool.address = this.beachSearchQuery;
          this.$refs.beachTool.debouncedSearch();
        }
      });
    },
    compareBeaches() {
      console.log('Comparing beaches:', this.homeBeach, 'and', this.compareBeach);
      // Set the tab to compare and pass data to the integrated tool
      this.beachToolTab = 'compare';
      
      // Use nextTick to ensure the component is rendered before calling its methods
      this.$nextTick(() => {
        if (this.$refs.beachTool && this.homeBeach && this.compareBeach) {
          // Set the compare beaches in the tool
          this.$refs.beachTool.compareAddress1 = this.homeBeach;
          this.$refs.beachTool.compareAddress2 = this.compareBeach;
          
          // Trigger the search for both beaches
          this.$refs.beachTool.debouncedSearchCompare1();
          this.$refs.beachTool.debouncedSearchCompare2();
        }
      });
    },

    quickSearch(beachName) {
      this.beachSearchQuery = beachName;
      this.searchBeach();
    },
    initImageCompare() {
      // This method is no longer needed as the image comparison feature has been removed.
      // Content related to slider, hotspots, and before/after images has been deleted from the template.
      console.log('Image comparison feature removed.');
    },
    
    initScrollAnimations() {
      // Get all the safety items
      const safetyItems = document.querySelectorAll('.safety-item');
      console.log(`Found ${safetyItems.length} safety items for scroll animations`);
      
      // Get all the rescue items
      const rescueItems = document.querySelectorAll('.rescue-item');
      // Get the rescue images container
      const rescueImagesContainer = this.$refs.rescueImagesContainer;
      
      if ((safetyItems.length === 0 && rescueItems.length === 0) && !rescueImagesContainer) {
        console.warn('No safety or rescue items found for scroll animations');
        return;
      }
      
      // Force reset all image masks to scrunched state initially
      document.querySelectorAll('.safety-item .image-mask').forEach(mask => {
        gsap.set(mask, {
          scaleY: 0.4,
          transformOrigin: 'center top'
        });
      });
      
      // No animations for rescue showcase
      if (rescueImagesContainer) {
        const rescueCard = rescueImagesContainer.querySelector('.centered-card');
        
        if (rescueCard) {
          // Set the card to be fully visible immediately
          gsap.set(rescueCard, {
            opacity: 1,
            y: 0,
            scale: 1
          });
          
          console.log('Removed animations for rescue card');
        }
      }
      
      // Create a ScrollTrigger for each safety item
      safetyItems.forEach((item, index) => {
        // Get the image mask and content elements
        const mask = item.querySelector('.image-mask');
        const content = item.querySelector('.safety-content');
        const title = content?.querySelector('.safety-content-title');
        const text = content?.querySelector('.safety-content-text');
        const statContainer = content?.querySelector('.safety-stat-container');
        const counterElement = content?.querySelector('.counter');
        
        if (!mask) {
          console.warn(`No image mask found in safety item ${index + 1}`);
          return;
        }
        
        // Set initial state - ensuring image is scrunched
        gsap.set(mask, {
          scaleY: 0.4,
          transformOrigin: 'center top'
        });
        
        // Create the GSAP animation with guaranteed scroll up/down effect
        const tl = gsap.timeline({
          scrollTrigger: {
            trigger: item,
            start: 'top 90%', // Start animation when the top of the item is 90% down the viewport
            end: 'top 50%', // End animation when the top of the item is 50% down the viewport
            scrub: 0.2, // Reduced scrub time for snappier animation
            once: false, // Animation will play each time item enters viewport
            toggleActions: 'play reverse play reverse', // Explicit instruction to reverse when scrolling up
            id: `safety-${index}`, // Unique ID for debugging
            onEnter: () => console.log(`Image ${index + 1} expanding (scrolling down)`),
            onLeaveBack: () => console.log(`Image ${index + 1} scrunching (scrolling up)`)
          }
        });
        
        // Animate the image mask with faster timing
        tl.to(mask, {
          scaleY: 1, // Expand to full height when scrolling down
          duration: 0.7, // Reduced duration for faster animation (0.9 -> 0.7)
          ease: 'back.out(1.2)' // Keep the same dynamic effect
        }, 0);
        
        // Animate the content if it exists
        if (title && text) {
          // Set initial states
          gsap.set([title, text], { 
            opacity: 0,
            y: 20
          });
          
          // Set initial state for stat container if it exists
          if (statContainer) {
            gsap.set(statContainer, {
              opacity: 0,
              y: 20
            });
          }
          
            // Animate title with even faster timing
          tl.to(title, {
            opacity: 1,
            y: 0,
              duration: 0.3, // Reduced from 0.4 to 0.3
              ease: 'power2.out' // Keep pronounced easing for quicker visibility
            }, 0.05); // Reduced delay from 0.1 to 0.05
          
            // Animate stat container with faster timing
          if (statContainer) {
            tl.to(statContainer, {
              opacity: 1,
              y: 0,
                duration: 0.3, // Reduced from 0.4 to 0.3
                ease: 'power2.out'
              }, 0.1); // Reduced delay from 0.2 to 0.1
            
            // Add counter animation for the safety items
            if (counterElement) {
              let endValue = 0;
              if (index === 0) { // First card: Pool Fencing
                endValue = 70; // Pool safety issue percentage 
              } else if (index === 1) { // Second card: Supervision
                endValue = 85; // Adult supervision percentage
              } else if (index === 2) { // Third card: Hazards
                endValue = 60; // Pool hazard percentage
              }
              
              // For the first card (index 0), check if we have the age 0-4 pool drowning percentage
              if (index === 0 && this.poolDrowningStats.age0to4Percentage > 0) {
                // Use the dynamically calculated percentage for pool fencing counter
                endValue = this.poolDrowningStats.age0to4Percentage;
              }

              if (endValue > 0) {
              const counterTl = gsap.timeline({
                scrollTrigger: {
                  trigger: statContainer,
                  start: 'top 70%',
                  toggleActions: 'play none none none',
                  onEnter: () => {
                    const startValue = 0;
                      const duration = 1.5;
                    const counter = { value: startValue };
                    
                    gsap.to(counter, {
                      value: endValue,
                      duration: duration,
                        ease: 'power2.out',
                      onUpdate: function() {
                        counterElement.innerText = Math.round(counter.value);
                      },
                      onComplete: function() {
                        counterElement.innerText = endValue;
                        gsap.fromTo(counterElement.parentNode, 
                            { backgroundColor: 'rgba(231, 111, 81, 0.2)' }, // Original highlight
                          { backgroundColor: 'rgba(255, 255, 255, 0.8)', duration: 0.5, ease: 'power1.out' }
                        );
                      }
                    });
                  }
                }
              });
              this.scrollTriggers.push(counterTl);
            }
            }
          }
          
                      // Animate text with even faster timing
          tl.to(text, {
            opacity: 1,
            y: 0,
              duration: 0.3, // Reduced from 0.4 to 0.3
              ease: 'power2.out'
            }, 0.15); // Further reduced delay from 0.3 to 0.15 for much quicker completion
        }
        
        // Store the timeline reference for cleanup
        this.scrollTriggers.push(tl);
        
        console.log(`Initialized scroll animation for safety item ${index + 1}`);
      });
      
      // Create a ScrollTrigger for each rescue item - same animation logic as safety items
      rescueItems.forEach((item, index) => {
        // Get the image mask and content elements
        const mask = item.querySelector('.image-mask');
        const content = item.querySelector('.rescue-content');
        const title = content?.querySelector('.rescue-content-title');
        const text = content?.querySelector('.rescue-content-text');
        const statContainer = content?.querySelector('.rescue-stat-container');
        
        if (!mask) {
          console.warn(`No image mask found in rescue item ${index + 1}`);
          return;
        }
        
        // Set initial state for rescue item masks too - ensuring image is scrunched
        gsap.set(mask, {
          scaleY: 0.4,
          transformOrigin: 'center top'
        });
        
        // Create the GSAP animation with same settings as safety items - including scroll up behavior
        const tl = gsap.timeline({
          scrollTrigger: {
            trigger: item,
            start: 'top 90%', // Updated to match safety items
            end: 'top 50%', // Updated to match safety items
            scrub: 0.2, // Updated to match safety items
            once: false,
            toggleActions: 'play reverse play reverse', // Explicit reverse animation when scrolling up
            id: `rescue-${index}`, // Unique ID for debugging
            onEnter: () => console.log(`Rescue image ${index + 1} expanding (scrolling down)`),
            onLeaveBack: () => console.log(`Rescue image ${index + 1} scrunching (scrolling up)`)
          }
        });
        
        // Animate the image mask with the same effect as safety items
        tl.to(mask, {
          scaleY: 1,
          duration: 0.7, // Updated to match safety items (0.9 -> 0.7)
          ease: 'back.out(1.2)'
        }, 0);
        
        // Animate the content if it exists
        if (title && text) {
          // Set initial states
          gsap.set([title, text], { 
            opacity: 0,
            y: 20
          });
          
          // Set initial state for stat container if it exists
          if (statContainer) {
            gsap.set(statContainer, {
              opacity: 0,
              y: 20
            });
          }
          
          // Animate title with a shorter delay and faster duration
          tl.to(title, {
            opacity: 1,
            y: 0,
            duration: 0.4,
            ease: 'power2.out'
          }, 0.1);
          
          // Animate stat container if it exists
          if (statContainer) {
            tl.to(statContainer, {
              opacity: 1,
              y: 0,
              duration: 0.4,
              ease: 'power2.out'
            }, 0.2);
          }
          
          // Animate text with reduced delay
          tl.to(text, {
            opacity: 1,
            y: 0,
            duration: 0.4,
            ease: 'power2.out'
          }, 0.3);
        }
        
        // Store the timeline for cleanup
        this.scrollTriggers.push(tl);
        
        console.log(`Initialized scroll animation for rescue item ${index + 1}`);
      });
    },
    async fetchLocationSuggestions() {
      if (this.userLocation.length > 2) {
        try {
          // Clear any pending error message timeout before new fetch
          if (this.errorMessageTimeoutId) {
            clearTimeout(this.errorMessageTimeoutId);
            this.errorMessageTimeoutId = null;
          }

          const response = await fetch(`https://nominatim.openstreetmap.org/search?format=json&addressdetails=1&q=${this.userLocation}+Australia`);
          const data = await response.json();
          
          const australianLocations = data.filter(location => location.address && location.address.country === 'Australia');
          
          if (australianLocations.length === 0) {
            // Set a timeout to show the error message
            this.errorMessageTimeoutId = setTimeout(() => {
              this.errorMessage = 'Location not found or not in Australia. Please enter a valid Australian location.';
              this.locationSuggestions = [];
            }, 10000); // 10 seconds delay
          } else {
            this.errorMessage = '';
            this.locationSuggestions = australianLocations;
          }
        } catch (error) {
          // Clear timeout if an actual error occurs
          if (this.errorMessageTimeoutId) {
            clearTimeout(this.errorMessageTimeoutId);
            this.errorMessageTimeoutId = null;
          }
          this.errorMessage = 'Error fetching location data. Please try again.';
          this.locationSuggestions = [];
        }
      } else {
        // Clear timeout and suggestions if input is too short
        if (this.errorMessageTimeoutId) {
          clearTimeout(this.errorMessageTimeoutId);
          this.errorMessageTimeoutId = null;
        }
        this.locationSuggestions = [];
        this.errorMessage = '';
      }
    },
    clearLocation() {
      this.userLocation = '';
      this.selectedLocation = null;
      this.autoDetectedState = null;
      // Clear any pending error message timeout
      if (this.errorMessageTimeoutId) {
        clearTimeout(this.errorMessageTimeoutId);
        this.errorMessageTimeoutId = null;
      }
      this.errorMessage = ''; // Also clear current error message
      this.locationSuggestions = []; // Clear suggestions
    },
    selectLocation(location) {
      this.userLocation = location.display_name;
      this.selectedLocation = location;
      this.locationSuggestions = [];
      // Clear any pending error message timeout as a location is selected
      if (this.errorMessageTimeoutId) {
        clearTimeout(this.errorMessageTimeoutId);
        this.errorMessageTimeoutId = null;
      }
      this.errorMessage = ''; // Clear error message

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
      
      // Auto-select the state if detected and show popup
      if (stateCode) {
        this.selectedState = stateCode;
        this.showRegulationPopup = true; // Show popup
      } else {
        this.selectedState = ''; // Clear selected state if not detected
      }
    },
    selectState(stateCode) {
      this.selectedState = stateCode;
      this.showRegulationPopup = true; // Show popup
    },
    handleStateChange() {
      // This method is called when the dropdown value changes
      if (this.selectedState) {
        this.showRegulationPopup = true; // Show popup
      }
    },
    getStateFullName(stateCode) {
      const state = this.australianStates.find(state => state.code === stateCode);
      return state ? state.name : stateCode;
    },
    closeRegulationPopup() {
      this.showRegulationPopup = false;
      // Reset postcode related fields
      this.userLocation = '';
      this.selectedLocation = null;
      this.autoDetectedState = '';
      this.locationSuggestions = [];
      this.errorMessage = '';
      this.selectedState = ''; // Also clear the selected state itself
    },
    handleMessage(event) {
      if (event.data && event.data.type === 'quiz-completed') {
        this.quizCompleted = true;
        setTimeout(() => {
          this.closeQuizPopup();
        }, 3000); // Automatically close the popup after 3 seconds
      }
    },
    // Method to show the river safety quiz
    showRiverSafetyQuiz() {
      this.showRiverSafetyQuizPopup = true;
      
      // Prevent page scrolling when popup is open
      document.body.style.overflow = 'hidden';
    },
    
    // Method to close the river safety quiz popup
    closeRiverSafetyQuiz() {
      this.showRiverSafetyQuizPopup = false;
      
      // Re-enable page scrolling
      document.body.style.overflow = '';
    },
    // Method to navigate to specific sections
    navigateToSection(sectionId) {
      // First update the URL hash (for bookmarking purposes)
      this.$router.push({ path: '/pool', hash: '#' + sectionId });
      
      // Then scroll to the element
      this.scrollToElement('#' + sectionId);
    },
    
    // Add a method to close the rip identifier popup
    closeRipIdentifier() {
      this.showRipIdentifierPopup = false;
      
      // Re-enable page scrolling
      document.body.style.overflow = '';
    },
    
    // Show the rip current quiz popup
    showRipCurrentQuiz() {
      this.showRipCurrentQuizPopup = true;
      
      // Prevent page scrolling when popup is open
      document.body.style.overflow = 'hidden';
    },
    
    // Close the rip current quiz popup
    closeRipCurrentQuiz() {
      this.showRipCurrentQuizPopup = false;
      
      // Re-enable page scrolling
      document.body.style.overflow = '';
    },
    
    // Method to show fence regulations popup
    showFencingRegulations() {
      // Select NSW as default or keep current selection
      if (!this.selectedState) {
        this.selectedState = 'nsw'; // NSW as default state
      }
      // Show the regulations popup
      this.showRegulationPopup = true;
    },
    
    // Method to open the pool safety quiz
    openQuizPopup() {
      this.showQuizPopup = true;
      
      // Prevent page scrolling when popup is open
      document.body.style.overflow = 'hidden';
    },
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800&display=swap');

/* Full-page structure */
.beach-home-container {
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;
  min-height: 100vh; /* Changed to 100vh as minimum, will expand with content */
  height: auto; /* Auto height to allow dynamic content sizing */
  color: #343a40;
  position: relative;
  overflow: visible; /* Changed from hidden to visible to allow content to flow */
  background-image: url('../assets/pexels-marctutorials-298692-870170.jpg');
  background-size: 130% auto;
  background-position: 0% center;
  background-attachment: fixed;
}

/* Hero section - full viewport height with extra space at bottom for overlap */
.hero-content {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  min-height: auto; /* Changed to auto to allow content to determine height */
  padding-top: 180px; /* Decreased to move content higher */
  padding-bottom: 160px; /* Reduced slightly */
  padding-left: 2%;
  position: relative;
  z-index: 5;
  transition: padding-bottom 0.5s ease-in-out; /* Added transition for padding-bottom */
  flex-grow: 1; /* Allow this to grow to fill available space */
}

.hero-content.suggestions-active-padding {
padding-bottom: 410px; /* Increased padding-bottom (160px + 250px) */
}

/* Hero section overlay */
.hero-content::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 150%; /* Extended from 120% to 150% to ensure shadow extends further down */
  background: linear-gradient(90deg, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.65) 15%, rgba(0,0,0,0.4) 30%, rgba(0,0,0,0.2) 45%, rgba(0,0,0,0) 60%);
  z-index: -1;
  pointer-events: none;
}

/* Highlight color in hero text - for reference */
.highlight {
  color: #e9c46a; /* Golden beach sand color */
  position: relative;
  font-weight: 900;
  text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
}

/* White content section - completely separate section with smooth edges */
.elegant-content-section {
  position: relative;
  min-height: 95vh;
  background-color: #ffffff;
  z-index: 10;
  transition: margin-top 0.5s ease-in-out; /* Apply transition to margin-top */
  opacity: 1;
  margin-top: -100px; /* Adjusted from -80px to -100px to position section slightly higher */
  transform: translateZ(0); /* Enable GPU acceleration for smoother transitions */
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  padding: 100px 0 0; /* Remove horizontal padding */
  overflow: hidden;
  box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.05);
  border-top-left-radius: 50px;
  border-top-right-radius: 50px;
}

.elegant-content-section.pushed-down-by-suggestions {
  margin-top: 0px; /* Changed from 100px to 0px */
}

/* Sandy colored section with curved edges */
.sandy-content-section {
  position: relative;
  min-height: 85vh; /* Increased from 70vh to make section longer */
  background-color: #B0E0E6; /* Changed to lighter blue */
  z-index: 11;
  transition: none;
  opacity: 1;
  margin-top: -40px; /* Reduced overlap to make room for beach comparison footer */
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding: 100px 0 160px; /* Increased bottom padding from 80px to 160px */
  overflow: hidden;
  box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.05);
  border-top-left-radius: 50px;
  border-top-right-radius: 50px;
}

/* Smooth transition for white section with no dark background */
.elegant-content-section::before {
  content: '';
  position: absolute;
  top: -120px; /* Adjusted from -100px */
  left: 0;
  width: 100%;
  height: 150px; /* Increased from 120px to 150px for smoother transition */
  background: linear-gradient(to bottom, rgba(255, 255, 255, 0), rgba(255, 255, 255, 0.85) 50%, #ffffff 95%);
  z-index: 0;
  pointer-events: none;
}

/* Sandy colored section with curved edges */
.sandy-content-section::before {
  content: '';
  position: absolute;
  top: -100px; /* Increased height */
  left: 0;
  width: 100%;
  height: 150px; /* Increased height for more gradient space */
  background: linear-gradient(to bottom, rgba(176, 224, 230, 0), rgba(176, 224, 230, 0.8) 60%, #B0E0E6 95%); /* Adjusted gradient for lighter blue */
  z-index: 0;
  pointer-events: none;
}

/* Custom curved top edge with more pronounced curves at the edges */
.elegant-content-section::after {
  display: none; /* Remove the elliptical shape */
  content: '';
  position: absolute;
  top: -2px;
  left: 0;
  width: 100%;
  height: 150px;
  background-color: transparent;
  z-index: 1;
  border-top-left-radius: 40px;
  border-top-right-radius: 40px;
}

/* Curved top edge for sandy section - enhanced curve */
.sandy-content-section::after {
  display: none; /* Remove the elliptical shape */
  content: '';
  position: absolute;
  top: -2px;
  left: 0;
  width: 100%;
  height: 150px;
  background-color: transparent;
  z-index: 1;
  border-top-left-radius: 40px;
  border-top-right-radius: 40px;
}

@media (max-width: 768px) {
  .elegant-content-section::after,
  .sandy-content-section::after,
  .rescue-content-section::after {
    display: none;
  }
  
  .elegant-content-section,
  .sandy-content-section,
  .rescue-content-section {
    border-top-left-radius: 35px;
    border-top-right-radius: 35px;
  }
}

@media (max-width: 480px) {
  .elegant-content-section::after,
  .sandy-content-section::after,
  .rescue-content-section::after {
    display: none;
  }
  
  .elegant-content-section,
  .sandy-content-section,
  .rescue-content-section {
    border-top-left-radius: 30px;
    border-top-right-radius: 30px;
  }
}

/* Left-aligned heading styles - clean approach */
.section-heading {
  width: 45%;
  text-align: left;
  padding-left: 4%;
  margin-top: 3%;
  opacity: 1; /* No fade in */
  position: relative;
}

.section-label {
  display: block;
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: rgba(1, 79, 134, 0.6);
  margin-bottom: 12px;
  font-weight: 500;
}

.section-title {
  color: #014f86; /* Deep blue color */
  font-size: 3.2rem;
  font-weight: 800;
  line-height: 1.2;
  text-align: left;
  position: relative;
  display: inline-block;
  letter-spacing: -0.02em;
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;
  margin-bottom: 20px;
}

/* Tagline styling inspired by the clean, modern design in the reference image */
.section-tagline {
font-size: 1.7rem;
line-height: 1.5;
color: #333;
font-weight: 500;
margin-top: 10px;
margin-bottom: 30px;
max-width: 95%;
opacity: 0.85;
position: relative;
font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Toddler statistic hover effect */
.section-tagline-container {
position: relative;
width: 100%;
}

.toddler-stat-trigger {
color: #0277bd;
font-weight: 600;
cursor: pointer;
position: relative;
border-bottom: 2px dotted #0277bd;
transition: all 0.3s ease;
}

.toddler-stat-trigger:hover {
color: #e74c3c;
border-bottom-color: #e74c3c;
}

.toddler-stat-popup {
position: absolute;
top: 140px;
left: 340px;
right: auto;
opacity: 0;
visibility: hidden;
z-index: 100;
transition: all 0.3s ease;
width: 320px;
pointer-events: none;
}

.toddler-stat-popup.visible {
opacity: 1;
visibility: visible;
}

.hand-drawn-arrow {
width: 120px;
height: 150px;
position: absolute;
top: -100px;
left: 250px;
right: auto;
transform: rotate(25deg);
z-index: 5;
}

.toddler-stat-content {
background-color: #fff9e6;
padding: 15px;
border-radius: 8px;
box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.2);
border-left: 5px solid #e74c3c;
position: relative;
}

.stat-percentage {
font-size: 2.5rem;
font-weight: 700;
color: #e74c3c;
display: block;
margin-bottom: 5px;
font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;
}

.stat-description {
font-size: 1rem;
line-height: 1.4;
color: #333;
font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Clean minimal underline */
.section-title::after {
  content: '';
  position: absolute;
  bottom: -12px;
  left: 0;
  width: 50px;
  height: 3px;
  background: #014f86;
  border-radius: 0; /* No radius for cleaner look */
}

/* Create sophisticated underline with subtle accent */
.section-title::before {
  display: none;
}

/* Clean navbar styling with soft transition */
.navbar-wrapper {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;
  transition: all 0.3s ease; /* Smooth transition */
  backdrop-filter: none;
  transform: translateY(0); /* Add this for smooth transitions */
}

/* Add this for hiding the navbar when scrolling down */
.navbar-wrapper.hidden {
  transform: translateY(-100%);
}

/* Clean navbar when scrolled with subtle shadow */
.navbar-wrapper.scrolled {
  background: rgba(255, 255, 255, 1); /* Solid white background */
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.1); /* Simple border-like shadow */
  backdrop-filter: none; /* No blur */
  border-bottom: none; /* No border */
}
.navbar-wrapper.scrolled .navbar {
  background: transparent;
  border-bottom: 1px solid rgba(1, 79, 134, 0.1);
}
/* Logo colors for light theme */
.navbar-wrapper.scrolled .logo-water,
.navbar-wrapper.scrolled .logo-family,
.navbar-wrapper.scrolled .logo-wise {
  color: #333;
  text-shadow: none;
}
/* Tab colors for light theme */
.navbar-wrapper.scrolled .navbar-tab,
.navbar-wrapper.scrolled .navbar-tab.active {
  color: rgba(1, 59, 111, 0.7); /* darker blue for light bg */
}
.navbar-wrapper.scrolled .navbar-tab::after,
.navbar-wrapper.scrolled .navbar-tab.active::after {
  background-color: transparent; /* remove underline */
  height: 0;
}

.navbar {
  background: rgba(0, 0, 0, 0.15);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  transition: all 0.4s ease;
}

.navbar-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0.8rem 2.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.navbar-logo {
  flex: 1;
}

.logo-link {
  font-size: 1.6rem;
  font-weight: 300;
  color: #ffffff;
  text-decoration: none;
  letter-spacing: -0.5px;
  transition: all 0.3s ease;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
  display: flex;
  align-items: center;
}

.logo-link:hover {
  text-shadow: 0 2px 8px rgba(255, 255, 255, 0.5);
}
.logo-water {  
  font-weight: 600;  
  color: #ffffff;
}
.logo-wise {  
  font-weight: 700;  
  color: #44ccff;  
  text-shadow: 0 0 10px rgba(68, 204, 255, 0.5);
}
.logo-family {  
  font-weight: 300;  
  color: #ffffff;  
  opacity: 0.9;
}
.navbar-wrapper.scrolled .logo-water {  
  color: #333;
}
.navbar-wrapper.scrolled .logo-wise {  
  color: #014f86;  
  text-shadow: none;
}
.navbar-wrapper.scrolled .logo-family {  
  color: #333;  
  opacity: 0.9;
}

.navbar-tabs {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  flex: 2;
}

.navbar-tab {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 0.2rem;
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  font-weight: 400;
  transition: all 0.3s ease;
  font-size: 1.2rem; /* Increased from 1rem */
  position: relative;
  letter-spacing: 0.5px;
}

.navbar-tab:hover {
  color: #ffffff;
}

.navbar-tab.active {
  color: #ffffff;
  font-weight: 500;
}

.navbar-tab::after {
  display: none;
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  width: 0;
  height: 0;
  background-color: transparent;
  transition: none;
}

.navbar-tab:hover::after {
  background-color: transparent;
}

.navbar-tab.active::after {
  background-color: transparent;
  height: 0;
}

.dropdown-arrow {
  font-size: 0.65em;
  margin-left: 4px;
  opacity: 0.8;
  transition: transform 0.3s ease;
}

.navbar-tab-dropdown:hover .navbar-tab .dropdown-arrow {
  transform: rotate(180deg);
}

.navbar-right {
  flex: 1;
  display: flex;
  justify-content: flex-end;
}

/* Hero Content Layout */
.hero-section {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-top: 20px; /* Decreased to move content higher */
  margin-bottom: 1.5rem; /* Slightly reduced */
  width: 100%; /* Full width for the text */
  max-width: 800px; /* Increased max-width for better visibility */
  animation: fadeIn 0.5s ease-out forwards;
  margin-left: 0; /* Removed left margin to move more to the left */
  text-align: left;
}

.dynamic-headline {
  font-size: 2.8rem; /* Further decreased from 3.2rem to 2.8rem */
  font-weight: 800;
  line-height: 1.1;
  color: white;
  display: flex;
  flex-direction: column;
  text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
  margin-bottom: 0.8rem;
  text-align: left;
}

.text-line {
  opacity: 0;
  transform: translateY(15px);
  animation: fadeInUp 0.6s ease-out forwards;
  margin-bottom: 0.3rem;
  white-space: nowrap;
  text-align: left;
}

.text-line:nth-child(1) {
  animation-delay: 0.1s;
}

.text-line:nth-child(2) {
  animation-delay: 0.3s;
}

.text-line:nth-child(3) {
  animation-delay: 0.5s;
}

/* Connector between headline and tools - without arrow */
.hero-connector {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-top: 0;
  opacity: 0;
  align-self: flex-start;
  width: 100%;
  position: relative;
  padding-bottom: 5px; /* Reduce from 10px */
  animation: fadeInUp 0.6s ease-out forwards;
  animation-delay: 0.8s;
  text-align: left;
}

.connector-text {
  color: white;
  font-size: 1.3rem; /* Increased from 1.1rem to 1.3rem */
  font-weight: 500;
  text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
  margin-bottom: 0;
  text-align: left;
  white-space: nowrap;
  width: auto;
  max-width: 100%;
  padding-right: 1rem;
}



/* Compare Beaches */
.beach-compare-container {
  display: flex;
  flex-direction: column;
  gap: 12px;
  background: #f5d78b;
  border-radius: 8px;
  padding: 16px;
  border: 2px solid #e0b43c;
  width: 100%;
  position: relative;
  min-height: auto; /* Auto height to fit content */
  height: auto; /* Ensure container expands */
  overflow: visible; /* Ensure nothing is cut off */
}

/* Fix indentation and hierarchy issues */
.search-interface-content.compare-beaches {
  padding: 14px 12px 20px 12px; /* Increased bottom padding */
  height: auto;
  overflow: visible;
  min-height: 180px; /* Ensure enough space for all elements */
  max-width: none; /* Remove max width constraint to allow horizontal expansion */
  width: auto; /* Allow width to be determined by content */
}

/* Rip Identifier */
.upload-label {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  padding: 16px; /* Increased padding */
  background: linear-gradient(45deg, #2c7da0, #014f86);
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s;
  color: #ffe8b3;
  font-weight: 500;
  border: 2px solid #e0b43c;
  font-size: 1.35rem; /* Further increased font size */
}

.upload-label:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(1, 79, 134, 0.3);
}

.upload-icon {
  font-size: 24px;
  margin-right: 12px;
}

.file-input {
    display: none;
  }

.image-preview-container {
  margin-top: 10px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}

.image-preview {
  max-width: 60%;
  max-height: 80px;
  border-radius: 12px;
  margin-right: 10px;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.2);
}

.analyze-button {
  background: linear-gradient(45deg, #e76f51, #f4a261);
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s;
  font-weight: 600;
  height: fit-content;
  box-shadow: 0 3px 10px rgba(231, 111, 81, 0.3);
}

.analyze-button:hover {
  background: linear-gradient(45deg, #e56b4c, #f09c58);
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(231, 111, 81, 0.4);
}

/* Beach Search */
.search-beach .search-input-container {
  display: flex;
  width: 100%;
  margin-bottom: 8px;
}
  
  .search-input {
  flex: 1;
  padding: 12px 16px;
  font-size: 17px; /* Increased font size */
  border: 2px solid #e0b43c;
  border-radius: 8px 0 0 8px;
  outline: none;
  background: #fff2d6;
  color: #333;
  font-family: 'Montserrat', sans-serif;
  transition: all 0.3s;
}

.search-input:focus {
  border-color: #e0b43c;
  background: #fffaf0;
  box-shadow: 0 0 0 4px rgba(224, 180, 60, 0.2);
}

.search-button {
  background: linear-gradient(90deg, #1a6aa5, #25a0c8);
  color: white;
  border: none;
  padding: 0 24px;
  border-radius: 0 8px 8px 0;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: all 0.3s;
  font-weight: 600;
  font-size: 17px; /* Increased font size */
}

.search-button:hover {
  background: linear-gradient(90deg, #155d91, #2196c1);
  box-shadow: 0 3px 10px rgba(37, 160, 200, 0.3);
}

.search-button-text {
  display: inline-block;
}

.popular-beaches {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 12px;
  margin-bottom: 5px;
}

.popular-label {
  font-size: 17px;
  color: #666;
  margin-right: 8px;
  font-weight: 500;
}

.popular-beach {
  background: #ffe8b3;
  border: 2px solid #e0b43c;
  padding: 8px 15px;
  border-radius: 20px;
  font-size: 17px;
  cursor: pointer;
  transition: all 0.2s;
  color: #1a6aa5;
  font-weight: 600;
}

.popular-beach:hover {
  background: #e0b43c;
  color: #003b6f;
  transform: translateY(-1px);
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Compare Beaches */
.beach-compare-container {
  display: flex;
  flex-direction: column;
  gap: 12px;
  background: #f5d78b;
  border-radius: 8px;
  padding: 16px;
  border: 2px solid #e0b43c;
  width: 100%;
  position: relative;
  min-height: auto; /* Auto height to fit content */
  height: auto; /* Ensure container expands */
  overflow: visible; /* Ensure nothing is cut off */
}

.beach-input-group {
  flex: 1 1 auto; /* Changed to allow growing and shrinking based on content */
  width: 100%;
  display: flex;
  flex-direction: column;
  background: rgba(255, 240, 200, 0.7);
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 12px; /* Increased margin for better spacing */
  position: relative; /* Ensure proper stacking */
  z-index: 2; /* Ensure visibility */
  min-width: 0; /* Allow flex item to shrink below its content width */
}

.beach-input-group label {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 8px;
  color: #3a3222;
  font-size: 22px;
  font-weight: 600;
}

.beach-input-group .search-input {
  border: 1px solid #e0b43c;
  border-radius: 4px;
  background: #fff;
  font-size: 20px;
  padding: 14px 18px;
  transition: all 0.2s ease;
  color: #333;
  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
}

.beach-input-group .search-input:focus {
  border-color: #e9b949;
  box-shadow: 0 0 0 3px rgba(233, 185, 73, 0.25), inset 0 1px 3px rgba(0, 0, 0, 0.05);
  outline: none;
}

.input-emoji {
  font-size: 28px;
}

.button-container {
  width: 100%;
  position: relative; /* Changed from absolute to relative */
  margin-top: 8px; /* Added margin for better spacing */
  padding: 0; /* Reset padding */
}

.compare-button {
  background: linear-gradient(to bottom, #e9b949, #e59d45);
  color: #003b6f;
  border: none;
  padding: 16px;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s;
  font-weight: 700;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  box-shadow: 0 2px 6px rgba(224, 180, 60, 0.3);
  z-index: 5;
  margin-top: 0; /* Reset margin-top */
  font-size: 22px; /* Further increased font size */
}

.compare-button:hover {
  background: linear-gradient(to bottom, #ebc04f, #db8f3c);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(224, 180, 60, 0.4);
}

.compare-button:active {
  transform: translateY(0);
  box-shadow: 0 2px 4px rgba(224, 180, 60, 0.3);
  transition-duration: 0.1s;
}

.button-emoji {
  font-size: 28px;
}

/* Responsive adjustments */
@media (max-width: 1200px) {
  .beach-home-container {
    background-size: 140% auto;
    background-position: 0% center;
  }
  
  .search-button-text {
    display: none;
  }
}

@media (max-width: 1024px) {
  .beach-home-container {
    background-size: 150% auto;
    background-position: 0% center;
  }
  
  .hero-content {
    padding-left: 5%;
  }
  
  .hero-section {
    width: 50%;
  }
  
  .dynamic-headline {
    font-size: 3.5rem;
  }
}

@media (max-width: 768px) {
  .beach-home-container {
    background-size: 180% auto;
    background-position: 0% center;
  }
  
  .hero-content {
    padding-left: 3%;
    align-items: flex-start;
  }
  
  .hero-section {
    width: 90%;
    max-width: 600px;
    align-items: flex-start;
  }
  
  .dynamic-headline {
    font-size: 2.8rem;
    text-align: left;
  }
  
  .text-line {
    text-align: left;
  }
  
  .hero-section {
    align-items: center;
    margin-top: 40px; /* Increased from 25px to 40px for consistency */
    margin-bottom: 2rem;
  }
  
  .beach-compare-container {
    flex-direction: column;
  }
  
  .beach-input-group {
    width: 100%;
  }
  
  .search-option {
    flex-direction: column;
    gap: 3px;
    padding: 8px 5px;
  }
  
  .option-emoji {
    font-size: 20px;
  }
  
  .hero-connector {
    align-items: flex-start;
    align-self: flex-start;
  }
  
  .connector-text {
    font-size: 1.1rem;
    white-space: normal;
    text-align: left;
  }
  
  .search-interface {
    max-height: 650px; /* Further extend for mobile layouts */
  }
  
  .beach-compare-container {
    padding: 12px;
  }
  
  .beach-input-group {
    margin-bottom: 0;
    padding: 8px;
  }
}

@media (max-width: 480px) {
  .beach-home-container {
    background-size: 200% auto;
    background-position: 0% center;
  }
  
  .hero-content {
    padding-top: 80px; /* Increased from 50px to maintain the move downward on mobile */
  }
  
  .hero-section {
    width: 95%;
  }
  
  .dynamic-headline {
    font-size: 2rem;
  }
  
  .hero-section {
    margin-bottom: 2rem;
  }
  
  .text-line {
    white-space: normal;
    text-align: center;
  }
  
  .search-interface-content {
    padding: 10px;
  }
  
  .popular-beaches {
    justify-content: center;
  }
  
  .hero-connector {
    align-items: center;
    align-self: center;
  }
  
  .connector-text {
    font-size: 1rem;
  }
}

/* Add a class for additional content that might appear below */
.additional-content {
  position: relative;
  z-index: 2;
  padding: 40px 5%;
  background-color: rgba(233, 196, 106, 0.95);
}

/* Remove all old sandy section styles */
.sandy-content-container,
.sandy-section-title,
.info-cards-container,
.info-card,
.info-card-icon,
.info-card h3,
.info-card p,
.sandy-section-cta,
.sandy-button {
  display: none;
}

/* Enhanced navbar when scrolled - light theme */
.navbar-wrapper.scrolled {
  background: rgba(255, 255, 255, 1); /* Solid white */
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.1); /* Simple border-like shadow */
  backdrop-filter: none; /* No blur */
  border-bottom: none; /* No border */
}

.navbar-wrapper.scrolled .navbar {
  background: transparent;
  border-bottom: 1px solid rgba(1, 79, 134, 0.1);
}

.navbar-wrapper.scrolled .logo-link {
  color: #014f86;
  text-shadow: none;
}

.navbar-wrapper.scrolled .navbar-tab {
  color: rgba(1, 59, 111, 0.7);
}

.navbar-wrapper.scrolled .navbar-tab:hover {
  color: #014f86;
}

.navbar-wrapper.scrolled .navbar-tab.active {
  color: #014f86;
  font-weight: 600;
}

.navbar-wrapper.scrolled .navbar-tab::after {
  display: none;
  background-color: transparent;
}

.navbar-wrapper.scrolled .navbar-tab:hover::after {
  display: none;
  background-color: transparent;
}

.navbar-wrapper.scrolled .navbar-tab.active::after {
  display: none;
  background-color: transparent;
}

/* Navbar search transitions */
  .navbar-search {
  transition: all 0.3s ease;
  overflow: hidden;
  max-height: 200px;
}

/* Collapsed search bar when scrolled */
.navbar-search.search-collapsed {
  max-height: 0;
  opacity: 0;
  pointer-events: none;
}



/* Add a slot for the search options in the navbar when scrolled */
.navbar-wrapper.scrolled .navbar-content {
  justify-content: space-between;
  padding: 0.8rem 2.5rem;
}

.navbar-wrapper.scrolled .navbar-tabs {
  flex: 1;
}

/* Responsive adjustments for scrolled navbar */
@media (max-width: 768px) {
  .navbar-wrapper.scrolled .navbar-content {
    padding: 0.6rem 1.5rem;
  }
}

@media (max-width: 480px) {
  .navbar-wrapper.scrolled .navbar-content {
    padding: 0.5rem 1rem;
  }
}

/* Navbar wrapper with transition */
.navbar-wrapper {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;
  transition: background-color 0.3s ease; /* Simple transition */
  backdrop-filter: none; /* No blur effect */
}



/* Improved Compact search in navbar when scrolled - updated for elegant white theme */
.navbar-integrated-search {
  background: transparent;
  padding: 0 2.5rem 0.4rem;
  transition: all 0.3s ease;
}

.navbar-integrated-search.expanded {
  padding: 0 2.5rem 0.6rem;
}

.search-bar-compact {
  max-width: 700px;
  margin: 0 auto;
  background: rgba(1, 79, 134, 0.7);
  border-radius: 50px; /* Pill shape when collapsed */
  padding: 6px 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  border: 1px solid rgba(255, 255, 255, 0.25);
}

.expanded .search-bar-compact {
  border-radius: 12px; /* More rectangular when expanded */
  padding: 8px 15px;
  background: rgba(1, 79, 134, 0.75);
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.search-options-compact {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-bottom: 0;
  transition: all 0.3s ease;
}

.expanded .search-options-compact {
  gap: 15px;
  margin-bottom: 8px;
}

.search-option-compact {
  background: rgba(254, 247, 229, 0.2);
  border: none;
  border-radius: 50%; /* Circular when collapsed */
  width: 36px;
  height: 36px;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(254, 247, 229, 0.9);
  cursor: pointer;
  transition: all 0.25s ease;
  font-size: 14px;
  font-weight: 600;
}

.expanded .search-option-compact {
  border-radius: 8px;
  width: auto;
  height: auto;
  padding: 8px 15px;
  justify-content: flex-start;
  gap: 8px;
  background: rgba(254, 247, 229, 0.25);
}

.search-option-compact:hover {
  background: rgba(254, 247, 229, 0.3);
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.search-option-compact.active {
  background: rgba(254, 247, 229, 0.35);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.option-emoji {
  font-size: 18px;
}

.option-label {
    display: none;
  opacity: 0;
  max-width: 0;
  transition: all 0.3s ease;
}

.expanded .option-label {
  display: inline-block;
  opacity: 1;
  max-width: 200px;
}

/* Active Tool Inputs */
.compact-tool-container {
  padding: 8px 0 0;
  transition: all 0.3s ease;
  animation: slideDown 0.3s ease-out;
  overflow: hidden;
  border-top: 1px solid rgba(254, 247, 229, 0.2);
}

@keyframes slideDown {
  from {
    max-height: 0;
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    max-height: 180px;
    opacity: 1;
    transform: translateY(0);
  }
}

.compact-tool-content {
  padding: 3px 0;
}

/* Upload Button */
.compact-upload-btn {
  background: linear-gradient(45deg, #2c7da0, #014f86);
  color: #ffe8b3;
  border: none;
  border-radius: 8px;
  padding: 6px 12px;
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  font-weight: 600;
  font-size: 14px;
  transition: all 0.2s;
  width: 100%;
  justify-content: center;
}

.compact-upload-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.hidden-file-input {
  display: none;
}

/* Search Beach Input */
.compact-search-input {
  display: flex;
  width: 100%;
}

.compact-search-input input {
  flex: 1;
  padding: 6px 10px;
  border: 1px solid #e0b43c;
  border-radius: 6px 0 0 6px;
  background: rgba(255, 255, 255, 0.9);
  font-size: 14px;
  outline: none;
}

.compact-search-input button {
  background: linear-gradient(90deg, #1a6aa5, #25a0c8);
  color: white;
  border: none;
  padding: 0 15px;
  border-radius: 0 6px 6px 0;
  font-weight: 600;
  cursor: pointer;
}

/* Compare Beaches Inputs */
.compact-compare-inputs {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  width: 100%;
}

.compact-input-group {
  flex: 1;
  min-width: 140px;
}

.compact-input-group input {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid #e0b43c;
  border-radius: 6px;
  background: rgba(255, 255, 255, 0.9);
  font-size: 14px;
  outline: none;
}

.compact-compare-inputs button {
  background: linear-gradient(45deg, #e0b43c, #f4a261);
  color: #003b6f;
  border: none;
  padding: 8px 15px;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  min-width: 100px;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .navbar-integrated-search {
    padding: 0 1.5rem 0.5rem;
  }
  
  .expanded .navbar-integrated-search {
    padding: 0 1.5rem 0.6rem;
  }
  
  .search-option-compact {
    width: 32px;
    height: 32px;
  }
  
  .expanded .search-option-compact {
    padding: 6px 10px;
  }
  
  .option-emoji {
    font-size: 16px;
  }
}

@media (max-width: 480px) {
  .navbar-integrated-search {
    padding: 0 1rem 0.3rem;
  }
  
  .expanded .navbar-integrated-search {
    padding: 0 1rem 0.5rem;
  }
  
  .search-bar-compact {
    padding: 4px 8px;
  }
  
  .expanded .search-bar-compact {
    padding: 5px 10px;
  }
  
  .search-option-compact {
    width: 28px;
    height: 28px;
  }
  
  .expanded .search-option-compact {
    padding: 5px 8px;
    font-size: 12px;
  }
  
  .option-emoji {
    font-size: 15px;
  }
  
  .expanded .option-label {
    display: none; /* Always hide labels on very small screens */
  }
}

/* Large Scroll Down indicator at middle bottom */
.large-scroll-indicator {
  position: absolute;
  bottom: 100px; /* Adjusted from 80px to move it up by 20px */
  left: 45%; /* Moved left to align with content */
  transform: translateX(-50%);
  width: 70px;
  height: 70px;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 100;
  animation: pulse-bounce 2s infinite ease-in-out;
  cursor: pointer;
}

.large-chevron-down {
  width: 100%;
  height: 100%;
  filter: drop-shadow(0 2px 5px rgba(0, 0, 0, 0.4));
}

@keyframes pulse-bounce {
  0%, 100% {
    transform: translateX(-50%) translateY(0);
    opacity: 0.9;
  }
  50% {
    transform: translateX(-50%) translateY(10px);
    opacity: 1;
  }
}

/* Previous scroll indicator - now removed */
.scroll-indicator {
  position: fixed;
  bottom: 80px;
  left: 65%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  opacity: 1;
  z-index: 100;
  transition: opacity 0.5s ease;
  animation: gentle-float 4s ease-in-out infinite;
}

@keyframes gentle-float {
  0%, 100% {
    transform: translateX(-50%) translateY(0);
  }
  50% {
    transform: translateX(-50%) translateY(-3px);
  }
}

.scroll-indicator.hidden {
  opacity: 0;
  transform: translateX(-50%) translateY(20px);
  visibility: hidden; 
}

/* Restore paragraph styling for the text */
.scroll-indicator p {
  margin: 0 0 2px 0;
  font-weight: 600;
  font-size: 1.4rem; /* Increased from 1rem to 1.4rem */
  letter-spacing: 0.01em;
  color: white;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
  white-space: nowrap;
}

.chevron-down {
  margin: 0;
  animation: pulse 2s infinite ease-in-out;
  filter: drop-shadow(0 2px 3px rgba(0, 0, 0, 0.4));
  width: 26px; /* Increased from 22px to 26px */
  height: 26px; /* Increased from 22px to 26px */
}

@keyframes pulse {
  0%, 100% {
    opacity: 0.9;
  }
  50% {
    opacity: 1;
  }
}

@keyframes fadeIn {
  from {
    opacity: 0.6;
  }
  to {
    opacity: 1;
  }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(15px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Make sure the heading is responsive */
@media (max-width: 768px) {
  .section-heading {
    width: 80%;
    padding-left: 0;
  }
  
  .section-title {
    font-size: 2.6rem;
  }
  
  .section-label {
    font-size: 0.75rem;
  }
  
  .elegant-content-section {
    padding-top: 90px;
    margin-top: -45px; /* Adjusted from -55px to -45px to position section slightly lower */
    border-radius: 0;
  }
  
  .elegant-content-section::after {
    height: 60px;
    -webkit-mask-image: radial-gradient(ellipse 50% 50% at 50% -20%, transparent 49.5%, #fff 50%);
    mask-image: radial-gradient(ellipse 50% 50% at 50% -20%, transparent 49.5%, #fff 50%);
  }
  
  .elegant-content-section::before {
    height: 90px;
    top: -60px;
  }
}

@media (max-width: 480px) {
  .section-title {
    font-size: 2rem;
  }
  
  .section-heading {
    width: 100%;
  }
  
  .section-label {
    font-size: 0.7rem;
    letter-spacing: 0.15em;
  }
  
  .elegant-content-section {
    padding-top: 70px;
    margin-top: -30px; /* Adjusted from -40px to -30px to position section slightly lower */
    border-radius: 0;
  }
  
  .elegant-content-section::after {
    height: 50px;
    -webkit-mask-image: radial-gradient(ellipse 50% 50% at 50% -20%, transparent 49.5%, #fff 50%);
    mask-image: radial-gradient(ellipse 50% 50% at 50% -20%, transparent 49.5%, #fff 50%);
  }
  
  .elegant-content-section::before {
    height: 70px;
    top: -40px;
  }
}

/* Compare Beaches responsive improvements */
@media (max-width: 768px) {
  .beach-compare-container {
    min-height: auto; /* Let it expand naturally */
    padding: 12px;
    gap: 10px;
  }
  
  .beach-input-group {
    padding: 8px;
  }
  
  .beach-input-group label {
    font-size: 13px;
  }
  
  .compare-button {
    padding: 10px;
  }
}

@media (max-width: 480px) {
  .beach-compare-container {
    min-height: auto; /* Let it expand naturally */
    padding: 10px;
    gap: 8px;
  }
  
  .beach-input-group {
    padding: 6px;
    margin-bottom: 6px;
  }
  
  .button-container {
    margin-top: 6px;
  }
  
  .compare-button {
    padding: 9px;
    font-size: 14px;
  }
}

/* Enhanced styles for the Compare Beaches tab */
.compare-title {
  color: #003b6f;
  font-size: 1.2rem;
  font-weight: 700;
  margin: 0 0 15px 0;
  text-align: center;
  position: relative;
  width: 100%;
}

.beach-inputs-wrapper {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
  width: 100%;
  min-width: 100%; /* Ensure minimum width is respected */
  flex-wrap: nowrap; /* Prevent wrapping to maintain horizontal layout */
}

.compare-arrow {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.8rem;
  padding: 5px;
  margin-top: 20px;
}

.compare-description {
  background-color: rgba(1, 79, 134, 0.08);
  border-radius: 8px;
  padding: 10px;
  margin-bottom: 15px;
  text-align: center;
}

.compare-description p {
  margin: 0;
  color: #003b6f;
  font-size: 0.85rem;
  font-weight: 500;
}

.search-interface-content.compare-beaches {
  padding: 18px 16px;
  height: auto;
  min-height: 180px;
}

.beach-compare-container {
  background: #faf0d7;
  border-radius: 12px;
  padding: 20px;
  border: 2px solid #e0b43c;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.beach-input-group {
  flex: 1;
  margin: 0 5px;
  position: relative;
}

.beach-input-group label {
  display: flex;
  align-items: center;
  gap: 5px;
  margin-bottom: 8px;
  color: #014f86;
  font-size: 0.95rem;
  font-weight: 600;
}

.beach-input-group .search-input {
  width: 100%;
  padding: 12px;
  border: 2px solid #e0b43c;
  background: white;
  border-radius: 8px;
  font-size: 0.95rem;
  color: #333;
  transition: all 0.3s;
}

.beach-input-group .search-input:focus {
  border-color: #014f86;
  box-shadow: 0 0 0 3px rgba(1, 79, 134, 0.15);
  outline: none;
}

.button-container {
  width: 100%;
  margin-top: 5px;
}

.compare-button {
  background: linear-gradient(to bottom, #014f86, #2a6f97);
  color: white;
  border: none;
  padding: 14px;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  box-shadow: 0 4px 8px rgba(1, 79, 134, 0.25);
}

.compare-button:hover {
  background: linear-gradient(to bottom, #003b6f, #1a5f87);
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(1, 79, 134, 0.3);
}

.compare-button:active {
  transform: translateY(0);
}

.button-emoji {
  font-size: 1.2rem;
}

@media (max-width: 768px) {
  .beach-inputs-wrapper {
    flex-direction: column;
    gap: 15px;
  }
  
  .compare-arrow {
    transform: rotate(90deg);
    margin: 0;
  }
  
  .beach-input-group {
    width: 100%;
    margin: 0;
  }
  
  .search-interface-content.compare-beaches {
    padding: 15px 12px;
    min-height: 260px;
  }
}

@media (max-width: 480px) {
  .compare-title {
    font-size: 1.1rem;
  }
  
  .beach-compare-container {
    padding: 15px;
  }
  
  .beach-input-group .search-input {
    padding: 10px;
  }
  
  .compare-button {
    padding: 12px;
  }
}



/* Vertical scroll-down label on right side */
.scroll-down-label {
  position: fixed;
  top: 50%;
  right: 20px; /* Slightly farther from the edge */
  transform: translateY(-50%) rotate(180deg); /* Rotate so text reads downward */
  writing-mode: vertical-rl;
  text-orientation: mixed;
  font-family: 'Montserrat', sans-serif;
  font-size: 0.9rem;
  letter-spacing: 0.18em;
  font-weight: 700;
  background: rgba(0, 0, 0, 0.55); /* Dark translucent background for contrast */
  color: #ffffff;
  padding: 14px 6px;
  border-radius: 8px;
  text-shadow: none;
  z-index: 1000; /* Above most elements but below navbar */
  pointer-events: none; /* Ensure it doesn't block interactions */
  transition: opacity 0.3s ease;
}

/* Hide scroll-down label when scrolled to white section */
.scroll-down-label.hidden {
  opacity: 0;
  visibility: hidden;
}

@media (max-width: 768px) {
  .scroll-down-label {
    display: none; /* Hide on smaller screens to avoid clutter */
  }
}

/* Ensure the tab bar content never overflows its rounded container */
.search-options {
  overflow: hidden; /* Clip any overflow so rounded corners stay clean */
}

/* Tighter tab styling so long labels fit comfortably */
.search-option {
  flex: 1 1 0;
  min-width: 0; /* Allow flex items to shrink */
  padding: 6px 3px; /* Further reduced padding */
  font-size: 12px; /* Further reduced font size */
  gap: 3px; /* Further reduced icon gap */
}

/* Styling for the text within search tabs to handle overflow */
.option-text {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 100%; /* Ensure it respects parent's width when shrinking */
}

/* Beach images comparison container styling */
.beach-images-comparison {
  position: absolute;
  top: 100px;
  right: 3%; /* Adjusted from 2% */
  width: 40%; /* Reduced from 47% to make image less wide */
  border-radius: 18px;
  overflow: visible; /* Changed from hidden to allow hotspot info to display */
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
  z-index: 10;
}

.comparison-container {
  width: 100%;
  position: relative;
  box-sizing: border-box;
}

.image-container {
  position: relative;
  width: 100%;
  overflow: hidden; /* Change from visible to hidden to ensure clean edges */
  border-radius: 18px; /* Full rounded corners instead of just top */
  margin-bottom: 0;
}

.comparison-image {
  width: 100%;
  height: 490px; /* Increased height to match wider width */
  object-fit: cover;
  display: block;
  border-radius: 18px; /* Apply full rounded corners to match container */
}

.comparison-before {
  position: absolute;
  top: 0;
  left: 0;
  width: 50%; /* Start with half of the container showing before image */
  height: 100%;
  overflow: hidden;
  z-index: 2;
  border-right: 4px solid white; /* Thicker divider line */
  border-top-right-radius: 0; /* Ensure right top edge is squared */
}

.comparison-before img {
  width: auto; /* Change from 100% to auto */
  max-width: none; /* Allow image to be wider than container */
  height: 100%; /* Keep full height */
  position: absolute;
  right: 0; /* Align to right edge for a square cut */
  min-width: 100%; /* Ensure minimum width covers container */
  object-fit: cover; /* Maintain aspect ratio while covering */
  transform: none; /* Ensure no transform is applied */
  border-top-right-radius: 0; /* Ensure right top edge is squared */
  clip-path: inset(0 0 0 0); /* Create a square cutout */
}

.slider-handle {
  position: absolute;
  left: 50%; /* Start at 50% */
  top: 0;
  bottom: 0;
  width: 4px; /* Slightly thicker */
  background: white;
  z-index: 3;
  cursor: ew-resize; /* East-west cursor to indicate dragging */
  transform: translateX(-50%);
  touch-action: none; /* Important for mobile touch */
  animation: sliderLineMove 2.5s ease-in-out infinite;
  box-shadow: 0 0 12px rgba(255, 255, 255, 0.7);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
}

@keyframes sliderLineMove {
  0%, 100% { transform: translateX(-50%); box-shadow: 0 0 12px rgba(255, 255, 255, 0.6); }
  25% { transform: translateX(-75%); box-shadow: 0 0 20px rgba(255, 255, 255, 0.9); }
  50% { transform: translateX(-50%); box-shadow: 0 0 12px rgba(255, 255, 255, 0.6); }
  75% { transform: translateX(-25%); box-shadow: 0 0 20px rgba(255, 255, 255, 0.9); }
}

.slider-button {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 45px; /* Slightly larger for better visibility */
  height: 45px;
  border-radius: 50%;
  background: white;
  transform: translate(-50%, -50%);
  box-shadow: 0 0 12px rgba(255, 255, 255, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: ew-resize;
  z-index: 4;
  animation: initialAttention 0.6s ease-out forwards, slideHint 2.5s ease-in-out 0.7s infinite;
  overflow: hidden;
}

@keyframes initialAttention {
  0% { transform: translate(-50%, -50%) scale(1.8); opacity: 0.5; }
  30% { transform: translate(-50%, -50%) scale(1.3); opacity: 0.8; }
  60% { transform: translate(-50%, -50%) scale(1.2); opacity: 1; }
  100% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
}

/* Removed vibrateHandle animation since we now use slideHint */

.slider-button::before, .slider-button::after {
  content: '';
  position: absolute;
  width: 0;
  height: 0;
  border-top: 6px solid transparent;
  border-bottom: 6px solid transparent;
}

.slider-button::before {
  left: 10px;
  border-right: 6px solid #014f86;
}

.slider-button::after {
  right: 10px;
  border-left: 6px solid #014f86;
}

.comparison-labels {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 20px;
  background: #014f86;
  color: white;
  font-weight: 500;
  border-radius: 0 0 12px 12px;
  margin-top: 0;
  position: relative;
  gap: 10px;
}

.comparison-label {
  font-size: 1.5rem;
  letter-spacing: 0.02em;
  font-weight: 600;
}

/* Responsive adjustments for beach images */
@media (max-width: 1200px) {
  .beach-images-comparison {
    width: 48%; /* Adjusted for better visibility */
  }
}

@media (max-width: 992px) {
  .section-heading {
    width: 100%;
  }
  .beach-images-comparison {
    position: relative;
    top: 0;
    right: 0;
    width: 95%;
    margin: 40px auto 20px;
  }
}

@media (max-width: 576px) {
  .comparison-image {
    height: 400px; /* Decreased height for mobile */
  }
  
  .comparison-labels {
    padding: 16px 15px;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
  }
  
  .comparison-label {
    font-size: 1.2rem;
    text-align: center;
  }
  
  .drag-to-compare {
    order: -1;
    width: 100%;
    margin-bottom: 10px;
  }
}

/* Drag to compare instruction */
.drag-to-compare {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  background-color: rgba(255, 255, 255, 0.15);
  color: white;
  border-radius: 30px;
  padding: 6px 16px;
  margin: 0;
  width: max-content;
  position: relative;
  z-index: 15;
  backdrop-filter: blur(3px);
  -webkit-backdrop-filter: blur(3px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.3);
  animation: dragPulse 2s infinite alternate;
  transition: all 0.3s ease;
}

.drag-to-compare:hover {
  background-color: rgba(255, 255, 255, 0.25);
  transform: scale(1.05);
}

@keyframes dragPulse {
  0% {
    transform: scale(1);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  }
  100% {
    transform: scale(1.05);
    box-shadow: 0 4px 12px rgba(255, 255, 255, 0.3);
  }
}

/* Removed SVG icons */

.drag-text {
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.1em;
}

@keyframes pulse {
  0%, 100% {
    opacity: 0.9;
  }
  50% {
    opacity: 1;
  }
}

@keyframes slideHint {
  0%, 100% {
    transform: translate(-50%, -50%);
    box-shadow: 0 0 12px rgba(255, 255, 255, 0.5);
  }
  25% {
    transform: translate(-85%, -50%);
    box-shadow: 0 0 20px rgba(255, 255, 255, 0.8);
  }
  50% {
    transform: translate(-50%, -50%);
    box-shadow: 0 0 12px rgba(255, 255, 255, 0.5);
  }
  75% {
    transform: translate(-15%, -50%);
    box-shadow: 0 0 20px rgba(255, 255, 255, 0.8);
  }
}

/* Hotspot styling for interactive differences */
.hotspot-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 6;
}

.australian .hotspot {
  pointer-events: auto;
}

.comparison-before .hotspot {
  pointer-events: auto;
}

.hotspot {
  position: absolute;
  width: 40px;
  height: 40px;
  cursor: pointer;
  z-index: 25; /* Increased z-index to ensure visibility */
  transition: opacity 0.3s ease, visibility 0.3s ease; /* Added transition for smooth fade effect */
  opacity: 1;
  visibility: visible;
  pointer-events: auto; /* Ensure hotspots are interactive */
}

.hotspot-dot {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 16px;
  height: 16px;
  background: white;
  border-radius: 50%;
  box-shadow: 0 0 0 3px rgba(1, 79, 134, 0.8);
  z-index: 9;
  transition: all 0.3s ease;
}

.hotspot-pulse {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 40px;
  height: 40px;
  background: rgba(1, 79, 134, 0.4);
  border-radius: 50%;
  z-index: 8;
  animation: pulse-hotspot 2s infinite;
}

@keyframes pulse-hotspot {
  0% {
    transform: translate(-50%, -50%) scale(0.5);
    opacity: 1;
  }
  100% {
    transform: translate(-50%, -50%) scale(1.5);
    opacity: 0;
  }
}

.hotspot-info {
  position: absolute;
  width: 250px;
  background: rgba(255, 255, 255, 0.95);
  border-radius: 8px;
  padding: 15px 18px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
  pointer-events: none;
  z-index: 50; /* Increased z-index to ensure tooltips appear above all other elements */
}

.hotspot-info.right {
  left: 40px;
  top: -60px;
}

.hotspot-info.left {
  right: 40px;
  top: -60px;
}

.hotspot-info h4 {
  margin: 0 0 8px;
  color: #014f86;
  font-size: 1.4rem;
  font-weight: 700;
}

.hotspot-info p {
  margin: 0;
  font-size: 1.15rem;
  line-height: 1.3;
  color: #333;
}

.hotspot:hover .hotspot-dot {
  transform: translate(-50%, -50%) scale(1.2);
  background: #014f86;
  box-shadow: 0 0 0 2px white;
}

.hotspot:hover .hotspot-info {
  opacity: 1;
  visibility: visible;
}

.hotspot-container.australian {
  opacity: 1;
  transition: opacity 0.3s ease;
}

.hotspot-container.hidden {
  opacity: 0;
  pointer-events: none;
}

/* Different heading styles for sandy section */
.sandy-content-section .section-label {
  color: rgba(1, 79, 134, 0.8); /* Darker blue for contrast on sandy background */
}

.sandy-content-section .section-title {
  color: #014f86; /* Maintain the same blue for consistency */
}

.sandy-content-section .section-title::after {
  background: #014f86;
}

/* Safety tips container - keeping the container but removing specific tips */
.safety-tips-container {
  display: none;
}

.safety-tip {
  display: none;
}

.tip-icon, .safety-tip h3, .safety-tip p {
  display: none;
}

/* New placeholder for sandy section content */
.sandy-content-placeholder {
  width: 100%;
  min-height: 300px;
  margin-top: 40px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

/* Horizontal safety items inspired by the tour layout in the image */
.safety-items-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin: 20px 0;
  padding: 0;
  max-width: 100vw; /* Allow full viewport width */
}

/* Modified safety item for new layout with image, content and text in bottom left */
.safety-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-direction: row;
  width: 96vw; /* Almost full viewport width */
  margin-left: 2vw; /* Center it */
  margin-bottom: 30px; /* Space between items */
  padding: 60px 4% 100px; /* Adjusted padding for better content placement */
  min-height: 350px; /* Increased vertical size */
  background: linear-gradient(135deg, #2980b9, #3F8AB1); /* Enhanced gradient background */
  border-radius: 18px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  border: 2px solid rgba(255, 255, 255, 0.7);
}

/* Image container for scroll animation */
.safety-image-container {
  width: 35%; /* Reduced image container width to give more space to content */
  height: 280px;
  position: relative;
  overflow: hidden;
  border-radius: 12px;
  margin-right: 5%;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.2);
  border: 3px solid rgba(255, 255, 255, 0.8);
}

/* Button overlay on the RECOGNIZING RIPS image */
.image-overlay-button {
  position: absolute;
  bottom: 15px;
  left: 50%;
  transform: translateX(-50%);
  background: linear-gradient(135deg, #d32f2f, #f44336);
  color: white;
  border: 2px solid #ffffff;
  border-radius: 24px;
  padding: 12px 24px;
  font-weight: 700;
  font-size: 1.2rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 10px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
  transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  z-index: 10;
  overflow: hidden;
  animation: pulsate 2s infinite alternate;
}

.image-overlay-button::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(45deg, rgba(255,255,255,0.1), rgba(255,255,255,0));
  opacity: 0;
  transition: opacity 0.3s ease;
  border-radius: 24px;
}

.image-overlay-button:hover {
  background: linear-gradient(135deg, #c62828, #e53935);
  transform: translateX(-50%) translateY(-5px) scale(1.05);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
}

.image-overlay-button:hover::before {
  opacity: 1;
}

.image-overlay-button:active {
  transform: translateX(-50%) translateY(-2px) scale(0.98);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
  transition: all 0.1s ease;
}

.image-overlay-button:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(211, 47, 47, 0.5), 0 10px 25px rgba(0, 0, 0, 0.4);
}

.image-overlay-button .video-icon {
  font-size: 1.2rem;
  background-color: rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.image-overlay-button:hover .video-icon,
.image-overlay-button:hover .quiz-icon {
  background-color: rgba(255, 255, 255, 0.5);
  transform: scale(1.2);
  transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.quiz-icon {
  font-size: 1.4rem;
  margin-left: 0.5rem;
  background-color: rgba(255, 255, 255, 0.2);
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: transform 0.3s ease;
}

/* Add subtle pulse animation to attract attention */
@keyframes buttonPulse {
  0%, 100% {
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3), 0 0 0 1px rgba(255, 255, 255, 0.1);
  }
  50% {
    box-shadow: 0 4px 20px rgba(211, 47, 47, 0.5), 0 0 0 1px rgba(255, 255, 255, 0.2);
  }
}

.safety-item:hover .image-overlay-button {
  animation: buttonPulse 2s infinite ease-in-out;
}

/* Image mask for animation */
.image-mask {
  width: 100%;
  height: 100%;
  position: relative;
  overflow: hidden;
  transform-origin: center top;
  transform: scaleY(0.4); /* Initial state - reduced to 40% for more dramatic squeeze effect */
  transition: transform 0.2s ease-out; /* Add transition for smoother animation */
  will-change: transform; /* Optimize for animation */
}

/* Safety image styling */
.safety-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
}

/* Content styling */
.safety-content {
  width: 55%; /* Increased content width */
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  z-index: 2; /* Ensure content is above the image */
  padding-bottom: 20px; /* Add space at the bottom */
}

.safety-content-title {
  font-size: 2.2rem; /* Further increased font size */
  font-weight: 800;
  margin-bottom: 20px; /* More space below title */
  color: white;
  opacity: 0; /* Initially hidden, will be animated by GSAP */
  transform: translateY(20px); /* Initial position for animation */
  will-change: opacity, transform; /* Optimize for animation */
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
  letter-spacing: 0.02em;
}

.safety-content-text {
  font-size: 1.8rem; /* Further increased font size */
  line-height: 1.4; /* Further reduced line height for better space usage */
  color: white; /* Keep text as white */
  font-weight: 600;
  opacity: 0; /* Initially hidden, will be animated by GSAP */
  transform: translateY(20px); /* Initial position for animation */
  will-change: opacity, transform; /* Optimize for animation */
  margin-bottom: 20px; /* Further increased bottom margin */
  letter-spacing: 0.02em;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.35);
}

/* Styling for the statistics counter */
.safety-stat-container {
  background-color: rgba(255, 255, 255, 0.85);
  border-radius: 16px; /* Larger radius for bigger appearance */
  padding: 24px 28px; /* Further increased padding */
  margin-bottom: 30px; /* Further increased margin */
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2); /* Enhanced shadow */
  border: 2px solid rgba(255, 255, 255, 0.95);
  opacity: 0; /* Initially hidden, will be animated by GSAP */
  transform: translateY(20px); /* Initial position for animation */
  will-change: opacity, transform; /* Optimize for animation */
  width: 98%; /* Almost full width for maximum impact */
}

.stat-row {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  gap: 25px; /* Increased gap between percentage and text */
}

.safety-stat-number {
  font-size: 6rem; /* Further increased font size */
  font-weight: 900;
  color: #e76f51; /* Warning/danger color */
  line-height: 1;
  min-width: 180px; /* Further increased width */
  text-shadow: none;
  position: relative;
  display: inline-block;
}

/* Removed underline */

.safety-stat-text {
  font-size: 2rem; /* Further increased font size */
  font-weight: 700;
  color: #014f86; /* Changed back to blue */
  margin: 0;
  flex: 1;
  line-height: 1.3; /* Tighter line height for larger text */
  max-width: 450px; /* Increased maximum width */
  text-shadow: none; /* Removed text shadow */
  letter-spacing: 0.01em;
}

/* Styles specific to the flags item */
.safety-item-flags .safety-content {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.safety-content-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 100px;
}

/* Add pulsate animation for buttons */
@keyframes pulsate {
  0% {
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
    transform: translateX(-50%) scale(1);
  }
  100% {
    box-shadow: 0 8px 25px rgba(211, 47, 47, 0.6), 0 0 10px rgba(255, 255, 255, 0.4);
    transform: translateX(-50%) scale(1.05);
  }
}

/* Modified - removed the icon */
.safety-item-icon {
  display: none;
}

/* Modified - removing old title styling */
.safety-item-title {
  display: none;
}

/* New styling for the flag text in bottom left */
.safety-flag-text {
  position: absolute;
  bottom: 35px; /* Slightly reduced spacing */
  left: 4%; /* Match the padding */
  font-size: 2.2rem; /* Increased font size */
  font-weight: 800;
  color: white;
  letter-spacing: 0.05em;
  text-shadow: 0 2px 5px rgba(0, 0, 0, 0.5);
  z-index: 5;
  /* Removed the vertical line */
  padding-left: 0;
}

/* Positioned at bottom right corner */
.safety-item-info {
  display: none; /* Hide the entire info container */
}

/* Add styling for icon marker */
.icon-marker {
  display: none; /* Hide the marker symbol */
  margin-right: 5px;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .sandy-content-section {
    padding: 90px 0 80px; /* No horizontal padding */
  }
  
  .sandy-content-section .section-heading {
    width: 90%;
    padding-left: 5%;
    padding-right: 5%;
  }

  .safety-item {
    width: 94vw;
    margin-left: 3vw;
    padding: 50px 5% 90px; /* Adjusted vertical padding */
    min-height: 400px; /* Increased height for content */
    flex-direction: column; /* Stack elements on tablets */
  }
  
  .safety-image-container {
    width: 90%;
    height: 220px;
    margin: 0 auto 25px;
  }
  
  .image-overlay-button {
    bottom: 15px;
    padding: 8px 16px;
    font-size: 0.9rem;
  }
  
  .image-overlay-button .video-icon {
    width: 22px;
    height: 22px;
    font-size: 1.1rem;
  }
  
  .safety-content {
    width: 100%;
    margin-bottom: 50px; /* Make room for the bottom text */
    text-align: left;
    padding-bottom: 0;
  }
  
  .stat-row {
    flex-direction: column;
    align-items: flex-start;
    gap: 5px;
  }
  
  .safety-stat-number {
    font-size: 3.2rem;
    min-width: auto;
  }
  
  .safety-content-title {
    margin-left: 0;
    margin-right: 0;
    text-align: left;
  }
  
  .safety-flag-text {
    font-size: 1.8rem;
    bottom: 35px; /* Adjusted for medium screens */
    left: 5%;
  }
  
  .safety-item-info {
    bottom: 35px; /* Adjusted for medium screens */
    right: 5%;
  }
}

@media (max-width: 480px) {
  .sandy-content-section {
    padding: 70px 0 60px; /* No horizontal padding */
  }
  
  .sandy-content-section .section-heading {
    width: 92%;
    padding-left: 4%;
    padding-right: 4%;
  }

  .safety-item {
    width: 92vw;
    margin-left: 4vw;
    padding: 40px 4% 80px; /* Adjusted padding */
    min-height: 420px; /* Adjusted height */
    margin-bottom: 25px;
  }
  
  .safety-image-container {
    height: 160px;
    width: 95%;
    margin-bottom: 25px;
  }
  
  .image-overlay-button {
    bottom: 10px;
    padding: 6px 12px;
    font-size: 0.8rem;
    border-radius: 18px;
  }
  
  .image-overlay-button .video-icon {
    width: 18px;
    height: 18px;
    font-size: 0.9rem;
  }
  
  .safety-content-title {
    font-size: 1.2rem;
    margin-bottom: 10px;
  }
  
  .safety-stat-container {
    padding: 12px 15px;
    margin-bottom: 12px;
  }
  
  .stat-row {
    gap: 10px;
  }
  
  .safety-stat-number {
    font-size: 2.7rem;
    min-width: auto;
  }
  
  .safety-stat-text {
    font-size: 0.9rem;
    line-height: 1.2;
  }
  
  .safety-content-text {
    font-size: 1rem;
    line-height: 1.5;
    margin-bottom: 12px;
  }
  
  .safety-content-wrapper {
    min-height: 80px;
  }
  
  .safety-flag-text {
    font-size: 1.4rem;
    bottom: 25px;
    left: 4%;
  }
  
  .safety-item-info {
    bottom: 25px;
    right: 4%;
  }
  
  .safety-priority {
    padding: 6px 12px;
    font-size: 0.85rem;
  }
}

/* Rest of existing styles remain unchanged */

/* Added style to make navbar always use the non-scrolled appearance */
.navbar-wrapper:not(.scrolled) {
  /* If navbar dynamic is disabled, still ensure good contrast with background */
  background: rgba(0, 0, 0, 0.15);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

.safety-priority {
  display: none; /* Hide the entire priority element */
}

/* Hide the marker symbol */
.safety-priority .icon-marker {
  display: none;
}

/* Toddler statistic hover effect */
.section-tagline-container {
position: relative;
width: 100%;
}

.toddler-stat-trigger {
color: #0277bd;
font-weight: 600;
cursor: pointer;
position: relative;
border-bottom: 2px dotted #0277bd;
transition: all 0.3s ease;
}

.toddler-stat-trigger:hover {
color: #e74c3c;
border-bottom-color: #e74c3c;
}

.toddler-stat-popup {
position: absolute;
top: 140px;
left: 340px;
right: auto;
opacity: 0;
visibility: hidden;
z-index: 100;
transition: all 0.3s ease;
width: 320px;
pointer-events: none;
}

.toddler-stat-popup.visible {
opacity: 1;
visibility: visible;
}

.hand-drawn-arrow {
width: 120px;
height: 150px;
position: absolute;
top: -100px;
left: 250px;
right: auto;
transform: rotate(25deg);
z-index: 5;
}

.toddler-stat-content {
background-color: #fff9e6;
padding: 15px;
border-radius: 8px;
box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.2);
border-left: 5px solid #e74c3c;
position: relative;
}

.stat-percentage {
font-size: 2.5rem;
font-weight: 700;
color: #e74c3c;
display: block;
margin-bottom: 5px;
font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;
}

.stat-description {
font-size: 1rem;
line-height: 1.4;
color: #333;
font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Rescue section styles */
.rescue-content-section {
  position: relative;
  min-height: 70vh;
  background-color: #FFE5E1; /* Slightly more saturated light red */
  z-index: 12; /* One higher than the sandy section */
  transition: none;
  opacity: 1;
  margin-top: -80px; /* Increased overlap to show more of sandy section behind */
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding: 100px 0 80px; /* No horizontal padding */
  overflow: hidden; /* Changed to hidden for internal content but we'll allow rescue-showcase to overflow */
  box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.05);
  border-top-left-radius: 50px;
  border-top-right-radius: 50px;
}

/* Curved top edge for rescue section */
.rescue-content-section::before {
  content: '';
  position: absolute;
  top: -80px; /* Adjusted to match reduced overlap */
  left: 0;
  width: 100%;
  height: 150px;
  background: transparent;
  z-index: 0;
  pointer-events: none;
}

.rescue-content-section::after {
  display: none; /* Remove the elliptical shape */
  content: '';
  position: absolute;
  top: -2px;
  left: 0;
  width: 100%;
  height: 150px;
  background-color: transparent;
  z-index: 1;
  border-top-left-radius: 40px;
  border-top-right-radius: 40px;
}

/* Curved top edge for rescue section showing sandy color behind */
.rescue-content-section::before {
  content: '';
  position: absolute;
  top: -120px; /* Increased from -80px to show more sandy color */
  left: 0;
  width: 100%;
  height: 200px; /* Increased from 150px to extend the gradient area */
  background: linear-gradient(to bottom, rgba(248, 228, 175, 1), rgba(248, 228, 175, 0.95) 45%, rgba(255, 229, 225, 0.8) 75%, #FFE5E1 95%);
  z-index: 0;
  pointer-events: none;
}

/* Rescue content placeholder */
.rescue-content-placeholder {
  width: 100%;
  min-height: 300px;
  margin-top: 60px; /* Increased from 40px to create more vertical space */
  display: flex;
  flex-direction: column;
  align-items: flex-end; /* Align items to the right */
}

/* Rescue items container */
.rescue-items-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin: 20px 0;
  padding: 0;
  max-width: 100vw;
}

/* Rescue item styling - similar to safety items but with blue accent colors */
.rescue-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-direction: row;
  width: 96vw;
  margin-left: 2vw;
  margin-bottom: 30px;
  padding: 60px 4% 100px;
  min-height: 350px;
  background: linear-gradient(135deg, #FFCEC8, #FFE5E1); /* Slightly more saturated red gradient */
  border-radius: 18px;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.6);
}

.rescue-image-container {
  width: 35%;
  height: 280px;
  position: relative;
  overflow: hidden;
  border-radius: 12px;
  margin-right: 5%;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.2);
  border: 3px solid rgba(255, 255, 255, 0.8);
}

.rescue-content {
  width: 55%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  z-index: 2;
  padding-bottom: 20px;
}

.rescue-content-title {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 20px;
  color: #D32F2F; /* Deeper red for stronger contrast */
  opacity: 0;
  transform: translateY(20px);
  will-change: opacity, transform;
}

.rescue-content-text {
  font-size: 1.7rem;
  line-height: 1.4;
  color: #424242; /* Darker gray for better readability on light background */
  font-weight: 500;
  opacity: 0;
  transform: translateY(20px);
  will-change: opacity, transform;
  margin-bottom: 20px;
  letter-spacing: 0.01em;
}

.rescue-stat-container {
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 16px;
  padding: 24px 28px;
  margin-bottom: 30px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.9);
  opacity: 0;
  transform: translateY(20px);
  will-change: opacity, transform;
  width: 98%;
}

.rescue-stat-number {
  font-size: 5.5rem;
  font-weight: 800;
  color: #D32F2F; /* Deeper red for stronger contrast */
  line-height: 1;
  min-width: 160px;
}

.rescue-stat-text {
  font-size: 1.9rem;
  font-weight: 600;
  color: #424242; /* Darker gray for better readability */
  margin: 0;
  flex: 1;
  line-height: 1.3;
  max-width: 450px;
}

.rescue-flag-text {
  position: absolute;
  bottom: 35px;
  left: 4%;
  font-size: 2rem;
  font-weight: 800;
  color: #D32F2F; /* Deeper red for stronger contrast */
  letter-spacing: 0.05em;
  text-shadow: 1px 1px 0 rgba(255, 255, 255, 0.7);
  z-index: 5;
}

.rescue-item-info {
  position: absolute;
  bottom: 35px;
  right: 4%;
  z-index: 5;
}

.rescue-priority {
  display: inline-block;
  padding: 8px 16px;
  background-color: #D32F2F; /* Deeper red for stronger contrast */
  color: white;
  font-size: 0.9rem;
  font-weight: 700;
  border-radius: 30px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Responsive adjustments for rescue section */
@media (max-width: 768px) {
  .rescue-content-section {
    padding: 90px 0 80px;
  }
  
  .rescue-content-section .section-heading {
    width: 90%;
    padding-left: 5%;
    padding-right: 5%;
  }

  .rescue-item {
    width: 94vw;
    margin-left: 3vw;
    padding: 50px 5% 90px;
    min-height: 400px;
    flex-direction: column;
  }
  
  .rescue-image-container {
    width: 90%;
    height: 220px;
    margin: 0 auto 25px;
  }
  
  .rescue-content {
    width: 100%;
    margin-bottom: 50px;
    text-align: left;
    padding-bottom: 0;
  }
  
  .rescue-stat-number {
    font-size: 3.2rem;
    min-width: auto;
  }
  
  .rescue-flag-text {
    font-size: 1.8rem;
    bottom: 35px;
    left: 5%;
  }
  
  .rescue-item-info {
    bottom: 35px;
    right: 5%;
  }
}

@media (max-width: 480px) {
  .rescue-content-section {
    padding: 70px 0 60px;
  }
  
  .rescue-content-section .section-heading {
    width: 92%;
    padding-left: 4%;
    padding-right: 4%;
  }

  .rescue-item {
    width: 92vw;
    margin-left: 4vw;
    padding: 40px 4% 80px;
    min-height: 420px;
    margin-bottom: 25px;
  }
  
  .rescue-image-container {
    height: 160px;
    width: 95%;
    margin-bottom: 25px;
  }
  
  .rescue-content-title {
    font-size: 1.2rem;
    margin-bottom: 10px;
  }
  
  .rescue-stat-container {
    padding: 12px 15px;
    margin-bottom: 12px;
  }
  
  .rescue-stat-number {
    font-size: 2.7rem;
    min-width: auto;
  }
  
  .rescue-stat-text {
    font-size: 0.9rem;
    line-height: 1.2;
  }
  
  .rescue-content-text {
    font-size: 1rem;
    line-height: 1.5;
    margin-bottom: 12px;
  }
  
  .rescue-flag-text {
    font-size: 1.4rem;
    bottom: 25px;
    left: 4%;
  }
  
  .rescue-item-info {
    bottom: 25px;
    right: 4%;
  }
  
  .rescue-priority {
    padding: 6px 12px;
    font-size: 0.85rem;
  }
}

/* Slanted cards with centered content inspired by Greenland design */
.rescue-showcase {
  position: relative;
  width: 100%;
  max-width: none; /* Remove max-width constraint to allow full width */
  margin: 80px 0 100px;
  padding: 20px 0 20px 0; /* Remove left padding completely */
  display: flex;
  justify-content: space-between; /* Space between steps and image */
  align-items: flex-start;
  min-height: 520px;
  overflow: visible; /* Keep visible to allow the card to extend outside */
  box-sizing: border-box;
  padding-right: 0; /* Keep no right padding */
}

.rescue-card.centered-card {
  margin: 0;
  right: -15%; /* Push much further beyond the right edge */
  z-index: 10;
  width: 60%; /* Keep width at 60% */
  transform: none;
  max-height: none;
  height: 520px;
  transition: none;
  animation: none;
  border-radius: 18px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
  position: absolute;
  top: 0;
}

@media (max-width: 1200px) {
  .rescue-card.centered-card {
    width: 60%;
    right: -15%;
  }
}

@media (max-width: 992px) {
  .rescue-card.centered-card {
    width: 60%;
    right: -15%;
    height: 450px;
  }
}

@media (max-width: 768px) {
  .rescue-card.centered-card {
    width: 100%;
    position: relative;
    top: 30px;
    right: -5%; /* Slight offset on mobile */
    margin-left: auto;
    margin-right: 0;
    height: 450px;
    transform: none !important;
  }
  
  .rescue-showcase {
    justify-content: center;
  }
  
  .rescue-showcase.scrolled-down .centered-card {
    transform: none !important;
  }
}

@media (max-width: 480px) {
  .rescue-card.centered-card {
    width: 95%;
    height: 350px;
    margin: 0 auto;
  }
}

.rescue-card {
  width: 38%;
  height: 760px;
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
  position: relative;
  transition: transform 0.5s ease, box-shadow 0.5s ease;
  cursor: pointer; /* Change cursor to indicate clickable */
  outline: none; /* Remove outline for cleaner look */
}

.rescue-card:hover:not(.centered-card) {
  transform: translateY(-10px) scale(1.02);
  box-shadow: 0 30px 60px rgba(0, 0, 0, 0.2);
}

.rescue-card.centered-card:hover {
  /* No transform or shadow change for centered card */
  transform: none;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
}

.rescue-card:focus {
  outline: none;
  box-shadow: 0 0 0 3px #D32F2F, 0 30px 60px rgba(0, 0, 0, 0.2);
}

/* Pulse animation on hover to draw attention */
.rescue-card:hover .card-button-indicator {
  transform: translateY(-5px);
  background-color: rgba(255, 255, 255, 0.95);
}

.rescue-card.left-card {
  margin-right: 40px;
  z-index: 2;
}

.rescue-card.right-card {
  margin-left: 40px;
  z-index: 2;
}

.rescue-card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
  transition: transform 0.8s ease;
}

.rescue-card:hover .rescue-card-image {
  transform: scale(1.05);
}

.rescue-card-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 30px 25px;
  background: linear-gradient(to top, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.2) 80%, transparent 100%);
}

.rescue-card-label {
  color: white;
  font-size: 1.6rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-shadow: 0 2px 4px rgba(0,0,0,0.5);
  background-color: rgba(0,0,0,0.3);
  padding: 6px 12px;
  border-radius: 6px;
  display: inline-block;
  margin-bottom: 8px;
}

.rescue-showcase-content {
  width: 24%;
  text-align: center;
  z-index: 3;
  padding: 20px;
  /* Ensure content is always at full opacity by default */
  opacity: 1;
}

.rescue-date {
  font-size: 0.9rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  color: #D32F2F;
  margin-bottom: 15px;
  position: relative;
  display: inline-block;
}

.rescue-date:after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 30px;
  height: 2px;
  background-color: #D32F2F;
}

.rescue-title {
  font-size: 3.2rem;
  font-weight: 700;
  color: #D32F2F;
  margin-bottom: 25px;
  line-height: 1.1;
  letter-spacing: -0.01em;
}

.rescue-cta-button {
  background-color: #D32F2F;
  color: white;
  border: none;
  padding: 12px 30px;
  border-radius: 30px;
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 10px rgba(211, 47, 47, 0.3);
}

.rescue-cta-button:hover {
  background-color: #B71C1C;
  transform: translateY(-3px);
  box-shadow: 0 8px 15px rgba(211, 47, 47, 0.4);
}

/* Responsive adjustments for slanted cards layout */
@media (max-width: 1200px) {
  .rescue-showcase {
    padding: 20px 30px;
  }
  
  .rescue-card {
    width: 40%;
    height: 680px;
  }
  
  .rescue-showcase-content {
    width: 20%;
  }
  
  .rescue-title {
    font-size: 2.8rem;
  }
}

@media (max-width: 992px) {
  .rescue-showcase {
    padding: 10px 20px;
  }
  
  .rescue-card {
    width: 42%;
    height: 600px;
  }
  
  .rescue-card-label {
    font-size: 1.2rem;
  }
  
  .rescue-title {
    font-size: 2.5rem;
  }
}

@media (max-width: 768px) {
  .rescue-showcase {
    flex-direction: column;
    margin: 60px auto;
    min-height: 1200px;
  }
  
  .rescue-card {
    width: 85%;
    height: 520px;
    margin-bottom: 20px;
  }
  
  /* Modified to allow vertical separation on scroll */
  .rescue-card.left-card {
    margin-bottom: 0;
    transform: translateY(0) rotateX(5deg) !important;
  }
  
  .rescue-card.right-card {
    margin-top: 0;
    transform: translateY(0) rotateX(-5deg) !important;
  }
  
  /* For the scrolling animation on mobile, cards separate vertically */
  .rescue-showcase.scrolled-down .left-card {
    transform: translateY(-60px) rotateX(10deg) !important;
  }
  
  .rescue-showcase.scrolled-down .right-card {
    transform: translateY(60px) rotateX(-10deg) !important;
  }
  
  .rescue-showcase-content {
    order: 3;
    width: 80%;
    margin: 30px 0;
  }
  
  .rescue-title {
    font-size: 2.2rem;
  }
}

@media (max-width: 480px) {
  .rescue-showcase {
    margin: 40px auto;
  }
  
  .rescue-card {
    width: 90%;
    height: 450px;
  }
  
  .rescue-card-label {
    font-size: 1.1rem;
  }
  
  .rescue-showcase-content {
    width: 95%;
  }
  
  .rescue-title {
    font-size: 1.8rem;
  }
  
  .rescue-cta-button {
    padding: 10px 25px;
    font-size: 0.9rem;
  }
}

/* Slanted cards with centered content inspired by Greenland design */
.rescue-showcase {
  position: relative;
  width: 100%;
  max-width: 1400px;
  margin: 80px auto 100px;
  padding: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  min-height: 800px;
  overflow: visible;
  box-sizing: border-box;
}

.rescue-card {
  width: 38%;
  height: 760px;
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
  position: relative;
  transition: transform 0.5s ease, box-shadow 0.5s ease;
  cursor: pointer; /* Change cursor to indicate clickable */
  outline: none; /* Remove outline for cleaner look */
}

.rescue-card:hover {
  transform: translateY(-10px) scale(1.02);
  box-shadow: 0 30px 60px rgba(0, 0, 0, 0.2);
}

.rescue-card:focus {
  box-shadow: 0 0 0 3px #D32F2F, 0 30px 60px rgba(0, 0, 0, 0.2);
  outline: none;
}

.rescue-card.left-card {
  transform: perspective(1200px) rotateY(5deg);
  z-index: 2;
}

.rescue-card.right-card {
  transform: perspective(1200px) rotateY(-5deg);
  z-index: 2;
}

.rescue-card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
  transition: transform 0.8s ease;
}

.rescue-card:hover .rescue-card-image {
  transform: scale(1.05);
}

.rescue-card-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 30px 25px;
  background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.4) 70%, transparent 100%);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  z-index: 5;
}

.rescue-card-label {
  color: white;
  font-size: 1.4rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-shadow: 0 2px 4px rgba(0,0,0,0.5);
  background-color: rgba(211, 47, 47, 0.8);
  padding: 8px 16px;
  border-radius: 6px;
  margin-bottom: 15px;
}

/* Button indicator styling */
.card-button-indicator {
  margin-top: 12px;
  background-color: #D32F2F;
  color: #ffffff;
  padding: 12px 22px;
  border-radius: 30px;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  font-weight: 700;
  font-size: 1.1rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.6);
  transition: all 0.3s ease;
  border: 3px solid #ffffff;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}

.rescue-card:hover:not(.centered-card) .card-button-indicator {
  transform: translateY(-5px);
  background-color: #ff4747;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5), 0 0 15px rgba(255, 71, 71, 0.4);
  border-color: #ffffff;
}

.rescue-card.centered-card:hover .card-button-indicator {
  /* No transform or color change */
  transform: none;
  background-color: #D32F2F;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.6);
}

.button-text {
  letter-spacing: 0.5px;
}

.button-icon {
  font-size: 1.4rem;
  transition: transform 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(255, 255, 255, 0.3);
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin-left: 2px;
}

.rescue-card:hover:not(.centered-card) .button-icon {
  transform: translateX(5px);
}

.rescue-card.centered-card:hover .button-icon {
  transform: none;
}

.rescue-showcase-content {
  width: 24%;
  text-align: center;
  z-index: 3;
  padding: 20px;
  /* Ensure content is always at full opacity by default */
  opacity: 1;
}

.rescue-date {
  font-size: 0.9rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  color: #D32F2F;
  margin-bottom: 15px;
  position: relative;
  display: inline-block;
}

.rescue-date:after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 30px;
  height: 2px;
  background-color: #D32F2F;
}

.rescue-title {
  font-size: 3.2rem;
  font-weight: 700;
  color: #D32F2F;
  margin-bottom: 25px;
  line-height: 1.1;
  letter-spacing: -0.01em;
}

.rescue-cta-button {
  background-color: #D32F2F;
  color: white;
  border: none;
  padding: 12px 30px;
  border-radius: 30px;
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 10px rgba(211, 47, 47, 0.3);
}

.rescue-cta-button:hover {
  background-color: #B71C1C;
  transform: translateY(-3px);
  box-shadow: 0 8px 15px rgba(211, 47, 47, 0.4);
}

/* Responsive adjustments for slanted cards layout */
@media (max-width: 1200px) {
  .rescue-showcase {
    padding: 20px 30px;
  }
  
  .rescue-card {
    width: 40%;
    height: 680px;
  }
  
  .rescue-card.centered-card {
    width: 65%;
    height: 850px;
  }
  
  .rescue-showcase-content {
    width: 20%;
  }
  
  .rescue-title {
    font-size: 2.8rem;
  }
  
  .card-button-indicator {
    padding: 10px 18px;
    font-size: 1rem;
  }
  
  .button-icon {
    width: 26px;
    height: 26px;
    font-size: 1.2rem;
  }
}

@media (max-width: 992px) {
  .rescue-showcase {
    padding: 10px 20px;
  }
  
  .rescue-card {
    width: 42%;
    height: 600px;
  }
  
  .rescue-card-label {
    font-size: 1.2rem;
  }
  
  .rescue-title {
    font-size: 2.5rem;
  }
  
  .card-button-indicator {
    padding: 8px 16px;
    font-size: 0.9rem;
  }
}

@media (max-width: 768px) {
  .rescue-showcase {
    flex-direction: column;
    margin: 60px auto;
    min-height: 1200px;
  }
  
  .rescue-card {
    width: 85%;
    height: 520px;
    margin-bottom: 20px;
  }
  
  /* Modified to allow vertical separation on scroll */
  .rescue-card.left-card {
    margin-bottom: 0;
    transform: translateY(0) rotateX(5deg) !important;
  }
  
  .rescue-card.right-card {
    margin-top: 0;
    transform: translateY(0) rotateX(-5deg) !important;
  }
  
  /* For the scrolling animation on mobile, cards separate vertically */
  .rescue-showcase.scrolled-down .left-card {
    transform: translateY(-60px) rotateX(10deg) !important;
  }
  
  .rescue-showcase.scrolled-down .right-card {
    transform: translateY(60px) rotateX(-10deg) !important;
  }
  
  .rescue-showcase-content {
    order: 3;
    width: 80%;
    margin: 30px 0;
  }
  
  .rescue-title {
    font-size: 2.2rem;
  }
}

@media (max-width: 480px) {
  .rescue-showcase {
    margin: 40px auto;
  }
  
  .rescue-card {
    width: 90%;
    height: 450px;
  }
  
  .rescue-card-label {
    font-size: 1.1rem;
  }
  
  .rescue-showcase-content {
    width: 95%;
  }
  
  .rescue-title {
    font-size: 1.8rem;
  }
  
  .rescue-cta-button {
    padding: 10px 25px;
    font-size: 0.9rem;
  }
  
  .card-button-indicator {
    padding: 8px 16px;
    font-size: 0.85rem;
  }
  
  .button-icon {
    width: 22px;
    height: 22px;
    font-size: 1rem;
  }
}

/* Make sure all section headings are aligned consistently */
.elegant-content-section .section-heading,
.sandy-content-section .section-heading,
.rescue-content-section .section-heading {
  padding-left: 4%;
  padding-right: 4%;
  width: 65%;
  margin-top: 3%;
  margin-bottom: 50px; /* Increased from 40px to create more space below the title */
  margin-left: 0; /* Reset margin since image is now below */
}

/* Learn More link in the recognizing rips section */
.learn-more-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background-color: #014f86;
  color: white;
  border: 2px solid #ffffff;
  border-radius: 20px;
  padding: 10px 18px;
  margin-top: 15px;
  font-weight: 700;
  font-size: 1.05rem;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
  position: relative;
  z-index: 10;
}

.learn-more-link:hover, .learn-more-link:focus {
  background-color: #013a63;
  transform: translateY(-3px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
  outline: none;
}

.video-icon {
  font-size: 1.1rem;
  background-color: rgba(255, 255, 255, 0.2);
  width: 22px;
  height: 22px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: transform 0.3s ease;
}

.learn-more-link:hover .video-icon {
  transform: scale(1.2);
  background-color: rgba(255, 255, 255, 0.3);
}

/* Learn More button styles are kept for other instances */
@media (max-width: 768px) {
  .learn-more-link {
    padding: 8px 16px;
    font-size: 0.9rem;
  }
}

@media (max-width: 480px) {
  .learn-more-link {
    padding: 8px 14px;
    font-size: 0.85rem;
  }
  
  .video-icon {
    width: 20px;
    height: 20px;
    font-size: 1rem;
  }
}

/* Rip Escape Simulation Popup Styles */
.rip-simulation-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.85);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  backdrop-filter: blur(15px);
  -webkit-backdrop-filter: blur(15px);
}

@keyframes popupIntro {
  0% {
    opacity: 0;
    transform: scale(0.9);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}

.rip-simulation-container {
width: auto;
max-width: fit-content;
background-color: rgba(17, 17, 17, 0.95);
border-radius: 16px;
overflow: hidden;
box-shadow: 
  0 30px 60px rgba(0, 0, 0, 0.5), 
  0 0 0 1px rgba(255, 255, 255, 0.1),
  0 0 30px rgba(1, 79, 134, 0.3);
animation: popupIntro 0.7s cubic-bezier(0.16, 1, 0.3, 1);
transform-origin: center;
border: 1px solid rgba(255, 255, 255, 0.08);
max-height: 95vh;
display: flex;
flex-direction: column;
}

/* Wider container for Rip Current Safety Quiz */
.quiz-container {
  max-width: 100vw !important;
  width: 2000px !important;
}

.rip-simulation-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  background: linear-gradient(135deg, #013a63, #2a6f97);
  color: white;
  position: relative;
  overflow: hidden;
}

.rip-simulation-header h3 {
  margin: 0;
  font-size: 1.3rem;
  font-weight: 600;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
  letter-spacing: 0.01em;
  display: flex;
  align-items: center;
}

.rip-simulation-header .close-button {
  background: rgba(255, 255, 255, 0.1);
  border: none;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  position: relative;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.rip-simulation-header .close-icon {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 14px;
  height: 14px;
}

.rip-simulation-header .close-icon::before, 
.rip-simulation-header .close-icon::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: white;
  border-radius: 1px;
}

.rip-simulation-header .close-icon::before {
  transform: rotate(45deg);
}

.rip-simulation-header .close-icon::after {
  transform: rotate(-45deg);
}

.rip-simulation-header .close-button:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: scale(1.1);
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.3);
}

.rip-simulation-content {
flex: 1;
overflow: auto;
padding: 5px;
background-color: #1a1a1a;
}

@media (max-width: 768px) {
  .rip-simulation-header {
    padding: 10px 14px;
  }
  
  .rip-simulation-header h3 {
    font-size: 1.1rem;
  }
  
  .rip-simulation-content {
    padding: 3px;
  }
  
  .rip-simulation-header .close-button {
    width: 28px;
    height: 28px;
  }
}

@media (max-width: 480px) {
  .rip-simulation-container {
    border-radius: 12px;
    width: auto;
  }
  
  .rip-simulation-header {
    padding: 8px 12px;
  }
  
  .rip-simulation-header h3 {
    font-size: 1rem;
  }
  
  .rip-simulation-content {
    padding: 2px;
  }
  
  .rip-simulation-header .close-button {
    width: 24px;
    height: 24px;
  }
  
  .rip-simulation-header .close-icon {
    width: 12px;
    height: 12px;
  }
}

/* Hover instruction styling */
.hover-instruction {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
  z-index: 3;
  pointer-events: none;
}

.rescue-card:hover:not(.centered-card) .hover-instruction {
  opacity: 1;
}

.rescue-card:hover:not(.centered-card) .rescue-card-image {
  filter: brightness(0.7) blur(2px);
}

/* No hover effects for centered card */
.rescue-card.centered-card:hover .hover-instruction {
  opacity: 0;
}

.rescue-card.centered-card:hover .rescue-card-image {
  filter: none;
}

.instruction-content {
  background-color: rgba(0, 0, 0, 0.8);
  border: 2px solid white;
  border-radius: 12px;
  padding: 20px;
  width: 85%;
  max-width: 400px;
  color: white;
  text-align: left;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
}

.instruction-content strong {
  display: block;
  font-size: 1.4rem;
  margin-bottom: 12px;
  color: #ffffff;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.instruction-content ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.instruction-content li {
  margin-bottom: 10px;
  padding-left: 20px;
  position: relative;
  font-size: 1.1rem;
  line-height: 1.4;
}

.instruction-content li:before {
  content: "→";
  position: absolute;
  left: 0;
  color: #D32F2F;
  font-weight: bold;
}

@media (max-width: 768px) {
  .instruction-content {
    padding: 15px;
    width: 90%;
  }
  
  .instruction-content strong {
    font-size: 1.2rem;
  }
  
  .instruction-content li {
    font-size: 1rem;
    margin-bottom: 8px;
  }
}

@media (max-width: 480px) {
  .instruction-content {
    padding: 12px;
    width: 95%;
  }
  
  .instruction-content strong {
    font-size: 1.1rem;
    margin-bottom: 8px;
  }
  
  .instruction-content li {
    font-size: 0.9rem;
    margin-bottom: 6px;
  }
}

/* Old lifeguard highlight style - now replaced by rules within .lifeguard-section */

.lifeguard-image {
  width: 100%;
  border-radius: 18px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
  height: 520px;
  object-fit: cover;
  object-position: 50% 0%;
}

@media (max-width: 1200px) {
  .lifeguard-highlight {
    width: 60%;
  }
}

@media (max-width: 992px) {
  .lifeguard-highlight {
    width: 70%;
  }
  
  .lifeguard-image {
    height: 490px;
    object-position: 50% 0%;
  }
}

@media (max-width: 768px) {
  .lifeguard-highlight {
    width: 90%;
    margin: 0 auto 40px;
  }
  
  .lifeguard-image {
    height: 460px;
    object-position: 50% 5%;
  }
  
  .rescue-content-section .section-heading {
    margin-bottom: 30px;
    width: 90%;
  }
}

@media (max-width: 480px) {
  .lifeguard-image {
    height: 410px;
    object-position: 50% 5%;
  }
}

/* Rescue content section */

/* Rescue hero section with image and large text */
.rescue-hero-section {
  display: flex;
  width: 100%;
  margin-top: 40px; /* Add top margin to create space below the title */
  margin-bottom: 70px;
  position: relative;
}

/* Lifeguard highlight image */
.lifeguard-highlight {
  position: relative;
  width: 45%;
  margin-left: 4%;
  z-index: 10;
  flex-shrink: 0;
}

/* Large emergency steps */
.emergency-steps-large {
  flex: 1;
  margin-left: 4%;
  margin-right: 3%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  padding-top: 0;
  width: 51%;
}

.emergency-title {
  font-size: 3.5rem;
  font-weight: 800;
  color: #D32F2F;
  margin-bottom: 30px;
  letter-spacing: -0.02em;
  line-height: 1;
  text-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.emergency-step {
  display: flex;
  align-items: center;
  margin-bottom: 28px;
  padding-bottom: 20px;
  border-bottom: 1px solid rgba(211, 47, 47, 0.2);
  position: relative;
  flex-wrap: nowrap;
  width: 100%;
}

.step-number {
  width: 48px;
  height: 48px;
  background-color: #D32F2F;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 1.6rem;
  margin-right: 20px;
  flex-shrink: 0;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
}

.step-headline {
  font-size: 2.2rem;
  font-weight: 800;
  color: #D32F2F;
  margin-right: 12px;
  letter-spacing: -0.02em;
  white-space: nowrap;
}

.step-brief {
  font-size: 1.3rem;
  color: #000;
  font-weight: 600;
  white-space: nowrap;
  flex-shrink: 1;
}

/* Responsive styles */
@media (max-width: 1200px) {
  .emergency-title {
    font-size: 2.6rem;
    margin-bottom: 24px;
  }
  
  .step-number {
    width: 42px;
    height: 42px;
    font-size: 1.4rem;
    margin-right: 16px;
  }
  
  .step-headline {
    font-size: 1.8rem;
  }
  
  .step-brief {
    font-size: 1rem;
  }
}

@media (max-width: 992px) {
  .rescue-hero-section {
    flex-direction: column;
  }
  
  .lifeguard-highlight {
    width: 70%;
    margin: 0 auto 40px;
  }
  
  .emergency-steps-large {
    margin: 0 auto;
    width: 85%;
    align-items: center;
  }
  
  .emergency-step {
    width: 100%;
    max-width: 500px;
  }
}

  @media (max-width: 768px) {
    .lifeguard-highlight {
      width: 90%;
    }
    
    .emergency-steps-large {
      width: 90%;
    }
    
    .emergency-title {
      font-size: 2.2rem;
      text-align: center;
    }
    
    .step-headline {
      font-size: 1.5rem;
    }
    
    .step-brief {
      font-size: 1.3rem;
    }
  }

  @media (max-width: 480px) {
    .emergency-title {
      font-size: 1.8rem;
    }
    
    .emergency-step {
      margin-bottom: 16px;
    }
    
    .step-number {
      width: 36px;
      height: 36px;
      font-size: 1.2rem;
      margin-right: 12px;
    }
    
    .step-headline {
      font-size: 1.2rem;
      margin-right: 10px;
    }
    
    .step-brief {
      font-size: 1.1rem;
    }
  }

/* Enhanced Animation for emergency steps */
@keyframes pulseBackground {
  0%, 50%, 100% { background-color: #D32F2F; }
}

@keyframes slideInBottom {
  0% { 
    opacity: 0;
    transform: translateY(50px);
  }
  100% { 
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeScale {
  0% { 
    opacity: 0;
    transform: scale(0.8);
  }
  100% { 
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes glowEffect {
  0%, 50%, 100% { box-shadow: none; }
}

.animate-element {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.8s ease, transform 0.8s cubic-bezier(0.215, 0.61, 0.355, 1);
  will-change: opacity, transform;
}

/* Enhanced title animation with dramatic entry */
.emergency-title.animate-element {
  transform: translateY(40px);
  opacity: 0;
}

.emergency-title.animated {
  opacity: 1;
  transform: translateY(0);
  animation: slideInBottom 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards;
  /* Glow effects handled by class removal */
}

.animate-element.animated {
  opacity: 1;
  transform: translateY(0);
}

/* Enhanced animation for step numbers with pulse effect */
.animate-element .step-number {
  transform: scale(0);
  transition: transform 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  transition-delay: 0.3s;
}

.animate-element.animated .step-number {
  transform: scale(1);
  /* Glow effects removed */
}

/* Enhanced animation for step headlines with staggered slide-in effect */
.animate-element .step-headline {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.8s ease, transform 0.8s cubic-bezier(0.165, 0.84, 0.44, 1);
  transition-delay: 0.5s;
}

.animate-element.animated .step-headline {
  opacity: 1;
  transform: translateY(0);
  text-shadow: 0 0 1px rgba(211, 47, 47, 0.3);
}

/* Enhanced animation for step brief descriptions with staggered fade-in effect */
.animate-element .step-brief {
  opacity: 0;
  transform: translateX(15px);
  transition: opacity 0.8s ease, transform 0.8s ease;
  transition-delay: 0.7s;
}

.animate-element.animated .step-brief {
  opacity: 1;
  transform: translateX(0);
}

/* Sequential animation delays for steps */
.emergency-step:nth-child(2) {
  transition-delay: 0.2s;
}

.emergency-step:nth-child(3) {
  transition-delay: 0.4s;
}

.emergency-step:nth-child(4) {
  transition-delay: 0.6s;
}

/* Escape Steps Styling - similar to emergency steps but positioned left */
.escape-steps {
  flex: 1;
  margin-left: -12%; /* Shift further left beyond the section padding */
  margin-right: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  padding-top: 0;
  width: 38%; /* Increased width to fit single-line text */
  position: absolute; /* Position absolutely to align with image */
  left: 0; /* Align to left edge */
  top: 0; /* Align to top of container */
  z-index: 20;
}

.escape-title {
  font-size: 3.2rem;
  font-weight: 800;
  color: #D32F2F;
  margin-bottom: 30px;
  letter-spacing: -0.02em;
  line-height: 1;
  text-shadow: 0 2px 5px rgba(0,0,0,0.1);
  white-space: nowrap;
}

.escape-step {
  display: flex;
  align-items: center;
  margin-bottom: 28px;
  padding-bottom: 20px;
  border-bottom: 1px solid rgba(211, 47, 47, 0.2);
  position: relative;
  flex-wrap: nowrap;
  width: 100%;
  white-space: nowrap; /* Ensure single-line text */
  overflow: visible;
  /* Make exactly like emergency-step */
  transition: transform 0.3s ease;
}

/* Animation delays removed - now handled by data-delay attributes */

@keyframes fadeInLeft {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* Updated animation for escape-title - Pulse effects removed */
.escape-pulse {
  /* Pulse animation removed */
}

@keyframes escapeTitlePulse {
  0% {
    text-shadow: none;
  }
  100% {
    text-shadow: none;
  }
}

/* Enhanced escape steps animations */
/* Make escape animations exactly match the emergency steps */
.escape-animate {
  opacity: 0;
  transform: translateY(30px);
}

.escape-animate .step-number {
  transform: scale(0);
  transition: transform 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  transition-delay: 0.3s;
}

.escape-animate .step-headline {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.8s ease, transform 0.8s cubic-bezier(0.165, 0.84, 0.44, 1);
  transition-delay: 0.5s;
}

.escape-animate .step-brief {
  opacity: 0;
  transform: translateX(15px);
  transition: opacity 0.8s ease, transform 0.8s ease;
  transition-delay: 0.7s;
}

.escape-animate.animated {
  opacity: 1;
  transform: translateY(0);
  transition: opacity 0.8s ease, transform 0.8s cubic-bezier(0.215, 0.61, 0.355, 1);
}

.escape-animate.animated .step-number {
  transform: scale(1);
}

.escape-animate.animated .step-headline {
  opacity: 1;
  transform: translateY(0);
}

.escape-animate.animated .step-brief {
  opacity: 1;
  transform: translateX(0);
}

@keyframes slideInStaggered {
  0% {
    opacity: 0;
    transform: translateY(30px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

.escape-step {
  position: relative;
  transition: transform 0.3s ease;
}

/* Hover effects removed */

.escape-step .step-number {
  transition: transform 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  /* Match emergency steps exactly */
  background-color: #D32F2F;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 1.6rem;
  margin-right: 20px;
  flex-shrink: 0;
  width: 48px;
  height: 48px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
}

/* Match emergency headline styling */
.escape-step .step-headline {
  font-size: 1.5rem;
  font-weight: 800;
  color: #D32F2F;
  margin-right: 12px;
  letter-spacing: -0.02em;
  white-space: nowrap;
}

/* Match emergency brief styling */
.escape-step .step-brief {
  font-size: 1.5rem;
  color: #000;
  font-weight: 600;
  white-space: nowrap;
  flex-shrink: 1;
}

/* Responsive styles for escape steps */
@media (max-width: 1200px) {
  .escape-steps {
    width: 42%;
  }
  
  .escape-title {
    font-size: 2.6rem;
  }
}

@media (max-width: 992px) {
  .escape-steps {
    width: 45%;
  }
  
  .escape-title {
    font-size: 2.2rem;
  }
}

@media (max-width: 768px) {
  .rescue-showcase {
    flex-direction: column;
    padding-left: 0;
  }
  
  .escape-steps {
    width: 90%;
    position: relative;
    left: auto;
    top: auto;
    margin: 0 auto 40px;
  }
  
  .escape-title {
    font-size: 2rem;
    text-align: center;
  }
  
  .escape-step {
    margin-bottom: 20px;
    padding-bottom: 15px;
  }
}

@media (max-width: 480px) {
  .escape-steps {
    width: 95%;
  }
  
  .escape-title {
    font-size: 1.8rem;
  }
}

/* === Custom Overrides: Step Text Enhancements === */
.step-headline,
.step-brief {
  text-transform: uppercase;
}

.step-headline {
  font-size: 1.5rem; /* Increased font size */
}

.step-brief {
  font-size: 1.5rem; /* Increased font size */
}

/* Emergency Steps Animation Enhancements - Glow effects removed */
.emergency-pulse {
  /* Pulse animation removed */
}

@keyframes titlePulse {
  0% {
    text-shadow: none;
    color: #D32F2F;
  }
  100% {
    text-shadow: none;
    color: #D32F2F;
  }
}

.step-connector {
  position: absolute;
  top: 100%;
  left: 24px;
  width: 1px;
  height: 20px;
  background: linear-gradient(to bottom, rgba(211, 47, 47, 0.5), transparent);
  z-index: 5;
}

.emergency-step {
  position: relative;
  transition: transform 0.3s ease;
}

/* Hover effects removed */

/* Improved mobile responsiveness for animations */
@media (max-width: 768px) {
  .step-connector {
    left: 21px;
    height: 15px;
  }
  
  @keyframes titlePulse {
    0%, 100% {
      text-shadow: none;
    }
  }
}

/* Slider text styling */
.slider-text {
  background-color: rgba(255, 255, 255, 0.2);
  color: white;
  border-radius: 30px;
  padding: 6px 16px;
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  white-space: nowrap;
  backdrop-filter: blur(3px);
  -webkit-backdrop-filter: blur(3px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.3);
  animation: textGlow 2.5s infinite alternate;
  z-index: 10;
  margin: 0 auto;
  margin-left: 215px;
}

@keyframes textGlow {
  0% {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
    background-color: rgba(255, 255, 255, 0.2);
  }
  100% {
    box-shadow: 0 4px 12px rgba(255, 255, 255, 0.4);
    background-color: rgba(255, 255, 255, 0.3);
  }
}

/* New styles for hero layout */
.hero-flex-container {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  padding-top: 20px;
  padding-left: 3%;
  position: relative;
  z-index: 5;
  width: 100%;
}

/* Add styles for the hero tool row */
.hero-tool-row {
  width: 100%;
  display: flex;
  justify-content: flex-start;
  padding-left: 2%;
  margin-top: 1rem;
  margin-bottom: 2rem;
  z-index: 5;
  position: relative;
}

.integrated-beach-tool {
  width: 85%;
  max-width: 900px;
  max-height: 600px;
  overflow-y: auto;
}

@media (max-width: 992px) {
  .integrated-beach-tool {
    width: 95%;
  }
}

@media (max-width: 768px) {
  .hero-flex-container {
    padding-top: 15px;
    padding-left: 2%;
  }
  
  .hero-tool-row {
    padding-left: 2%;
  }
  
  .integrated-beach-tool {
    width: 96%;
  }
  
  .hero-section {
    text-align: left;
    margin-top: 10px;
  }
  
  .hero-content {
    padding-top: 150px;
  }
}

@media (max-width: 480px) {
  .hero-flex-container {
    padding-left: 1.5%;
    padding-top: 10px;
  }
  
  .hero-tool-row {
    margin-top: 0.75rem;
    margin-bottom: 1.5rem;
    padding-left: 1.5%;
  }
  
  .integrated-beach-tool {
    width: 95%;
  }
  
  .hero-content {
    padding-top: 120px;
    padding-bottom: 140px;
  }
}

/* Safety Standards Container Styles */
.safety-standards-container {
max-width: 800px;
width: 100%;
margin: 0;
padding: 0;
background: rgba(0, 0, 0, 0.7);
border-radius: 12px;
box-shadow: 0 10px 35px rgba(0, 0, 0, 0.4), 0 0 0 1px rgba(255, 255, 255, 0.1);
margin-top: 25px;
margin-bottom: 45px; /* Adjusted to ensure it doesn't overlap with subsequent elements */
overflow: visible; /* Changed from hidden to allow suggestions to show */
position: relative;
z-index: 20;
border: 1px solid rgba(255, 255, 255, 0.15);
backdrop-filter: blur(5px);
-webkit-backdrop-filter: blur(5px);
/* Add transition for height changes */
transition: max-height 0.5s ease-in-out, height 0.5s ease-in-out;
max-height: 350px; /* Default max-height, adjusted */
}

.safety-standards-container.suggestions-active {
max-height: 650px; /* Expanded max-height, adjusted */
height: auto; /* Allow it to grow based on content */
}

/* Section top with toggle buttons */
.section-top {
display: flex;
flex-direction: column;
padding: 1.4rem 1.4rem 0.8rem;
background: rgba(0, 71, 106, 0.6);
border-bottom: 1px solid rgba(0, 186, 255, 0.5);
position: relative;
}

/* Toggle buttons for selecting between options */
.option-toggle {
display: flex;
justify-content: flex-start;
gap: 1rem;
margin-top: 1rem;
margin-bottom: 0.5rem;
width: 100%;
}

.toggle-btn {
padding: 0.7rem 1.2rem;
background: rgba(0, 51, 82, 0.7);
color: rgba(255, 255, 255, 0.8);
border: 1px solid rgba(0, 186, 255, 0.3);
border-radius: 8px;
cursor: pointer;
font-size: 1rem;
font-weight: 600;
transition: all 0.3s ease;
display: flex;
align-items: center;
gap: 0.5rem;
flex: 0 0 auto;
justify-content: center;
max-width: 180px;
width: auto;
}

.toggle-btn:hover {
background: rgba(0, 71, 106, 0.8);
border-color: rgba(0, 186, 255, 0.6);
transform: translateY(-2px);
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.toggle-btn.active {
background: rgba(0, 123, 194, 0.7);
border-color: rgba(0, 225, 255, 0.8);
color: white;
box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3), 0 0 0 1px rgba(0, 225, 255, 0.4);
}

.toggle-icon {
font-size: 1.2rem;
margin-right: 0.2rem;
}

/* Option content container */
.option-content {
padding: 1.4rem;
background: rgba(0, 51, 82, 0.7);
transition: all 0.3s ease;
border-bottom: 1px solid rgba(0, 186, 255, 0.5);
}

.location-finder {
background: rgba(0, 51, 82, 0.7);
border-radius: 0;
padding: 1.4rem;
margin-bottom: 0;
border-left: none;
border-bottom: 1px solid rgba(0, 186, 255, 0.5);
transition: all 0.3s ease;
position: relative;
display: flex;
flex-wrap: wrap;
align-items: center;
}

.location-finder::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  height: 100%;
  width: 4px;
  background: rgba(0, 186, 255, 0.8);
  border-radius: 4px 0 0 0;
}

.location-finder:hover {
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
  transform: translateY(-3px);
}

.search-container {
  margin-bottom: 0;
  max-width: 100%;
  flex: 1;
  min-width: 250px;
}

.section-subtitle {
color: #44ccff;
font-size: 1.25rem;
margin: 0 0 1rem;
font-weight: 700;
text-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
letter-spacing: 0.02em;
text-align: center;
position: relative;
}

.section-subtitle:after {
  content: '';
  position: absolute;
  bottom: -0.4rem;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 2px;
  background: rgba(0, 186, 255, 0.8);
}

.search-input-container {
  position: relative;
  display: flex;
  align-items: center;
  margin: 1.5rem auto 0;
  max-width: 800px;
  width: 95%;
}

.search-icon {
  position: absolute;
  left: 1.2rem;
  top: 50%;
  transform: translateY(-50%);
  font-size: 1.2rem;
  color: rgba(0, 225, 255, 0.9);
  filter: drop-shadow(0 1px 3px rgba(0, 0, 0, 0.5));
  z-index: 2;
}

.search-input {
width: 100%;
padding: 0.9rem 3rem 0.9rem 3.5rem;
border-radius: 8px;
border: 1px solid rgba(0, 225, 255, 0.4);
background: rgba(0, 0, 0, 0.5);
color: white;
font-size: 1.1rem;
outline: none;
transition: all 0.3s ease;
box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3), inset 0 0 10px rgba(0, 225, 255, 0.1);
}

.search-input:focus {
  border-color: rgba(0, 225, 255, 0.9);
  box-shadow: 0 0 20px rgba(0, 225, 255, 0.4), inset 0 0 15px rgba(0, 225, 255, 0.2);
  background: rgba(0, 20, 40, 0.6);
}

.search-input::placeholder {
  color: rgba(255, 255, 255, 0.6);
  opacity: 1;
  font-size: 1.1rem;
  font-weight: 300;
  letter-spacing: 0.02em;
}

.clear-button {
position: absolute;
right: 1.5rem;
top: 50%;
transform: translateY(-50%);
background: rgba(0, 0, 0, 0.3);
border: 1px solid rgba(255, 255, 255, 0.2);
color: rgba(255, 255, 255, 0.9);
cursor: pointer;
font-size: 1.1rem;
height: 32px;
width: 32px;
border-radius: 50%;
display: flex;
align-items: center;
justify-content: center;
transition: all 0.3s ease;
box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
z-index: 2;
}

.clear-button:hover {
  background-color: rgba(231, 76, 60, 0.5);
  color: #fff;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
}

.error-message {
  color: #ff6b6b;
  margin: 0.8rem 0;
  font-size: 1rem;
  padding: 0.7rem 1.2rem;
  background: rgba(231, 76, 60, 0.2);
  border-radius: 0.8rem;
  display: flex;
  align-items: center;
  border-left: 3px solid #ff6b6b;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.2);
}

.error-icon {
  margin-right: 0.7rem;
  font-size: 1.1rem;
  filter: drop-shadow(0 1px 2px rgba(0, 0, 0, 0.3));
}

.no-margin {
  margin: 0;
}

.location-suggestions {
  max-height: 280px;
  overflow-y: auto;
  background: rgba(0, 41, 61, 0.8);
  border-radius: 0;
  margin-top: 0;
  border: none;
  border-top: 1px solid rgba(0, 225, 255, 0.4);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
  z-index: 10;
  position: absolute;
  list-style-type: none;
  padding: 0;
  scrollbar-width: thin;
  scrollbar-color: rgba(0, 225, 255, 0.6) rgba(0, 0, 0, 0.2);
  width: 100%;
  left: 0;
}

.suggestion-item {
  padding: 1.2rem 1.4rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.15);
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.19, 1, 0.22, 1);
  display: flex;
  align-items: center;
  color: rgba(255, 255, 255, 0.9);
  font-size: 1.05rem;
  position: relative;
  overflow: hidden;
}

.suggestion-item::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  height: 100%;
  width: 0;
  background: linear-gradient(to right, rgba(0, 186, 255, 0.2), transparent);
  transition: width 0.3s ease;
}

.suggestion-item:hover {
  background: rgba(0, 60, 100, 0.6);
  color: #ffffff;
  padding-left: 2rem;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.suggestion-item:hover::before {
  width: 100%;
}

.suggestion-item:last-child {
  border-bottom: none;
}

.location-icon {
  margin-right: 1rem;
  font-size: 1.2rem;
  color: #44ccff;
  filter: drop-shadow(0 1px 3px rgba(0, 0, 0, 0.4));
  position: relative;
  z-index: 1;
}

.selected-location-info {
  margin-top: 1.5rem;
  padding: 1.5rem;
  background: rgba(0, 186, 255, 0.15);
  border-radius: 1.2rem;
  border-left: 5px solid rgba(0, 225, 255, 0.7);
  animation: fadeIn 0.5s cubic-bezier(0.19, 1, 0.22, 1);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(3px);
  -webkit-backdrop-filter: blur(3px);
}

.location-header {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
}

.location-pin {
  font-size: 1.5rem;
  margin-right: 1rem;
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.4));
  color: #44ccff;
}

.location-header h5 {
  margin: 0;
  font-size: 1.4rem;
  color: #44ccff;
  font-weight: 700;
  text-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
  letter-spacing: 0.02em;
}

.location-name {
  margin: 0 0 1rem;
  padding: 0.8rem 1.2rem;
  background: rgba(0, 30, 50, 0.5);
  border-radius: 0.8rem;
  font-size: 1.1rem;
  color: white;
  border: 1px solid rgba(0, 186, 255, 0.3);
  box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.3);
}

.state-detected {
  display: flex;
  align-items: center;
  color: #2eee80;
  font-size: 1.1rem;
  padding: 0.8rem 1.2rem;
  background: rgba(46, 204, 113, 0.2);
  border-radius: 0.8rem;
  font-weight: 600;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.2);
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
  border-left: 3px solid #2ecc71;
}

.check-icon {
  margin-right: 0.8rem;
  font-size: 1.2rem;
  filter: drop-shadow(0 1px 3px rgba(0, 0, 0, 0.3));
}

/* State selector styles */
.state-selector-container {
margin: 0;
padding: 1.4rem;
position: relative;
background: rgba(0, 51, 82, 0.7);
border-bottom: 1px solid rgba(0, 186, 255, 0.5);
display: flex;
flex-direction: column;
align-items: center;
}

.select-prompt {
  text-align: center;
  margin: 1rem 0 1.2rem;
  font-weight: 600;
  color: rgba(255, 255, 255, 1);
  display: flex;
  align-items: center;
  justify-content: center;
  text-shadow: 0 2px 5px rgba(0, 0, 0, 0.4);
  font-size: 1rem;
  letter-spacing: 0.02em;
}

.prompt-icon {
  margin-right: 0.7rem;
  font-size: 1.2rem;
  animation: bounce 1.2s infinite alternate;
  filter: drop-shadow(0 2px 3px rgba(0, 0, 0, 0.5));
}

@keyframes bounce {
  from { transform: translateY(0); }
  to { transform: translateY(6px); }
}

.select-wrapper {
  position: relative;
  width: 85%;
  max-width: 400px;
  margin: 0 auto 1.8rem;
}

.state-dropdown {
width: 100%;
background: rgba(0, 51, 82, 0.7);
border: 1px solid rgba(0, 225, 255, 0.5);
border-radius: 8px;
padding: 0.7rem 1.4rem;
font-size: 1rem;
color: white;
font-weight: 600;
appearance: none;
-webkit-appearance: none;
cursor: pointer;
box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3), inset 0 0 10px rgba(0, 225, 255, 0.1);
transition: all 0.3s cubic-bezier(0.19, 1, 0.22, 1);
text-align: center;
outline: none;
text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
letter-spacing: 0.02em;
}

.state-dropdown:hover {
  border-color: rgba(0, 225, 255, 0.8);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4), 0 0 20px rgba(0, 186, 255, 0.2);
  transform: translateY(-2px);
}

.state-dropdown:focus {
  border-color: rgba(0, 255, 255, 0.9);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4), 0 0 20px rgba(0, 186, 255, 0.4);
  background: rgba(0, 60, 100, 0.8);
}

.select-arrow {
  position: absolute;
  right: 1.5rem;
  top: 50%;
  transform: translateY(-50%);
  color: rgba(0, 225, 255, 0.8);
  font-size: 0.8rem;
  pointer-events: none;
  filter: drop-shadow(0 1px 2px rgba(0, 0, 0, 0.4));
  transition: all 0.3s ease;
}

.select-wrapper:hover .select-arrow {
  color: rgba(0, 255, 255, 1);
  transform: translateY(-50%) scale(1.2);
}

/* Regulation Content Styles */
.regulation-content {
background: rgba(0, 51, 82, 0.7);
border-radius: 0 0 12px 12px;
padding: 0;
margin-bottom: 0;
overflow: hidden;
box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
animation: fadeIn 0.6s cubic-bezier(0.19, 1, 0.22, 1);
border: none;
border-bottom: 1px solid rgba(0, 186, 255, 0.3);
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.state-header {
background: linear-gradient(to right, rgba(0, 123, 194, 0.9), rgba(0, 60, 90, 0.95));
padding: 1.4rem;
display: flex;
align-items: center;
border-bottom: 1px solid rgba(0, 225, 255, 0.4);
position: relative;
overflow: hidden;
}

.state-header::after {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 50%;
  height: 100%;
  background: linear-gradient(to left, rgba(0, 225, 255, 0.1), transparent);
  pointer-events: none;
}

.state-icon {
font-size: 2rem;
margin-right: 1.2rem;
background: rgba(0, 20, 40, 0.6);
width: 50px;
height: 50px;
border-radius: 50%;
display: flex;
align-items: center;
justify-content: center;
box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3), inset 0 0 15px rgba(0, 225, 255, 0.3);
border: 2px solid rgba(0, 186, 255, 0.5);
z-index: 2;
}

.state-header h5 {
margin: 0;
font-size: 1.5rem;
color: white;
font-weight: 800;
text-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
letter-spacing: 0.01em;
z-index: 2;
}

.regulation-details {
display: grid;
grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
gap: 1.5rem;
padding: 1.5rem;
}

.regulation-item {
background: rgba(0, 20, 40, 0.5);
border-radius: 1rem;
padding: 1.5rem;
box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
transition: all 0.4s cubic-bezier(0.19, 1, 0.22, 1);
border: 1px solid rgba(0, 186, 255, 0.2);
backdrop-filter: blur(2px);
-webkit-backdrop-filter: blur(2px);
}

.regulation-item:hover {
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.3), 0 0 15px rgba(0, 186, 255, 0.2);
  transform: translateY(-5px);
  border-color: rgba(0, 186, 255, 0.4);
}

.regulation-item h6 {
color: #44ccff;
font-size: 1.25rem;
margin: 0 0 1rem;
font-weight: 700;
display: flex;
align-items: center;
border-bottom: 1px solid rgba(0, 225, 255, 0.3);
padding-bottom: 0.8rem;
text-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
letter-spacing: 0.02em;
}

.requirement-icon {
  margin-right: 0.9rem;
  font-size: 1.5rem;
  filter: drop-shadow(0 2px 3px rgba(0, 0, 0, 0.4));
}

.regulation-item ul {
  margin: 0;
  padding-left: 1.8rem;
  color: rgba(255, 255, 255, 0.95);
}

.regulation-item li {
margin-bottom: 0.7rem;
line-height: 1.5;
position: relative;
padding-left: 0.5rem;
font-size: 1rem;
}

.regulation-item li::before {
  content: '';
  position: absolute;
  left: -1.2rem;
  top: 0.7rem;
  width: 8px;
  height: 8px;
  background: rgba(0, 225, 255, 0.8);
  border-radius: 50%;
  box-shadow: 0 0 8px rgba(0, 225, 255, 0.6);
}

.regulation-link {
  padding: 2rem;
  text-align: center;
  background: rgba(0, 30, 60, 0.5);
  border-top: 1px solid rgba(0, 225, 255, 0.3);
  position: relative;
  overflow: hidden;
}

.regulation-link::after {
  content: '';
  position: absolute;
  top: -10px;
  left: 0;
  width: 100%;
  height: 10px;
  box-shadow: 0 0 20px 10px rgba(0, 186, 255, 0.1);
  pointer-events: none;
}

.resource-link {
display: inline-flex;
align-items: center;
color: #44ccff;
text-decoration: none;
padding: 0.8rem 1.8rem;
border: 2px solid rgba(0, 225, 255, 0.5);
border-radius: 2rem;
transition: all 0.4s cubic-bezier(0.19, 1, 0.22, 1);
background: rgba(0, 41, 81, 0.8);
font-weight: 700;
font-size: 1rem;
letter-spacing: 0.02em;
box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
position: relative;
overflow: hidden;
}

.resource-link::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 150%;
  height: 150%;
  background: radial-gradient(circle, rgba(0,186,255,0.3) 0%, rgba(0,0,0,0) 70%);
  transform: translate(-50%, -50%) scale(0);
  opacity: 0;
  transition: transform 0.5s cubic-bezier(0.19, 1, 0.22, 1), opacity 0.5s ease;
}

.resource-link:hover {
  background: rgba(0, 81, 122, 0.9);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4), 0 0 20px rgba(0, 186, 255, 0.3);
  transform: translateY(-3px) scale(1.03);
  border-color: rgba(0, 255, 255, 0.8);
  color: #ffffff;
}

.resource-link:hover::before {
  transform: translate(-50%, -50%) scale(1);
  opacity: 1;
}

.link-icon {
  margin-right: 0.9rem;
  font-size: 1.4rem;
  filter: drop-shadow(0 2px 3px rgba(0, 0, 0, 0.4));
  position: relative;
  z-index: 2;
}

/* Mobile responsive styles */
@media (max-width: 768px) {
.safety-standards-container {
  width: 100%;
  max-width: 600px;
  padding: 0;
  margin-top: 20px;
  margin-bottom: 40px;
}

.section-top {
  padding: 1.2rem 1.2rem 0.8rem;
}

.option-toggle {
  flex-direction: row;
  align-items: center;
  gap: 0.8rem;
}

.toggle-btn {
  width: auto;
  max-width: none;
  padding: 0.6rem 1rem;
}

.location-finder {
  flex-direction: column;
  align-items: flex-start;
}

.search-container {
  width: 100%;
  margin-bottom: 1rem;
}

.location-finder {
  padding: 1.2rem;
}

.option-content {
  padding: 1.2rem;
}

.regulation-content,
.regulation-item {
  padding: 1rem;
}

.search-input {
  padding: 0.8rem 3rem 0.8rem 3rem;
  font-size: 1rem;
}

.state-header h5 {
  font-size: 1.2rem;
}

.regulation-details {
  grid-template-columns: 1fr;
  gap: 1rem;
}

.select-wrapper {
  width: 92%;
}

.state-dropdown {
  padding: 0.6rem 1.2rem;
  font-size: 1rem;
}

.select-arrow {
  right: 1.2rem;
}
}

@media (max-width: 480px) {
.safety-standards-container {
  width: 100%;
  max-width: 420px;
  padding: 0;
  margin-top: 15px;
  margin-bottom: 30px;
}

.section-top {
  padding: 1rem 1rem 0.7rem;
}

.option-toggle {
  margin-top: 0.8rem;
  gap: 0.6rem;
}

.toggle-btn {
  padding: 0.5rem 0.8rem;
  font-size: 0.9rem;
  max-width: 220px;
}

.toggle-icon {
  font-size: 1.1rem;
}

.section-subtitle {
  font-size: 1.1rem;
  margin-bottom: 0.6rem;
}

.location-finder,
.option-content {
  padding: 1rem;
}

.regulation-content,
.regulation-item {
  padding: 0.8rem;
}

.search-input {
  padding: 0.7rem 2.5rem 0.7rem 2.5rem;
  font-size: 0.9rem;
}

.search-icon {
  left: 0.8rem;
  font-size: 0.9rem;
}

.clear-button {
  right: 0.8rem;
  height: 28px;
  width: 28px;
  font-size: 0.9rem;
}

.state-header {
  padding: 0.8rem;
}

.state-icon {
  width: 40px;
  height: 40px;
  font-size: 1.5rem;
  margin-right: 0.8rem;
}

.state-header h5 {
  font-size: 1.1rem;
}

.regulation-item h6 {
  font-size: 1.1rem;
}

.regulation-item li {
  font-size: 0.9rem;
}

.resource-link {
  font-size: 0.9rem;
  padding: 0.7rem 1.5rem;
}
}

/* Dropdown styling */
.navbar-tab-dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  transform: translateY(-15px);
  background-color: rgba(0, 0, 0, 0.98);
  min-width: 320px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4), 0 0 20px rgba(0, 0, 0, 0.2);
  border-radius: 16px;
  padding: 20px;
  opacity: 0;
  visibility: hidden;
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  z-index: 1001;
  margin-top: 10px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  backdrop-filter: blur(15px);
  border: 1px solid rgba(255, 255, 255, 0.12);
  overflow: hidden;
}

.navbar-tab-dropdown:hover .dropdown-menu {
  transform: translateY(0);
  opacity: 1;
  visibility: visible;
}

.menu-section {
  margin-bottom: 10px;
  animation: fadeIn 0.5s ease forwards;
  animation-delay: 0.1s;
}

.menu-section:nth-child(3) {
  animation-delay: 0.2s;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.menu-section-header {
  font-size: 0.7rem;
  font-weight: 700;
  color: #44ccff;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  padding: 5px 0;
  margin-bottom: 10px;
  position: relative;
  display: flex;
  align-items: center;
}

.menu-section-header:after {
  content: '';
  flex-grow: 1;
  height: 1px;
  background: linear-gradient(to right, rgba(68, 204, 255, 0.3), rgba(68, 204, 255, 0));
  margin-left: 10px;
}

.menu-section-header:before {
  content: '●';
  font-size: 8px;
  margin-right: 6px;
  color: #44ccff;
}

.menu-divider {
  height: 1px;
  background: linear-gradient(to right, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
  margin: 8px 0 12px;
}

.dropdown-item {
  display: flex;
  align-items: center;
  color: white;
  text-decoration: none;
  padding: 14px 16px;
  font-size: 1.1rem;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  text-align: left;
  position: relative;
  border-radius: 12px;
  background-color: rgba(255, 255, 255, 0.12);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.25);
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.07);
  margin-bottom: 6px;
  backdrop-filter: blur(5px);
}

.dropdown-item:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
  background: linear-gradient(to bottom, #44ccff, #0077cc);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.dropdown-item:hover {
  background-color: rgba(255, 255, 255, 0.18);
  transform: translateY(-4px) scale(1.02);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
}

.dropdown-item:hover:before {
  opacity: 1;
  height: 100%;
}

.dropdown-item:active {
  transform: translateY(-2px) scale(0.98);
  transition-duration: 0.1s;
}

.highlight-item {
  background: linear-gradient(135deg, rgba(0, 123, 194, 0.35), rgba(0, 77, 128, 0.45));
  border-left: none;
  font-weight: 700;
  position: relative;
  display: flex;
  align-items: center;
  border: 1px solid rgba(68, 204, 255, 0.45);
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.35), inset 0 0 25px rgba(0, 123, 194, 0.25);
  overflow: visible;
  letter-spacing: 0.01em;
  padding-right: 32px;
  margin-bottom: 8px;
}

.highlight-item:after {
  content: '★';
  position: absolute;
  top: 50%;
  right: 12px;
  transform: translateY(-50%);
  color: #44ccff;
  font-size: 1.1rem;
  text-shadow: 0 0 10px rgba(68, 204, 255, 0.8);
  z-index: 2;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { opacity: 0.7; transform: translateY(-50%) scale(1); }
  50% { opacity: 1; transform: translateY(-50%) scale(1.1); }
  100% { opacity: 0.7; transform: translateY(-50%) scale(1); }
}

.highlight-item:before {
  opacity: 1;
  background: linear-gradient(to bottom, #44ccff, #0077cc);
  width: 6px;
}

.highlight-item:hover {
  background: linear-gradient(135deg, rgba(0, 123, 194, 0.4), rgba(0, 77, 128, 0.5));
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.25), 0 0 15px rgba(0, 123, 194, 0.3);
  border-color: rgba(68, 204, 255, 0.6);
  transform: translateY(-5px);
}

.highlight-icon {
  font-size: 1.2rem;
  margin-right: 12px;
  color: #ffffff;
  background: linear-gradient(135deg, #44ccff, #0077cc);
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  box-shadow: 0 0 15px rgba(68, 204, 255, 0.6);
  transition: all 0.3s ease;
  border: 2px solid rgba(255, 255, 255, 0.8);
}

/* Scrolled dropdown styles */
.navbar-wrapper.scrolled .dropdown-menu {
  background-color: rgba(0, 0, 0, 0.9);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4), 0 0 15px rgba(0, 0, 0, 0.2);
  backdrop-filter: blur(10px);
}

.navbar-wrapper.scrolled .menu-section-header {
  color: #44ccff;
}

.navbar-wrapper.scrolled .menu-section-header:after {
  background: linear-gradient(to right, rgba(68, 204, 255, 0.3), rgba(68, 204, 255, 0));
}

.navbar-wrapper.scrolled .menu-section-header:before {
  color: #44ccff;
}

.navbar-wrapper.scrolled .menu-divider {
  background: linear-gradient(to right, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
}

.navbar-wrapper.scrolled .dropdown-item {
  color: white;
  background-color: rgba(255, 255, 255, 0.12);
  border: 1px solid rgba(255, 255, 255, 0.07);
}

.navbar-wrapper.scrolled .dropdown-item:before {
  background: linear-gradient(to bottom, #44ccff, #0077cc);
}

.navbar-wrapper.scrolled .dropdown-item:hover {
  background-color: rgba(255, 255, 255, 0.18);
  color: white;
  transform: translateY(-3px);
  box-shadow: 0 7px 14px rgba(0, 0, 0, 0.3);
}

.navbar-wrapper.scrolled .highlight-item {
  background: linear-gradient(135deg, rgba(0, 123, 194, 0.35), rgba(0, 77, 128, 0.45));
  border: 1px solid rgba(68, 204, 255, 0.45);
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.35), inset 0 0 25px rgba(0, 123, 194, 0.25);
}

.navbar-wrapper.scrolled .highlight-item:after {
  color: #44ccff;
  text-shadow: 0 0 10px rgba(68, 204, 255, 0.8);
}

.navbar-wrapper.scrolled .highlight-item:before {
  background: linear-gradient(to bottom, #44ccff, #0077cc);
}

.navbar-wrapper.scrolled .highlight-item:hover {
  background: linear-gradient(135deg, rgba(0, 123, 194, 0.4), rgba(0, 77, 128, 0.5));
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.25), 0 0 15px rgba(0, 123, 194, 0.3);
  border-color: rgba(68, 204, 255, 0.6);
}

.navbar-wrapper.scrolled .highlight-icon {
  color: white;
  background: linear-gradient(135deg, #0277bd, #014f86);
  box-shadow: 0 0 10px rgba(1, 79, 134, 0.3);
  border: 2px solid rgba(255, 255, 255, 0.9);
}

/* Specific styles for Rip Identifier popup */
/* Default rip identifier container size for main page */
.rip-identifier-container {
  max-width: 1400px !important; /* Original width for main page */
  width: 95% !important; /* Original width for main page */
  background-color: rgba(10, 15, 25, 0.97) !important; /* Slightly different background */
  box-shadow: 
    0 30px 60px rgba(0, 0, 0, 0.6), 
    0 0 0 1px rgba(255, 255, 255, 0.15),
    0 0 30px rgba(0, 100, 180, 0.4) !important; /* Blueish glow for water theme */
}

/* Wider rip identifier container only for navbar popup */
.navbar-tab-dropdown .dropdown-menu ~ .rip-simulation-overlay .rip-identifier-container {
  max-width: 1800px !important; /* Wider container only for navbar popup */
  width: 98% !important; /* Wider container only for navbar popup */
}

.rip-identifier-container .rip-simulation-content {
  padding: 0 !important; /* Remove padding to maximize space for the content */
  background-color: transparent !important; /* Let the container background show through */
  overflow-y: auto !important; /* Ensure content is scrollable as needed */
}

.rip-identifier-container .rip-simulation-header {
  background: linear-gradient(135deg, #014871, #2a84b9) !important; /* Blueish header for water theme */
  border-bottom: 1px solid rgba(255, 255, 255, 0.2) !important;
}

/* === Ensure navbar tabs styling when scrolled === */
/* Default subtle style for all tabs when scrolled */
.navbar-wrapper.scrolled .navbar-tab {
  color: rgba(1, 59, 111, 0.7);
}
/* Highlight only the active tab */
.navbar-wrapper.scrolled .navbar-tab.active {
  color: #014f86;
  font-weight: 600;
}
/* No underlines for any tabs */
.navbar-wrapper.scrolled .navbar-tab::after,
.navbar-wrapper.scrolled .navbar-tab.active::after,
.navbar-wrapper.scrolled .navbar-tab:not(.active)::after {
  display: none;
  background-color: transparent;
  height: 0;
  width: 0;
}
</style>