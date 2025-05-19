<template>
  <div class="beach-safety-page">
    <div class="bg-image"></div>
    <div class="overlay"></div>
    
    <!-- Beach Menu Component -->
    <BeachMenu :menuOpen="menuOpen" @toggle-menu="toggleMenu" />
    
    <div class="content-wrapper">
      <div class="main-content">
        <!-- Add Progress Bar Here -->
        <div class="safety-progress-nav">
          <div class="progress-bar">
            <div class="progress-step active">
              <div class="step-number">1</div>
              <div class="step-label">Picking the Right Spot</div>
            </div>
            <div class="progress-connector"></div>
            <div class="progress-step">
              <router-link to="/understanding-danger" class="step-link">
                <div class="step-number">2</div>
                <div class="step-label">Understanding Rip Currents</div>
              </router-link>
            </div>
            <div class="progress-connector"></div>
            <div class="progress-step">
              <router-link to="/spot-rip-currents" class="step-link">
                <div class="step-number">3</div>
                <div class="step-label">Avoiding Rip Currents</div>
              </router-link>
            </div>
          </div>
        </div>
        
        <div class="title-section">
          <h1>Essential Beach Safety Practices</h1>
          <div class="statistic-banner">
          </div>
        </div>

        <!-- Enhanced Golden Rules Section with Danger Zones -->
        <div class="content-section">
          <h2 class="section-title">🌊 Australian Beach Safety Guide</h2>
          
          <div class="section-body">
            <div class="intro-card">
              <p>Australian beaches are beautiful but unpredictable. These essential rules help you enjoy them safely — especially for families unfamiliar with surf conditions. Many drownings happen simply because these signs were missed.</p>
              
              <div class="key-statistic">
                <div class="statistic-icon">⚠️</div>
                <div class="statistic-text">
                  <span class="statistic-number">95%</span>
                  <span class="statistic-description">of drownings occur outside flagged swimming zones</span>
                </div>
              </div>
            </div>
            
            <div class="flags-banner-container">
              <img src="./assets/flags.jpeg" alt="Lifeguards with red and yellow flags alongside surfers at an Australian beach" class="flags-banner-image">
              <div class="banner-overlay"></div>
              <div class="banner-caption">Always Swim Between the Red and Yellow Flags</div>
              
              <!-- Interactive Hotspots -->
              <div class="interactive-hotspots">
                <div class="hotspot hotspot-1">
                  <div class="hotspot-number">1</div>
                  <div class="hotspot-content">
                    <h4>Always Swim Between the Red and Yellow Flags</h4>
                    <p>This is the safest area of the beach, actively patrolled by lifeguards.</p>
                  </div>
                </div>
                
                <div class="hotspot hotspot-2">
                  <div class="hotspot-number">2</div>
                  <div class="hotspot-content">
                    <h4>Designated Safe Swimming Zone</h4>
                    <p>Lifeguards carefully choose and set up flags in areas with safer conditions and fewer hazards.</p>
                  </div>
                </div>
                
                <div class="hotspot hotspot-4">
                  <div class="hotspot-number">3</div>
                  <div class="hotspot-content">
                    <h4>Faster Response</h4>
                    <p>Lifeguards can quickly assist if you need help</p>
                  </div>
                </div>
              </div>
            </div>
            
            <div class="safety-guide-grid">
              <!-- Danger Zone Section -->
              <div class="guide-section full-width">
                <div class="section-header">
                  <div class="section-icon danger-icon">⚠️</div>
                  <h3>Danger Zones to Avoid</h3>
                </div>
                
                <div class="flip-cards-container">
                  <!-- Rock Headlands Card -->
                  <div class="flip-card">
                    <div class="flip-card-inner">
                      <div class="flip-card-front">
                        <div class="card-image rockheads-image"></div>
                        <h4 class="card-title">Rocks & Headlands</h4>
                      </div>
                      <div class="flip-card-back">
                        <h4>Rocks & Headlands</h4>
                        <ul class="danger-points">
                          <li>Strong currents often form around rocky outcrops and headlands</li>
                          <li>Waves can suddenly wash you onto sharp surfaces causing injuries</li>
                        </ul>
                      </div>
                    </div>
                  </div>
                  
                  <!-- Strong Wave Areas Card -->
                  <div class="flip-card">
                    <div class="flip-card-inner">
                      <div class="flip-card-front">
                        <div class="card-image strong-waves-image"></div>
                        <h4 class="card-title">Strong Wave Areas</h4>
                      </div>
                      <div class="flip-card-back">
                        <h4>Strong Wave Areas</h4>
                        <ul class="danger-points">
                          <li>Large breaking waves often indicate dangerous rip currents</li>
                          <li>Powerful waves can knock you over and drag you into deeper water</li>
                        </ul>
                      </div>
                    </div>
                  </div>
                  
                  <!-- Unpatrolled Areas Card -->
                  <div class="flip-card">
                    <div class="flip-card-inner">
                      <div class="flip-card-front">
                        <div class="card-image unpatrolled-image"></div>
                        <h4 class="card-title">Unpatrolled Areas</h4>
                      </div>
                      <div class="flip-card-back">
                        <h4>Unpatrolled Areas</h4>
                        <ul class="danger-points">
                          <li>No lifeguards available to assist if you get into trouble</li>
                          <li>Hidden hazards like sudden drop-offs or submerged objects</li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            
            <div class="safety-advice">
              <div class="advice-icon">💡</div>
              <div class="advice-content">
                <h4>Beach Safety Tip</h4>
                <p>When arriving at a beach, first look for red and yellow flags, check for warning signs, and observe the water for at least 5 minutes to spot potential hazards before entering.</p>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Combined Flag Colors and When Not to Swim Section -->
        <div class="content-section">
          <h2 class="section-title">🚨 Flag Colors & What They Mean</h2>
          
          <div class="section-body">
            <div class="left-content full-width">
              <p>Beach flags and signs communicate important safety information. Knowing what they mean can save lives.</p>
              
              <div class="flip-cards-container">
                <div class="flip-card flag-card">
                  <div class="flip-card-inner">
                    <div class="flip-card-front flag-front">
                      <img src="./assets/red_yellow.jpg" alt="Red and Yellow Flag" class="real-flag-image">
                      <h4 class="card-title">Red and Yellow</h4>
                    </div>
                    <div class="flip-card-back flag-back">
                      <h4>Red and Yellow</h4>
                      <p class="flag-description">Swim between these flags. This area is patrolled by lifeguards and is the safest place to swim.</p>
                    </div>
                  </div>
                </div>
                
                <div class="flip-card flag-card">
                  <div class="flip-card-inner">
                    <div class="flip-card-front flag-front">
                      <img src="./assets/red_flag.jpg" alt="Red Flag" class="real-flag-image">
                      <h4 class="card-title">Red Flag</h4>
                    </div>
                    <div class="flip-card-back flag-back">
                      <h4>Red Flag</h4>
                      <p class="flag-description">DANGER! Beach closed. Do not enter the water under any circumstances.</p>
                    </div>
                  </div>
                </div>
                
                <div class="flip-card flag-card">
                  <div class="flip-card-inner">
                    <div class="flip-card-front flag-front">
                      <img src="./assets/yellow_flag.jpg" alt="Yellow Flag" class="real-flag-image">
                      <h4 class="card-title">Yellow Flag</h4>
                    </div>
                    <div class="flip-card-back flag-back">
                      <h4>Yellow Flag</h4>
                      <p class="flag-description">WARNING! Potentially dangerous conditions. Swim with extreme caution.</p>
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
      <div class="arrow-label">Understanding Rip Currents</div>
      <div class="arrow-icon">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M8 12h8"/><path d="m12 8 4 4-4 4"/></svg>
      </div>
    </div>
  </div>
</template>

<script>
import BeachMenu from './components/BeachMenu.vue'

export default {
  name: 'BeachSafetyPractices',
  components: {
    BeachMenu
  },
  data() {
    return {
      menuOpen: false,
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
        path: '/understanding-danger',
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

/* Practice Card Styles */
.practice-card {
  background: rgba(1, 54, 92, 0.7);
  border-radius: 0.75rem;
  padding: 1.5rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  border-left: 3px solid #f39c12;
  margin-bottom: 1.5rem;
}

.practice-header {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
}

.practice-icon {
  font-size: 2rem;
  margin-right: 1rem;
}

.practice-header h3 {
  font-size: 1.3rem;
  color: #f39c12;
  margin: 0;
  font-weight: 700;
}

.practice-points {
  list-style: none;
  padding: 0;
  margin: 0 0 1.5rem;
}

.practice-points li {
  display: flex;
  margin-bottom: 0.75rem;
  align-items: flex-start;
}

.point-marker {
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

.point-content {
  flex: 1;
}

.point-content strong {
  color: #f39c12;
  font-weight: 700;
}

.practice-fact {
  background: rgba(243, 156, 18, 0.2);
  border-radius: 0.5rem;
  padding: 1rem;
  font-style: italic;
  border-left: 3px solid #f39c12;
}

.fact-title {
  font-weight: 700;
  color: #f39c12;
  margin-right: 0.5rem;
}

/* Flags Grid Styles */
.flags-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 1rem 0;
}

.flag-card {
  background: rgba(1, 54, 92, 0.6);
  border-radius: 0.75rem;
  padding: 1.25rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
}

.flag-visual {
  height: 80px;
  border-radius: 0.3rem;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  margin-bottom: 1rem;
  position: relative;
}

.flag-stripe {
  height: 50%;
  width: 100%;
}

.red-yellow .red {
  background-color: #e74c3c;
}

.red-yellow .yellow {
  background-color: #f1c40f;
}

.red .red-full {
  background-color: #e74c3c;
  height: 100%;
}

.yellow .yellow-full {
  background-color: #f1c40f;
  height: 100%;
}

.black-white .black {
  background-color: #2c3e50;
}

.black-white .white {
  background-color: #ecf0f1;
}

.flag-info h4 {
  color: #f39c12;
  margin: 0 0 0.5rem;
  font-size: 1.1rem;
  font-weight: 600;
}

.flag-info p {
  margin: 0;
  line-height: 1.4;
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

@media (max-width: 768px) {
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
  
  .practice-card {
    padding: 1.25rem;
  }
  
  .flag-visual {
    height: 60px;
  }
  
  .checklist-number {
    width: 35px;
    height: 35px;
    font-size: 1.1rem;
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
  
  .practice-card {
    padding: 1rem;
  }
  
  .practice-header {
    flex-direction: column;
    text-align: center;
  }
  
  .practice-icon {
    margin-right: 0;
    margin-bottom: 0.5rem;
  }
  
  .checklist-item {
    padding: 1rem;
  }
  
  .checklist-number {
    width: 30px;
    height: 30px;
    font-size: 1rem;
    margin-right: 0.75rem;
  }
  
  .flag-card {
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
}

/* Next Section Arrow Styles */
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

/* Combined Section Styles */
.intro-card {
  background: rgba(1, 54, 92, 0.7);
  border-radius: 0.75rem;
  padding: 1.5rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  border-left: 3px solid #f39c12;
  margin-bottom: 1.5rem;
}

.key-statistic {
  display: flex;
  align-items: center;
  background: rgba(243, 156, 18, 0.15);
  border-radius: 0.75rem;
  padding: 0.75rem 1.25rem;
  margin-top: 1rem;
}

.statistic-icon {
  font-size: 2rem;
  margin-right: 1rem;
}

.statistic-text {
  display: flex;
  flex-direction: column;
}

.statistic-number {
  font-size: 1.6rem;
  font-weight: 700;
  color: #f39c12;
  line-height: 1.2;
}

.statistic-description {
  font-size: 1rem;
  color: rgba(255, 255, 255, 0.9);
}

.most-critical-rule {
  background: rgba(243, 156, 18, 0.2);
  border-radius: 0.75rem;
  padding: 1.25rem;
  margin-bottom: 1rem;
  border-left: 4px solid #f39c12;
}

.rule-header {
  display: flex;
  align-items: center;
  margin-bottom: 0.75rem;
}

.rule-icon {
  font-size: 2rem;
  margin-right: 1rem;
}

.rule-header h3 {
  font-size: 1.2rem;
  color: #f39c12;
  margin: 0;
  font-weight: 700;
}

.rule-reasons {
  list-style: none;
  padding: 0;
  margin: 1rem 0 0;
}

.rule-reasons li {
  display: flex;
  align-items: flex-start;
  margin-bottom: 0.5rem;
  font-size: 0.95rem;
}

.reason-marker {
  display: inline-block;
  width: 18px;
  height: 18px;
  background-color: rgba(243, 156, 18, 0.2);
  color: #f39c12;
  border-radius: 50%;
  text-align: center;
  line-height: 18px;
  margin-right: 0.75rem;
  flex-shrink: 0;
  font-weight: bold;
}

/* Split Content Layout */
.split-content {
  display: flex;
  gap: 2rem;
  margin-top: 1rem;
}

.left-content, .right-content {
  flex: 1;
}

.flags-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin: 1rem 0;
}

.flag-card {
  background: rgba(1, 54, 92, 0.6);
  border-radius: 0.75rem;
  padding: 1rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  height: 100%;
}

.flag-visual {
  height: 60px;
  border-radius: 0.3rem;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  margin-bottom: 0.75rem;
  position: relative;
}

.flag-stripe {
  height: 50%;
  width: 100%;
}

.red-yellow .red {
  background-color: #e74c3c;
}

.red-yellow .yellow {
  background-color: #f1c40f;
}

.red .red-full {
  background-color: #e74c3c;
  height: 100%;
}

.yellow .yellow-full {
  background-color: #f1c40f;
  height: 100%;
}

.black-white .black {
  background-color: #2c3e50;
}

.black-white .white {
  background-color: #ecf0f1;
}

.flag-info h4 {
  color: #f39c12;
  margin: 0 0 0.4rem;
  font-size: 1rem;
  font-weight: 600;
}

.flag-info p {
  margin: 0;
  line-height: 1.3;
  font-size: 0.9rem;
}

.context-note {
  display: flex;
  background: rgba(52, 152, 219, 0.2);
  border-radius: 0.75rem;
  padding: 1rem;
  margin-bottom: 1rem;
  border-left: 4px solid #3498db;
}

.context-icon {
  font-size: 1.5rem;
  margin-right: 0.75rem;
  color: #3498db;
  flex-shrink: 0;
}

.subsection-title {
  font-size: 1.3rem;
  color: #e74c3c;
  margin: 1rem 0 0.75rem;
  font-weight: 600;
  text-align: center;
}

.dont-swim-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin: 0.75rem 0;
}

.dont-swim-item {
  display: flex;
  align-items: center;
  background: rgba(231, 76, 60, 0.2);
  border-radius: 0.75rem;
  padding: 1rem 1.25rem;
  transition: transform 0.2s ease;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  border-left: 3px solid #e74c3c;
}

.dont-swim-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.2);
}

.dont-swim-icon {
  font-size: 1.8rem;
  margin-right: 1rem;
  flex-shrink: 0;
}

.dont-swim-text {
  font-size: 1.1rem;
  font-weight: 500;
  line-height: 1.3;
}

/* Enhanced Safety Guide Grid */
.safety-guide-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  margin: 1.5rem 0;
}

.guide-section {
  display: flex;
  flex-direction: column;
}

.section-header {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
}

.section-icon {
  font-size: 2.2rem;
  margin-right: 1rem;
  padding: 0.5rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.main-icon {
  background-color: rgba(243, 156, 18, 0.2);
  color: #f39c12;
}

.danger-icon {
  background-color: rgba(231, 76, 60, 0.2);
  color: #e74c3c;
}

.section-header h3 {
  font-size: 1.3rem;
  color: #ffffff;
  margin: 0;
  font-weight: 700;
}

.most-critical-rule {
  background: rgba(243, 156, 18, 0.2);
  border-radius: 0.75rem;
  padding: 1.25rem;
  border-left: 4px solid #f39c12;
  height: 100%;
}

.most-critical-rule h4 {
  font-size: 1.2rem;
  color: #f39c12;
  margin: 0 0 0.75rem;
  font-weight: 700;
}

.rule-reasons {
  list-style: none;
  padding: 0;
  margin: 1rem 0 0;
}

.rule-reasons li {
  display: flex;
  align-items: flex-start;
  margin-bottom: 0.5rem;
  font-size: 0.95rem;
}

.reason-marker {
  display: inline-block;
  width: 18px;
  height: 18px;
  background-color: rgba(243, 156, 18, 0.2);
  color: #f39c12;
  border-radius: 50%;
  text-align: center;
  line-height: 18px;
  margin-right: 0.75rem;
  flex-shrink: 0;
  font-weight: bold;
}

/* Danger Zones List */
.danger-zones-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  height: 100%;
}

.danger-zone-item {
  display: flex;
  align-items: center;
  background: rgba(231, 76, 60, 0.15);
  border-radius: 0.75rem;
  padding: 1rem;
  border-left: 3px solid #e74c3c;
}

.zone-icon {
  font-size: 2rem;
  margin-right: 1rem;
  flex-shrink: 0;
}

.zone-details {
  flex: 1;
}

.zone-details h4 {
  font-size: 1.1rem;
  color: #e74c3c;
  margin: 0 0 0.3rem;
  font-weight: 600;
}

.zone-details p {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.4;
}

.safety-advice {
  display: flex;
  background: rgba(46, 204, 113, 0.2);
  border-radius: 0.75rem;
  padding: 1.25rem;
  margin-top: 1.5rem;
  border-left: 4px solid #2ecc71;
}

.advice-icon {
  font-size: 2rem;
  margin-right: 1rem;
  display: flex;
  align-items: center;
  color: #2ecc71;
}

.advice-content {
  flex: 1;
}

.advice-content h4 {
  margin: 0 0 0.5rem;
  color: #2ecc71;
  font-weight: 600;
}

.advice-content p {
  margin: 0;
}

/* Responsive adjustments */
@media (max-width: 992px) {
  .safety-guide-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .danger-zones-list {
    flex-direction: row;
    flex-wrap: wrap;
  }
  
  .danger-zone-item {
    width: calc(50% - 0.75rem);
    flex-direction: column;
    align-items: flex-start;
    text-align: center;
  }
  
  .zone-icon {
    margin: 0 0 0.75rem;
    font-size: 2.5rem;
  }
  
  .split-content {
    flex-direction: column;
    gap: 1.5rem;
  }
  
  /* Keep the layout in two columns as long as possible */
  .dont-swim-grid {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 768px) {
  .section-header, .rule-header, .key-statistic, .context-note, .safety-advice {
    flex-direction: column;
    text-align: center;
  }
  
  .section-icon, .rule-icon, .statistic-icon, .context-icon, .advice-icon {
    margin-right: 0;
    margin-bottom: 0.75rem;
  }
  
  .danger-zones-list {
    flex-direction: column;
  }
  
  .danger-zone-item {
    width: 100%;
    flex-direction: row;
    align-items: center;
    text-align: left;
  }
  
  .zone-icon {
    margin: 0 1rem 0 0;
    font-size: 2rem;
  }
  
  .flags-grid {
    grid-template-columns: 1fr;
  }
  
  /* On smaller screens, stack them in a single column */
  .dont-swim-grid {
    grid-template-columns: 1fr;
  }
  
  .dont-swim-item {
    padding: 0.9rem 1.1rem;
  }
  
  .dont-swim-icon {
    font-size: 1.6rem;
  }
  
  .dont-swim-text {
    font-size: 1rem;
  }
}

@media (max-width: 480px) {
  .intro-card, .most-critical-rule, .context-note, 
  .flag-card, .safety-advice {
    padding: 0.75rem;
  }
  
  .section-header h3 {
    font-size: 1.2rem;
  }
  
  .most-critical-rule, .danger-zone-item {
    padding: 1rem;
  }
  
  .most-critical-rule h4 {
    font-size: 1.1rem;
  }
  
  .zone-details h4 {
    font-size: 1rem;
  }
  
  .zone-icon, .section-icon, .dont-swim-icon {
    font-size: 1.6rem;
  }
  
  .statistic-number {
    font-size: 1.4rem;
  }
  
  .statistic-description {
    font-size: 0.9rem;
  }
  
  .subsection-title {
    font-size: 1.2rem;
  }
  
  .dont-swim-item {
    padding: 0.8rem 1rem;
  }
  
  .dont-swim-icon {
    margin-right: 0.8rem;
  }
}

/* Add CSS for the flags image */
.flags-banner-container {
  position: relative;
  width: 100%;
  margin: 1.5rem 0 2rem;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
}

.flags-banner-image {
  width: 100%;
  height: 400px;
  display: block;
  object-fit: cover;
  object-position: center;
}

.banner-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 30%;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.7), transparent);
}

.banner-caption {
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
  .flags-banner-image {
    height: 300px;
  }
  
  .banner-caption {
    font-size: 0.9rem;
    padding: 0.75rem;
  }
}

@media (max-width: 480px) {
  .flags-banner-image {
    height: 250px;
  }
  
  .banner-caption {
    font-size: 0.8rem;
    padding: 0.5rem;
  }
}

/* Add styles for interactive hotspots */
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
  right: 25%;
}

.hotspot-2 {
  top: 50%;
  right: 20%;
}

.hotspot-4 {
  bottom: 30%;
  left: 20%;
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
  content: "Hover me!";
  position: absolute;
  bottom: -30px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.7rem;
  white-space: nowrap;
  opacity: 0.8;
  font-weight: normal;
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

@media (max-width: 768px) {
  .hotspot-number {
    width: 32px;
    height: 32px;
  }
  
  .hotspot-number::after {
    font-size: 0.65rem;
    bottom: -25px;
  }
}

@media (max-width: 480px) {
  .hotspot-number {
    width: 28px;
    height: 28px;
    font-size: 0.9rem;
  }
  
  .hotspot-number::after {
    display: none;
  }
}

.hotspot-content {
  position: absolute;
  background: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(5px);
  padding: 12px 15px;
  border-radius: 8px;
  width: 220px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.4);
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
  z-index: 6;
  left: 50%;
  transform: translateX(-50%) translateY(10px);
  bottom: 100%;
  margin-bottom: 10px;
  pointer-events: none;
  border-left: 3px solid #f39c12;
}

.hotspot:hover .hotspot-content {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
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
  border-top: 8px solid rgba(0, 0, 0, 0.8);
}

.hotspot-content h4 {
  color: #f39c12;
  margin: 0 0 5px;
  font-size: 0.9rem;
  font-weight: 600;
}

.hotspot-content p {
  margin: 0;
  font-size: 0.85rem;
  line-height: 1.3;
}

@media (max-width: 768px) {
  .hotspot-content {
    width: 180px;
    padding: 10px 12px;
  }
  
  .hotspot-number {
    width: 25px;
    height: 25px;
    font-size: 0.9rem;
  }
}

@media (max-width: 480px) {
  .hotspot-content {
    width: 150px;
  }
  
  .hotspot-number {
    width: 22px;
    height: 22px;
    font-size: 0.8rem;
  }
  
  .hotspot-content h4 {
    font-size: 0.8rem;
  }
  
  .hotspot-content p {
    font-size: 0.75rem;
  }
}

/* Add CSS for flip cards */
.full-width {
  grid-column: 1 / -1;
}

.flip-cards-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 1.5rem;
  width: 100%;
}

.flip-card {
  background-color: transparent;
  perspective: 1000px;
  height: 300px;
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 0.6s;
  transform-style: preserve-3d;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
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
  border-radius: 10px;
  overflow: hidden;
}

.flip-card-front {
  background: linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.5));
  color: white;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
}

.card-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  z-index: -1;
  transition: all 0.3s ease;
}

.flip-card:hover .card-image {
  transform: scale(1.05);
}

.rockheads-image {
  background-image: url('./assets/rockheads.jpg');
}

.strong-waves-image {
  background-image: url('./assets/strong_wave_area.jpg');
}

.unpatrolled-image {
  background-image: url('./assets/unpatrolled_area.jpg');
}

.card-title {
  width: 100%;
  text-align: center;
  background: rgba(231, 76, 60, 0.8);
  margin: 0;
  padding: 15px;
  font-size: 1.2rem;
  font-weight: 600;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.4);
}

.flip-card-back {
  background: #e74c3c;
  color: white;
  transform: rotateY(180deg);
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
}

.flip-card-back h4 {
  font-size: 1.3rem;
  margin: 0 0 1rem;
  text-align: center;
  border-bottom: 1px solid rgba(255, 255, 255, 0.3);
  padding-bottom: 0.75rem;
}

.danger-points {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 15px;
  flex: 1;
}

.danger-points li {
  position: relative;
  padding-left: 25px;
  line-height: 1.4;
  font-size: 1rem;
}

.danger-points li:before {
  content: "!";
  position: absolute;
  left: 0;
  top: 0;
  width: 18px;
  height: 18px;
  background: white;
  color: #e74c3c;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 0.8rem;
}

/* Responsive adjustments */
@media (max-width: 992px) {
  .flip-cards-container {
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  }
  
  .flip-card {
    height: 280px;
  }
}

@media (max-width: 768px) {
  .flip-cards-container {
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 15px;
  }
  
  .flip-card {
    height: 260px;
  }
  
  .flip-card-back h4 {
    font-size: 1.2rem;
    margin-bottom: 0.75rem;
  }
  
  .danger-points li {
    font-size: 0.95rem;
  }
}

@media (max-width: 480px) {
  .flip-cards-container {
    grid-template-columns: 1fr;
  }
}

/* Add additional CSS for flag flip cards */
.flag-front .flag-visual {
  height: 150px;
  margin: 30px 30px 20px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
  border-radius: 5px;
}

.flag-back {
  background: linear-gradient(135deg, #01365c, #012a47);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.flag-back h4 {
  color: #f39c12;
  border-bottom: 1px solid rgba(243, 156, 18, 0.3);
  margin-bottom: 1.5rem;
  width: 80%;
}

.flag-description {
  font-size: 1.1rem;
  line-height: 1.4;
  padding: 0 1rem;
}

.flag-card .card-title {
  background: rgba(1, 54, 92, 0.85);
}

.flag-front {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  background: rgba(255, 255, 255, 0.05);
}

@media (max-width: 768px) {
  .flag-front .flag-visual {
    height: 120px;
    margin: 20px 20px 15px;
  }
  
  .flag-description {
    font-size: 1rem;
    padding: 0 0.8rem;
  }
}

/* Add additional CSS for real flag images */
.real-flag-image {
  width: 100%;
  height: 220px;
  object-fit: cover;
  object-position: center;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}

.flag-front {
  padding: 0;
}

.flag-front .card-title {
  border-radius: 0;
  margin-top: auto;
}

@media (max-width: 768px) {
  .real-flag-image {
    height: 180px;
  }
}
</style> 