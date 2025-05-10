<template>
  <div class="beach-safety-page">
    <div class="bg-image"></div>
    <div class="overlay"></div>
    
    <!-- Beach Menu Component -->
    <BeachMenu :menuOpen="menuOpen" @toggle-menu="toggleMenu" />
    
    <div class="content-wrapper">
      <div class="main-content">
        <div class="title-section">
          <h1>Understanding Australian Beach Conditions</h1>
        </div>

        <div class="content-section">
          <h2 class="section-title left">🌊 Understanding Beach Safety Challenges</h2>
          
          <div class="tabs-container">
            <div class="tab-controls">
              <button 
                v-for="tab in tabs" 
                :key="tab.id"
                @click="setActiveTab(tab.id)"
                :class="['tab-button', { active: activeTab === tab.id }]"
              >
                <span class="tab-icon">{{ tab.icon }}</span>
                <span class="tab-label">{{ tab.label }}</span>
              </button>
            </div>
            
            <div class="tab-content">
              <!-- Overview Tab -->
              <div v-show="activeTab === 'overview'" class="tab-pane">
                <!-- Key Statistic Banner -->
                <div class="key-statistic-banner">
                  <div class="statistic-icon">⚠️</div>
                  <div class="statistic-content">
                    <h2 class="statistic-headline">Immigrant children make up nearly <span class="highlight">40%</span> of all beach drowning deaths in Australia</h2>
                    <p class="statistic-subheadline">— most of these tragedies could have been prevented with proper knowledge and supervision.</p>
                  </div>
                </div>

                <!-- Enhanced Image Comparison -->
                <section class="visual-section comparison-section">
                  <h3 class="visual-section-title">Popular Asian Beaches vs. Australian Beaches</h3>
                  <div class="swipeable-comparison enhanced">
                    <div class="comparison-slider">
                      <div class="slider-handle" :style="{ left: sliderPosition + '%' }" @mousedown="startSliderDrag" @touchstart="startSliderDrag">
                        <div class="handle-line"></div>
                        <div class="handle-arrow left-arrow">◀</div>
                        <div class="handle-arrow right-arrow">▶</div>
                      </div>
                      <div class="before-image" :style="{ width: sliderPosition + '%' }">
                        <img src="./assets/asian_beach.jpg" alt="Calm beach waters">
                        <div class="image-label left">Asian Beaches</div>
                        
                        <!-- Info points for Asian Beach -->
                        <div class="info-point point-1 asian" style="top: 30%; left: 25%;">
                          <div class="info-number">1</div>
                          <div class="info-tooltip right">
                            <p>Gentle waves - safe for children</p>
                          </div>
                        </div>
                        
                        <div class="info-point point-2 asian" style="top: 60%; left: 40%;">
                          <div class="info-number">2</div>
                          <div class="info-tooltip right">
                            <p>Predictable water conditions</p>
                          </div>
                        </div>
                        
                        <div class="info-point point-3 asian" style="top: 75%; left: 70%;">
                          <div class="info-number">3</div>
                          <div class="info-tooltip left">
                            <p>Calm waters - easy to swim</p>
                          </div>
                        </div>
                      </div>
                      
                      <div class="after-image">
                        <img src="./assets/australia_beaches.avif" alt="Rough Australian beach">
                        <div class="image-label right">Australia</div>
                        
                        <!-- Info points for Australian Beach -->
                        <div class="info-point point-1 aussie" style="top: 30%; left: 30%;">
                          <div class="info-number">1</div>
                          <div class="info-tooltip right">
                            <p>Powerful waves - dangerous for inexperienced swimmers</p>
                          </div>
                        </div>
                        
                        <div class="info-point point-2 aussie" style="top: 55%; left: 60%;">
                          <div class="info-number">2</div>
                          <div class="info-tooltip right">
                            <p>Rip currents - pulls you out faster than Olympic swimmers can swim</p>
                          </div>
                        </div>
                        
                        <div class="info-point point-3 aussie" style="top: 45%; left: 80%;">
                          <div class="info-number">3</div>
                          <div class="info-tooltip left">
                            <p>Immigrants often struggle to adapt to rapidly changing conditions</p>
                          </div>
                        </div>
                      </div>
                    </div>
                    <p class="comparison-caption">
                      Australian beaches: beautiful but dangerous. <strong>50% higher</strong> drowning risk than Asian/European beaches.
                      <span class="swipe-instruction">👆 Swipe or drag to compare</span>
                    </p>
                  </div>
                </section>
              </div>
              
              <!-- Immigrant Risk Tab -->
              <div v-show="activeTab === 'immigrants'" class="tab-pane">
                <div class="immigrant-intro">
                  <h3 class="subsection-title immigrant-heading">Understanding Immigrant Vulnerability at Australian Beaches</h3>
                </div>
                
                <div class="vulnerability-sections">
                  <section class="vulnerability-section">
                    <div class="drowning-statistics">
                      <div class="chart-title main-chart-title">Drowning Risk Relative to Immigrant Population Size</div>
                      <h4 class="section-title immigrant-section-title section-subtitle">Drowning Rate by Country (per 100,000 immigrants)</h4>
                      <div class="chart-container">
                        <div class="chart-columns">
                          <div v-for="(country, index) in drowningRateData" :key="index" class="chart-column">
                            <div class="country-flag" :class="country.code"></div>
                            <div class="column-bar rate-bar" :style="{height: getRateBarHeight(country.rate)}">
                              <span class="death-count">{{ country.rate.toFixed(1) }}</span>
                            </div>
                            <div class="country-name">{{ country.name }}</div>
                          </div>
                        </div>
                      </div>
                      
                      <div class="chart-note">
                        <p>Nepal and South Korea show alarmingly high drowning rates despite smaller populations—likely due to limited exposure to ocean swimming in their home countries and significant differences in coastal conditions.</p>
                      </div>
                    </div>
                  </section>
                  </div>
              </div>
              
              <!-- Breaking the Cycle Tab -->
              <div v-show="activeTab === 'education'" class="tab-pane">
                <div class="education-intro">
                  <div class="waterwise-mission">
                    <h4>Our Mission at WaterWise Family</h4>
                    <p>At WaterWise Family, we are driven by the urgent need to protect immigrant children from the heartbreaking reality that they account for 40% of drownings on Australian beaches. We empower parents with the knowledge and confidence to navigate coastal dangers and open life-saving conversations with their children — ensuring every family can enjoy the beach safely, together.</p>
                  </div>
                </div>
              
                <div class="education-flow">
                  <div class="flow-section">
                    <h4 class="flow-title">The Challenge</h4>
                    <div class="flow-content">
                      <div class="summary-icon">⚠️</div>
                      <p>Beach safety knowledge doesn't develop automatically with time spent in Australia—even after decades of residency, the risk remains.</p>
                    </div>
                  </div>
                  
                  <div class="flow-section">
                    <h4 class="flow-title">The Ongoing Cycle of Immigrant Risk</h4>
                    <div class="timeline-compact">                      
                      <div class="timeline-card high-risk">
                        <div class="timeline-header">
                          <span class="time-period">0-5 Years</span>
                          <span class="risk-level">Highest Risk</span>
                        </div>
                        <div class="timeline-body">
                          <h5>40% of drownings</h5>
                          <ul class="timeline-points">
                            <li>No recognition of rip currents</li>
                            <li>Swimming skills unsuited to ocean</li>
                          </ul>
                        </div>
                      </div>
                      
                      <div class="timeline-card medium-risk">
                        <div class="timeline-header">
                          <span class="time-period">5-20 Years</span>
                          <span class="risk-level">Moderate Risk</span>
                        </div>
                        <div class="timeline-body">
                          <h5>Adaptation Phase</h5>
                          <ul class="timeline-points">
                            <li>Some awareness through exposure</li>
                            <li>Cultural attitudes still influence safety</li>
                          </ul>
                        </div>
                      </div>
                      
                      <div class="timeline-card persistent-risk">
                        <div class="timeline-header">
                          <span class="time-period">20+ Years</span>
                          <span class="risk-level">Persistent Risk</span>
                        </div>
                        <div class="timeline-body">
                          <h5>26% lived here 30+ years</h5>
                          <ul class="timeline-points">
                            <li>False confidence without education</li>
                            <li>Cannot pass safety knowledge to children</li>
                          </ul>
                        </div>
                      </div>
                    </div>
                  </div>
                  
                  <div class="flow-section">
                    <h4 class="flow-title">Breaking the Cycle: Our Solution</h4>
                    <div class="flow-content">
                      <div class="summary-icon">🎓</div>
                      <p>Our targeted resources equip parents with vital safety knowledge and conversation starters, breaking the cycle of drownings and building beach confidence across generations.</p>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Children's Risk Tab -->
              <div v-show="activeTab === 'children'" class="tab-pane">
                <div class="child-risk-intro">
                </div>
              
                <div class="children-risk-data">
                  <h3 class="section-title children-section-title">Natural Water Drowning Risk by Age Group</h3>
                  
                  <div class="children-chart-container">
                    <div class="age-comparison">
                      <div class="age-group high-risk">
                        <div class="age-header">
                          <h4>Children 0-4 Years</h4>
                          <span class="risk-badge very-high">VERY HIGH RISK</span>
                        </div>
                        <div class="drowning-visual">
                          <div class="statistic-number">45%</div>
                          <div class="stat-subtitle">of Child Incidents</div>
                        </div>
                        <div class="risk-factors">
                          <h5>Key Risk Factors:</h5>
                          <div class="key-risk-points">
                            <div class="risk-point">
                              <div class="risk-icon">🏊</div>
                              <div class="risk-text">Poor swimming skills</div>
                            </div>
                            <div class="risk-point">
                              <div class="risk-icon">👶</div>
                              <div class="risk-text">Mobile but unaware of dangers</div>
                            </div>
                          </div>
                        </div>
                      </div>
                      
                      <div class="age-group medium-risk">
                        <div class="age-header">
                          <h4>Children 5-14 Years</h4>
                          <span class="risk-badge high">HIGH RISK</span>
                        </div>
                        <div class="drowning-visual">
                          <div class="statistic-number">32%</div>
                          <div class="stat-subtitle">of child Incidents</div>
                        </div>
                        <div class="risk-factors">
                          <h5>Key Risk Factors:</h5>
                          <div class="key-risk-points">
                            <div class="risk-point">
                              <div class="risk-icon">💪</div>
                              <div class="risk-text">Overconfidence in swimming abilities</div>
                            </div>
                            <div class="risk-point">
                              <div class="risk-icon">🌊</div>
                              <div class="risk-text">Limited understanding of rip currents</div>
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
        
        <div class="content-section" style="margin-top: 1rem;">
          <div class="section-header left">
            <h2 class="section-title left beach">🏖️ Find the Right Beach for Your Family</h2>
            <p class="section-subtitle left">Know Before You Go</p>
            <p class="beach-intro-message">Australian beaches don't have to be a mystery – understanding their unique risks before your visit can help keep your family safe.</p>
          </div>
          
          <div class="section-body">
            <div class="feature-card">
              <div class="feature-content">
                <h3>Australian Beach Safety Comparison Tool</h3>
                
                <BeachComparisonTool />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <div class="scroll-indicator" v-if="!scrolled" @click="scrollDown">
      <span>Compare Beaches</span>
      <div class="scroll-arrow">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
      </div>
    </div>
</div>
</template>

<script>
import BeachComparisonTool from './components/BeachComparisonTool.vue'
import BeachMenu from './components/BeachMenu.vue'

export default {
name: 'BeachSafety',
components: {
  BeachComparisonTool,
  BeachMenu
},
data() {
  return {
    scrolled: false,
    menuOpen: false,
    activeCard: null,
    activeTab: 'overview',  // default active tab
    sliderPosition: 50, // for the image comparison slider
    isDragging: false,
    audioPlaying: false,
    tabs: [
      { id: 'overview', label: 'Overview', icon: '🌊' },
      { id: 'immigrants', label: 'Vulnerable Groups', icon: '👨‍👩‍👧‍👦' },
      { id: 'children', label: 'Children\'s Risk', icon: '👶' }
    ],
    drowningRateData: [
      { name: 'Nepal', rate: 15.8, code: 'flag-np' },
      { name: 'South Korea', rate: 12.6, code: 'flag-kr' },
      { name: 'New Zealand', rate: 11.2, code: 'flag-nz' },
      { name: 'UK', rate: 8.4, code: 'flag-gb' },
      { name: 'China', rate: 7.9, code: 'flag-cn' },
      { name: 'Italy', rate: 6.7, code: 'flag-it' },
      { name: 'Vietnam', rate: 5.3, code: 'flag-vn' },
      { name: 'Germany', rate: 4.8, code: 'flag-de' },
      { name: 'India', rate: 3.5, code: 'flag-in' },
      { name: 'USA', rate: 2.1, code: 'flag-us' }
    ]
  }
},
mounted() {
  // Initialize scrolled state
  this.scrolled = false;
  window.addEventListener('scroll', this.handleScroll);
  window.addEventListener('mousemove', this.handleSliderDrag);
  window.addEventListener('mouseup', this.stopSliderDrag);
  window.addEventListener('touchmove', this.handleSliderDrag);
  window.addEventListener('touchend', this.stopSliderDrag);
  
  // Set the active navigation link for this page
  this.setActiveNavLink();
},
beforeDestroy() {
  window.removeEventListener('scroll', this.handleScroll);
  window.removeEventListener('mousemove', this.handleSliderDrag);
  window.removeEventListener('mouseup', this.stopSliderDrag);
  window.removeEventListener('touchmove', this.handleSliderDrag);
  window.removeEventListener('touchend', this.stopSliderDrag);
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
  setActiveTab(tabId) {
    this.activeTab = tabId;
  },
  setActiveCard(cardId) {
    // If clicking the already active card, close it
    // Otherwise, set this card as the active one
    this.activeCard = (this.activeCard === cardId) ? null : cardId;
  },
  handleScroll() {
    // Track whether user has scrolled to the Compare Beaches section
    const featureCard = document.querySelector('.feature-card');
    
    if (featureCard) {
      const featureCardRect = featureCard.getBoundingClientRect();
      const windowHeight = window.innerHeight;
      
      // If the top of the feature card is in the viewport, mark as scrolled
      if (featureCardRect.top <= windowHeight * 0.8) {
        this.scrolled = true;
      } else {
        this.scrolled = false;
      }
    }
  },
  scrollDown() {
    // Smoothly scroll to the feature card section
    const featuresSection = document.querySelector('.feature-card');
    if (featuresSection) {
      featuresSection.scrollIntoView({ behavior: 'smooth' });
    } else {
      // Fallback - scroll down 80% of the page
      const scrollTarget = document.documentElement.scrollHeight * 0.8;
      window.scrollTo({
        top: scrollTarget,
        behavior: 'smooth'
      });
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
    
    // Add active class to beach safety links
    const desktopBeachLink = document.querySelector('.nav-link[href="/beach-safety"]');
    const mobileBeachLink = document.querySelector('.mobile-nav-link[href="/beach-safety"]');
    
    if (desktopBeachLink) desktopBeachLink.classList.add('active');
    if (mobileBeachLink) mobileBeachLink.classList.add('active');
  },
  getRateBarHeight(rate) {
    const maxHeight = 140; // Reduced maximum height for the bar
    const minRate = 0; // Minimum rate for the bar to be at full height
    const maxRate = 15; // Maximum rate for the bar to be at minimum height
    
    const barHeight = ((rate - minRate) / (maxRate - minRate)) * maxHeight;
    return barHeight + 'px';
  },
  // Image comparison slider methods
  startSliderDrag(event) {
    this.isDragging = true;
    // Prevent default behavior for touch events
    if (event.type === 'touchstart') {
      event.preventDefault();
    }
  },
  handleSliderDrag(event) {
    if (!this.isDragging) return;
    
    const sliderContainer = document.querySelector('.comparison-slider');
    if (!sliderContainer) return;
    
    const rect = sliderContainer.getBoundingClientRect();
    let clientX;
    
    // Check if it's a touch or mouse event
    if (event.type === 'touchmove') {
      clientX = event.touches[0].clientX;
    } else {
      clientX = event.clientX;
    }
    
    // Calculate percentage position
    let position = ((clientX - rect.left) / rect.width) * 100;
    
    // Constrain to 0-100%
    position = Math.max(0, Math.min(100, position));
    
    this.sliderPosition = position;
  },
  stopSliderDrag() {
    this.isDragging = false;
  },
  toggleAudio() {
    this.audioPlaying = !this.audioPlaying;
    // TODO: Implement actual audio playback logic
    if (this.audioPlaying) {
      // Play audio
      console.log('Playing audio explanation');
      // This would be where you'd trigger audio playback
    } else {
      // Stop audio
      console.log('Stopping audio explanation');
      // This would be where you'd stop audio playback
    }
  },
  navigateToSection(section) {
    console.log(`Navigating to section: ${section}`);
    // This would navigate to the corresponding section or view
    // For now, it's just a placeholder
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
  padding-top: 5rem; /* Added more padding for the fixed nav */
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

.section-title.left {
  text-align: left;
  margin-left: 0.25rem;
  font-size: clamp(1.4rem, 3vw, 1.8rem);
}

.section-text {
  font-size: 1rem;
  line-height: 1.5;
  color: rgba(255, 255, 255, 0.9);
  margin: 1rem 0;
}

/* For other sections that need centered titles */
.section-title.centered {
  text-align: center;
}

/* For the vulnerability section titles */
.vulnerability-section .section-title {
  font-size: 1.15rem;
  color: #f39c12;
  margin: 0 0 1.25rem;
  font-weight: 600;
  text-align: center;
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

.emphasis {
  font-weight: 600;
  font-size: 1.05em;
  color: #f39c12;
  padding: 0.8rem;
  border-left: 3px solid #f39c12;
  background: rgba(243, 156, 18, 0.1);
  border-radius: 0 0.5rem 0.5rem 0;
}

.image-comparison {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  margin: 1rem 0 1.5rem;
}

.comparison-image {
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
}

.comparison-image img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  display: block;
}

.image-caption {
  background: rgba(0, 0, 0, 0.6);
  color: white;
  margin: 0;
  padding: 0.5rem;
  font-size: 0.85rem;
  text-align: center;
  font-weight: 500;
}

.scroll-indicator {
  position: fixed;
  bottom: 1.25rem;
  right: 1.25rem;
  background: #f39c12;
  border-radius: 2rem;
  padding: 0.5rem 1rem;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.5rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
  z-index: 100;
  transition: all 0.3s ease;
  cursor: pointer;
  color: white;
  font-weight: 600;
  font-size: 0.9rem;
}

.scroll-indicator:hover {
  background: #e67e22;
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
}

.scroll-indicator:active {
  transform: translateY(-2px);
  background: #e67e22;
}

.scroll-arrow {
  width: 1.25rem;
  height: 1.25rem;
  display: flex;
  justify-content: center;
  align-items: center;
  animation: bounce 1.5s infinite;
}

@keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-10px);
  }
  60% {
    transform: translateY(-5px);
  }
}

.scroll-arrow svg {
  width: 100%;
  height: 100%;
}

.feature-card {
  display: flex;
  flex-direction: column;
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(243, 156, 18, 0.3);
  backdrop-filter: blur(5px);
  border-radius: 1rem;
  padding: 1.5rem 1.5rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  margin: 1.5rem auto;
  max-width: 90%;
  width: 100%;
}

.feature-card:hover {
  background: rgba(0, 0, 0, 0.5);
}

.feature-content {
  flex: 1;
  width: 100%;
}

.feature-content h3 {
  font-size: 1.8rem;
  margin-bottom: 1rem;
  color: #f39c12;
  font-weight: 700;
  text-align: center;
}

.feature-content p {
  font-size: 1.1rem;
  margin-bottom: 1.5rem;
  color: #ffffff;
  max-width: 900px;
}

.subsection-title {
  font-size: 1.25rem;
  margin: 1.5rem 0 0.75rem;
  color: #f39c12;
  font-weight: 600;
  letter-spacing: 0.01em;
}

.hazard-list {
  margin: 0.75rem 0 1.25rem 1.25rem;
  padding: 0;
  list-style-position: outside;
}

.hazard-list li {
  margin-bottom: 0.75rem;
  line-height: 1.5;
  position: relative;
  padding-left: 0.5rem;
}

.hazard-list li strong {
  color: #f39c12;
  font-weight: 600;
}

.danger-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0;
}

.danger-card {
  background: rgba(1, 54, 92, 0.7);
  border-radius: 0.75rem;
  border-left: 3px solid #f39c12;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  margin-bottom: 1rem;
}

.danger-card.active {
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
  background: rgba(1, 54, 92, 0.8);
}

.card-header {
  display: flex;
  align-items: center;
  padding: 1rem;
  position: relative;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.card-header:hover {
  background: rgba(1, 54, 92, 0.9);
}

.danger-icon {
  font-size: 1.8rem;
  margin-right: 1rem;
  color: #f39c12;
}

.card-header h4 {
  margin: 0;
  font-size: 1.2rem;
  font-weight: 600;
  color: white;
  flex: 1;
}

.expand-icon {
  font-size: 1.5rem;
  font-weight: 300;
  color: rgba(255, 255, 255, 0.7);
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-body {
  height: 0;
  overflow: hidden;
  transition: height 0.3s ease;
}

.card-body.expanded {
  height: auto;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.card-content {
  padding: 1rem;
}

.card-body p {
  margin: 0.7rem 0;
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.9);
}

.risk-note {
  background: rgba(243, 156, 18, 0.15);
  border-left: 2px solid #f39c12;
  padding: 0.7rem;
  border-radius: 0 0.3rem 0.3rem 0;
  margin-top: 0.8rem !important;
  font-size: 0.9rem !important;
}

.learn-more-link {
  display: inline-block;
  margin-top: 0.8rem;
  color: #f39c12;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.2s ease;
}

.learn-more-link:hover {
  color: #e67e22;
  text-decoration: underline;
}

/* Tab Styles */
.tabs-container {
  width: 100%;
  margin: 1rem 0;
}

.tab-controls {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-bottom: 1.5rem;
  border-bottom: 2px solid rgba(255, 255, 255, 0.2);
  padding-bottom: 1rem;
}

.tab-button {
  background: rgba(1, 54, 92, 0.4);
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 0.5rem;
  padding: 0.85rem 1.2rem;
  color: white;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex: 1;
  justify-content: center;
  outline: none;
  min-width: 120px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.tab-button.active {
  background: #f39c12;
  color: white;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
  border: 2px solid #ffcc00;
  transform: translateY(-3px);
}

.tab-button:hover:not(.active) {
  background: rgba(1, 54, 92, 0.8);
  border-color: rgba(255, 255, 255, 0.5);
  transform: translateY(-2px);
  box-shadow: 0 5px 13px rgba(0, 0, 0, 0.25);
}

.tab-icon {
  font-size: 1.2rem;
}

.tab-content {
  background: rgba(1, 54, 92, 0.3);
  border-radius: 0.75rem;
  padding: 1.5rem;
  min-height: 250px;
  border: 2px solid rgba(255, 255, 255, 0.15);
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.25);
}

.tab-pane {
  animation: fadeTab 0.3s ease-in-out;
}

@keyframes fadeTab {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Danger Introduction Styles */
.danger-intro {
  margin-bottom: 1.5rem;
  padding: 1rem;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
  border-left: 3px solid #f39c12;
}

.danger-intro p {
  margin-bottom: 1rem;
  line-height: 1.6;
}

.danger-stats {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  gap: 1rem;
  margin: 1.5rem 0;
}

.stat {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: rgba(243, 156, 18, 0.15);
  padding: 1rem;
  border-radius: 0.5rem;
  min-width: 150px;
  max-width: 250px;
  flex: 1;
}

.stat-number {
  font-size: 2rem;
  font-weight: 700;
  color: #f39c12;
  margin-bottom: 0.3rem;
}

.stat-text {
  font-size: 1rem;
  text-align: center;
  color: white;
  line-height: 1.3;
}

/* Immigrant Risk Tab Styles */
.immigrant-intro {
  margin-bottom: 1.5rem;
}

.subsection-title.immigrant-heading {
  font-size: 1.8rem;
  margin-bottom: 1.2rem;
  color: #f39c12;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.section-title.immigrant-section-title {
  font-size: 1.6rem;
  margin-bottom: 1.2rem;
  color: #ffffff;
}

.graph-transition {
  display: flex;
  align-items: center;
  margin: 1.5rem 0 1rem;
  width: 100%;
}

.transition-line {
  flex: 1;
  height: 1px;
  background: rgba(243, 156, 18, 0.3);
}

.transition-text {
  font-size: 1.3rem;
  font-weight: 600;
  color: #f39c12;
  margin: 0 1rem;
  white-space: nowrap;
}

.key-statistic {
  display: flex;
  align-items: center;
  background: rgba(231, 76, 60, 0.2);
  border-radius: 0.75rem;
  padding: 1.25rem;
  margin: 1.5rem 0;
  border-left: 4px solid #e74c3c;
}

.statistic-icon {
  font-size: 2.2rem;
  margin-right: 1rem;
}

.statistic-content {
  display: flex;
  flex-direction: column;
}

.statistic-number {
  font-size: 2.5rem;
  font-weight: 700;
  color: #e74c3c;
  line-height: 1;
  margin-bottom: 0.3rem;
}

.statistic-text {
  font-size: 1.1rem;
  color: white;
  line-height: 1.3;
}

.vulnerability-sections {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.vulnerability-section {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
  padding: 1.5rem;
}

.section-title {
  font-size: clamp(1.2rem, 2.5vw, 1.6rem);
  margin: 0 0 1rem;
  color: #ffffff;
  font-weight: 700;
  letter-spacing: 0.01em;
}

.section-title.left {
  text-align: left;
  margin-left: 0.25rem;
  font-size: clamp(1.4rem, 3vw, 1.8rem);
}

.key-finding {
  background: rgba(243, 156, 18, 0.2);
  border-left: 3px solid #f39c12;
  padding: 0.8rem 1rem;
  margin: 1rem 0;
  border-radius: 0 0.5rem 0.5rem 0;
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.finding-label {
  font-weight: 700;
  color: #f39c12;
  font-size: 1rem;
}

.finding-text {
  font-size: 1rem;
  color: white;
}

.drowning-statistics {
  margin: 2rem 0;
  padding: 1.5rem;
  background: rgba(0, 0, 0, 0.3);
  border-radius: 0.75rem;
}

.chart-title {
  font-size: 1.4rem;
  color: white;
  text-align: center;
  margin-bottom: 1rem;
  font-weight: 600;
}

.chart-title.main-chart-title {
  font-size: 1.7rem;
  color: #f39c12;
  font-weight: 700;
  margin-bottom: 0.5rem;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.section-title.immigrant-section-title.section-subtitle {
  font-size: 1.3rem;
  margin: 0 0 1.5rem;
  text-align: center;
  color: rgba(255, 255, 255, 0.9);
  font-weight: 500;
  letter-spacing: normal;
}

.chart-container {
  margin: 1rem 0;
  padding: 0.5rem 0;
  position: relative;
  overflow-x: auto;
}

.chart-container::before {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 1px;
  background: rgba(255, 255, 255, 0.2);
}

.chart-columns {
  display: flex;
  justify-content: space-around;
  height: 200px; /* Reduced from 300px */
  min-width: 700px;
  margin: 0 auto;
  align-items: flex-end;
}

.chart-column {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0 0.25rem;
  flex: 1;
  max-width: 75px;
}

.country-flag {
  width: 30px;
  height: 20px;
  margin-bottom: 0.5rem;
  background-size: cover;
  background-position: center;
  border-radius: 2px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.flag-cn { background-image: url('https://flagcdn.com/w40/cn.png'); }
.flag-gb { background-image: url('https://flagcdn.com/w40/gb.png'); }
.flag-nz { background-image: url('https://flagcdn.com/w40/nz.png'); }
.flag-in { background-image: url('https://flagcdn.com/w40/in.png'); }
.flag-vn { background-image: url('https://flagcdn.com/w40/vn.png'); }
.flag-kr { background-image: url('https://flagcdn.com/w40/kr.png'); }
.flag-it { background-image: url('https://flagcdn.com/w40/it.png'); }
.flag-us { background-image: url('https://flagcdn.com/w40/us.png'); }
.flag-de { background-image: url('https://flagcdn.com/w40/de.png'); }
.flag-np { background-image: url('https://flagcdn.com/w40/np.png'); }

.column-bar {
  width: 40px;
  background: #01365c;
  border-radius: 4px 4px 0 0;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding-top: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  position: relative;
  margin-bottom: 6px;
  transition: all 0.3s ease;
}

.column-bar:hover {
  background: #f39c12;
  transform: translateY(-5px);
}

.death-count {
  color: white;
  font-weight: 700;
  font-size: 1.1rem;
}

.country-name {
  font-size: 0.95rem;
  text-align: center;
  margin-top: 0.4rem;
  color: rgba(255, 255, 255, 0.9);
  max-width: 80px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.chart-note {
  margin-top: 1.5rem;
  padding: 1rem;
  background: rgba(243, 156, 18, 0.1);
  border-radius: 0.5rem;
  font-size: 1.1rem;
  border-left: 2px solid #f39c12;
}

.chart-note p {
  margin: 0;
  line-height: 1.5;
}

.risk-explanation {
  margin: 1.5rem 0;
}

.risk-explanation h4 {
  font-size: 1.1rem;
  margin-bottom: 1rem;
  color: #f39c12;
  font-weight: 600;
}

.risk-factors {
  padding-left: 1.2rem;
  margin-bottom: 1.5rem;
}

.risk-factors li {
  margin-bottom: 0.8rem;
  line-height: 1.5;
}

.risk-factors li strong {
  color: #f39c12;
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
  
  .section-title.beach {
    font-size: 1.4rem;
  }
  
  .section-subtitle {
    font-size: 1rem;
  }
  
  .info-card {
    padding: 1rem;
  }
  
  .info-icon {
    font-size: 1.5rem;
    min-width: 1.5rem;
  }
  
  .info-content h4 {
    font-size: 1rem;
  }
  
  .info-content p {
    font-size: 0.9rem;
  }
  
  .tool-intro {
    font-size: 1rem;
    margin: 1.25rem 0;
  }
  
  .tab-controls {
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .tab-button {
    width: 100%;
    justify-content: flex-start;
  }
  
  .danger-intro {
    padding: 0.75rem;
  }
  
  .danger-stats {
    flex-direction: column;
    gap: 0.75rem;
  }
  
  .stat {
    max-width: 100%;
    width: 100%;
    padding: 0.75rem;
  }
  
  .stat-number {
    font-size: 1.75rem;
  }
  
  .statistic-highlight {
    padding: 1rem;
    margin: 1rem 0;
  }
  
  .highlight-text {
    font-size: 1.2rem;
  }
  
  .highlight-text strong {
    font-size: 1.5rem;
  }
  
  .highlight-subtext {
    font-size: 0.9rem;
  }
  
  .chart-title {
    font-size: 1.1rem;
  }
  
  .drowning-statistics {
    padding: 1rem;
    margin: 1.5rem 0;
  }
  
  .chart-container {
    margin: 1rem 0;
  }
  
  .column-bar {
    width: 30px;
  }
  
  .country-name {
    font-size: 0.7rem;
    max-width: 60px;
  }
  
  .risk-factors li {
    margin-bottom: 0.7rem;
  }
  
  .scroll-indicator {
    bottom: 1.25rem;
    right: 1.25rem;
    padding: 0.5rem 1rem;
    font-size: 0.9rem;
  }
  
  .scroll-arrow {
    width: 1.25rem;
    height: 1.25rem;
  }
  
  .image-comparison {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  .key-finding {
    padding: 0.7rem;
  }
  
  .finding-label, .finding-text {
    font-size: 0.9rem;
  }
  
  .children-risk-box {
    padding: 1rem;
    margin: 1.25rem 0;
  }
  
  .risk-box-header {
    gap: 0.5rem;
  }
  
  .risk-icon {
    font-size: 1.3rem;
  }
  
  .risk-box-header h4 {
    font-size: 1rem;
  }
  
  .children-risk-box p {
    font-size: 0.9rem;
  }
  
  .time-stats {
    flex-direction: column;
    gap: 0.75rem;
  }
  
  .timeline-section {
    padding: 1rem;
    margin: 1.5rem 0;
  }
  
  .timeline-title {
    font-size: 1.1rem;
    margin-bottom: 1rem;
  }
  
  .timeline-container {
    margin-left: 1rem;
  }
  
  .period-years {
    font-size: 1rem;
  }
  
  .risk-level {
    font-size: 0.8rem;
  }
  
  .period-content {
    padding: 0.75rem;
  }
  
  .period-content h5 {
    font-size: 1rem;
  }
  
  .period-factors {
    font-size: 0.85rem;
    padding-left: 1rem;
  }
  
  .timeline-insight {
    padding: 0.7rem;
  }
  
  .education-gap {
    flex-direction: column;
    gap: 1rem;
  }
  
  .gap-column {
    padding: 0.75rem;
  }
  
  .gap-list {
    font-size: 0.85rem;
    padding-left: 1rem;
  }
  
  .children-risk-box {
    padding: 1rem;
    margin: 1.25rem 0;
  }
  
  .knowledge-comparison {
    margin: 1.25rem 0;
  }
  
  .header-icon {
    font-size: 1.75rem;
  }
  
  .header-cell h5 {
    font-size: 1rem;
  }
  
  .comparison-row {
    flex-direction: column;
  }
  
  .row-cell.australian {
    border-right: none;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  }
  
  .row-cell {
    padding: 0.75rem;
  }
  
  .row-icon {
    font-size: 1.25rem;
    min-width: 1.5rem;
  }
  
  .row-cell p {
    font-size: 0.9rem;
  }
  
  .education-solution {
    padding: 1rem;
  }
  
  .solution-list {
    padding-left: 1rem;
  }
  
  .solution-list li {
    font-size: 0.9rem;
    margin-bottom: 0.6rem;
  }
  
  .key-statistic {
    padding: 1rem;
  }
  
  .statistic-icon {
    font-size: 1.8rem;
  }
  
  .statistic-number {
    font-size: 2rem;
  }
  
  .statistic-text {
    font-size: 1rem;
  }
  
  .vulnerability-section {
    padding: 1.25rem;
  }
  
  .section-text {
    font-size: 0.95rem;
  }
  
  .timeline-context {
    padding: 0.75rem 1rem;
  }
  
  .timeline-context p {
    font-size: 0.95rem;
  }
  
  .timeline-periods {
    flex-direction: column;
    gap: 2.5rem;
  }
  
  .timeline-period-horizontal {
    padding: 0;
  }
  
  .timeline-track-horizontal {
    display: none;
  }
  
  .period-dot {
    left: 15px;
    top: -10px;
  }
  
  .period-content-horizontal {
    margin-top: 0;
    padding-left: 35px;
  }
  
  .period-header {
    align-items: flex-start;
    text-align: left;
  }
  
  .period-content-horizontal h5 {
    text-align: left;
  }
  
  .education-summary {
    padding: 0.75rem 1rem;
  }
  
  .summary-icon {
    font-size: 1.75rem;
  }
  
  .education-summary p {
    font-size: 0.95rem;
  }
  
  .section-title.left {
    font-size: 1.3rem;
  }
  
  .section-subtitle.left {
    font-size: 0.9rem;
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
  
  .feature-card {
    padding: 1rem;
  }
  
  .feature-content h3 {
    font-size: 1.3rem;
    margin-bottom: 0.75rem;
  }
  
  .subsection-title {
    font-size: 1.1rem;
  }
  
  .hazard-list li {
    margin-bottom: 0.6rem;
  }
}

.slide-enter-active, .slide-leave-active {
  transition: max-height 0.3s ease, opacity 0.3s ease;
  max-height: 300px;
  opacity: 1;
  overflow: hidden;
}

.slide-enter-from, .slide-leave-to {
  max-height: 0;
  opacity: 0;
}

/* Timeline Styles */
.timeline-section {
  margin: 2rem 0;
  padding: 1.5rem;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
  position: relative;
}

.timeline-title {
  font-size: 1.2rem;
  color: #f39c12;
  margin-bottom: 1.5rem;
  font-weight: 600;
  text-align: center;
}

.timeline-context {
  margin-bottom: 1.5rem;
  background: rgba(1, 54, 92, 0.3);
  border-radius: 0.5rem;
  padding: 1rem 1.25rem;
}

.timeline-context p {
  margin: 0;
  font-size: 1rem;
  line-height: 1.5;
  color: rgba(255, 255, 255, 0.9);
}

/* Horizontal Timeline Styles */
.horizontal-timeline {
  position: relative;
  padding: 1.5rem 0;
  margin: 0 auto;
}

.timeline-track-horizontal {
  position: absolute;
  top: 35px;
  left: 0;
  right: 0;
  height: 3px;
  background: rgba(255, 255, 255, 0.2);
  z-index: 1;
}

.timeline-periods {
  display: flex;
  justify-content: space-between;
  position: relative;
}

.timeline-period-horizontal {
  flex: 1;
  position: relative;
  padding: 0 0.75rem;
}

.period-dot {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  position: absolute;
  top: 28px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 2;
}

.high-risk .period-dot {
  background: #e74c3c;
  box-shadow: 0 0 0 4px rgba(231, 76, 60, 0.3);
}

.medium-risk .period-dot {
  background: #f39c12;
  box-shadow: 0 0 0 4px rgba(243, 156, 18, 0.3);
}

.persistent-risk .period-dot {
  background: #3498db;
  box-shadow: 0 0 0 4px rgba(52, 152, 219, 0.3);
}

.period-content-horizontal {
  background: rgba(1, 54, 92, 0.4);
  border-radius: 0.5rem;
  padding: 1rem;
  margin-top: 2.5rem;
  height: calc(100% - 2.5rem);
  display: flex;
  flex-direction: column;
}

.period-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 0.75rem;
  text-align: center;
}

.period-years {
  font-size: 1.1rem;
  font-weight: 700;
  color: white;
}

.risk-level {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.8);
}

.high-risk .risk-level {
  color: #e74c3c;
}

.medium-risk .risk-level {
  color: #f39c12;
}

.persistent-risk .risk-level {
  color: #3498db;
}

.period-content-horizontal h5 {
  margin: 0 0 0.5rem;
  font-size: 1.05rem;
  color: white;
  font-weight: 600;
  text-align: center;
}

.timeline-period-horizontal .period-factors {
  margin: 0;
  padding-left: 1.25rem;
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.9);
}

.timeline-period-horizontal .period-factors li {
  margin-bottom: 0.4rem;
  line-height: 1.4;
}

/* Vertical Timeline Styles (now unused) */
.timeline-container {
  position: relative;
  padding: 1rem 0;
  margin-left: 1.5rem;
}

.timeline-track {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  width: 3px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 3px;
}

.timeline-period {
  position: relative;
  padding: 0 0 2rem 2rem;
}

.timeline-period:last-child {
  padding-bottom: 0;
}

.timeline-period::before {
  content: '';
  position: absolute;
  left: -8px;
  top: 0;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  z-index: 2;
}

.period-marker {
  display: flex;
  flex-direction: column;
  margin-bottom: 0.75rem;
}

.period-content {
  background: rgba(1, 54, 92, 0.4);
  border-radius: 0.5rem;
  padding: 1rem;
}

.period-content h5 {
  margin: 0 0 0.5rem;
  font-size: 1.05rem;
  color: white;
  font-weight: 600;
}

.period-content p {
  margin: 0 0 0.75rem;
  font-size: 0.95rem;
}

.period-factors {
  margin: 0;
  padding-left: 1.25rem;
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.9);
}

.period-factors li {
  margin-bottom: 0.4rem;
  line-height: 1.4;
}

.timeline-insight {
  margin-top: 1.5rem;
  padding: 0.8rem 1rem;
  background: rgba(243, 156, 18, 0.15);
  border-radius: 0.5rem;
  border-left: 3px solid #f39c12;
}

.timeline-insight p {
  margin: 0;
  font-size: 1rem;
  line-height: 1.5;
}

/* Education Tab Styles */
.education-intro {
  margin-bottom: 1rem;
}

.education-summary {
  display: flex;
  align-items: center;
  background: rgba(46, 204, 113, 0.15);
  border-radius: 0.75rem;
  padding: 1rem 1.25rem;
  margin: 1rem 0 1.5rem;
  border-left: 3px solid #2ecc71;
}

.summary-icon {
  font-size: 2rem;
  margin-right: 1rem;
  color: #2ecc71;
}

.education-summary p {
  margin: 0;
  font-size: 1.05rem;
  line-height: 1.5;
  color: rgba(255, 255, 255, 0.95);
}

.safety-education {
  margin: 2rem 0;
}

.safety-education h4 {
  font-size: 1.1rem;
  margin-bottom: 1rem;
  color: #f39c12;
  font-weight: 600;
}

.knowledge-comparison {
  margin: 1.5rem 0;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.comparison-header {
  display: flex;
  width: 100%;
}

.header-cell {
  flex: 1;
  text-align: center;
  padding: 1rem 0.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.header-cell.australian {
  background: rgba(46, 204, 113, 0.2);
}

.header-cell.immigrant {
  background: rgba(231, 76, 60, 0.2);
}

.header-icon {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.header-cell h5 {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 600;
  color: white;
}

.comparison-rows {
  display: flex;
  flex-direction: column;
}

.comparison-row {
  display: flex;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.row-cell {
  flex: 1;
  padding: 1rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.row-cell.australian {
  background: rgba(46, 204, 113, 0.05);
  border-right: 1px solid rgba(255, 255, 255, 0.1);
}

.row-cell.immigrant {
  background: rgba(231, 76, 60, 0.05);
}

.row-icon {
  font-size: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 2rem;
}

.row-cell p {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.4;
}

.education-solution {
  background: rgba(1, 54, 92, 0.4);
  border-radius: 0.75rem;
  padding: 1.25rem;
  margin: 1.5rem 0;
  border-left: 3px solid #2ecc71;
}

.education-solution h4 {
  color: #2ecc71;
  font-size: 1.1rem;
  margin: 0 0 1rem;
  font-weight: 600;
}

.solution-list {
  padding-left: 1.25rem;
  margin: 0;
}

.solution-list li {
  margin-bottom: 0.7rem;
  line-height: 1.5;
  color: rgba(255, 255, 255, 0.95);
}

.solution-list li strong {
  color: #2ecc71;
  font-weight: 600;
}

.section-header {
  text-align: center;
  margin-bottom: 1.5rem;
}

.section-header.left {
  text-align: left;
  margin-left: 0.25rem;
}

.section-title.beach {
  font-size: clamp(1.4rem, 3vw, 1.8rem);
  margin-bottom: 0.25rem;
}

.section-subtitle {
  font-size: clamp(1rem, 2vw, 1.2rem);
  color: rgba(255, 255, 255, 0.9);
  margin: 0;
  font-weight: 500;
}

.section-subtitle.left {
  text-align: left;
  margin-left: 0.25rem;
}

.info-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.info-card {
  background: rgba(1, 54, 92, 0.6);
  border-radius: 0.75rem;
  padding: 1.25rem;
  display: flex;
  align-items: flex-start;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  border-left: 3px solid #f39c12;
}

.info-card.safety {
  border-left: 3px solid #3498db;
  background: linear-gradient(to right, rgba(52, 152, 219, 0.3), rgba(1, 54, 92, 0.6));
}

.info-card.safety .info-icon,
.info-card.safety .info-content h4 {
  color: #3498db;
}

.info-card.conditions {
  border-left: 3px solid #f39c12;
  background: linear-gradient(to right, rgba(243, 156, 18, 0.3), rgba(1, 54, 92, 0.6));
}

.info-card.conditions .info-icon,
.info-card.conditions .info-content h4 {
  color: #f39c12;
}

.info-card.patrol {
  border-left: 3px solid #2ecc71;
  background: linear-gradient(to right, rgba(46, 204, 113, 0.3), rgba(1, 54, 92, 0.6));
}

.info-card.patrol .info-icon,
.info-card.patrol .info-content h4 {
  color: #2ecc71;
}

.info-card:hover {
  transform: none;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.info-icon {
  font-size: 1.8rem;
  margin-right: 1rem;
  min-width: 1.8rem;
}

.info-content h4 {
  font-size: 1.1rem;
  margin: 0 0 0.5rem;
  font-weight: 600;
}

.info-content p {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.4;
  color: white;
}

.tool-intro {
  text-align: center;
  font-size: 1.1rem;
  margin: 1.5rem 0;
  color: rgba(255, 255, 255, 0.95);
  font-weight: 500;
}

.impact-note {
  background: linear-gradient(to right, rgba(231, 76, 60, 0.8), rgba(192, 57, 43, 0.8));
  border-left: 5px solid #e74c3c;
  padding: 1.2rem 1.5rem;
  margin: 1.5rem 0;
  border-radius: 0.75rem;
  font-weight: 600;
  font-size: 1.1rem;
  color: white;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
  position: relative;
  overflow: hidden;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
  line-height: 1.6;
}

.impact-note::before {
  content: "";
}

/* New compact timeline styles */
.timeline-section.compact {
  margin: 1rem 0;
  padding: 1rem;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
}

.timeline-compact {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-top: 1rem;
}

.timeline-card {
  flex: 1;
  min-width: 220px;
  background: rgba(1, 54, 92, 0.4);
  border-radius: 0.75rem;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
  overflow: hidden;
  transform: translateY(0);
}

.timeline-card:hover {
  transform: translateY(0);
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
}

.timeline-card.high-risk {
  border-top: none;
  background: linear-gradient(145deg, rgba(231, 76, 60, 0.85), rgba(192, 57, 43, 0.85));
}

.timeline-card.medium-risk {
  border-top: none;
  background: linear-gradient(145deg, rgba(241, 196, 15, 0.85), rgba(243, 156, 18, 0.85));
}

.timeline-card.persistent-risk {
  border-top: none;
  background: linear-gradient(145deg, rgba(52, 152, 219, 0.85), rgba(41, 128, 185, 0.85));
}

.timeline-header {
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  background: rgba(0, 0, 0, 0.15);
}

.time-period {
  font-weight: 800;
  font-size: 1.1rem;
  color: white;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
}

.high-risk .risk-level {
  color: white;
  font-weight: 700;
  background: rgba(192, 57, 43, 0.7);
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.medium-risk .risk-level {
  color: white;
  font-weight: 700;
  background: rgba(243, 156, 18, 0.7);
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.persistent-risk .risk-level {
  color: white;
  font-weight: 700;
  background: rgba(41, 128, 185, 0.7);
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem; 
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.timeline-body {
  padding: 1rem;
}

.timeline-body h5 {
  margin: 0 0 0.75rem;
  font-size: 1.2rem;
  font-weight: 700;
  color: white;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
}

.timeline-points {
  margin: 0;
  padding-left: 1.25rem;
  font-size: 1rem;
  color: rgba(255, 255, 255, 0.95);
}

.timeline-points li {
  margin-bottom: 0.5rem;
  font-weight: 500;
}

/* Knowledge gap comparison styles */
.knowledge-gap {
  margin: 1.5rem 0 0;
  padding: 1rem;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
}

.knowledge-gap h4 {
  font-size: 1.1rem;
  margin: 0 0 0.5rem;
  color: #f39c12;
}

.knowledge-gap p {
  margin-bottom: 1rem;
  font-size: 0.95rem;
}

.comparison-grid {
  border-radius: 0.5rem;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.comparison-header {
  display: flex;
  font-weight: 600;
}

.comparison-header .comparison-cell {
  padding: 0.75rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

.comparison-icon {
  font-size: 1.5rem;
}

.comparison-cell.australian {
  background: rgba(46, 204, 113, 0.2);
  flex: 1;
}

.comparison-cell.immigrant {
  background: rgba(231, 76, 60, 0.2);
  flex: 1;
}

.comparison-row {
  display: flex;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.comparison-row .comparison-cell {
  padding: 0.75rem;
  font-size: 0.9rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.comparison-row .comparison-cell.australian {
  background: rgba(46, 204, 113, 0.05);
  border-right: 1px solid rgba(255, 255, 255, 0.1);
}

.comparison-row .comparison-cell.immigrant {
  background: rgba(231, 76, 60, 0.05);
}

.cell-icon {
  font-size: 1.2rem;
}

@media (max-width: 768px) {
  .timeline-compact {
    flex-direction: column;
  }
  
  .timeline-card {
    width: 100%;
  }
  
  .comparison-row .comparison-cell {
    font-size: 0.85rem;
    padding: 0.6rem;
  }
}

@media (max-width: 480px) {
  .comparison-row {
    flex-direction: column;
  }
  
  .comparison-row .comparison-cell.australian {
    border-right: none;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  }
}

/* Styles for WaterWise mission section */
.waterwise-mission {
  margin: 0 0 1.5rem;
  padding: 1.5rem;
  background: linear-gradient(145deg, rgba(46, 204, 113, 0.7), rgba(39, 174, 96, 0.7));
  border-radius: 0.75rem;
  border-left: 4px solid #2ecc71;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
}

.waterwise-mission h4 {
  font-size: 1.3rem;
  color: white;
  margin: 0 0 1rem;
  font-weight: 700;
  letter-spacing: 0.01em;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
}

.waterwise-mission p {
  margin: 0;
  line-height: 1.6;
  font-size: 1rem;
  color: rgba(255, 255, 255, 0.95);
  font-weight: 500;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}

/* Education flow styling */
.education-flow {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-top: 0;
}

.flow-section {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
  overflow: hidden;
}

.flow-title {
  font-size: 1.1rem;
  color: #f39c12;
  margin: 0;
  padding: 0.75rem 1rem;
  background: rgba(0, 0, 0, 0.2);
  font-weight: 600;
}

.flow-content {
  padding: 1rem;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.flow-content .summary-icon {
  font-size: 1.8rem;
  color: #f39c12;
  min-width: 1.8rem;
}

.flow-content p {
  margin: 0;
  line-height: 1.5;
}

.flow-section .timeline-compact {
  padding: 1rem;
  margin: 0;
}

/* Risk cards for immigrant section */
.risk-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  margin: 1rem 0;
}

.risk-card {
  background: rgba(1, 54, 92, 0.4);
  border-radius: 0.75rem;
  padding: 1rem;
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  border-left: 3px solid #f39c12;
}

.risk-card:nth-child(1) {
  background: linear-gradient(to right, rgba(52, 152, 219, 0.3), rgba(1, 54, 92, 0.6));
  border-left: 3px solid #3498db;
}

.risk-card:nth-child(1) .risk-icon,
.risk-card:nth-child(1) .risk-content h4 {
  color: #3498db;
}

.risk-card:nth-child(2) {
  background: linear-gradient(to right, rgba(155, 89, 182, 0.3), rgba(1, 54, 92, 0.6));
  border-left: 3px solid #9b59b6;
}

.risk-card:nth-child(2) .risk-icon,
.risk-card:nth-child(2) .risk-content h4 {
  color: #9b59b6;
}

.risk-card:nth-child(3) {
  background: linear-gradient(to right, rgba(231, 76, 60, 0.3), rgba(1, 54, 92, 0.6));
  border-left: 3px solid #e74c3c;
}

.risk-card:nth-child(3) .risk-icon,
.risk-card:nth-child(3) .risk-content h4 {
  color: #e74c3c;
}

.risk-icon {
  font-size: 2rem;
  min-width: 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.risk-content h4 {
  font-size: 1.1rem;
  margin: 0 0 0.5rem;
  color: #f39c12;
  font-weight: 600;
}

.risk-content p {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.5;
  color: white;
  font-weight: 400;
}

.risk-card:nth-child(1) .risk-content p {
  color: rgba(255, 255, 255, 0.95);
}

.risk-card:nth-child(2) .risk-content p {
  color: rgba(255, 255, 255, 0.95);
}

.risk-card:nth-child(3) .risk-content p {
  color: rgba(255, 255, 255, 0.95);
}

@media (max-width: 768px) {
  .risk-cards {
    grid-template-columns: 1fr;
  }
}

/* Graph transition styling */
.graph-transition {
  display: flex;
  align-items: center;
  margin: 1.5rem 0 1rem;
  width: 100%;
}

.transition-line {
  flex: 1;
  height: 1px;
  background: rgba(243, 156, 18, 0.3);
}

.transition-text {
  font-size: 1.3rem;
  font-weight: 600;
  color: #f39c12;
  margin: 0 1rem;
  white-space: nowrap;
}

/* Visual Section Styles */
.visual-section {
  margin-bottom: 2.5rem;
  animation: fadeIn 0.8s ease-out;
}

.visual-section-title {
  font-size: 1.4rem;
  margin-bottom: 1.2rem;
  color: #f39c12;
  font-weight: 600;
  text-align: center;
}

/* 1. Image Comparison Slider */
.swipeable-comparison {
  width: 100%;
  margin: 0 auto;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
}

.comparison-slider {
  position: relative;
  width: 100%;
  height: 300px;
  overflow: hidden;
}

.before-image,
.after-image {
  position: absolute;
  top: 0;
  height: 100%;
  overflow: hidden;
}

.before-image {
  left: 0;
  z-index: 2;
}

.after-image {
  right: 0;
  width: 100%;
  z-index: 1;
}

.before-image img,
.after-image img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.slider-handle {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 40px;
  transform: translateX(-50%);
  z-index: 3;
  cursor: ew-resize;
  display: flex;
  align-items: center;
  justify-content: center;
}

.handle-line {
  height: 100%;
  width: 4px;
  background-color: #fff;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.5);
}

.handle-arrow {
  position: absolute;
  background-color: #fff;
  border-radius: 50%;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.5);
  top: 50%;
  transform: translateY(-50%);
  color: #01579b;
  font-weight: bold;
}

.left-arrow {
  left: -16px;
}

.right-arrow {
  right: -16px;
}

.image-label {
  position: absolute;
  top: 15px;
  background-color: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 5px 12px;
  border-radius: 4px;
  font-weight: 600;
  font-size: 0.9rem;
  z-index: 3;
}

.image-label.left {
  left: 15px;
}

.image-label.right {
  right: 15px;
}

.comparison-caption {
  background-color: rgba(1, 87, 155, 0.85);
  margin: 0;
  padding: 1rem;
  color: white;
  font-size: 1.1rem;
  text-align: center;
  font-weight: 500;
  line-height: 1.5;
}

.swipe-instruction {
  display: block;
  margin-top: 0.5rem;
  font-size: 1.2rem;
  font-weight: 600;
  opacity: 1;
  color: #ffcc00;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5);
  animation: pulse-instruction 2s infinite;
}

@keyframes pulse-instruction {
  0% { transform: scale(1); }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); }
}

/* 2. Stat Cards */
.stat-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.2rem;
}

.stat-card {
  background: linear-gradient(145deg, rgba(1, 87, 155, 0.8), rgba(0, 60, 113, 0.8));
  border-radius: 1rem;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s ease;
}

.stat-card:hover {
  transform: translateY(-5px);
}

.stat-icon {
  font-size: 2.5rem;
  margin-bottom: 0.75rem;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 800;
  color: #f39c12;
  margin-bottom: 0.75rem;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.stat-description {
  color: white;
  font-size: 1.1rem;
  font-weight: 500;
  line-height: 1.4;
}

/* 3. Rip Current Visual */
.rip-current-visual {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 1rem;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
}

.rip-diagram {
  position: relative;
  width: 100%;
  max-width: 600px;
  margin-bottom: 1.5rem;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.rip-diagram img {
  width: 100%;
  display: block;
}

.animated-rip {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

.water-flow {
  position: absolute;
  left: 50%;
  top: 55%;
  width: 20px;
  height: 20px;
  background: rgba(52, 152, 219, 0.5);
  border-radius: 50%;
  transform: translate(-50%, -50%);
  animation: flowOutToSea 4s infinite;
}

.delay1 {
  animation-delay: 1s;
  left: 48%;
}

.delay2 {
  animation-delay: 2s;
  left: 52%;
}

@keyframes flowOutToSea {
  0% {
    top: 70%;
    opacity: 1;
    width: 10px;
    height: 10px;
  }
  100% {
    top: 20%;
    opacity: 0;
    width: 25px;
    height: 25px;
  }
}

.audio-toggle {
  display: flex;
  align-items: center;
  background: #f39c12;
  padding: 0.75rem 1.25rem;
  border-radius: 2rem;
  cursor: pointer;
  margin-bottom: 1.5rem;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
  transition: all 0.3s ease;
}

.audio-toggle:hover {
  background: #e67e22;
  transform: translateY(-2px);
}

.toggle-icon {
  font-size: 1.5rem;
  margin-right: 0.75rem;
}

.tip-box {
  background: linear-gradient(to right, rgba(52, 152, 219, 0.7), rgba(41, 128, 185, 0.7));
  width: 100%;
  padding: 1.25rem;
  border-radius: 0.75rem;
  display: flex;
  align-items: center;
}

.tip-icon {
  font-size: 2rem;
  margin-right: 1rem;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.1); }
  100% { transform: scale(1); }
}

.tip-content {
  font-size: 1.1rem;
  line-height: 1.4;
  color: white;
}

/* 4. Navigation Cards */
.nav-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.2rem;
}

.nav-card {
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid rgba(243, 156, 18, 0.5);
  border-radius: 0.75rem;
  padding: 1.5rem;
  display: flex;
  align-items: center;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
}

.nav-card:hover {
  background: rgba(243, 156, 18, 0.3);
  transform: translateY(-5px);
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.3);
}

.nav-icon {
  font-size: 2rem;
  margin-right: 1rem;
  flex-shrink: 0;
}

.nav-title {
  font-size: 1.1rem;
  font-weight: 600;
  color: white;
  flex: 1;
}

.nav-arrow {
  font-size: 1.5rem;
  opacity: 0.7;
  transition: transform 0.3s ease;
}

.nav-card:hover .nav-arrow {
  opacity: 1;
  transform: translateX(5px);
}

/* Media Queries */
@media (max-width: 768px) {
  .visual-section-title {
    font-size: 1.3rem;
  }
  
  .comparison-slider {
    height: 250px;
  }
  
  .stat-cards, .nav-cards {
    grid-template-columns: 1fr;
  }
  
  .stat-icon, .stat-number {
    font-size: 2rem;
  }
  
  .stat-description {
    font-size: 1rem;
  }
  
  .tip-content {
    font-size: 1rem;
  }
  
  .audio-toggle {
    padding: 0.6rem 1rem;
  }
}

@media (max-width: 480px) {
  .visual-section-title {
    font-size: 1.2rem;
  }
  
  .comparison-slider {
    height: 200px;
  }
  
  .image-label {
    font-size: 0.8rem;
    padding: 4px 8px;
  }
  
  .comparison-caption {
    font-size: 0.95rem;
    padding: 0.75rem;
  }
  
  .stat-icon {
    font-size: 1.75rem;
  }
  
  .stat-number {
    font-size: 1.75rem;
  }
  
  .stat-description {
    font-size: 0.9rem;
  }
  
  .rip-current-visual {
    padding: 1rem;
  }
  
  .audio-toggle {
    padding: 0.5rem 0.75rem;
    font-size: 0.9rem;
  }
  
  .toggle-icon {
    font-size: 1.2rem;
  }
  
  .tip-box {
    padding: 1rem;
  }
  
  .tip-icon {
    font-size: 1.5rem;
  }
  
  .tip-content {
    font-size: 0.9rem;
  }
  
  .nav-card {
    padding: 1rem;
  }
  
  .nav-icon {
    font-size: 1.5rem;
  }
  
  .nav-title {
    font-size: 0.95rem;
  }
}

.comparison-section {
  margin-bottom: 3rem;
}

.swipeable-comparison.enhanced {
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
  border: 2px solid rgba(255, 255, 255, 0.2);
}

.swipeable-comparison.enhanced .comparison-slider {
  height: 350px;
}

.swipeable-comparison.enhanced .comparison-caption {
  padding: 1.25rem;
  font-size: 1.2rem;
}

.stats-section {
  margin-top: 1rem;
  padding: 1rem 1.5rem;
}

.visual-section-title.secondary-title {
  font-size: 1.2rem;
  margin-bottom: 1rem;
  opacity: 0.9;
}

.stat-cards.compact {
  gap: 0.8rem;
}

.stat-card.compact {
  padding: 1rem;
  gap: 0.3rem;
}

.stat-icon.small {
  font-size: 1.8rem;
  margin-bottom: 0.4rem;
}

.stat-number.small {
  font-size: 1.8rem;
  margin-bottom: 0.4rem;
}

.stat-description.small {
  font-size: 0.9rem;
}

@media (max-width: 768px) {
  .swipeable-comparison.enhanced .comparison-slider {
    height: 280px;
  }
  
  .swipeable-comparison.enhanced .comparison-caption {
    padding: 1rem;
    font-size: 1.1rem;
  }
  
  .stat-icon.small, .stat-number.small {
    font-size: 1.6rem;
  }
}

@media (max-width: 480px) {
  .swipeable-comparison.enhanced .comparison-slider {
    height: 230px;
  }
  
  .swipeable-comparison.enhanced .comparison-caption {
    padding: 0.8rem;
    font-size: 1rem;
  }
}

.key-statistic-banner {
  background: linear-gradient(135deg, #e74c3c, #c0392b);
  padding: 1rem;
  border-radius: 1rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
  animation: fadeUp 0.8s ease-out;
  display: flex;
  align-items: center;
  position: relative;
  overflow: hidden;
  border-left: 5px solid #f39c12;
}

.statistic-icon {
  font-size: 2.5rem;
  margin-right: 1.2rem;
  color: #fff200;
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.3));
  z-index: 1;
  flex-shrink: 0;
  animation: pulse 2s infinite;
}

.statistic-content {
  z-index: 1;
  flex: 1;
}

.statistic-headline {
  font-size: 1.3rem;
  color: white;
  margin: 0 0 0.25rem;
  font-weight: 700;
  line-height: 1.2;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  text-align: left;
}

.statistic-headline .highlight {
  color: #fff200;
  font-weight: 800;
  font-size: 1.5rem;
  display: inline-block;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
  position: relative;
}

.statistic-subheadline {
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.9);
  margin: 0;
  font-weight: 500;
  line-height: 1.3;
}

.swipeable-comparison.enhanced .comparison-slider {
  height: 400px;
}

@media (max-width: 768px) {
  .swipeable-comparison.enhanced .comparison-slider {
    height: 320px;
  }
  
  .key-statistic-banner {
    padding: 0.85rem;
    margin-bottom: 1.25rem;
  }
  
  .statistic-icon {
    font-size: 2rem;
    margin-right: 1rem;
  }
  
  .statistic-headline {
    font-size: 1.15rem;
  }
  
  .statistic-headline .highlight {
    font-size: 1.3rem;
  }
  
  .statistic-subheadline {
    font-size: 0.85rem;
  }
}

@media (max-width: 480px) {
  .swipeable-comparison.enhanced .comparison-slider {
    height: 260px;
  }
  
  .key-statistic-banner {
    padding: 0.75rem;
    margin-bottom: 1rem;
  }
  
  .statistic-icon {
    font-size: 1.75rem;
    margin-right: 0.75rem;
  }
  
  .statistic-headline {
    font-size: 1rem;
  }
  
  .statistic-headline .highlight {
    font-size: 1.1rem;
  }
  
  .statistic-subheadline {
    font-size: 0.8rem;
    line-height: 1.2;
  }
}

.key-statistic-banner::before {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background: url('./assets/ausbeachcond.avif') right center no-repeat;
  background-size: cover;
  opacity: 0.1;
  z-index: 0;
}

.statistic-headline .highlight::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: #fff200;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.info-point {
  position: absolute;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  z-index: 5;
  cursor: pointer;
  transition: all 0.3s ease;
}

.info-point.asian {
  background-color: rgba(46, 204, 113, 0.8);
  border: 2px solid white;
}

.info-point.aussie {
  background-color: rgba(231, 76, 60, 0.8);
  border: 2px solid white;
}

.info-number {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 700;
  font-size: 1rem;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
}

.info-tooltip {
  position: absolute;
  width: 200px;
  background-color: rgba(0, 0, 0, 0.8);
  border-radius: 6px;
  padding: 0.8rem;
  color: white;
  font-size: 0.85rem;
  opacity: 0;
  transition: opacity 0.3s ease;
  pointer-events: none;
  z-index: 10;
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.4);
}

.info-tooltip.left {
  right: 40px;
  top: 50%;
  transform: translateY(-50%);
}

.info-tooltip.right {
  left: 40px;
  top: 50%;
  transform: translateY(-50%);
}

.info-tooltip::after {
  content: '';
  position: absolute;
  top: 50%;
  width: 0;
  height: 0;
  border: 8px solid transparent;
  transform: translateY(-50%);
}

.info-tooltip.left::after {
  right: -16px;
  border-left-color: rgba(0, 0, 0, 0.8);
}

.info-tooltip.right::after {
  left: -16px;
  border-right-color: rgba(0, 0, 0, 0.8);
}

.info-tooltip p {
  margin: 0;
  line-height: 1.3;
  font-weight: 500;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.info-point:hover {
  transform: scale(1.15);
}

.info-point:hover .info-tooltip {
  opacity: 1;
}

@media (max-width: 768px) {
  .info-point {
    width: 25px;
    height: 25px;
  }
  
  .info-number {
    font-size: 0.9rem;
  }
  
  .info-tooltip {
    width: 160px;
    padding: 0.6rem;
    font-size: 0.8rem;
  }
}

@media (max-width: 480px) {
  .info-point {
    width: 20px;
    height: 20px;
  }
  
  .info-number {
    font-size: 0.8rem;
  }
  
  .info-tooltip {
    width: 120px;
    padding: 0.5rem;
    font-size: 0.7rem;
  }
}

.beach-intro-message {
  font-size: 1.15rem;
  line-height: 1.5;
  margin: 1rem 0;
  padding: 1rem 1.5rem;
  background: linear-gradient(to right, rgba(243, 156, 18, 0.2), rgba(1, 54, 92, 0.2));
  border-left: 4px solid #f39c12;
  border-radius: 0.5rem;
  color: #ffffff;
  font-weight: 500;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
  max-width: 90%;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

@media (max-width: 768px) {
  .beach-intro-message {
    font-size: 1.05rem;
    padding: 0.85rem 1.2rem;
    margin: 0.75rem 0;
  }
}

@media (max-width: 480px) {
  .beach-intro-message {
    font-size: 1rem;
    padding: 0.75rem 1rem;
    margin: 0.5rem 0;
  }
}

.statistics-heading {
  font-size: 1.7rem;
  font-weight: 600;
  color: #f39c12;
  margin: 1.8rem 0 1.5rem;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

/* Children's Risk Tab Styles */
.children-section-title {
  font-size: 1.6rem;
  color: #f39c12;
  margin-bottom: 1.5rem;
  text-align: center;
  font-weight: 700;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.children-chart-container {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.age-comparison {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  justify-content: center;
}

.age-group {
  flex: 1;
  min-width: 280px;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
}

.age-group.high-risk {
  background: linear-gradient(145deg, rgba(231, 76, 60, 0.9), rgba(192, 57, 43, 0.9));
}

.age-group.medium-risk {
  background: linear-gradient(145deg, rgba(243, 156, 18, 0.9), rgba(230, 126, 34, 0.9));
}

.age-header {
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: rgba(0, 0, 0, 0.2);
  flex-wrap: wrap;
  gap: 0.5rem;
}

.age-header h4 {
  font-size: 1.3rem;
  margin: 0;
  color: white;
  font-weight: 700;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
}

.risk-badge {
  padding: 0.35rem 0.75rem;
  border-radius: 2rem;
  font-size: 0.8rem;
  font-weight: 700;
  background: rgba(0, 0, 0, 0.2);
  color: white;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.risk-badge.very-high {
  background: #c0392b;
}

.risk-badge.high {
  background: #d35400;
}

.drowning-visual {
  padding: 1.5rem;
  text-align: center;
}

.statistic-number {
  font-size: 2.5rem;
  font-weight: 800;
  color: white;
  text-shadow: 0 2px 5px rgba(0, 0, 0, 0.4);
  margin-bottom: 0.5rem;
  line-height: 1.1;
}

.stat-subtitle {
  font-size: 1rem;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.9);
  margin-bottom: 1rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.stat-description {
  font-size: 1rem;
  line-height: 1.5;
  color: white;
  margin: 0 auto;
  max-width: 90%;
}

.highlight-stat {
  color: #fff200;
  font-weight: 700;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.4);
}

.drowning-icons {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  justify-content: center;
  margin-bottom: 1rem;
}

.child-icon {
  font-size: 1.5rem;
  animation: fadeInUp 0.5s ease-out;
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.more-indicator {
  color: rgba(255, 255, 255, 0.9);
  font-weight: 600;
  font-size: 0.9rem;
  margin-top: 0.5rem;
}

.risk-factors {
  padding: 0 1.5rem 1.5rem;
}

.risk-factors h5 {
  color: white;
  font-size: 1.1rem;
  margin: 0 0 0.75rem;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.risk-factors ul {
  margin: 0;
  padding-left: 1.25rem;
  color: rgba(255, 255, 255, 0.95);
}

.risk-factors li {
  margin-bottom: 0.5rem;
  line-height: 1.4;
}

.prevention-tips {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
  padding: 1.5rem;
  border-left: 4px solid #2ecc71;
}

.prevention-tips h4 {
  font-size: 1.4rem;
  color: #2ecc71;
  margin: 0 0 1.25rem;
  text-align: center;
  font-weight: 700;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.tips-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
  gap: 1.25rem;
}

.tip {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  background: rgba(0, 0, 0, 0.2);
  padding: 1.25rem;
  border-radius: 0.75rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.tip:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.tip-icon {
  font-size: 2rem;
  color: #2ecc71;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
  min-width: 2rem;
}

.tip-content h5 {
  font-size: 1.1rem;
  color: #2ecc71;
  margin: 0 0 0.75rem;
  font-weight: 700;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.tip-content p {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.5;
  color: rgba(255, 255, 255, 0.95);
}

@media (max-width: 768px) {
  .children-section-title {
    font-size: 1.4rem;
  }
  
  .age-header h4 {
    font-size: 1.2rem;
  }
  
  .statistic-number {
    font-size: 2.8rem;
  }
  
  .child-icon {
    font-size: 1.5rem;
  }
  
  .prevention-tips h4 {
    font-size: 1.3rem;
  }
  
  .tip {
    padding: 1rem;
  }
  
  .tip-icon {
    font-size: 1.75rem;
  }
  
  .tip-content h5 {
    font-size: 1rem;
  }
  
  .tip-content p {
    font-size: 0.9rem;
  }
}

@media (max-width: 480px) {
  .age-header {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .risk-badge {
    align-self: flex-start;
  }
  
  .statistic-number {
    font-size: 2.25rem;
  }
  
  .prevention-tips {
    padding: 1.25rem;
  }
  
  .prevention-tips h4 {
    font-size: 1.2rem;
  }
  
  .tip {
    flex-direction: column;
    padding: 1rem;
  }
  
  .tip-icon {
    margin-bottom: 0.5rem;
  }
}

.key-risk-points {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-top: 0.75rem;
}

.risk-point {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  background: rgba(0, 0, 0, 0.25);
  padding: 0.75rem;
  border-radius: 0.5rem;
}

.high-risk .risk-point {
  border-left: 3px solid rgba(231, 76, 60, 0.8);
}

.medium-risk .risk-point {
  border-left: 3px solid rgba(243, 156, 18, 0.8);
}

@media (max-width: 768px) {
  .risk-text {
    font-size: 1rem;
  }
  
  .risk-point {
    padding: 0.6rem;
  }
  
  .risk-icon {
    font-size: 1.3rem;
  }
}

@media (max-width: 480px) {
  .risk-text {
    font-size: 0.9rem;
  }
  
  .risk-point {
    padding: 0.5rem;
  }
}
</style> 