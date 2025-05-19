<template>
    <div class="app-container">
      <!-- Navigation Bar -->
      <div class="navbar-wrapper">
        <nav class="navbar animate-in">
          <div class="navbar-content">
            <div class="navbar-logo animate-fade-in">
              <h1>WaterWiseFamily</h1>
            </div>
            
            <div class="navbar-tabs">
              <button 
                v-for="(mode, index) in modes" 
                :key="mode.name" 
                :class="['navbar-tab', { active: currentMode === mode.name }, 'animate-slide-in']"
                :style="{ animationDelay: (index * 0.1) + 's' }"
                @click="currentMode = mode.name"
              >
                <span class="tab-emoji">{{ mode.emoji }}</span>
                <span class="tab-text">{{ mode.name }}</span>
              </button>
            </div>
            
            <div class="navbar-spacer"></div>
          </div>
        </nav>
      </div>
  
      <!-- Search Section -->
      <div class="search-section animate-fade-up">
        <div class="search-container animate-scale-in">
          <div 
            class="search-tabs" 
            :class="{
              'tab-first-active': selectedSearchType === 'rip_identifier',
              'tab-second-active': selectedSearchType === 'search_beach',
              'tab-third-active': selectedSearchType === 'compare_beach'
            }"
            :active-tab="getActiveTabIndex()"
          >
            <button 
              v-for="(type, index) in searchTypes" 
              :key="type.value"
              :class="['search-tab', { active: selectedSearchType === type.value }, 'animate-pop-in']"
              :style="{ animationDelay: (index * 0.15 + 0.3) + 's' }"
              @click="selectedSearchType = type.value"
            >
              <span class="search-tab-emoji">{{ type.emoji }}</span>
              <span class="search-tab-text">{{ type.label }}</span>
            </button>
          </div>
          
          <div class="search-content animate-fade-in" style="animation-delay: 0.6s;">
            <!-- Search Beach -->
            <div v-if="selectedSearchType === 'search_beach'" class="search-panel animate-slide-up">
              <div class="search-panel-header">
                <h3>Find Safe Beaches</h3>
                <p>Search for beaches by name or location to view safety information</p>
              </div>
              
              <div class="input-group">
                <div class="input-with-icon">
                  <svg class="input-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <input 
                    type="text" 
                    class="search-input" 
                    placeholder="Enter beach name or location..." 
                    v-model="searchQuery"
                  />
                </div>
                <button class="search-button" @click="performSearch">
                  Search
                  <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </button>
              </div>
            </div>
            
            <!-- Compare Beach -->
            <div v-if="selectedSearchType === 'compare_beach'" class="search-panel animate-slide-up">
              <div class="search-panel-header">
                <h3>Compare Beach Safety</h3>
                <p>Compare safety features and conditions between two beaches</p>
              </div>
              
              <div class="compare-inputs">
                <div class="input-with-icon">
                  <svg class="input-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <input 
                    type="text" 
                    class="search-input" 
                    placeholder="First beach name..." 
                    v-model="firstBeach"
                  />
                </div>
                
                <div class="compare-divider">
                  <svg class="compare-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M8 7h12m0 0l-4-4m4 4l-4 4m-8 6H4m0 0l4 4m-4-4l4-4" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </div>
                
                <div class="input-with-icon">
                  <svg class="input-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <input 
                    type="text" 
                    class="search-input" 
                    placeholder="Second beach name..." 
                    v-model="secondBeach"
                  />
                </div>
              </div>
              
              <button class="compare-button" @click="compareBeaches">
                Compare Safety Features
                <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
            </div>
            
            <!-- Rip Identifier -->
            <div v-if="selectedSearchType === 'rip_identifier'" class="search-panel animate-slide-up">
              <div class="search-panel-header">
                <h3>Identify Rip Currents</h3>
                <p>Upload a beach photo to identify potential rip currents</p>
              </div>
              
              <div class="search-options">
                <button class="upload-button">
                  <svg class="upload-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M17 8l-5-5-5 5" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M12 3v12" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  Upload Beach Photo
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'WaterSafetyGuide',
    data() {
      return {
        modes: [
          { name: 'Beach', emoji: '🏖️' },
          { name: 'Pool', emoji: '🏊‍♂️' }
        ],
        currentMode: 'Beach',
        searchTypes: [
          { label: 'Rip Identifier', value: 'rip_identifier', emoji: '🌊' },
          { label: 'Search Beach', value: 'search_beach', emoji: '🏖️' },
          { label: 'Compare Beach', value: 'compare_beach', emoji: '⚖️' }
        ],
        selectedSearchType: 'rip_identifier',
        searchQuery: '',
        firstBeach: '',
        secondBeach: ''
      }
    },
    methods: {
      getModeEmoji() {
        const mode = this.modes.find(m => m.name === this.currentMode);
        return mode ? mode.emoji : '🏖️';
      },
      performSearch() {
        const searchType = this.searchTypes.find(type => type.value === this.selectedSearchType);
        console.log(`Performing ${searchType.label} search with query: ${this.searchQuery}`);
        // Implement actual search functionality here
      },
      compareBeaches() {
        console.log(`Comparing beaches: ${this.firstBeach} and ${this.secondBeach}`);
        // Implement beach comparison functionality here
      },
      getActiveTabIndex() {
        const index = this.searchTypes.findIndex(type => type.value === this.selectedSearchType);
        return index >= 0 ? index : 0;
      }
    }
  }
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
  
  /* Base Styles */
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  
  body {
    margin: 0;
    padding: 0;
  }
  
  .app-container {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #092955; /* Dark blue from the scheme for text */
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    position: relative;
    animation: fadeIn 0.3s ease forwards;
    overflow: hidden; /* Prevent image from causing scrollbars */
    padding-top: 0; /* Remove any top padding */
  }
  
  /* Full background image */
  .app-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('./assets/pexels-borja-ruiz-cereceda-3732184-12894229.jpg');
    background-size: cover;
    background-position: center;
    z-index: 0;
    opacity: 0.9;
  }
  
  /* Add a semi-transparent overlay to improve readability */
  .app-container::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to right, 
      rgba(245, 233, 201, 0.8) 0%,
      rgba(245, 233, 201, 0.5) 50%,
      rgba(245, 233, 201, 0.3) 100%);
    z-index: 1;
  }
  
  /* Navbar Styles */
  .navbar-wrapper {
    position: relative;
    width: 100%;
    overflow: visible;
    height: auto;
    background-color: transparent;
    z-index: 100;
  }
  
  .navbar {
    background: linear-gradient(to bottom, #092955, #0a3265); /* Simplified gradient for elegance */
    position: relative;
    width: 100%;
    z-index: 100;
    border-bottom: none;
    clip-path: ellipse(70% 90% at 50% 0%); /* Symmetric curve at the middle */
    padding-bottom: 2.3rem; /* Padding for the curve */
    margin-top: 0;
    padding-top: 1rem;
    overflow: visible;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15); /* Refined shadow for elegance */
  }
  
  /* Add wavy shadow effect to simulate beach waves - adjusted for symmetry */
  .navbar::before {
    content: '';
    position: absolute;
    bottom: -8px;
    left: 0;
    right: 0;
    height: 8px;
    background: repeating-linear-gradient(
      45deg,
      rgba(63, 138, 177, 0.1),
      rgba(63, 138, 177, 0.1) 5px,
      rgba(241, 184, 86, 0.07) 5px,
      rgba(241, 184, 86, 0.07) 10px
    );
    filter: blur(1.5px);
    z-index: 1;
    transform: scaleX(0.92);
    margin: 0 auto;
    border-radius: 50%;
    box-shadow: 0 2px 10px rgba(63, 138, 177, 0.15);
    animation: waveMove 8s infinite linear;
  }
  
  @keyframes waveMove {
    0% {
      background-position: 0 0;
    }
    100% {
      background-position: 50px 0;
    }
  }
  
  /* Add second wavy line for layered effect - adjusted for symmetry */
  .navbar::after {
    content: '';
    position: absolute;
    bottom: -4px;
    left: 5%;
    right: 5%;
    height: 6px;
    background: repeating-linear-gradient(
      -45deg,
      rgba(241, 184, 86, 0.1),
      rgba(241, 184, 86, 0.1) 8px,
      rgba(63, 138, 177, 0.08) 8px,
      rgba(63, 138, 177, 0.08) 16px
    );
    filter: blur(2px);
    border-radius: 50%;
    z-index: 2;
    transform: scaleX(0.95);
    box-shadow: 0 1px 8px rgba(9, 41, 85, 0.1);
    animation: waveMove 12s infinite linear reverse;
  }
  
  /* Add third subtle highlight for wave crest effect - adjusted for symmetry */
  .navbar-content::after {
    content: '';
    position: absolute;
    bottom: -15px;
    left: 15%;
    right: 15%;
    height: 1.5px;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
    filter: blur(1px);
    z-index: 3;
    animation: breathe 4s infinite ease-in-out;
  }
  
  /* Additional right-side highlight to match left side */
  .navbar-content::before {
    content: '';
    position: absolute;
    bottom: -12px;
    left: 5%;
    right: 5%;
    height: 4px;
    background: radial-gradient(
      ellipse at center,
      rgba(63, 138, 177, 0.3) 0%,
      rgba(63, 138, 177, 0.1) 50%,
      transparent 100%
    );
    border-radius: 50%;
    filter: blur(3px);
    z-index: 2;
    opacity: 0.6;
    transform: scaleX(0.9) translateY(2px);
  }
  
  @keyframes breathe {
    0%, 100% {
      opacity: 0.3;
      transform: scaleX(0.9);
    }
    50% {
      opacity: 0.6;
      transform: scaleX(1);
    }
  }
  
  .navbar-content {
    max-width: 1280px;
    margin: 0 auto;
    padding: 1rem 1.5rem 0.5rem 1rem;
    display: flex;
    align-items: flex-start;
    position: relative;
    justify-content: flex-start;
    padding-bottom: 0.8rem;
  }
  
  .navbar-logo {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    margin-left: -1rem;
    margin-top: -0.75rem;
    padding-left: 0;
    position: relative;
    z-index: 5;
    flex-shrink: 0;
  }
  
  .navbar-logo h1 {
    font-size: 1.5rem;
    font-weight: 700;
    margin: 0;
    transform: translateY(-2px) translateX(-10px);
    background: linear-gradient(90deg, #3f8ab1, #f1b856); /* Medium blue to orange gradient */
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-fill-color: transparent;
    letter-spacing: -0.01em;
    text-shadow: 0 2px 4px rgba(2, 132, 199, 0.1);
  }
  
  .navbar-tabs {
    display: flex;
    gap: 1rem;
    justify-content: center;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    z-index: 3;
    margin-left: 0;
  }
  
  .navbar-tab {
    padding: 0.65rem 1.5rem;
    border-radius: 1.75rem;
    border: 2px solid rgba(220, 238, 255, 0.4);
    background: rgba(255, 255, 255, 0.1);
    cursor: pointer;
    font-size: 1rem;
    font-weight: 600;
    color: #ffffff;
    display: flex;
    align-items: center;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.2);
    margin: 0 0.6rem;
  }
  
  .navbar-tab::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to bottom, rgba(255, 255, 255, 0.2), transparent);
    opacity: 0.5;
  }
  
  .navbar-tab:hover, .navbar-tab.active {
    color: #ffffff;
    transform: translateY(-3px);
    border-color: #eed9a5;
    background: rgba(255, 255, 255, 0.2);
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.25);
  }
  
  .navbar-tab.active {
    background: #3f8ab1;
    color: #ffffff;
    border-color: #f1b856;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.25), inset 0 -2px 0 #f1b856;
    transform: translateY(-2px);
    border-width: 2.5px;
  }
  
  .tab-emoji {
    margin-right: 0.65rem;
    font-size: 1.4rem;
    filter: drop-shadow(0 2px 2px rgba(0, 0, 0, 0.3));
  }
  
  .tab-text {
    font-weight: 700;
    letter-spacing: 0.25px;
    font-size: 1rem;
  }
  
  .navbar-spacer {
    flex: 1;
  }
  
  /* Search Section */
  .search-section {
    padding: 0;
    position: relative;
    z-index: 2;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    min-height: 80vh;
    margin-top: 0.5rem; /* Slight spacing after navbar */
  }
  
  .search-container {
    max-width: 750px;
    width: 50%; 
    margin-left: 15%;
    margin-top: -40px;
    background-color: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-radius: 1.5rem;
    box-shadow: 0 20px 40px rgba(9, 41, 85, 0.25), 0 15px 20px rgba(9, 41, 85, 0.2);
    overflow: hidden;
    border: 1px solid rgba(238, 217, 165, 0.9);
    position: relative;
    animation: slideOverlap 1.2s ease forwards;
    transform-origin: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  
  .search-container:hover {
    transform: translateY(-5px) scale(1.01);
    box-shadow: 0 25px 50px rgba(9, 41, 85, 0.3), 0 20px 25px rgba(9, 41, 85, 0.2);
  }
  
  @keyframes slideOverlap {
    0% {
      transform: translateX(-15%);
      opacity: 0.3;
    }
    60% {
      transform: translateX(-15%);
      opacity: 1;
    }
    100% {
      transform: translateX(0);
      opacity: 1;
    }
  }
  
  .search-tabs {
    display: flex;
    background: linear-gradient(to right, #225091, #2a6bc2);
    border-bottom: 3px solid #f1b856;
    position: relative;
    padding: 0;
    border-radius: 6px 6px 0 0;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(9, 41, 85, 0.25);
  }
  
  .search-tab {
    flex: 1;
    padding: 1rem 0.75rem;
    text-align: center;
    background: linear-gradient(to bottom, rgba(79, 149, 213, 0.6), rgba(59, 129, 193, 0.4));
    border: none;
    cursor: pointer;
    font-size: 0.9rem;
    font-weight: 600;
    color: #ffffff;
    transition: all 0.3s ease;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    border-right: none;
    box-shadow: inset 0 -1px 0 rgba(255, 255, 255, 0.3);
    text-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
    letter-spacing: 0.5px;
  }
  
  .search-tab::after {
    content: '';
    position: absolute;
    right: 0;
    top: 20%;
    height: 60%;
    width: 2px;
    background: linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.1));
    opacity: 0.8;
    box-shadow: 0 0 6px rgba(255, 255, 255, 0.4);
  }
  
  .search-tab:hover {
    color: #ffffff;
    background: linear-gradient(to bottom, rgba(95, 165, 229, 0.8), rgba(75, 145, 209, 0.6));
    text-shadow: 0 0 10px rgba(255, 255, 255, 0.7);
  }
  
  .search-tab.active {
    color: #092955;
    background: linear-gradient(to bottom, #f1b856, #e0c38c);
    font-weight: 700;
    box-shadow: 0 -5px 10px -2px rgba(9, 41, 85, 0.15);
    position: relative;
    border-top: 3px solid #f1b856;
    padding-top: calc(1rem - 3px);
    z-index: 3;
    text-shadow: none;
  }
  
  .search-tab:last-child::after,
  .search-tab.active::after {
    display: none;
  }
  
  .search-tab.active .search-tab-text {
    color: #092955;
    position: relative;
    display: inline-block;
    font-weight: 800;
    transform: none;
  }
  
  .search-tab.active .search-tab-text::after {
    content: '';
    position: absolute;
    bottom: -4px;
    left: 0;
    width: 100%;
    height: 2px;
    background: #3f8ab1;
    box-shadow: 0 1px 3px rgba(9, 41, 85, 0.3);
  }
  
  .search-tab.active .search-tab-emoji {
    transform: scale(1.2);
    filter: drop-shadow(0 3px 3px rgba(9, 41, 85, 0.4));
    margin-right: 0.5rem;
    font-size: 1.2rem;
  }
  
  .search-tabs::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    height: 3px;
    width: calc(100% / 3);
    background: #f1b856;
    transition: transform 0.3s ease;
    z-index: 2;
  }
  
  .search-tabs.tab-first-active::after {
    transform: translateX(0);
  }
  
  .search-tabs.tab-second-active::after {
    transform: translateX(100%);
  }
  
  .search-tabs.tab-third-active::after {
    transform: translateX(200%);
  }
  
  .search-content {
    padding: 1.5rem;
    background: rgba(255, 255, 255, 0.8);
    border-radius: 0 0 1.5rem 1.5rem;
    overflow: hidden;
  }
  
  .search-panel-header {
    margin-bottom: 1.5rem;
    text-align: center;
  }
  
  .search-panel-header h3 {
    font-size: 1.35rem;
    font-weight: 600;
    color: #092955;
    margin-bottom: 0.5rem;
    background: linear-gradient(90deg, #092955, #3f8ab1);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    text-fill-color: transparent;
  }
  
  .search-panel-header p {
    color: #3f8ab1;
    font-size: 0.9375rem;
  }
  
  .input-group {
    display: flex;
    gap: 0.75rem;
    margin-bottom: 1rem;
    background: transparent;
  }
  
  .input-with-icon {
    position: relative;
    flex: 1;
  }
  
  .input-icon {
    position: absolute;
    left: 1rem;
    top: 50%;
    transform: translateY(-50%);
    width: 1.25rem;
    height: 1.25rem;
    color: #3f8ab1;
  }
  
  .search-input {
    width: 100%;
    padding: 0.75rem 1rem 0.75rem 2.75rem;
    border: 1px solid #dceeff;
    border-radius: 0.5rem;
    font-size: 0.9375rem;
    transition: all 0.3s ease;
    background-color: rgba(255, 255, 255, 0.9);
  }
  
  .search-input:focus {
    outline: none;
    border-color: #f1b856;
    box-shadow: 0 0 0 3px rgba(241, 184, 86, 0.2);
  }
  
  .search-button {
    padding: 0 1.5rem;
    background: linear-gradient(90deg, #3f8ab1, #3d7230);
    color: white;
    border: none;
    border-radius: 0.5rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    box-shadow: 0 4px 6px rgba(9, 41, 85, 0.2);
  }
  
  .search-button:hover {
    background: linear-gradient(90deg, #092955, #3f8ab1);
    transform: translateY(-2px);
    box-shadow: 0 6px 10px rgba(9, 41, 85, 0.3);
  }
  
  .search-icon {
    width: 1.25rem;
    height: 1.25rem;
  }
  
  .search-options {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  
  .upload-button {
    padding: 1.8rem;
    border: 2px dashed #eed9a5;
    border-radius: 0.75rem;
    background: linear-gradient(135deg, rgba(220, 238, 255, 0.2) 0%, rgba(238, 217, 165, 0.2) 100%);
    color: #3f8ab1;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.75rem;
  }
  
  .upload-button:hover {
    border-color: #f1b856;
    color: #092955;
    transform: translateY(-3px);
    box-shadow: 0 8px 15px rgba(9, 41, 85, 0.15);
  }
  
  .upload-icon {
    width: 2.5rem;
    height: 2.5rem;
    color: #f1b856;
    filter: drop-shadow(0 2px 3px rgba(9, 41, 85, 0.2));
  }
  
  .or-divider {
    display: flex;
    align-items: center;
    text-align: center;
    color: #94a3b8;
    font-size: 0.875rem;
    margin: 0.5rem 0;
  }
  
  .or-divider::before,
  .or-divider::after {
    content: '';
    flex: 1;
    border-bottom: 1px solid #e2e8f0;
  }
  
  .or-divider::before {
    margin-right: 1rem;
  }
  
  .or-divider::after {
    margin-left: 1rem;
  }
  
  .description-input {
    width: 100%;
    padding: 0.75rem 1rem;
    border: 1px solid #e2e8f0;
    border-radius: 0.5rem;
    font-size: 0.9375rem;
    min-height: 100px;
    resize: vertical;
    font-family: inherit;
  }
  
  .description-input:focus {
    outline: none;
    border-color: #0ea5e9;
    box-shadow: 0 0 0 3px rgba(14, 165, 233, 0.1);
  }
  
  .compare-inputs {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1.5rem;
  }
  
  .compare-divider {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 3rem;
    height: 3rem;
    background: linear-gradient(135deg, #eed9a5, #f1b856);
    border-radius: 50%;
    flex-shrink: 0;
    box-shadow: 0 4px 6px rgba(9, 41, 85, 0.15);
  }
  
  .compare-icon {
    width: 1.5rem;
    height: 1.5rem;
    color: #ffffff;
  }
  
  .compare-button {
    width: 100%;
    padding: 0.75rem 1.5rem;
    background: linear-gradient(90deg, #3f8ab1, #3d7230);
    color: white;
    border: none;
    border-radius: 0.5rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    box-shadow: 0 4px 6px rgba(9, 41, 85, 0.2);
  }
  
  .compare-button:hover {
    background: linear-gradient(90deg, #092955, #3f8ab1);
    transform: translateY(-2px);
    box-shadow: 0 6px 10px rgba(9, 41, 85, 0.3);
  }
  
  /* Safety Section - Completely Removed */
  
  /* Responsive Styles */
  @media (max-width: 1400px) {
    .search-container {
      width: 55%;
      margin-left: 13%;
      margin-top: -30px;
    }
  }
  
  @media (max-width: 1200px) {
    .search-container {
      width: 60%;
      margin-left: 10%;
      margin-top: -20px;
    }
    
    .app-container::after {
      transform: translateX(-10%) translateY(60px);
    }
  }
  
  @media (max-width: 992px) {
    .search-container {
      width: 70%;
      margin-left: 8%;
      margin-top: 0;
    }
    
    .app-container::after {
      transform: translateX(-5%) translateY(50px);
    }
  }
  
  @media (max-width: 768px) {
    .search-section {
      justify-content: center;
      min-height: auto;
      padding: 2rem 1rem;
    }
    
    .search-container {
      width: 100%;
      margin-left: 0;
      margin-top: 0;
      animation: fadeIn 1.2s ease forwards;
    }
    
    .navbar {
      clip-path: ellipse(90% 95% at 50% 0%); /* Adjusted for mobile, deeper in middle */
      padding-bottom: 2.5rem;
    }
    
    .navbar-content {
      flex-direction: column;
      gap: 1rem;
      padding: 1rem;
      position: relative;
    }
    
    .navbar-logo {
      margin-left: 0;
      transform: none;
      justify-content: center;
    }
    
    .navbar-tabs {
      position: static;
      transform: none;
      margin-top: 0.5rem;
    }
    
    .tab-text {
      display: none;
    }
    
    .navbar-tab {
      padding: 0.7rem 1rem;
      flex: 1;
      justify-content: center;
    }
    
    .tab-emoji {
      margin-right: 0.5rem;
      font-size: 1.6rem;
    }
    
    .search-tabs {
      flex-direction: column;
    }
    
    .search-tab {
      border-bottom: 1px solid #e2e8f0;
    }
    
    .search-tab.active::after {
      display: none;
    }
    
    .input-group {
      flex-direction: column;
    }
    
    .compare-inputs {
      flex-direction: column;
    }
    
    .compare-divider {
      margin: 1rem 0;
    }
    
    /* Adjust wave effects for mobile */
    .navbar::before,
    .navbar::after,
    .navbar-content::after {
      transform: scaleX(1);
      left: 0;
      right: 0;
    }
  }
  
  @media (max-width: 480px) {
    .search-tab-text {
      display: none;
    }
    
    .search-tab-emoji {
      margin-right: 0;
      font-size: 1.5rem;
    }
    
    .safety-cards-container {
      grid-template-columns: 1fr;
    }
    
    .action-text {
      display: none;
    }
    
    .action-button {
      padding: 0.5rem;
    }
    
    .action-icon {
      margin-right: 0;
    }
  }
  
  .search-panel {
    padding: 1.25rem;
    background: rgba(255, 255, 255, 0.9);
    border-radius: 0.75rem;
    margin-top: 0.5rem;
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    box-shadow: 0 4px 12px rgba(9, 41, 85, 0.1);
  }
  
  /* Animation Classes */
  .animate-fade-in {
    animation: fadeIn 0.8s ease forwards;
    opacity: 0;
  }
  
  .animate-in {
    animation: fadeInDown 0.6s ease forwards;
    opacity: 0;
  }
  
  .animate-slide-in {
    animation: slideInRight 0.5s ease forwards;
    opacity: 0;
    transform: translateX(-20px);
  }
  
  .animate-pop-in {
    animation: popIn 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
    opacity: 0;
    transform: scale(0.8);
  }
  
  .animate-fade-up {
    animation: fadeInUp 0.7s ease forwards;
    opacity: 0;
  }
  
  .animate-scale-in {
    animation: scaleIn 0.6s ease forwards;
    opacity: 0;
    transform: scale(0.95);
  }
  
  .animate-slide-up {
    animation: slideInUp 0.5s ease forwards;
    opacity: 0;
    transform: translateY(20px);
  }
  
  /* Animation Keyframes */
  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }
  
  @keyframes fadeInDown {
    from { 
      opacity: 0;
      transform: translateY(-20px);
    }
    to { 
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  @keyframes fadeInUp {
    from { 
      opacity: 0;
      transform: translateY(20px);
    }
    to { 
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  @keyframes slideInRight {
    from { 
      opacity: 0;
      transform: translateX(-20px);
    }
    to { 
      opacity: 1;
      transform: translateX(0);
    }
  }
  
  @keyframes popIn {
    from { 
      opacity: 0;
      transform: scale(0.8);
    }
    to { 
      opacity: 1;
      transform: scale(1);
    }
  }
  
  @keyframes scaleIn {
    from { 
      opacity: 0;
      transform: scale(0.95);
    }
    to { 
      opacity: 1;
      transform: scale(1);
    }
  }
  
  @keyframes slideInUp {
    from { 
      opacity: 0;
      transform: translateY(20px);
    }
    to { 
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  /* Add arrow indicator pointing down from active tab */
  .search-tab.active::before {
    content: '';
    position: absolute;
    bottom: -8px;
    left: 50%;
    transform: translateX(-50%);
    width: 14px;
    height: 14px;
    background: #e0c38c;
    border: 2px solid #f1b856;
    border-top: none;
    border-left: none;
    transform-origin: center;
    transform: translateX(-50%) rotate(45deg);
    z-index: 4;
    box-shadow: 2px 2px 0 #e0c38c;
  }
  
  .search-tab-text {
    position: relative;
    z-index: 2;
    text-transform: uppercase;
    font-size: 0.8rem;
  }
  
  .search-tab:hover .search-tab-text {
    transform: translateY(-2px);
    transition: transform 0.3s ease;
  }
  
  .search-tab-emoji {
    margin-right: 0.5rem;
    font-size: 1.2rem;
    filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.6));
  }
  </style>