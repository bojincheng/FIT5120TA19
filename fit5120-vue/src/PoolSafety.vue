<template>
  <div class="pool-safety-page">
    <div class="bg-image"></div>
    <div class="bg-overlay"></div>
    
    <!-- Pool Menu Component -->
    <PoolMenu :menuOpen="menuOpen" @toggle-menu="toggleMenu" />
    
    <div class="content-wrapper">
      <div class="main-content">
        <div class="title-section">
          <h1>Pool Safety Basics</h1>
          <div class="statistic-banner">
          </div>
        </div>

        <!-- Tabbed Content Section -->
        <div class="content-section">
          <div class="tabs-container">
            <div class="tab-buttons">
              <button 
                class="tab-button" 
                :class="{ active: activeTab === 'overview' }"
                @click="activeTab = 'overview'"
              >
                <span class="tab-icon">📋</span>
                <span class="tab-label">Overview</span>
              </button>
            </div>
            
            <div class="tab-content">
              <!-- Overview Tab -->
              <div v-if="activeTab === 'overview'" class="tab-pane">
                <h3 class="tab-title" style="text-align: left;">Pool Safety Overview</h3>
                
                <div class="alert-card">
                  <div class="alert-icon">⚠️</div>
                  <p class="alert-text">It only takes 20 silent seconds for a toddler to drown — backyard pools are their greatest danger</p>
                </div>
                
                <div class="pool-image-container">
                  <img src="./assets/backyard_pool.jpg" alt="Backyard pool with safety fence" class="pool-safety-image">
                  <div class="image-overlay"></div>
                  
                  <!-- Interactive Hotspots -->
                  <div class="interactive-hotspots">
                    <div class="hotspot hotspot-1">
                      <div class="hotspot-number">1</div>
                      <div class="hotspot-content">
                        <h4>Backyard Pool Risk</h4>
                        <p>Over 50% of child drownings occur in backyard pools, making them the most dangerous water environment for children</p>
                    </div>
                  </div>
                  
                    <div class="hotspot hotspot-2">
                      <div class="hotspot-number">2</div>
                      <div class="hotspot-content">
                        <h4>Silent & Deceptive</h4>
                        <p>In backyard pools, drowning happens silently in just 20 seconds - often with family members nearby but unaware</p>
                    </div>
                  </div>
                  
                    <div class="hotspot hotspot-3">
                      <div class="hotspot-number">3</div>
                      <div class="hotspot-content">
                        <h4>Backyard Pool Complacency</h4>
                        <p>Backyard pools create a dangerous sense of security — families feel safe at home but brief distractions around the pool area quickly become deadly</p>
                    </div>
                  </div>
                </div>
                
                  <div class="image-caption">Hover over numbers to learn why backyard pools are so dangerous</div>
                    </div>
                    
                <p class="drowning-summary">Backyard pools are the most dangerous because they create a false sense of security where families assume they'll notice if something goes wrong — but toddlers slip beneath the water quietly, without splashing or calling out.</p>
                    </div>
                  </div>
                </div>
              </div>
      </div>
    </div>
  </div>
</template>

<script>
import PoolMenu from './components/PoolMenu.vue'

export default {
  name: 'PoolSafety',
  components: {
    PoolMenu
  },
  data() {
    return {
      menuOpen: false,
      activeTab: 'overview'
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
    }
  }
}
</script>

<style scoped>
.pool-safety-page {
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
  opacity: 0.65; /* Further reduce opacity of the original image */
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

.section-title {
  font-size: clamp(1.2rem, 2.5vw, 1.6rem);
  margin: 0 0 1rem;
  color: #ffffff;
  font-weight: 700;
  letter-spacing: 0.01em;
}

/* Tabs Styling */
.tabs-container {
  width: 100%;
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
  border-bottom-color: #ffcc00;
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

.tab-pane {
  animation: fadeIn 0.5s ease-out;
}

.tab-title {
  font-size: 1.5rem;
  color: white;
  margin-top: 0;
  margin-bottom: 1.5rem;
  font-weight: 600;
  text-align: center;
}

/* Overview Tab Styling */
.alert-card {
  background: rgba(224, 79, 79, 0.25);
  border-radius: 0.75rem;
  padding: 1rem 1.5rem;
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  border-left: 3px solid rgba(224, 79, 79, 0.7);
}

.alert-icon {
  font-size: 2rem;
  margin-right: 1rem;
}

.alert-text {
  margin: 0;
  font-size: 1.2rem;
  font-weight: 500;
  line-height: 1.4;
}

.pool-image-container {
  position: relative;
  width: 100%;
  max-width: 900px;
  margin: 2rem auto;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
}

.pool-safety-image {
  width: 100%;
  height: auto;
  display: block;
}

.image-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.2);
  pointer-events: none;
}

/* Interactive hotspots styles */
.interactive-hotspots {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

.hotspot {
  position: absolute;
  pointer-events: auto;
}

.hotspot-1 {
  top: 25%;
  left: 20%;
}

.hotspot-2 {
  top: 40%;
  right: 20%;
}

.hotspot-3 {
  bottom: 25%;
  left: 35%;
}

.hotspot-number {
  width: 36px;
  height: 36px;
  background: #ffcc00;
  color: #003d5b;
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
    box-shadow: 0 0 0 0 rgba(255, 204, 0, 0.7);
  }
  
  70% {
    transform: scale(1.1);
    box-shadow: 0 0 0 10px rgba(255, 204, 0, 0);
  }
  
  100% {
    transform: scale(1);
    box-shadow: 0 0 0 0 rgba(255, 204, 0, 0);
  }
}

.hotspot-content {
  position: absolute;
  background: rgba(0, 61, 91, 0.95);
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
  border-left: 3px solid #ffcc00;
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
  border-top: 8px solid rgba(0, 61, 91, 0.95);
}

.hotspot:hover .hotspot-number {
  transform: scale(1.2);
  background-color: #e6b800;
  border: 2px solid white;
  box-shadow: 0 4px 12px rgba(255, 204, 0, 0.6);
}

.hotspot:hover .hotspot-content {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(-5px);
}

.hotspot-content h4 {
  color: #ffcc00;
  margin: 0 0 7px;
  font-size: 1rem;
  font-weight: 600;
}

.hotspot-content p {
  margin: 0;
  font-size: 0.9rem;
  line-height: 1.4;
}

.image-caption {
  margin-top: 0.75rem;
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.8);
  text-align: center;
}

.drowning-summary {
  font-size: 1.4rem;
  line-height: 1.6;
  color: white;
  text-align: center;
  margin: 1.5rem 0;
  width: 100%;
  font-weight: 700;
  padding: 1.75rem;
  background: linear-gradient(135deg, rgba(231, 76, 60, 0.9), rgba(192, 57, 43, 0.9));
  border-radius: 0.75rem;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.35);
  border-left: 6px solid #ffcc00;
  border-right: 6px solid #ffcc00;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  position: relative;
  overflow: hidden;
  transform: translateY(0);
  transition: transform 0.3s ease;
  animation: pulse-warning 3s infinite;
}

@keyframes pulse-warning {
  0% {
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.35);
  }
  50% {
    box-shadow: 0 12px 30px rgba(231, 76, 60, 0.5);
  }
  100% {
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.35);
  }
}

/* Styles for the family image */
.image-text-layout {
  display: flex;
  flex-direction: row;
  gap: 2rem;
  margin-bottom: 2rem;
  align-items: center;
}

.family-image-container {
  flex: 1;
  max-width: 45%;
  border-radius: 1rem;
  overflow: hidden;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
  position: relative;
  cursor: pointer;
}

.family-image {
  width: 100%;
  height: auto;
  display: block;
  transition: transform 0.5s ease;
}

.family-image-container:hover .family-image {
  transform: scale(1.05);
}

.image-hover-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(231, 76, 60, 0.9);
  opacity: 0;
  transition: opacity 0.4s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.family-image-container:hover .image-hover-overlay {
  opacity: 1;
}

.hover-text {
  color: white;
    text-align: center;
  }
  
.hover-text h4 {
  font-size: 1.5rem;
  font-weight: 700;
    margin-bottom: 1rem;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.hover-text p {
  font-size: 1.1rem;
  line-height: 1.5;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
}

.hover-instruction {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  background: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 0.5rem;
  text-align: center;
  font-size: 0.9rem;
  font-weight: 500;
}

.risk-explanation {
  text-align: center;
  color: #e74c3c;
  font-weight: 600;
  font-size: 1.2rem;
  margin: 1.5rem auto 0;
  max-width: 80%;
  line-height: 1.5;
}

.emotional-message {
  text-align: center;
  color: #e74c3c;
  font-weight: 700;
  font-size: 1.3rem;
  margin: 1.5rem auto 0;
  max-width: 80%;
  line-height: 1.5;
  font-style: italic;
}

.impact-text {
  flex: 1;
}

@media (max-width: 1024px) {
  .image-text-layout {
  flex-direction: column;
    gap: 1.5rem;
  }
  
  .family-image-container {
    max-width: 100%;
    margin: 0 auto;
  }
}

/* Responsive Styles */
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
    border-left-color: #ffcc00;
    background: rgba(255, 204, 0, 0.1);
  }
  
  .alert-card {
    flex-direction: column;
    text-align: center;
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
  
  .tab-icon {
    font-size: 1.3rem;
    margin-right: 0.5rem;
  }
  
  .tab-label {
    font-size: 0.9rem;
  }
}
</style> 