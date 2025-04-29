<template>
  <div class="pool-supervision-page">
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
              <div class="progress-step active">
                <div class="step-number">1</div>
                <div class="step-label">Understanding Danger</div>
              </div>
              <div class="progress-step" @click="navigateToPage('/backyard-pool')">
                <div class="step-number">2</div>
                <div class="step-label">Backyard Pool Safety</div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="title-section">
          <h1>Pool Supervision Guidelines</h1>
          <div class="statistic-banner">
            <h2 class="headline">Active supervision is the <span class="highlight">first line of defense</span> against drowning</h2>
            <p class="subheadline">— Learn how to effectively supervise children around water</p>
          </div>
        </div>

        <!-- Silent Seconds Danger Card -->
        <div class="content-section">
          <div class="danger-card">
            <div class="card-header">
              <h3 class="danger-title">The Silent 20 Seconds</h3>
            </div>
            
            <div class="card-body">
              <p class="danger-intro">Drowning is silent and swift. Many parents believe they would hear splashing or calls for help, but the reality is that children who drown rarely make any noise. Just 20 silent seconds is all it takes for a toddler to drown.</p>
              
              <div class="video-section">
                <h4 class="video-title">See The Reality of Drowning</h4>
                
                <div class="language-tabs">
                  <button 
                    v-for="lang in languages" 
                    :key="lang.code" 
                    :class="['lang-tab', { active: selectedLanguage === lang.code }]"
                    @click="selectedLanguage = lang.code"
                  >
                    {{ lang.name }}
                  </button>
                </div>
                
                <div class="video-container">
                  <video 
                    ref="videoPlayer" 
                    :src="getVideoSource()" 
                    class="video-player" 
                    controls 
                    preload="metadata"
                    
                  ></video>
                </div>
                
                <p class="video-caption">This demonstration shows how quickly and silently drowning can happen, even with others nearby. <span class="language-note">Currently showing in {{ getCurrentLanguage().name }}</span></p>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Navigation Arrow -->
        <div class="next-section-arrow" v-if="showNavigationArrow" @click="navigateToPage('/backyard-pool')">
          <div class="arrow-label">Next: Backyard Pool Safety</div>
          <div class="arrow-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10"/>
              <path d="M8 12h8"/>
              <path d="m12 8 4 4-4 4"/>
            </svg>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PoolMenu from './components/PoolMenu.vue'

export default {
  name: 'PoolSupervision',
  components: {
    PoolMenu
  },
  data() {
    return {
      menuOpen: false,
      selectedLanguage: 'en',
      languages: [
        { code: 'en', name: 'English' },
        { code: 'ar', name: 'Arabic' },
        { code: 'km', name: 'Cambodian' },
        { code: 'yue', name: 'Cantonese' },
        { code: 'zh', name: 'Mandarin' },
        { code: 'mk', name: 'Macedonian' },
        { code: 'so', name: 'Somali' },
        { code: 'tr', name: 'Turkish' },
        { code: 'vi', name: 'Vietnamese' }
      ],
      showNavigationArrow: false
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
    getVideoSource() {
      const languageMap = {
        'en': 'Drowning_English.mp4',
        'ar': 'Drowning_Arabic.mp4',
        'km': 'Drowning_Cambodian.mp4',
        'yue': 'Drowning_Cantonese.mp4',
        'zh': 'Drowning_Mandarin.mp4',
        'mk': 'Drowning_Macedonian.mp4',
        'so': 'Drowning_Somali.mp4',
        'tr': 'Drowning_Turkish.mp4',
        'vi': 'Drowning_Vietnamese.mp4'
      };
      
      return `./videos/${languageMap[this.selectedLanguage]}`;
    },
    getCurrentLanguage() {
      return this.languages.find(lang => lang.code === this.selectedLanguage);
    },
    navigateToPage(route) {
      // Ensure we're using router navigation, not page reload
      if (this.$router) {
        this.$router.push(route);
        // Scroll to top after navigation
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    },
    // Handle scroll to show/hide navigation arrow
    handleScroll() {
      const scrollPosition = window.scrollY + window.innerHeight;
      const pageHeight = document.documentElement.scrollHeight;
      
      // Show arrow when user has scrolled to about 90% of the page height
      this.showNavigationArrow = scrollPosition > pageHeight * 0.9;
    }
  },
  mounted() {
    // Add scroll event listener to check position
    window.addEventListener('scroll', this.handleScroll);
  },
  beforeDestroy() {
    // Remove scroll event listener when component is destroyed
    window.removeEventListener('scroll', this.handleScroll);
  },
  watch: {
    selectedLanguage() {
      // Reset video when language changes
      if (this.$refs.videoPlayer) {
        this.$refs.videoPlayer.pause();
        this.$refs.videoPlayer.currentTime = 0;
      }
    }
  }
}
</script>

<style scoped>
.pool-supervision-page {
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
  background-image: url('./POOLHOME.png');
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
  width: 0%;
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
  background: linear-gradient(135deg, rgba(231, 76, 60, 0.8), rgba(192, 57, 43, 0.8));
  padding: 1.25rem 1.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
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

.danger-intro {
  font-size: 1.2rem;
  line-height: 1.6;
  margin-bottom: 2rem;
  text-align: center;
  font-weight: 500;
}

.video-section {
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
  padding: 1.5rem;
  margin-top: 1.5rem;
}

.video-title {
  font-size: 1.3rem;
  color: #00e1ff;
  margin: 0 0 1rem;
  text-align: center;
  font-weight: 600;
}

.video-container {
  position: relative;
  border-radius: 0.5rem;
  overflow: hidden;
  margin-bottom: 1rem;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
}

.video-player {
  width: 100%;
  display: block;
  aspect-ratio: 16/9;
  background-color: #000;
}

.language-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
  justify-content: center;
}

.lang-tab {
  background: rgba(0, 41, 61, 0.6);
  border: 1px solid rgba(0, 225, 255, 0.3);
  border-radius: 0.25rem;
  padding: 0.4rem 0.8rem;
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.8);
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.lang-tab:hover {
  background: rgba(0, 123, 194, 0.4);
  border-color: rgba(0, 225, 255, 0.5);
  color: white;
}

.lang-tab.active {
  background: rgba(0, 123, 194, 0.6);
  border-color: rgba(0, 225, 255, 0.7);
  color: white;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
}

.video-caption {
  text-align: center;
  font-style: italic;
  font-size: 1rem;
  color: rgba(255, 255, 255, 0.9);
  margin: 0;
}

.language-note {
  font-weight: 500;
  color: rgba(0, 225, 255, 0.8);
}

/* Navigation Arrow Styles */
.next-section-arrow {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  display: flex;
  align-items: center;
  background: rgba(0, 225, 255, 0.8);
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
  background: rgba(0, 225, 255, 1);
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
  animation: none;
}

.arrow-label {
  font-weight: 600;
  margin-right: 0.5rem;
  font-size: 1rem;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
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
  
  .progress-section {
    padding: 1.25rem 0.75rem 0.75rem;
    width: 95%;
  }
  
  .progress-container {
    margin: 0 auto;
  }
  
  .progress-track {
    margin: 0 0.5rem;
  }
  
  .step-number {
    width: 30px;
    height: 30px;
    font-size: 1rem;
  }
  
  .step-label {
    font-size: 0.8rem;
    max-width: 80px;
  }
  
  .danger-title {
    font-size: 1.4rem;
  }
  
  .card-body {
    padding: 1.25rem;
  }
  
  .danger-intro {
    font-size: 1.1rem;
  }
  
  .video-caption {
    font-size: 0.9rem;
  }
  
  .language-tabs {
    gap: 0.3rem;
  }
  
  .lang-tab {
    padding: 0.3rem 0.6rem;
    font-size: 0.8rem;
  }
  
  .video-section {
    padding: 1.25rem;
  }
  
  .next-section-arrow {
    bottom: 1.5rem;
    right: 1.5rem;
    padding: 0.7rem 1rem;
  }
  
  .arrow-label {
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
  
  .step-label {
    font-size: 0.7rem;
    max-width: 70px;
  }
  
  .danger-title {
    font-size: 1.3rem;
  }
  
  .card-body {
    padding: 1rem;
  }
  
  .danger-intro {
    font-size: 1rem;
  }
  
  .video-caption {
    font-size: 0.9rem;
  }
  
  .language-tabs {
    gap: 0.25rem;
  }
  
  .lang-tab {
    padding: 0.25rem 0.5rem;
    font-size: 0.75rem;
    flex-grow: 1;
    text-align: center;
  }
  
  .video-section {
    padding: 1rem;
  }
  
  .next-section-arrow {
    bottom: 1rem;
    right: 1rem;
    padding: 0.6rem 0.9rem;
  }
  
  .arrow-label {
    font-size: 0.85rem;
  }
}
</style> 