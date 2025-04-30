<template>
  <div class="home-page">
    <div class="bg-image"></div>
    <div class="overlay"></div>
    <div class="content-wrapper">
      <div class="header">
        <h1>Welcome to WaterWiseFamily</h1>
        <p class="emotional-hook">In Australia, drowning takes more young lives than any other accident — most never saw it coming.</p>
        
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
              <p>Essential knowledge for keeping your family safe at the beach</p>
              <ul class="features">
                <li>Understanding rip currents</li>
                <li>Wave safety protocols</li>
                <li>Beach condition awareness</li>
                <li>Emergency response</li>
              </ul>
            </div>
            <button class="select-button" @click="continueToSafety('beach')">
              <span>Start Beach Safety Guide</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </button>
        </div>
          <div class="statistics-box beach-stat">
            <div class="stat-icon">⚠️</div>
            <p class="stat-text">Nearly 50% of beach drownings involve immigrants.</p>
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
              <p>Comprehensive guide to pool safety and prevention</p>
              <ul class="features">
                <li>Active supervision techniques</li>
                <li>Pool barrier requirements</li>
                <li>Emergency preparedness</li>
                <li>Safety equipment guide</li>
        </ul>
      </div>
            <button class="select-button" @click="continueToSafety('pool')">
              <span>Start Pool Safety Guide</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </button>
        </div>
          <div class="statistics-box pool-stat">
            <div class="stat-icon">⚠️</div>
            <p class="stat-text">80% of child drownings happen in home pools.</p>
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
}
</script>

<style scoped>
.home-page {
  height: 100vh;
  position: relative;
  color: #ffffff;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
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
  font-size: clamp(2rem, 4vw, 3rem);
  margin-bottom: 0.5rem;
  color: #ffffff;
  font-weight: 800;
  letter-spacing: -0.02em;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
}

.emotional-hook {
  font-size: clamp(1rem, 1.8vw, 1.2rem);
  color: #ffffff;
  margin: 0.5rem auto 1rem;
  max-width: 800px;
  line-height: 1.4;
  font-weight: 500;
  text-align: center;
  font-style: italic;
  text-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
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
  gap: 1rem;
  width: 100%;
  animation: slideUp 0.8s ease-out 1.2s both;
  opacity: 0;
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
}

.option-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 1rem;
  padding: 1.25rem;
  position: relative;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.7);
  display: flex;
  flex-direction: column;
  height: 100%;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
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
}

.pool {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(248, 249, 250, 0.9) 100%);
  border-left: 4px solid #3498db;
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

@media (max-width: 768px) {
  .home-page {
    height: auto;
    min-height: 100vh;
    padding: 0.75rem;
  }

  .content-wrapper {
    padding: 0.75rem;
  }

  .options-container {
    grid-template-columns: 1fr;
    gap: 0.75rem;
  }

  .option-card {
    padding: 1rem;
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

  .emotional-hook {
    font-size: 0.95rem;
    margin: 0.75rem auto 1.5rem;
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
}

@media (max-width: 480px) {
  .home-page {
    padding: 0.5rem;
  }
  
  h1 {
    font-size: 1.8rem;
  }
  
  .emotional-hook {
    font-size: 0.95rem;
    margin: 0.5rem auto 1rem;
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
}

/* For very tall screens, ensure content fits without scrolling */
@media (min-height: 900px) {
  .options-container {
    max-height: 65vh;
  }
  
  .option-card {
    max-height: 100%;
  }
}

/* For very short screens, ensure content fits without scrolling */
@media (max-height: 700px) {
  .home-page {
    height: auto;
    min-height: 100vh;
  }
  
  h1 {
    font-size: 1.8rem;
    margin-bottom: 0.25rem;
  }
  
  .emotional-hook {
    font-size: 0.9rem;
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
</style> 