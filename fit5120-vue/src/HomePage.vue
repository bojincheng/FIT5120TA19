<template>
  <div class="home-page">
    <div class="bg-image"></div>
    <div class="overlay"></div>
    <div class="content-wrapper">
      <div class="header">
        <h1>Drowning looks different depending on where you are — so your knowledge should too.</h1>
        
        <div class="progress-steps">
          <div class="step">
            <div class="step-number">1</div>
            <span>Choose Focus</span>
          </div>
          <div class="step-connector"></div>
          <div class="step">
            <div class="step-number">2</div>
            <span>Learn Safety</span>
          </div>
          <div class="step-connector"></div>
          <div class="step">
            <div class="step-number">3</div>
            <span>Stay Protected</span>
          </div>
        </div>
      </div>

      <div class="options-container">
        <div class="option-wrapper">
          <div 
            class="option-card beach" 
            tabindex="0"
            @keydown.enter="continueToSafety('beach')"
            @keydown.space.prevent="continueToSafety('beach')"
            role="button"
          >
            <div class="card-content">
              <div class="icon">🏖️</div>
              <h2>Beach Safety</h2>
              <p>Immigrants are 5x more at risk than Australians.</p>
              <div class="title-with-lines">
                <div class="line"></div>
                <h3 class="aussie-waters-heading">Familiarising Yourself with Aussie Waters</h3>
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
                  <h3>Preventing Risk</h3>
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
                    <h3>Facing the Risk</h3>
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
                        <span></span>
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

        <div class="option-wrapper">
          <div 
            class="option-card pool" 
            tabindex="0"
            @keydown.enter="continueToSafety('pool')"
            @keydown.space.prevent="continueToSafety('pool')"
            role="button"
          >
            <div class="card-content">
              <div class="icon">🏊‍♂️</div>
              <h2>Pool Safety</h2>
              <p>80% of child drownings happen in home pools.</p>
              <div class="title-with-lines">
                <div class="line"></div>
                <h3 class="pool-risk-heading">Understanding the Risk</h3>
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
                <h3 class="pool-risk-heading">Preventing Risks</h3>
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
                <h3 class="pool-risk-heading">Test Your Preparedness</h3>
                <div class="line"></div>
              </div>
              
              <div class="pool-image-container" @click="navigateToPoolSafetyQuiz">
                <img src="./assets/are_you_ready.jpg" alt="Test your pool safety knowledge" class="pool-condition-image">
                <div class="image-overlay">
                  <span>Test Your Pool Safety Knowledge</span>
                </div>
              </div>
            </div>
            <button class="select-button" @click="continueToSafety('pool')">
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

const router = useRouter();

function continueToSafety(type) {
  if (type === 'beach') {
    router.push('/beach-safety');
  } else if (type === 'pool') {
    router.push('/pool-safety');
  }
  
  window.scrollTo(0, 0);
}

function navigateToBeachComparison() {
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
}

function navigateToBackyardPool() {
  router.push('/backyard-pool').then(() => {
    // Use a small timeout to ensure the page loads first
    setTimeout(() => {
      // Scroll to middle of the page
      const pageHeight = document.body.scrollHeight;
      window.scrollTo(0, pageHeight / 3);
    }, 100);
  });
}

function navigateToPreventingRisk() {
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
}

function navigateToBeachSafetyPractices() {
  router.push('/beach-safety-practices').then(() => {
    window.scrollTo(0, 0);
  });
}

function navigateToUnderstandingDanger() {
  router.push('/understanding-danger').then(() => {
    window.scrollTo(0, 0);
  });
}

function navigateToSpotRipCurrents() {
  router.push('/spot-rip-currents').then(() => {
    window.scrollTo(0, 0);
  });
}

function navigateToBeachSafetyRescue() {
  router.push('/beach-safety-rescue').then(() => {
    window.scrollTo(0, 0);
  });
}

function navigateToSurviveRipCurrents() {
  router.push('/survive-rip-currents').then(() => {
    window.scrollTo(0, 0);
  });
}

function navigateToPoolSafetyQuiz() {
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
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.4);
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
  z-index: 1;
  animation: fadeIn 0.8s ease-out;
  margin-bottom: 0.5rem;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-20px); }
  to { opacity: 1; transform: translateY(0); }
}

h1 {
  font-size: clamp(1.5rem, 2.8vw, 2.1rem);
  margin-bottom: 1rem;
  color: #ffffff;
  font-weight: 700;
  letter-spacing: -0.01em;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
  width: 100%;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.progress-steps {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  margin-bottom: 1rem;
}

.step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.25rem;
}

.step-number {
  width: 1.75rem;
  height: 1.75rem;
  background: #ffffff;
  color: #01579b;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 0.9rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.step span {
  font-size: 0.85rem;
  color: #ffffff;
  font-weight: 500;
  text-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
}

.step-connector {
  width: 1.5rem;
  height: 2px;
  background: #ffffff;
  margin-top: 0.875rem;
  opacity: 0.8;
}

.options-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
  width: 100%;
  animation: slideUp 0.8s ease-out 1.2s both;
  opacity: 0;
  margin-bottom: 1.5rem;
}

@keyframes slideUp {
  from { 
    opacity: 0; 
    transform: translateY(30px);
  }
  to { 
    opacity: 1; 
    transform: translateY(0);
  }
}

.option-wrapper {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  height: 100%;
}

.option-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 1rem;
  padding: 1.25rem;
  position: relative;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.7);
  display: flex;
  flex-direction: column;
  height: 100%;
  min-height: 850px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  overflow-y: auto;
  overflow-x: hidden;
  max-width: 100%;
}

.option-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
}

.option-card:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.5), 0 15px 30px rgba(0, 0, 0, 0.15);
}

.card-content {
  text-align: center;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  overflow-x: hidden;
  padding-right: 5px;
  margin-bottom: 10px;
  max-width: 100%;
}

.card-content::-webkit-scrollbar {
  width: 8px;
}

.card-content::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.05);
  border-radius: 4px;
}

.card-content::-webkit-scrollbar-thumb {
  background: rgba(0, 0, 0, 0.15);
  border-radius: 4px;
}

.card-content::-webkit-scrollbar-thumb:hover {
  background: rgba(0, 0, 0, 0.25);
}

.icon {
  font-size: 3rem;
  margin-bottom: 0.75rem;
  filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.1));
  transition: transform 0.3s ease;
}

.option-card:hover .icon {
  transform: scale(1.1);
}

h2 {
  font-size: clamp(1.7rem, 2.5vw, 2.1rem);
  margin-bottom: 0.5rem;
  color: #1a5276;
  font-weight: 700;
}

p {
  color: #2c3e50;
  margin-bottom: 1rem;
  line-height: 1.4;
  font-size: 1.15rem;
}

.features {
  list-style: none;
  padding: 0;
  margin: 0.75rem 0;
  text-align: left;
}

.features li {
  margin: 0.5rem 0;
  padding-left: 1.5rem;
  position: relative;
  color: #2c3e50;
  font-size: 1.1rem;
  transition: transform 0.2s ease;
}

.option-card:hover .features li {
  transform: translateX(5px);
}

.features li::before {
  content: "→";
  position: absolute;
  left: 0;
  color: #3498db;
  font-weight: bold;
  font-size: 1.2rem;
}

.select-button {
  width: 100%;
  padding: 0.8rem;
  border: none;
  border-radius: 0.5rem;
  background: #01579b;
  color: white;
  font-weight: 600;
  font-size: 1.05rem;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: 0.75rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.select-button:hover {
  background: #0277bd;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(1, 87, 155, 0.4);
}

.select-button svg {
  transition: transform 0.3s ease;
}

.select-button:hover svg {
  transform: translateX(3px);
}

.beach {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(248, 249, 250, 0.9) 100%);
  border-left: 4px solid #f39c12;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.beach .card-content {
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
  padding: 0 5px 0 0;
}

.pool {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(248, 249, 250, 0.9) 100%);
  border-left: 4px solid #3498db;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.pool .card-content {
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
  padding: 0 5px 0 0;
}

.continue-container {
  display: none;
}

.statistics-box {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 0.8rem;
  padding: 0.75rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
  margin-top: 0.5rem;
}

.statistics-box:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
}

.stat-icon {
  font-size: 1.25rem;
  flex-shrink: 0;
}

.stat-text {
  color: #01579b;
  font-size: 0.9rem;
  line-height: 1.4;
  margin: 0;
  font-weight: 500;
}

.beach-stat {
  border-left: 4px solid #f39c12;
}

.pool-stat {
  border-left: 4px solid #01579b;
}

.beach-image-container {
  position: relative;
  margin: 0.75rem auto;
  border-radius: 0.75rem;
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.3s ease;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  max-width: 80%;
  width: 240px;
  height: 160px;
}

.beach-image-container:hover {
  transform: scale(1.05);
}

.beach-condition-image {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
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
  transition: all 0.3s ease;
}

.beach-image-container:hover .image-overlay {
  padding-bottom: 1.5rem;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0.4), transparent);
}

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

.preventing-risk {
  text-align: center;
  margin-top: 1rem;
}

.preventing-risk h3 {
  color: #e74c3c;
  font-size: 1.2rem;
  margin: 0 10px;
  font-weight: 600;
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
}

.aussie-waters-heading {
  color: #e74c3c;
  font-size: 1.2rem;
  margin: 0 10px;
  font-weight: 600;
}

.line {
  height: 2px;
  width: 40px;
  flex-shrink: 1;
  background-color: #e74c3c;
}

.risk-link {
  color: #01579b;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
  border-bottom: 1px dashed #01579b;
  padding-bottom: 2px;
}

.risk-link:hover {
  color: #e74c3c;
  border-bottom-color: #e74c3c;
}

.prevention-images {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  margin-top: 1rem;
  flex-wrap: wrap;
  max-width: 100%;
  box-sizing: border-box;
}

.prevention-image-container {
  position: relative;
  border-radius: 0.75rem;
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.3s ease;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  width: 240px;
  height: 160px;
}

.prevention-image-container:hover {
  transform: scale(1.05);
}

.prevention-image {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
}

.facing-risk-link {
  margin-top: 1.5rem;
}

.facing-risk-link h3 {
  color: #e74c3c;
  font-size: 1.2rem;
  margin: 0 10px;
  font-weight: 600;
}

.risk-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  background: #e74c3c;
  color: white;
  padding: 0.8rem 1.5rem;
  border-radius: 2rem;
  font-weight: 600;
  text-decoration: none;
  box-shadow: 0 4px 15px rgba(231, 76, 60, 0.4);
  transition: all 0.3s ease;
  border: none;
  cursor: pointer;
  margin-top: 0.75rem;
}

.pool-image-container {
  position: relative;
  margin: 0.75rem auto;
  border-radius: 0.75rem;
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.3s ease;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  max-width: 80%;
  width: 240px;
  height: 160px;
  box-sizing: border-box;
}

.pool-image-container:hover {
  transform: scale(1.05);
}

.pool-condition-image {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
}

.pool-risk-heading {
  color: #e74c3c;
  font-size: 1.2rem;
  margin: 0 10px;
  font-weight: 600;
}

@media (max-width: 768px) {
  .home-page {
    height: auto;
    min-height: 100vh;
    padding: 2rem 0.75rem;
  }

  .content-wrapper {
    padding: 0.75rem;
  }

  .options-container {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }

  .option-card {
    padding: 1rem;
    min-height: 700px;
    height: auto;
    overflow-y: visible;
  }
  
  .card-content {
    overflow-y: visible;
  }

  .option-wrapper {
    gap: 0.75rem;
  }
  
  .statistics-box {
    padding: 0.6rem;
  }

  .stat-icon {
    font-size: 1.25rem;
  }

  .stat-text {
    font-size: 0.85rem;
  }

  .progress-steps {
    gap: 0.5rem;
    margin-bottom: 1.5rem;
  }

  .step-number {
    width: 1.75rem;
    height: 1.75rem;
    font-size: 0.9rem;
  }

  .step span {
    font-size: 0.8rem;
  }

  .step-connector {
    width: 1.5rem;
  }

  .icon {
    font-size: 2.75rem;
  }

  h2 {
    font-size: 1.4rem;
  }

  p {
    font-size: 0.95rem;
  }

  .features li {
    font-size: 0.9rem;
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
}

@media (max-width: 480px) {
  .home-page {
    padding: 1.5rem 0.5rem;
  }
  
  h1 {
    font-size: 1.8rem;
  }
  
  .progress-steps {
    flex-wrap: wrap;
    justify-content: space-between;
    gap: 0.25rem;
  }

  .step {
    flex: 1;
    min-width: 80px;
  }

  .step-connector {
    display: none;
  }
  
  .option-card {
    padding: 0.875rem;
    border-radius: 0.75rem;
    min-height: auto;
  }
  
  .features li {
    font-size: 0.85rem;
    margin: 0.4rem 0;
  }
  
  .select-button {
    padding: 0.6rem;
    font-size: 0.9rem;
  }

  .statistics-box {
    padding: 0.5rem;
  }

  .stat-text {
    font-size: 0.8rem;
  }

  .icon {
    font-size: 2.5rem;
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

/* For very tall screens, ensure content fits without scrolling */
@media (min-height: 900px) {
  .options-container {
    max-height: none;
  }
  
  .option-card {
    max-height: none;
  }
}

/* For very short screens, ensure content fits without scrolling */
@media (max-height: 700px) {
  .home-page {
    height: auto;
    min-height: 100vh;
    padding: 1rem 0;
  }
  
  h1 {
    font-size: 1.8rem;
    margin-bottom: 0.25rem;
  }
  
  .icon {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
  }
  
  h2 {
    font-size: 1.4rem;
    margin-bottom: 0.25rem;
  }
  
  p {
    font-size: 0.85rem;
    margin-bottom: 0.5rem;
  }
  
  .features {
    margin: 0.5rem 0;
  }
  
  .features li {
    margin: 0.3rem 0;
    font-size: 0.8rem;
  }
  
  .select-button {
    margin-top: 0.5rem;
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
</style> 