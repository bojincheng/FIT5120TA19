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
            <h2 class="headline">It only takes <span class="highlight">20 silent seconds</span> for a toddler to drown</h2>
            <p class="subheadline">— Learn how to stop tragedy before it happens</p>
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
              <button 
                class="tab-button" 
                :class="{ active: activeTab === 'parents' }"
                @click="activeTab = 'parents'"
              >
                <span class="tab-icon">👨‍👩‍👧‍👦</span>
                <span class="tab-label">Young Parents</span>
              </button>
              <button 
                class="tab-button" 
                :class="{ active: activeTab === 'mission' }"
                @click="activeTab = 'mission'"
              >
                <span class="tab-icon">🎯</span>
                <span class="tab-label">Our Mission</span>
              </button>
            </div>
            
            <div class="tab-content">
              <!-- Overview Tab -->
              <div v-if="activeTab === 'overview'" class="tab-pane">
                <h3 class="tab-title">Pool Safety Overview</h3>
                
                <div class="alert-card">
                  <div class="alert-icon">⚠️</div>
                  <p class="alert-text">For young families, pool safety is a critical issue — and sadly, too often overlooked.</p>
                </div>
                
                <div class="statistics-grid">
                  <div class="stat-card">
                    <div class="stat-header">
                      <span class="stat-emoji">⚰️</span>
                      <h4>Leading Cause of Death</h4>
                    </div>
                    <p>Drowning is the <strong>leading cause of accidental death</strong> in Australian children aged 1–4 years</p>
                  </div>
                  
                  <div class="stat-card">
                    <div class="stat-header">
                      <span class="stat-emoji">🏠</span>
                      <h4>Backyard Risk</h4>
                    </div>
                    <p>Over <strong>50%</strong> of these tragedies occur in backyard pools, where families least expect danger</p>
                  </div>
                  
                  <div class="stat-card">
                    <div class="stat-header">
                      <span class="stat-emoji">⏱️</span>
                      <h4>Silent & Swift</h4>
                    </div>
                    <p>It can happen in as little as <strong>20 seconds</strong>, often silently, while a parent is just momentarily distracted</p>
                  </div>
                  
                  <div class="stat-card">
                    <div class="stat-header">
                      <span class="stat-emoji">📊</span>
                      <h4>Annual Toll</h4>
                    </div>
                    <p>Every year, <strong>15–20 young children drown</strong> in pools, and many more suffer life-long injuries from non-fatal drowning</p>
                  </div>
                </div>
                
                <div class="info-section">
                  <h4 class="info-title">The Backyard Danger</h4>
                  
                  <div class="info-content-layout">
                    <div class="info-text">
                      <p>Backyard pools are the most dangerous because they create a false sense of security. Families assume they'll notice if something goes wrong — but toddlers slip beneath the water quietly, without splashing or calling out.</p>
                      
                      <div class="emotional-impact">
                        <div class="impact-quote">
                          <div class="quote-mark">"</div>
                          <p>For many parents, these tragedies leave a lasting scar. The overwhelming sense of responsibility and grief can be devastating, especially knowing that simple safety steps could have made all the difference.</p>
                        </div>
                      </div>
                    </div>
                    
                    <div class="pool-ring-image">
                      <img src="./assets/POOLRING.jpg" alt="Orange life ring floating in blue pool water" />
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- Young Parents Tab -->
              <div v-if="activeTab === 'parents'" class="tab-pane">
                <h3 class="tab-title">Resources for Young Parents</h3>
                
                <div class="parents-card">
                  <div class="alert-banner">
                    <div class="alert-icon">⚠️</div>
                    <div class="alert-content">
                      <div class="stat-number-large">77%</div>
                      <div class="alert-text">of drowning victims under 5 years old were missing from sight for less than 5 minutes</div>
                    </div>
                  </div>
                  
                  <div class="section-divider">
                    <span class="divider-text">The Emotional Impact</span>
                  </div>
                  
                  <div class="impact-container">
                    <div class="image-text-layout">
                      <div class="family-image-container">
                        <img src="./assets/young_panrets.jpeg" alt="Young parents walking with their children" class="family-image" />
                      </div>
                      
                      <div class="impact-text">
                        <p class="impact-intro">For parents who lose a child to drowning, the impact is heartbreaking and lifelong. Many carry a heavy burden of guilt, grief, and trauma, often feeling they "should have done more" — even though drowning can happen so quickly and silently.</p>
                        
                        <div class="emotional-stat-card">
                          <div class="stat-badge-wrapper">
                            <div class="stat-badge">
                              <div class="badge-inner">80%</div>
                            </div>
                            <div class="badge-shadow"></div>
                          </div>
                          <div class="stat-content">
                            <p>Over <span class="highlight-text">80% of parents</span> affected by child drowning experience severe emotional distress, including anxiety, depression, and ongoing trauma.</p>
                            <p class="source">(Australian Psychological Society)</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  
                  <div class="section-divider">
                    <span class="divider-text">Common Challenges</span>
                  </div>
                  
                  <div class="parent-challenge-section">
                    <p class="challenge-intro">But staying vigilant isn't always easy, especially for young families juggling the demands of multiple children under 6.</p>
                    
                    <div class="challenge-cards">
                      <div class="challenge-card">
                        <div class="challenge-title">
                          <div class="challenge-icon">👨‍👩‍👧‍👦</div>
                          <h5>Divided attention</h5>
                        </div>
                        <p>Managing several young children makes constant supervision difficult, especially in busy, chaotic moments.</p>
                      </div>
                      
                      <div class="challenge-card">
                        <div class="challenge-title">
                          <div class="challenge-icon">🔍</div>
                          <h5>False sense of security</h5>
                        </div>
                        <p>Many parents assume being "close by" is enough, not realizing how quickly a child can drown.</p>
                      </div>
                      
                      <div class="challenge-card">
                        <div class="challenge-title">
                          <div class="challenge-icon">⏰</div>
                          <h5>Limited time and resources</h5>
                        </div>
                        <p>Between work, parenting, and daily life, finding time for pool safety checks or CPR training can feel overwhelming.</p>
                      </div>
                      
                      <div class="challenge-card">
                        <div class="challenge-title">
                          <div class="challenge-icon">💰</div>
                          <h5>Cost of safety upgrades</h5>
                        </div>
                        <p>Pool fencing repairs or compliance checks can be costly, and some parents may delay them.</p>
                      </div>
                    </div>
                  </div>
                  
                  <div class="solution-footer">
                    <div class="solution-icon">💡</div>
                    <div class="solution-content">
                      <p>Understanding these challenges is the first step to overcoming them. Our resources are designed to provide practical, manageable solutions that fit into busy family life.</p>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- Mission Tab -->
              <div v-if="activeTab === 'mission'" class="tab-pane">
                <div class="mission-card">
                  <div class="mission-header">
                    <div class="mission-banner">
                      <div class="banner-header">
                        <h3>Our Mission</h3>
                      </div>
                      <h4 class="mission-headline">At WaterWiseFamily, we believe no parent should have to experience the heartbreak of losing a child to drowning — yet in Australia, drowning remains the leading cause of accidental death for children under 5.</h4>
                    </div>
                  </div>
                  
                  <div class="mission-section challenge-section">
                    <div class="section-header">
                      <div class="section-icon">⚠️</div>
                      <h4>The Key Challenge</h4>
                    </div>
                    
                    <div class="section-content">
                      <p>For young families, especially those with multiple children under 6, constant supervision can feel nearly impossible. Life is full of distractions — answering the door, tending to another child, stepping inside for a moment — and that's often all it takes. Backyard pools, while convenient and fun, are the most dangerous, leading to the majority of child drownings in Australia.</p>
                      
                      <div class="awareness-gaps">
                        <h5>Many parents simply aren't aware of:</h5>
                        <ul class="gap-list">
                          <li class="gap-item">
                            <div class="gap-icon">⏱️</div>
                            <p>How fast drowning happens — in just 20 silent seconds.</p>
                          </li>
                          
                          <li class="gap-item">
                            <div class="gap-icon">🔍</div>
                            <p>The hidden hazards in and around pools, like unsecured gates or small amounts of water left in play pools.</p>
                          </li>
                          
                          <li class="gap-item">
                            <div class="gap-icon">⚠️</div>
                            <p>The false sense of safety that comes with being "nearby" but not fully present.</p>
                          </li>
          </ul>
                      </div>
                    </div>
                  </div>
                  
                  <div class="mission-section solution-section">
                    <div class="section-header">
                      <div class="section-icon">💡</div>
                      <h4>Our Solution</h4>
                    </div>
                    
                    <div class="section-content">
                      <p>At WaterWise Family, we provide practical, easy-to-follow education to help parents stay one step ahead of danger:</p>
                      
                      <div class="solution-steps">
                        <div class="solution-step">
                          <div class="step-number">1</div>
                          <p>We teach the right safety practices, so parents can confidently supervise and manage pool risks, even with multiple young kids.</p>
                        </div>
                        
                        <div class="solution-step">
                          <div class="step-number">2</div>
                          <p>We raise awareness of key hazards — like non-compliant fencing, unsupervised water play, and the myth that drowning is loud.</p>
                        </div>
                        
                        <div class="solution-step">
                          <div class="step-number">3</div>
                          <p>We offer tools and resources to make supervision easier, from safety checklists to emergency action plans.</p>
      </div>
                        
                        <div class="solution-step">
                          <div class="step-number">4</div>
                          <p>We support families in building safe habits that fit into their busy lives — because prevention starts with knowledge and action.</p>
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

.statistics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: linear-gradient(135deg, rgba(231, 76, 60, 0.8), rgba(192, 57, 43, 0.8));
  border-radius: 0.75rem;
  padding: 1.25rem;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
  border: none;
  color: white;
}

.stat-card:nth-child(1) {
  background: linear-gradient(135deg, rgba(231, 76, 60, 0.85), rgba(192, 57, 43, 0.85));
}

.stat-card:nth-child(2) {
  background: linear-gradient(135deg, rgba(241, 196, 15, 0.85), rgba(243, 156, 18, 0.85));
}

.stat-card:nth-child(3) {
  background: linear-gradient(135deg, rgba(46, 204, 113, 0.9), rgba(39, 174, 96, 0.9));
}

.stat-card:nth-child(4) {
  background: linear-gradient(135deg, rgba(155, 89, 182, 0.85), rgba(142, 68, 173, 0.85));
}

.stat-header {
  display: flex;
  align-items: center;
  margin-bottom: 0.75rem;
}

.stat-emoji {
  font-size: 1.8rem;
  margin-right: 0.75rem;
}

.stat-header h4 {
  margin: 0;
  color: white;
  font-size: 1.1rem;
  font-weight: 700;
}

.stat-card p {
  margin: 0;
  line-height: 1.5;
}

.stat-card strong {
  color: white;
  font-weight: 700;
  text-decoration: underline;
  text-underline-offset: 2px;
}

.info-section {
  background: rgba(0, 61, 91, 0.5);
  border-radius: 0.75rem;
  padding: 1.5rem;
  margin-top: 1rem;
}

.info-title {
  color: #00e1ff;
  margin: 0 0 1rem;
  font-size: 1.3rem;
}

.emotional-impact {
  margin: 1.5rem 0;
}

.impact-quote {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
  padding: 1.5rem;
  position: relative;
  border-left: 3px solid rgba(255, 255, 255, 0.2);
}

.quote-mark {
  font-size: 3rem;
  position: absolute;
  top: -0.75rem;
  left: 0.5rem;
  color: rgba(255, 255, 255, 0.1);
  font-family: serif;
}

.impact-quote p {
  margin: 0;
  font-style: italic;
  line-height: 1.6;
}

.action-card {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
  padding: 1.5rem;
  margin-top: 1.5rem;
  border-left: 3px solid #ffcc00;
}

.action-card h4 {
  color: #ffcc00;
  margin: 0 0 1rem;
  font-size: 1.2rem;
  text-align: center;
}

.action-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-top: 1.5rem;
  justify-content: center;
}

.action-button {
  padding: 0.75rem 1.25rem;
  border: none;
  border-radius: 0.5rem;
  display: flex;
  align-items: center;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  color: white;
}

.action-button.supervision {
  background: linear-gradient(135deg, #3498db, #2980b9);
}

.action-button.barriers {
  background: linear-gradient(135deg, #e67e22, #d35400);
}

.action-button.response {
  background: linear-gradient(135deg, #e74c3c, #c0392b);
}

.action-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
}

.button-icon {
  font-size: 1.5rem;
  margin-right: 0.75rem;
}

/* Parents Tab Styling */
.parents-card {
  background: rgba(0, 61, 91, 0.6);
  border-radius: 1rem;
  padding: 2rem;
  margin-bottom: 1rem;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
}

.alert-banner {
  display: flex;
  align-items: center;
  background: linear-gradient(135deg, rgba(231, 76, 60, 0.9), rgba(192, 57, 43, 0.9));
  border-radius: 0.75rem;
  padding: 1.5rem;
  margin-bottom: 2rem;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
  transform: translateY(-10px);
}

.alert-icon {
  font-size: 3rem;
  margin-right: 1.5rem;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.1); }
  100% { transform: scale(1); }
}

.alert-content {
  flex: 1;
}

.stat-number-large {
  font-size: 3.5rem;
  font-weight: 800;
  color: white;
  line-height: 1;
  margin-bottom: 0.5rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.alert-text {
  font-size: 1.2rem;
  font-weight: 500;
  color: white;
  line-height: 1.4;
}

.section-divider {
  display: flex;
  align-items: center;
  margin: 3rem 0 1.5rem;
  color: #ffcc00;
}

.section-divider:before,
.section-divider:after {
  content: "";
  flex: 1;
  height: 1px;
  background: rgba(255, 204, 0, 0.4);
}

.divider-text {
  padding: 0 1rem;
  font-size: 1.4rem;
  font-weight: 700;
  white-space: nowrap;
}

.impact-container {
  padding: 0 1rem;
}

.impact-intro {
  font-size: 1.15rem;
  line-height: 1.7;
  margin-bottom: 2rem;
  font-weight: 500;
  color: white;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
  padding: 0 0.5rem;
}

.emotional-stat-card {
  display: flex;
  align-items: center;
  background: rgba(0, 0, 0, 0.3);
  border-radius: 1rem;
  padding: 1.5rem;
  margin: 0 auto 2rem;
  max-width: 800px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
  transform: translateY(0);
  transition: transform 0.3s ease;
  border-left: 4px solid rgba(231, 76, 60, 0.7);
}

.stat-badge-wrapper {
  position: relative;
  margin-right: 2rem;
}

.stat-badge {
  width: 90px;
  height: 90px;
  position: relative;
  z-index: 2;
}

.badge-shadow {
  position: absolute;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.3);
  border-radius: 50%;
  top: 5px;
  left: 5px;
  z-index: 1;
  filter: blur(5px);
}

.badge-inner {
  position: absolute;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #e74c3c, #c0392b);
  color: white;
  font-size: 2rem;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.25);
}

.stat-content {
  flex: 1;
}

.stat-content p {
  margin: 0 0 0.5rem;
  font-size: 1.1rem;
  line-height: 1.6;
}

.highlight-text {
  color: #e74c3c;
  font-weight: 700;
}

.source {
  font-style: italic;
  opacity: 0.7;
  font-size: 0.9rem;
  text-align: right;
  margin-top: 0.5rem !important;
}

.challenge-intro {
  font-size: 1.2rem;
  font-weight: 500;
  text-align: center;
  margin-bottom: 2rem;
  color: rgba(255, 255, 255, 0.9);
}

.challenge-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.5rem;
  margin-top: 1.5rem;
}

.challenge-card {
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.25);
  border: none;
  color: white;
  position: relative;
  overflow: hidden;
}

.challenge-card:nth-child(1) {
  background: linear-gradient(135deg, rgba(52, 152, 219, 0.9), rgba(41, 128, 185, 0.9));
}

.challenge-card:nth-child(2) {
  background: linear-gradient(135deg, rgba(231, 76, 60, 0.9), rgba(192, 57, 43, 0.9));
}

.challenge-card:nth-child(3) {
  background: linear-gradient(135deg, rgba(46, 204, 113, 0.9), rgba(39, 174, 96, 0.9));
}

.challenge-card:nth-child(4) {
  background: linear-gradient(135deg, rgba(155, 89, 182, 0.9), rgba(142, 68, 173, 0.9));
}

.challenge-card::before {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  width: 100px;
  height: 100px;
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  transform: translate(30%, -30%);
}

.challenge-title {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
  position: relative;
  z-index: 2;
}

.challenge-icon {
  font-size: 2.5rem;
  margin-right: 1rem;
  background: rgba(255, 255, 255, 0.2);
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
  flex-shrink: 0;
}

.challenge-title h5 {
  margin: 0;
  color: white;
  font-size: 1.4rem;
  font-weight: 800;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  letter-spacing: 0.5px;
}

.challenge-card p {
  margin: 0;
  line-height: 1.7;
  font-size: 1.1rem;
  color: rgba(255, 255, 255, 1);
  position: relative;
  z-index: 2;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
  font-weight: 500;
}

.solution-footer {
  display: flex;
  align-items: center;
  background: linear-gradient(135deg, rgba(52, 152, 219, 0.3), rgba(41, 128, 185, 0.3));
  border-radius: 1rem;
  padding: 1.5rem 2rem;
  margin-top: 3rem;
  border: 1px solid rgba(52, 152, 219, 0.4);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.solution-icon {
  font-size: 2.5rem;
  margin-right: 1.5rem;
  color: #3498db;
}

.solution-content p {
  margin: 0;
  font-size: 1.15rem;
  line-height: 1.6;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.95);
}

@media (max-width: 768px) {
  .parents-card {
    padding: 1.5rem;
  }
  
  .alert-banner {
    flex-direction: column;
    text-align: center;
    padding: 1.25rem;
  }
  
  .alert-icon {
    margin-right: 0;
    margin-bottom: 1rem;
  }
  
  .stat-number-large {
    font-size: 3rem;
  }
  
  .emotional-stat-card {
    flex-direction: column;
    text-align: center;
  }
  
  .stat-badge-wrapper {
    margin-right: 0;
    margin-bottom: 1.5rem;
  }
  
  .challenge-cards {
    grid-template-columns: 1fr;
  }
  
  .solution-footer {
    flex-direction: column;
    text-align: center;
  }
  
  .solution-icon {
    margin-right: 0;
    margin-bottom: 1rem;
  }
}

/* Mission Tab Styles */
.mission-card {
  background: rgba(0, 61, 91, 0.6);
  border-radius: 1rem;
  padding: 2rem;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
}

.mission-header {
  margin-bottom: 2.5rem;
  padding: 0;
}

.mission-banner {
  background: linear-gradient(135deg, rgba(0, 123, 194, 0.9), rgba(0, 98, 155, 0.9));
  border-radius: 1rem;
  padding: 2rem;
  margin-bottom: 2.5rem;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.3);
  position: relative;
  overflow: hidden;
  transform: translateY(-10px);
}

.mission-banner::before {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  width: 150px;
  height: 150px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  transform: translate(30%, -30%);
}

.mission-banner::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  width: 120px;
  height: 120px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 50%;
  transform: translate(-30%, 30%);
}

.banner-header {
  margin-bottom: 1rem;
}

.banner-header h3 {
  color: white;
  font-size: 1.8rem;
  font-weight: 800;
  margin: 0;
  text-transform: uppercase;
  letter-spacing: 1px;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.mission-headline {
  font-size: 1.4rem;
  line-height: 1.8;
  color: white;
  font-weight: 600;
  text-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
  position: relative;
  z-index: 2;
  text-align: left;
  margin: 0;
}

.mission-section {
  margin-bottom: 2rem;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
}

.challenge-section {
  background: rgba(231, 76, 60, 0.2);
  border: 1px solid rgba(231, 76, 60, 0.3);
}

.solution-section {
  background: rgba(46, 204, 113, 0.2);
  border: 1px solid rgba(46, 204, 113, 0.3);
}

.section-header {
  display: flex;
  align-items: center;
  padding: 1rem 1.5rem;
  background: rgba(0, 0, 0, 0.2);
}

.section-icon {
  font-size: 1.8rem;
  margin-right: 1rem;
}

.challenge-section .section-header {
  background: linear-gradient(135deg, rgba(231, 76, 60, 0.8), rgba(192, 57, 43, 0.8));
}

.solution-section .section-header {
  background: linear-gradient(135deg, rgba(46, 204, 113, 0.8), rgba(39, 174, 96, 0.8));
}

.section-header h4 {
  margin: 0;
  color: white;
  font-size: 1.4rem;
  font-weight: 700;
}

.section-content {
  padding: 1.5rem;
}

.section-content p {
  font-size: 1.1rem;
  line-height: 1.6;
  margin: 0 0 1.5rem;
}

.awareness-gaps h5 {
  font-size: 1.2rem;
  color: #ffcc00;
  margin: 0 0 1rem;
  font-weight: 600;
}

.gap-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.gap-item {
  display: flex;
  align-items: flex-start;
  background: rgba(231, 76, 60, 0.3);
  padding: 1rem 1.25rem;
  border-radius: 0.5rem;
}

.gap-icon {
  font-size: 1.5rem;
  margin-right: 1rem;
  flex-shrink: 0;
}

.gap-item p {
  margin: 0;
}

.solution-steps {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.solution-step {
  display: flex;
  align-items: center;
  background: rgba(46, 204, 113, 0.3);
  padding: 1rem 1.25rem;
  border-radius: 0.5rem;
}

.step-number {
  width: 35px;
  height: 35px;
  border-radius: 50%;
  background: rgba(46, 204, 113, 0.9);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  font-weight: 700;
  margin-right: 1rem;
  flex-shrink: 0;
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);
}

.solution-step p {
  margin: 0;
}

@media (max-width: 768px) {
  .mission-card {
    padding: 1.5rem;
  }
  
  .mission-headline {
    font-size: 1.1rem;
    line-height: 1.6;
  }
  
  .section-header {
    padding: 1rem;
  }
  
  .section-content {
    padding: 1.25rem;
  }
  
  .gap-item, .solution-step {
    padding: 1rem;
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
  
  .statistics-grid {
    grid-template-columns: 1fr;
  }
  
  .action-buttons {
    flex-direction: column;
  }
  
  .action-button {
    width: 100%;
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
  
  .mission-header {
    padding: 1.25rem 0.75rem;
  }
}

/* Add these styles for the pool ring image */
.info-content-layout {
  display: flex;
  flex-direction: row;
  gap: 1.5rem;
  margin-top: 1rem;
}

.info-text {
  flex: 1;
}

.pool-ring-image {
  flex: 1;
  max-width: 350px;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
}

.pool-ring-image img {
  width: 100%;
  height: auto;
  display: block;
  object-fit: cover;
}

@media (max-width: 768px) {
  .info-content-layout {
    flex-direction: column;
  }
  
  .pool-ring-image {
    max-width: 100%;
    margin-top: 1rem;
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
}

.family-image {
  width: 100%;
  height: auto;
  display: block;
  transition: transform 0.5s ease;
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
</style> 