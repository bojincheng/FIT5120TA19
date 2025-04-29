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
            <div class="statistic-banner">
              <h2 class="headline">Immigrant children make up nearly <span class="highlight">40%</span> of all beach drowning deaths in Australia</h2>
              <p class="subheadline">— most of these tragedies could have been prevented with proper knowledge and supervision.</p>
            </div>
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
              <p>While many international beaches, such as those in parts of India or Europe, are known for their calm and predictable waters, Australian coastal environments are dynamic and powerful, even for experienced swimmers.</p>
              
              <div class="image-comparison">
                <div class="comparison-image">
                  <img src="./IndianWaters.jpg" alt="Calm waters in India">
                  <p class="image-caption">Calm waters abroad: Lakes, rivers, or sheltered beaches in many countries</p>
                </div>
                <div class="comparison-image">
                  <img src="./roughAussieBeach.jpg" alt="Rough Australian beach with powerful waves">
                  <p class="image-caption">Powerful waters in Australia: Strong waves and dangerous undercurrents</p>
                </div>
              </div>
              
              <p>This contrast means that familiar swimming habits from other countries may not be safe in Australia. The environmental differences require specific knowledge and caution, particularly for visitors and new residents unfamiliar with these conditions.</p>
              
                  <p class="impact-note">Australian beaches feature powerful rip currents that can pull swimmers hundreds of meters offshore in minutes—a particular danger for children and visitors who can't identify these invisible currents or lack the swimming strength to escape them.</p>
                </div>
                
                <!-- Immigrant Risk Tab -->
                <div v-show="activeTab === 'immigrants'" class="tab-pane">
                  <div class="immigrant-intro">
                    <h3 class="subsection-title">Understanding Immigrant Vulnerability at Australian Beaches</h3>
                    
                    <div class="risk-cards">
                      <div class="risk-card">
                        <div class="risk-icon">🌊</div>
                        <div class="risk-content">
                          <h4>Water Conditions</h4>
                          <p>Immigrants from regions with calm waters are often unprepared for Australia's powerful surf and rip currents.</p>
                        </div>
                      </div>
                      
                      <div class="risk-card">
                        <div class="risk-icon">🏊‍♂️</div>
                        <div class="risk-content">
                          <h4>Cultural Understanding</h4>
                          <p>Many lack knowledge of beach safety protocols and how rapidly ocean conditions can change.</p>
                        </div>
                      </div>
                      
                      <div class="risk-card">
                        <div class="risk-icon">⏳</div>
                        <div class="risk-content">
                          <h4>Persistent Risk</h4>
                          <p>Even after decades in Australia, immigrants remain vulnerable without proper beach education.</p>
                        </div>
                      </div>
                    </div>
                    
                    <div class="graph-transition">
                      <div class="transition-line"></div>
                      <div class="transition-text">These risks affect immigrants from diverse backgrounds</div>
                      <div class="transition-line"></div>
                    </div>
                  </div>
                  
                  <div class="vulnerability-sections">
                    <section class="vulnerability-section">
                      <h4 class="section-title">Risk by Country of Origin</h4>
                      
                      <div class="drowning-statistics">
                        <div class="chart-title">Immigrant Drowning Deaths at Australian Beaches (2014-2023)</div>
                        <div class="chart-container">
                          <div class="chart-columns">
                            <div v-for="(country, index) in overseasDrowningData" :key="index" class="chart-column">
                              <div class="country-flag" :class="country.code"></div>
                              <div class="column-bar" :style="{height: getBarHeight(country.deaths)}">
                                <span class="death-count">{{ country.deaths }}</span>
                              </div>
                              <div class="country-name">{{ country.name }}</div>
                            </div>
                  </div>
                </div>
                
                        <div class="chart-note">
                          <p>China and the UK have the highest numbers, while countries like Vietnam and the USA have seen decreases in drowning deaths. Recent increases have been recorded among people from India, Afghanistan, Iran, and Sri Lanka.</p>
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
              </div>
            </div>
          </div>
          
          <div class="content-section" style="margin-top: 1rem;">
            <div class="section-header left">
              <h2 class="section-title left beach">🏖️ Find the Right Beach for Your Family</h2>
              <p class="section-subtitle left">Know Before You Go</p>
            </div>
            
            <div class="section-body">
              <div class="info-cards">
                <div class="info-card safety">
                  <div class="info-icon">📊</div>
                  <div class="info-content">
                    <h4>Safety Varies by Beach</h4>
                    <p>Wave height, currents, topography, and patrol status all impact safety levels.</p>
                  </div>
                </div>
                
                <div class="info-card conditions">
                  <div class="info-icon">🔄</div>
                  <div class="info-content">
                    <h4>Conditions Change Quickly</h4>
                    <p>Tides, wind, and weather can transform calm waters into hazardous conditions within hours.</p>
                  </div>
                </div>
                
                <div class="info-card patrol">
                  <div class="info-icon">👮‍♂️</div>
                  <div class="info-content">
                    <h4>Choose Patrolled Beaches</h4>
                    <p>Beaches with lifeguards significantly reduce risk – prioritize these locations.</p>
                  </div>
                </div>
              </div>
              
              <p class="tool-intro">Our beach comparison tool helps you identify the safest options based on your family's needs and experience level:</p>
              
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
      tabs: [
        { id: 'overview', label: 'Overview', icon: '🌊' },
        { id: 'immigrants', label: 'Immigrant Risk', icon: '👨‍👩‍👧‍👦' },
        { id: 'education', label: 'Our Mission', icon: '🎓' }
      ],
      overseasDrowningData: [
        { name: 'China', deaths: 113, code: 'flag-cn' },
        { name: 'UK', deaths: 109, code: 'flag-gb' },
        { name: 'New Zealand', deaths: 55, code: 'flag-nz' },
        { name: 'India', deaths: 46, code: 'flag-in' },
        { name: 'Vietnam', deaths: 40, code: 'flag-vn' },
        { name: 'South Korea', deaths: 35, code: 'flag-kr' },
        { name: 'Italy', deaths: 29, code: 'flag-it' },
        { name: 'USA', deaths: 28, code: 'flag-us' },
        { name: 'Germany', deaths: 24, code: 'flag-de' },
        { name: 'Nepal', deaths: 22, code: 'flag-np' }
      ]
    }
  },
  mounted() {
    // Initialize scrolled state
    this.scrolled = false;
    window.addEventListener('scroll', this.handleScroll);
    
    // Set the active navigation link for this page
    this.setActiveNavLink();
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.handleScroll);
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
    getBarHeight(deaths) {
      const maxHeight = 140; // Reduced maximum height for the bar
      const minDeaths = 0; // Minimum deaths for the bar to be at full height
      const maxDeaths = 120; // Maximum deaths for the bar to be at minimum height
      
      const barHeight = ((deaths - minDeaths) / (maxDeaths - minDeaths)) * maxHeight;
      return barHeight + 'px';
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
    background-image: url('./Aussie_beachhome.jpg');
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
    font-size: 1.2rem;
    color: white;
    text-align: center;
    margin-bottom: 1.5rem;
    font-weight: 600;
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
    width: 30px; /* Slightly narrower */
    background: #01365c;
    border-radius: 4px 4px 0 0;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    padding-top: 5px; /* Reduced padding */
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
    position: relative;
    margin-bottom: 4px; /* Reduced margin */
    transition: all 0.3s ease;
  }
  
  .column-bar:hover {
    background: #f39c12;
    transform: translateY(-5px);
  }
  
  .death-count {
    color: white;
    font-weight: 700;
    font-size: 0.9rem;
  }
  
  .country-name {
    font-size: 0.75rem; /* Slightly smaller font */
    text-align: center;
    margin-top: 0.25rem; /* Reduced margin */
    color: rgba(255, 255, 255, 0.9);
    max-width: 70px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  
  .chart-note {
    margin-top: 1rem;
    padding: 0.75rem;
    background: rgba(243, 156, 18, 0.1);
    border-radius: 0.5rem;
    font-size: 0.9rem;
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
    font-size: 1rem;
    font-weight: 600;
    color: #f39c12;
    margin: 0 1rem;
    white-space: nowrap;
  }
</style> 