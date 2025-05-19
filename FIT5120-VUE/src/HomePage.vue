<template>
  <div class="home-page">
    <div class="bg-image"></div>
    <div class="overlay"></div>
    <div class="content-wrapper">
      <div class="header">
        <h1>Drowning looks different depending on where you are — so your knowledge should too.</h1>
        
        <div class="progress-steps">
          <div class="step" :class="{ 'active': currentStep === 1 }">
            <div class="step-number">1</div>
            <span>Choose Focus</span>
          </div>
          <div class="step-connector"></div>
          <div class="step" :class="{ 'active': currentStep === 2 }">
            <div class="step-number">2</div>
            <span>Learn Safety</span>
          </div>
          <div class="step-connector"></div>
          <div class="step" :class="{ 'active': currentStep === 3 }">
            <div class="step-number">3</div>
            <span>Stay Protected</span>
          </div>
        </div>
      </div>

      <div class="options-container" ref="optionsContainer" @touchstart="handleTouchStart" @touchmove="handleTouchMove" @touchend="handleTouchEnd">
        <div class="card-navigation" v-if="isMobile">
          <button class="nav-btn prev" @click="goToPrevCard" :disabled="currentCardIndex === 0">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>
          </button>
          <div class="card-indicators">
            <span class="indicator" :class="{ 'active': currentCardIndex === 0 }" @click="setCardIndex(0)"></span>
            <span class="indicator" :class="{ 'active': currentCardIndex === 1 }" @click="setCardIndex(1)"></span>
          </div>
          <button class="nav-btn next" @click="goToNextCard" :disabled="currentCardIndex === cards.length - 1">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>
        </div>
        
        <div class="option-wrapper" :class="{'slide-in': showBeachCard}">
          <div 
            class="option-card beach" 
            tabindex="0"
            @keydown.enter="continueToSafety('beach')"
            @keydown.space.prevent="continueToSafety('beach')"
            role="button"
          >
            <div class="card-image-header">
              <img src="https://images.pexels.com/photos/355328/pexels-photo-355328.jpeg" alt="Beach Safety" class="card-header-image">
              <div class="card-overlay"></div>
              <div class="card-badge">Beach</div>
            </div>
            <div class="card-content">
              <div class="icon">🏖️</div>
              <h2>Beach Safety</h2>
              <div class="stat-indicator">
                <div class="stat-bar"></div>
              <p>Immigrants are 5x more at risk than Australians.</p>
              </div>
              <div class="title-with-lines">
                <div class="line"></div>
                <h3 class="aussie-waters-heading">Step 1: Familiarising Yourself with Aussie Waters</h3>
                <div class="line"></div>
              </div>
              <div class="beach-cards-container">
                <div class="beach-image-container" @click="continueToSafety('beach')">
                  <img src="./assets/ausbeachcond.avif" alt="Beach Conditions" class="beach-condition-image">
                  <div class="image-overlay">
                    <span>Understanding Australian Beach Conditions</span>
                  </div>
                </div>
                <div class="beach-image-container" @click="navigateToBeachComparison">
                  <img src="./assets/comparing_beaches.png" alt="Comparing Beaches" class="beach-condition-image">
                  <div class="image-overlay">
                    <span>Comparing Beach Safety Levels</span>
                  </div>
                </div>
              </div>
              <div class="preventing-risk">
                <div class="title-with-lines">
                  <div class="line"></div>
                  <h3>Step 2: Preventing Risk</h3>
                  <div class="line"></div>
                </div>
                <div class="prevention-images">
                  <div class="prevention-image-container" @click="navigateToBeachSafetyPractices">
                    <img src="./assets/understnading_beach_flags.jpg" alt="Understanding Beach Flags" class="prevention-image">
                    <div class="image-overlay">
                      <span>Understanding Flags</span>
                    </div>
                  </div>
                  <div class="prevention-image-container" @click="navigateToUnderstandingDanger">
                    <img src="./assets/understnading_rips.avif" alt="Understanding Rip Currents" class="prevention-image">
                    <div class="image-overlay">
                      <span>Understanding Rips</span>
                    </div>
                  </div>
                </div>
                <div class="facing-risk-link">
                  <div class="title-with-lines">
                    <div class="line"></div>
                    <h3>Step 3: Facing the Risk</h3>
                    <div class="line"></div>
                  </div>
                  <div class="prevention-images">
                    <div class="prevention-image-container" @click="navigateToBeachSafetyRescue">
                      <img src="./assets/near_shore.jpg" alt="Near Shore Rescue" class="prevention-image">
                      <div class="image-overlay">
                        <span>Near Shore Rescue</span>
                      </div>
                    </div>
                    <div class="prevention-image-container" @click="navigateToSurviveRipCurrents">
                      <img src="./assets/rippppsss.jpg" alt="Survive Rip Currents" class="prevention-image">
                      <div class="image-overlay">
                        <span>Survive Rip Currents</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <button class="select-button" @click="continueToSafety('beach')">
              <span>Start Beach Safety Guide</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </button>
        </div>
        </div>

        <div class="option-wrapper" :class="{'slide-in': showPoolCard}">
          <div 
            class="option-card pool" 
            tabindex="0"
            @keydown.enter="continueToSafety('pool')"
            @keydown.space.prevent="continueToSafety('pool')"
            role="button"
          >
            <div class="card-image-header pool-header">
              <img src="https://images.pexels.com/photos/870170/pexels-photo-870170.jpeg" alt="Kids jumping into pool" class="card-header-image">
              <div class="card-overlay"></div>
              <div class="card-badge pool-badge">Pool</div>
            </div>
            <div class="card-content">
              <div class="icon">🏊‍♂️</div>
              <h2>Pool Safety</h2>
              <div class="stat-indicator">
                <div class="stat-bar pool-stat-bar"></div>
              <p>80% of child drownings happen in home pools.</p>
              </div>
              <div class="title-with-lines">
                <div class="line"></div>
                <h3 class="pool-risk-heading">Step 1: Understanding the Risk</h3>
                <div class="line"></div>
              </div>
              <div class="pool-image-container" @click="continueToSafety('pool')">
                <img src="./assets/pool_danger_overview.jpg" alt="Pool danger overview" class="pool-condition-image">
                <div class="image-overlay">
                  <span>Understanding Pool Dangers</span>
                </div>
              </div>
              
              <div class="title-with-lines">
                <div class="line"></div>
                <h3 class="pool-risk-heading">Step 2: Preventing Risks</h3>
                <div class="line"></div>
              </div>
              
              <div class="pool-image-container" @click="navigateToBackyardPool">
                <img src="./assets/fencing_link.png" alt="Pool fencing requirements" class="pool-condition-image">
                <div class="image-overlay">
                  <span>Pool Barrier Safety</span>
                </div>
              </div>
              
              <div class="title-with-lines">
                <div class="line"></div>
                <h3 class="pool-risk-heading">Step 3: Test Your Preparedness</h3>
                <div class="line"></div>
              </div>
              
              <div class="pool-image-container" @click="navigateToPoolSafetyQuiz">
                <img src="./assets/are_you_ready.jpg" alt="Test your pool safety knowledge" class="pool-condition-image">
                <div class="image-overlay">
                  <span>Test Your Pool Safety Knowledge</span>
                </div>
              </div>
            </div>
            <button class="select-button pool-button" @click="continueToSafety('pool')">
              <span>Start Pool Safety Guide</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </button>
        </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { ref, onMounted, computed, watch } from 'vue';

const router = useRouter();
const showBeachCard = ref(false);
const showPoolCard = ref(false);
const optionsContainer = ref(null);
const currentStep = ref(1);

// Touch swiping variables
const touchStartX = ref(0);
const touchEndX = ref(0);
const currentCardIndex = ref(0);
const cards = ['beach', 'pool'];

// Check if on mobile device
const isMobile = computed(() => {
  return window.innerWidth <= 768;
});

onMounted(() => {
  // Setup responsive behavior
  window.addEventListener('resize', checkMobile);
  checkMobile();
  
  // Add staggered animation for cards on page load with more dynamic timing
  setTimeout(() => {
    showBeachCard.value = true;
    
    setTimeout(() => {
      showPoolCard.value = true;
    }, 400);
  }, 600);
  
  // Add intersection observer to animate elements as they enter viewport
  setupIntersectionObserver();
});

function checkMobile() {
  // This will update the isMobile computed property
  if (window.innerWidth <= 768) {
    // On mobile, set initial view to center on the first card
    setTimeout(() => {
      const firstCard = document.querySelector('.option-card.beach');
      if (firstCard) {
        firstCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }, 1000);
  }
}

function setupIntersectionObserver() {
  // Create observer for animating elements when they come into view
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.2 });
  
  // Observe elements with animate-on-scroll class
  document.querySelectorAll('.beach-image-container, .prevention-image-container, .pool-image-container')
    .forEach(el => observer.observe(el));
}

function handleTouchStart(e) {
  touchStartX.value = e.touches[0].clientX;
}

function handleTouchMove(e) {
  touchEndX.value = e.touches[0].clientX;
}

function handleTouchEnd() {
  const swipeThreshold = 80; // Reduced threshold for more responsive swiping
  const swipeDistance = touchEndX.value - touchStartX.value;
  
  // Check if the swipe is significant enough
  if (Math.abs(swipeDistance) > swipeThreshold) {
    if (swipeDistance > 0) {
      // Swipe right - show previous card
      goToPrevCard();
    } else {
      // Swipe left - show next card
      goToNextCard();
    }
  }
}

function goToPrevCard() {
  if (currentCardIndex.value > 0) {
    currentCardIndex.value--;
    scrollToCurrentCard();
  }
}

function goToNextCard() {
  if (currentCardIndex.value < cards.length - 1) {
    currentCardIndex.value++;
    scrollToCurrentCard();
  }
}

function setCardIndex(index) {
  currentCardIndex.value = index;
  scrollToCurrentCard();
}

function scrollToCurrentCard() {
  const currentCard = cards[currentCardIndex.value];
  const cardElement = document.querySelector(`.option-card.${currentCard}`);
  if (cardElement) {
    cardElement.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
}

// Watch card index changes to update step indicator
watch(currentCardIndex, (newIndex) => {
  // Step 1 is always active when choosing, step 2+ appear when proceeding to actual content
  currentStep.value = 1;
});

function continueToSafety(type) {
  // Add a nice transition before navigation
  const cardElement = document.querySelector(`.option-card.${type}`);
  if (cardElement) {
    cardElement.classList.add('card-selected');
    
    // Wait for animation to complete before navigating
    setTimeout(() => {
  if (type === 'beach') {
    router.push('/beach-safety');
  } else if (type === 'pool') {
    router.push('/pool-safety');
  }
  
  window.scrollTo(0, 0);
    }, 400);
  } else {
    // Fallback if animation fails
    if (type === 'beach') {
      router.push('/beach-safety');
    } else if (type === 'pool') {
      router.push('/pool-safety');
    }
    
    window.scrollTo(0, 0);
  }
}

function navigateToBeachComparison() {
  addExitTransition(() => {
  router.push('/beach-safety').then(() => {
    // Use a slight delay to ensure the page is loaded before scrolling
    setTimeout(() => {
      // Target the beach comparison section
      const comparisonSection = document.querySelector('.feature-card');
      if (comparisonSection) {
        comparisonSection.scrollIntoView({ behavior: 'smooth' });
      }
    }, 300);
    });
  });
}

function navigateToBackyardPool() {
  addExitTransition(() => {
  router.push('/backyard-pool').then(() => {
    // Use a small timeout to ensure the page loads first
    setTimeout(() => {
      // Scroll to middle of the page
      const pageHeight = document.body.scrollHeight;
      window.scrollTo(0, pageHeight / 3);
    }, 100);
    });
  });
}

function navigateToPreventingRisk() {
  addExitTransition(() => {
  router.push('/beach-safety').then(() => {
    setTimeout(() => {
      // Target the risk prevention section (adjust selector as needed)
      const riskSection = document.querySelector('.risk-prevention');
      if (riskSection) {
        riskSection.scrollIntoView({ behavior: 'smooth' });
      } else {
        // Fallback if specific section not found
        window.scrollTo(0, 0);
      }
    }, 300);
    });
  });
}

function navigateToBeachSafetyPractices() {
  addExitTransition(() => {
  router.push('/beach-safety-practices').then(() => {
    window.scrollTo(0, 0);
    });
  });
}

function navigateToUnderstandingDanger() {
  addExitTransition(() => {
  router.push('/understanding-danger').then(() => {
    window.scrollTo(0, 0);
    });
  });
}

function navigateToSpotRipCurrents() {
  addExitTransition(() => {
  router.push('/spot-rip-currents').then(() => {
    window.scrollTo(0, 0);
    });
  });
}

function navigateToBeachSafetyRescue() {
  addExitTransition(() => {
  router.push('/beach-safety-rescue').then(() => {
    window.scrollTo(0, 0);
    });
  });
}

function navigateToSurviveRipCurrents() {
  addExitTransition(() => {
  router.push('/survive-rip-currents').then(() => {
    window.scrollTo(0, 0);
    });
  });
}

function navigateToPoolSafetyQuiz() {
  addExitTransition(() => {
  router.push('/pool-supervision').then(() => {
    // Wait for page to load
    setTimeout(() => {
      // Find the component and trigger the quiz modal
      const app = document.querySelector('.pool-supervision-page');
      if (app) {
        // Create and dispatch a custom event to open the quiz
        const event = new CustomEvent('show-quiz');
        app.dispatchEvent(event);
      }
      window.scrollTo(0, 0);
    }, 300);
  });
  });
}

// Helper function to add transition effects before navigation
function addExitTransition(callback) {
  // Add a nice fade-out effect for the whole page
  document.body.classList.add('page-transition');
  
  // Wait for animation to complete before navigating
  setTimeout(() => {
    document.body.classList.remove('page-transition');
    callback();
  }, 300);
}
</script>

<style scoped>
.home-page {
  height: auto;
  min-height: 100vh;
  position: relative;
  color: #ffffff;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem 0;
}

.bg-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('./assets/cswimming.jpg');
  background-size: cover;
  background-position: center;
  z-index: 0;
  animation: slowZoom 30s infinite alternate ease-in-out;
}

@keyframes slowZoom {
  0% { transform: scale(1); }
  100% { transform: scale(1.1); }
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(to bottom, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.7));
  z-index: 1;
}

.content-wrapper {
  width: 100%;
  max-width: 1200px;
  padding: 1rem;
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
}

.header {
  text-align: center;
  position: relative;
  z-index: 3;
  animation: fadeIn 0.8s ease-out;
  margin-bottom: 0.5rem;
  width: 100%;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-20px); }
  to { opacity: 1; transform: translateY(0); }
}

h1 {
  font-size: clamp(1.6rem, 2.5vw, 2.2rem);
  margin-bottom: 1.5rem;
  color: #ffffff;
  font-weight: 700;
  letter-spacing: -0.01em;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
  width: 100%;
  transform: translateX(0);
  animation: glowText 3s infinite alternate;
  text-align: center;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
  padding: 0 10px;
  line-height: 1.4;
}

@keyframes glowText {
  0% { text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3); }
  100% { text-shadow: 0 2px 20px rgba(255, 255, 255, 0.5), 0 0 30px rgba(255, 255, 255, 0.2); }
}

.progress-steps {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  margin-bottom: 1.5rem;
  padding: 0.75rem 2rem;
  background: rgba(0, 0, 0, 0.6);
  border-radius: 3rem;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
  max-width: fit-content;
  margin-left: auto;
  margin-right: auto;
  width: auto;
  position: sticky;
  top: 1rem;
  z-index: 10;
  backdrop-filter: blur(5px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  transform: translateY(0);
  transition: transform 0.3s ease, background 0.3s ease;
}

.progress-steps:hover {
  transform: translateY(-2px);
  background: rgba(0, 0, 0, 0.7);
}

.step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.4rem;
  min-width: 100px;
  padding: 0.5rem 0;
  transition: all 0.3s ease;
}

.step-number {
  width: 2.5rem;
  height: 2.5rem;
  background: #ffffff;
  color: #01579b;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.2rem;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.4);
  border: 2px solid rgba(255, 255, 255, 0.9);
  transition: all 0.4s ease;
  position: relative;
  overflow: hidden;
}

.step-number::after {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(255,255,255,0.8) 0%, rgba(255,255,255,0) 70%);
  opacity: 0;
  transform: scale(0);
  transition: transform 0.6s ease-out, opacity 0.6s ease-out;
}

.step:hover .step-number::after {
  opacity: 0.5;
  transform: scale(1);
}

.step span {
  font-size: 1rem;
  color: #ffffff;
  font-weight: 600;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
  text-align: center;
  transition: all 0.3s ease;
}

.step:hover span {
  transform: translateY(-2px);
}

.step-connector {
  width: 2.5rem;
  height: 3px;
  background: #ffffff;
  margin-top: 1.25rem;
  opacity: 0.9;
  border-radius: 2px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  position: relative;
  overflow: hidden;
}

.step-connector::after {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, rgba(255,255,255,0) 0%, rgba(255,255,255,1) 50%, rgba(255,255,255,0) 100%);
  animation: shimmer 2s infinite;
}

@keyframes shimmer {
  0% { left: -100%; }
  100% { left: 100%; }
}

/* Active step styling */
.step.active .step-number {
  background: #f0f8ff;
  color: #01579b;
  box-shadow: 0 0 20px rgba(240, 248, 255, 0.8);
  transform: scale(1.1);
}

.step.active span {
  transform: translateY(-2px);
  color: #f0f8ff;
  text-shadow: 0 0 10px rgba(240, 248, 255, 0.5);
}

/* Card navigation controls for mobile */
.card-navigation {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 1rem;
  width: 100%;
}

.card-indicators {
  display: flex;
  gap: 0.5rem;
}

.indicator {
  width: 10px;
  height: 10px;
  background: rgba(255, 255, 255, 0.4);
  border-radius: 50%;
  cursor: pointer;
  transition: all 0.3s ease;
}

.indicator.active {
  background: #ffffff;
  transform: scale(1.2);
}

.nav-btn {
  background: rgba(0, 0, 0, 0.6);
  border: none;
  color: white;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.3);
  transition: all 0.3s ease;
}

.nav-btn:hover {
  background: rgba(0, 0, 0, 0.8);
  transform: translateY(-2px);
}

.nav-btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

.options-container {  display: grid;  grid-template-columns: repeat(2, minmax(0, 1fr));  gap: 1.5rem;  width: 100%;  margin-bottom: 1.5rem;  perspective: 1000px;  max-width: 100%;  overflow-x: hidden;}

.option-wrapper {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  height: 100%;
    opacity: 0; 
  transform: translateY(50px) translateX(50px) rotateY(10deg);
  transition: opacity 0.6s ease, transform 0.6s ease;
  transform-style: preserve-3d;
  }

.option-wrapper.slide-in {
    opacity: 1; 
  transform: translateY(0) translateX(0) rotateY(0);
  }

/* Card image header */
.card-image-header {
  position: relative;
  height: 240px;
  width: 100%;
  border-radius: 1rem 1rem 0 0;
  overflow: hidden;
}

.card-header-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.option-card:hover .card-header-image {
  transform: scale(1.1);
}

.card-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(to bottom, rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.6));
}

.card-badge {
  position: absolute;
  top: 15px;
  right: 15px;
  background: #f39c12;
  color: white;
  padding: 0.3rem 0.8rem;
  border-radius: 1rem;
  font-weight: bold;
  font-size: 0.9rem;
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.3);
  transition: all 0.3s ease;
}

.pool-badge {
  background: #3498db;
}

.option-card:hover .card-badge {
  transform: translateY(-3px);
  box-shadow: 0 5px 12px rgba(0, 0, 0, 0.4);
}

.option-card {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  border-radius: 1rem;
  position: relative;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.7);
  display: flex;
  flex-direction: column;
  height: 100%;
  min-height: 850px;
  transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
  overflow: hidden;
  max-width: 100%;
  transform-style: preserve-3d;
}

.option-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
}

.option-card:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.5), 0 15px 30px rgba(0, 0, 0, 0.15);
}

/* Card selection animation */
.option-card.card-selected {
  transform: scale(1.05) translateY(-15px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
  opacity: 0;
  transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1), opacity 0.3s ease 0.1s;
}

.card-content {
  text-align: center;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  overflow-x: hidden;
  padding: 1.25rem;
  margin-bottom: 10px;
  max-width: 100%;
}

.card-content::-webkit-scrollbar {
  width: 6px;
}

.card-content::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.05);
  border-radius: 3px;
}

.card-content::-webkit-scrollbar-thumb {
  background: rgba(0, 0, 0, 0.15);
  border-radius: 3px;
}

.card-content::-webkit-scrollbar-thumb:hover {
  background: rgba(0, 0, 0, 0.25);
}

.icon {
  font-size: 2.8rem;
  margin-bottom: 0.75rem;
  filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.1));
  transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.option-card:hover .icon {
  transform: scale(1.15) translateY(-5px);
}

h2 {
  font-size: clamp(1.7rem, 2.5vw, 2.1rem);
  margin-bottom: 0.7rem;
  color: #1a5276;
  font-weight: 700;
  position: relative;
  display: inline-block;
  transition: transform 0.3s ease;
}

h2::after {
  content: '';
  position: absolute;
  left: 50%;
  bottom: -5px;
  width: 0;
  height: 3px;
  background: #1a5276;
  transition: width 0.3s ease, left 0.3s ease;
  transform: translateX(-50%);
}

.option-card:hover h2::after {
  width: 50%;
}

.option-card:hover h2 {
  transform: translateY(-3px);
}

/* Stat indicator styling */
.stat-indicator {
  position: relative;
  background: rgba(0, 0, 0, 0.05);
  border-radius: 0.5rem;
  padding: 0.5rem 1rem;
  margin-bottom: 1.25rem;
  overflow: hidden;
}

.stat-bar {
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 4px;
  background: #f39c12;
  border-radius: 0.5rem 0 0 0.5rem;
}

.pool-stat-bar {
  background: #3498db;
}

p {
  color: #2c3e50;
  margin-bottom: 0;
  line-height: 1.5;
  font-size: 1.05rem;
  font-weight: 500;
}

.select-button {
  width: 100%;
  padding: 0.9rem;
  border: none;
  border-radius: 0 0 0.5rem 0.5rem;
  background: #01579b;
  color: white;
  font-weight: 600;
  font-size: 1.05rem;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  margin-top: auto;
  position: relative;
  overflow: hidden;
  z-index: 1;
}

.select-button::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.3) 50%, rgba(255,255,255,0.1) 100%);
  transition: left 0.7s ease;
  z-index: -1;
}

.select-button:hover {
  background: #0277bd;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(1, 87, 155, 0.4);
}

.select-button:hover::before {
  left: 100%;
}

.pool-button {
  background: #0288d1;
}

.pool-button:hover {
  background: #039be5;
}

.select-button svg {
  transition: transform 0.3s ease;
}

.select-button:hover svg {
  transform: translateX(5px);
}

.beach {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(248, 249, 250, 0.95) 100%);
  border-left: 4px solid #f39c12;
  border-right: 1px solid rgba(255, 255, 255, 0.7);
  border-top: 1px solid rgba(255, 255, 255, 0.7);
  border-bottom: 1px solid rgba(255, 255, 255, 0.7);
}

.pool {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(248, 249, 250, 0.95) 100%);
  border-left: 4px solid #3498db;
  border-right: 1px solid rgba(255, 255, 255, 0.7);
  border-top: 1px solid rgba(255, 255, 255, 0.7);
  border-bottom: 1px solid rgba(255, 255, 255, 0.7);
}

/* Enhanced beach and pool image containers */
.beach-image-container, 
.prevention-image-container,
.pool-image-container {
  position: relative;
  margin: 0.75rem auto;
  border-radius: 0.75rem;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.15);
  max-width: 80%;
  width: 240px;
  height: 160px;
  opacity: 0;
  transform: translateY(20px);
}

/* Animation when elements come into view */
.beach-image-container.in-view, 
.prevention-image-container.in-view,
.pool-image-container.in-view {
  opacity: 1;
  transform: translateY(0);
}

.beach-image-container:hover, 
.prevention-image-container:hover,
.pool-image-container:hover {
  transform: translateY(-5px) scale(1.03);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
}

.beach-condition-image,
.prevention-image,
.pool-condition-image {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.beach-image-container:hover .beach-condition-image,
.prevention-image-container:hover .prevention-image,
.pool-image-container:hover .pool-condition-image {
  transform: scale(1.1);
}

.image-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.8), transparent);
  color: white;
  padding: 1rem 0.75rem;
  font-weight: 600;
  text-align: center;
  opacity: 1;
  transition: all 0.4s ease;
}

.beach-image-container:hover .image-overlay,
.prevention-image-container:hover .image-overlay,
.pool-image-container:hover .image-overlay {
  padding-bottom: 1.75rem;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0.4), transparent);
}

/* Beach cards container layout */
.beach-cards-container {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  justify-content: center;
  margin: 0.75rem auto;
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
}

.beach-cards-container .beach-image-container {
  max-width: calc(50% - 0.5rem);
  width: 240px;
  height: 160px;
  margin: 0;
}

/* Section headings */
.preventing-risk {
  text-align: center;
  margin-top: 1.25rem;
}

.preventing-risk h3,
.aussie-waters-heading,
.pool-risk-heading {
  color: #e74c3c;
  font-size: 1.2rem;
  margin: 0 10px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.title-with-lines {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  max-width: 100%;
  margin: 0.75rem 0;
  box-sizing: border-box;
  padding: 0 5px;
  transition: all 0.3s ease;
}

.title-with-lines:hover h3 {
  transform: scale(1.05);
}

.line {
  height: 2px;
  width: 40px;
  flex-shrink: 1;
  background-color: #e74c3c;
  transition: width 0.3s ease;
}

.title-with-lines:hover .line {
  width: 50px;
}

/* Prevention images layout */
.prevention-images {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  margin-top: 1rem;
  flex-wrap: wrap;
  max-width: 100%;
  box-sizing: border-box;
}

/* Page transition effect */
.page-transition {
  animation: fadeOut 0.3s ease forwards;
}

@keyframes fadeOut {
  from { opacity: 1; }
  to { opacity: 0; }
}

/* Responsive styles */
@media (max-width: 768px) {
  .home-page {
    height: auto;
    min-height: 100vh;
    padding: 2rem 0.75rem;
  }

  .content-wrapper {
    padding: 0.75rem;
  }

  .progress-steps {
    padding: 0.75rem 1.5rem;
    gap: 1.5rem;
    width: 90%;
    max-width: 500px;
    position: sticky;
    top: 0.5rem;
  }
  
  .step-number {
    width: 2.25rem;
    height: 2.25rem;
    font-size: 1.1rem;
  }
  
  .step span {
    font-size: 0.9rem;
  }
  
  .step-connector {
    width: 1.75rem;
  }

  .options-container {
    grid-template-columns: 1fr;
    gap: 1.5rem;
    display: flex;
    flex-direction: column;
    overflow-x: hidden;
  }

  .option-card {
    min-height: 700px;
    height: auto;
    overflow-y: visible;
  }
  
  .card-content {
    overflow-y: visible;
    padding: 1rem;
  }

  .option-wrapper {
    transform: translateX(100%);
    opacity: 0;
  }

  .option-wrapper.slide-in {
    transform: translateX(0);
    opacity: 1;
  }

  .icon {
    font-size: 2.5rem;
  }

  h2 {
    font-size: 1.5rem;
  }

  p {
    font-size: 0.95rem;
  }

  .beach-cards-container {
    gap: 0.5rem;
  }

  .beach-cards-container .beach-image-container,
  .beach-image-container,
  .prevention-image-container,
  .pool-image-container {
    width: 220px;
    height: 150px;
  }
  
  /* Improved swipe indicators for mobile */
  .options-container::after {
    content: "← Swipe →";
    position: absolute;
    bottom: -30px;
    left: 50%;
    transform: translateX(-50%);
    color: white;
    font-size: 0.9rem;
    background: rgba(0, 0, 0, 0.5);
    padding: 0.4rem 1rem;
    border-radius: 20px;
    animation: pulse 2s infinite;
    pointer-events: none;
  }
  
  @keyframes pulse {
    0% { opacity: 0.6; }
    50% { opacity: 1; }
    100% { opacity: 0.6; }
  }
}

@media (max-width: 480px) {
  .home-page {
    padding: 1.5rem 0.5rem;
  }
  
  h1 {
    font-size: 1.6rem;
    transform: translateX(0);
  }
  
  .progress-steps {
    flex-wrap: nowrap;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.5rem 0.75rem;
    margin-bottom: 1rem;
    max-width: 95%;
    position: sticky;
    top: 0.5rem;
  }

  .step {
    flex: 0 0 auto;
    min-width: 70px;
    margin: 0;
  }
  
  .step-connector {
    width: 1.25rem;
  }
  
  .step-number {
    width: 2rem;
    height: 2rem;
    font-size: 1rem;
  }
  
  .step span {
    font-size: 0.85rem;
  }
  
  .option-card {
    border-radius: 0.75rem;
    min-height: auto;
  }
  
  .card-image-header {
    height: 120px;
  }
  
  .card-badge {
    font-size: 0.8rem;
    padding: 0.25rem 0.7rem;
  }
  
  .select-button {
    padding: 0.7rem;
    font-size: 0.9rem;
  }

  .icon {
    font-size: 2.3rem;
  }

  h2 {
    font-size: 1.3rem;
  }

  p {
    font-size: 0.9rem;
  }

  .beach-cards-container {
    gap: 0.4rem;
  }
  
  .beach-cards-container .beach-image-container,
  .beach-image-container,
  .prevention-image-container,
  .pool-image-container {
    width: 180px;
    height: 130px;
  }
  
  .prevention-images {
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }
}

/* Ensure content fits on different screen heights */
@media (min-height: 900px) {
  .options-container {
    max-height: none;
  }
  
  .option-card {
    max-height: none;
  }
}

@media (max-height: 700px) {
  .home-page {
    height: auto;
    min-height: 100vh;
    padding: 1rem 0;
  }
  
  h1 {
    font-size: 1.6rem;
    margin-bottom: 0.25rem;
  }
  
  .icon {
    font-size: 2.3rem;
    margin-bottom: 0.5rem;
  }
  
  h2 {
    font-size: 1.3rem;
    margin-bottom: 0.25rem;
  }
  
  p {
    font-size: 0.85rem;
    margin-bottom: 0.5rem;
  }
  
  .select-button {
    padding: 0.6rem;
  }
}

/* Fix image handling */
img {
  max-width: 100%;
  height: auto;
  object-fit: cover;
}

/* Fix text overflow */
h1, h2, h3, p, span {
  max-width: 100%;
  overflow-wrap: break-word;
  word-wrap: break-word;
}

.pool-header .card-header-image {
  object-position: center 70%;
}
</style> 