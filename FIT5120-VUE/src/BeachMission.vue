<template>
  <div class="beach-mission-page">
    <div class="bg-image"></div>
    <div class="overlay"></div>
    
    <!-- Beach Menu Component -->
    <BeachMenu :menuOpen="menuOpen" @toggle-menu="toggleMenu" />
    
    <div class="content-wrapper">
      <div class="main-content">
        <div class="title-section">
          <h1>Our Mission</h1>
        </div>

        <div class="content-section">
          <div class="mission-hero">
            <div class="mission-image">
              <img src="./assets/mission.jpeg" alt="Mother with child at beach" />
              <div class="mission-overlay">
                <div class="mission-quote-container">
                  <h2 class="mission-quote">The ocean is beautiful — but without knowledge, it can take what we love most.</h2>
                </div>
              </div>
            </div>
          </div>
          
          <div class="mission-flow">
            <div class="flow-section">
              <h3 class="flow-title">The Challenge</h3>
              <div class="flow-content">
                <div class="summary-icon">⚠️</div>
                <p>Beach safety knowledge doesn't develop automatically with time spent in Australia—even after decades of residency, the risk remains.</p>
              </div>
            </div>
            
            <div class="flow-section">
              <h3 class="flow-title">Drowning Risk Based on Years of Residency</h3>
              <div class="risk-timeline">                      
                <div class="risk-card high-risk" @click="flipCard($event)">
                  <div class="card-front">
                    <div class="risk-header">
                      <div class="risk-years">0-5 Years</div>
                      <div class="risk-level">
                        <span class="risk-badge">Highest Risk</span>
                        <div class="risk-icon">⚠️⚠️⚠️</div>
                      </div>
                    </div>
                    <div class="risk-phase">Unfamiliarity Phase</div>
                    <div class="flip-prompt">Click for more info</div>
                  </div>
                  <div class="card-back">
                    <div class="back-header">Unfamiliarity Phase</div>
                    <div class="back-stat">40% of drownings</div>
                    <div class="back-content">
                      <ul class="back-list">
                        <li>No recognition of rip currents</li>
                        <li>Swimming skills unsuited to ocean conditions</li>
                      </ul>
                    </div>
                    <div class="flip-prompt">Click to flip back</div>
                  </div>
                </div>
                
                <div class="risk-card medium-risk" @click="flipCard($event)">
                  <div class="card-front">
                    <div class="risk-header">
                      <div class="risk-years">5-20 Years</div>
                      <div class="risk-level">
                        <span class="risk-badge">Moderate Risk</span>
                        <div class="risk-icon">⚠️⚠️</div>
                      </div>
                    </div>
                    <div class="risk-phase">Adaptation Phase</div>
                    <div class="flip-prompt">Click for more info</div>
                  </div>
                  <div class="card-back">
                    <div class="back-header">Adaptation Phase</div>
                    <div class="back-stat">Growing awareness</div>
                    <div class="back-content">
                      <ul class="back-list">
                        <li>Some awareness through exposure</li>
                        <li>Cultural attitudes still influence safety</li>
                      </ul>
                    </div>
                    <div class="flip-prompt">Click to flip back</div>
                  </div>
                </div>
                
                <div class="risk-card persistent-risk" @click="flipCard($event)">
                  <div class="card-front">
                    <div class="risk-header">
                      <div class="risk-years">20+ Years</div>
                      <div class="risk-level">
                        <span class="risk-badge">Persistent Risk</span>
                        <div class="risk-icon">⚠️</div>
                      </div>
                    </div>
                    <div class="risk-phase">False Confidence Phase</div>
                    <div class="flip-prompt">Click for more info</div>
                  </div>
                  <div class="card-back">
                    <div class="back-header">False Confidence Phase</div>
                    <div class="back-stat">26% lived here 30+ years</div>
                    <div class="back-content">
                      <ul class="back-list">
                        <li>False confidence without education</li>
                        <li>Cannot pass safety knowledge to children</li>
                      </ul>
                    </div>
                    <div class="flip-prompt">Click to flip back</div>
                  </div>
                </div>
              </div>
            </div>
            
            <div class="flow-section">
              <h3 class="flow-title">Mission Statement</h3>
              <div class="flow-content solution-content">
                <div class="summary-icon">🎓</div>
                <p>We believe every family deserves to enjoy Australia's beautiful beaches safely. That's why we're dedicated to arming immigrant parents with life-saving knowledge—breaking the generational cycle of water safety gaps and ensuring no child is lost to preventable tragedy.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import BeachMenu from './components/BeachMenu.vue'

export default {
  name: 'BeachMission',
  components: {
    BeachMenu
  },
  data() {
    return {
      menuOpen: false
    }
  },
  mounted() {
    // Set the active navigation link for this page
    this.setActiveNavLink();
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
      
      // Add active class to our mission links
      const desktopMissionLink = document.querySelector('.nav-link[href="/our-mission"]');
      const mobileMissionLink = document.querySelector('.mobile-nav-link[href="/our-mission"]');
      
      if (desktopMissionLink) desktopMissionLink.classList.add('active');
      if (mobileMissionLink) mobileMissionLink.classList.add('active');
    },
    flipCard(event) {
      // Find the closest risk-card parent element
      const card = event.currentTarget;
      
      // Toggle the 'flipped' class to trigger the CSS transition
      card.classList.toggle('flipped');
      
      // Prevent any parent elements from receiving the click event
      event.stopPropagation();
    }
  }
}
</script>

<style scoped>
  .beach-mission-page {
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
    font-size: clamp(2.2rem, 5vw, 3rem);
    margin: 0 0 1rem;
    color: #ffffff;
    font-weight: 800;
    letter-spacing: -0.02em;
    text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
  }
  
  .content-section {
    background: rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(10px);
    border-radius: 1rem;
    padding: 2rem;
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
  
  .mission-hero {
    background: rgba(0, 0, 0, 0.2);
    border-radius: 1rem;
    padding: 2rem;
    margin-bottom: 2rem;
    border-left: 4px solid #f39c12;
    animation: fadeIn 1s ease-out 0.5s both;
  }
  
  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }
  
  .mission-image {
    position: relative;
    height: 400px;
    border-radius: 0.75rem;
    overflow: hidden;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
  }
  
  .mission-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center bottom;
    transform: scale(1);
    transition: transform 0.3s ease;
  }
  
  .mission-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to bottom, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.1));
    border-radius: 0.75rem;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding-top: 0;
    padding-left: 0;
    padding-right: 0;
    text-align: center;
  }
  
  .mission-quote-container {
    max-width: 100%;
    width: 100%;
    background-color: rgba(0, 0, 0, 0.6);
    padding: 1rem;
    margin-top: 0;
    border-top-left-radius: 0.75rem;
    border-top-right-radius: 0.75rem;
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
  }
  
  .mission-quote {
    font-size: 1.4rem;
    color: #ffffff;
    margin: 0;
    font-weight: 700;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.7);
    line-height: 1.4;
    font-style: italic;
  }
  
  .mission-flow {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }
  
  .flow-section {
    background: rgba(0, 0, 0, 0.2);
    border-radius: 0.75rem;
    overflow: hidden;
  }
  
  .flow-title {
    font-size: 1.4rem;
    color: #f39c12;
    margin: 0;
    padding: 1rem 1.5rem;
    background: rgba(0, 0, 0, 0.2);
    font-weight: 600;
  }
  
  .flow-content {
    padding: 1.5rem;
    display: flex;
    align-items: center;
    gap: 1rem;
  }
  
  .summary-icon {
    font-size: 2.2rem;
    color: #f39c12;
    min-width: 2.2rem;
    text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
  }
  
  .flow-content p {
    margin: 0;
    line-height: 1.6;
    font-size: 1.15rem;
  }
  
  .solution-content .summary-icon {
    color: #2ecc71;
  }
  
  .risk-timeline {
    display: flex;
    flex-wrap: wrap;
    gap: 1.5rem;
    padding: 1.5rem;
  }
  
  .risk-card {
    flex: 1;
    min-width: 280px;
    border-radius: 0.75rem;
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
    overflow: hidden;
    transition: transform 0.3s ease;
    padding: 0;
    display: flex;
    flex-direction: column;
    text-align: center;
    position: relative;
    transform-style: preserve-3d;
    perspective: 1000px;
    cursor: pointer;
    height: 250px;
  }
  
  .risk-card:hover {
    transform: translateY(-5px);
  }
  
  .card-front, 
  .card-back {
    backface-visibility: hidden;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    transition: transform 0.6s cubic-bezier(0.4, 0.0, 0.2, 1);
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  
  .card-front {
    transform: rotateY(0deg);
    z-index: 2;
    display: flex;
    flex-direction: column;
  }
  
  .card-back {
    transform: rotateY(180deg);
    background: inherit;
    padding: 1.5rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  
  .risk-card.flipped .card-front {
    transform: rotateY(180deg);
  }
  
  .risk-card.flipped .card-back {
    transform: rotateY(0deg);
  }
  
  .risk-card.high-risk {
    background: linear-gradient(145deg, rgba(231, 76, 60, 0.85), rgba(192, 57, 43, 0.85));
  }
  
  .risk-card.medium-risk {
    background: linear-gradient(145deg, rgba(241, 196, 15, 0.85), rgba(243, 156, 18, 0.85));
  }
  
  .risk-card.persistent-risk {
    background: linear-gradient(145deg, rgba(52, 152, 219, 0.85), rgba(41, 128, 185, 0.85));
  }
  
  .risk-header {
    padding: 1rem;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    justify-content: center;
    align-items: center;
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    background: rgba(0, 0, 0, 0.15);
  }
  
  .risk-years {
    font-weight: 800;
    font-size: 1.2rem;
    color: white;
    text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
    margin-bottom: 0.5rem;
  }
  
  .risk-level {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
  }
  
  .risk-badge {
    background: rgba(255, 255, 255, 0.2);
    padding: 0.25rem 0.75rem;
    border-radius: 1rem;
    font-weight: 600;
    font-size: 0.85rem;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }
  
  .risk-icon {
    font-size: 1.5rem;
    color: #ffffff;
    text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
    line-height: 1;
  }
  
  .risk-phase {
    font-size: 1.3rem;
    color: white;
    padding: 1rem 1rem 0.5rem;
    font-weight: 600;
    margin-top: 0.5rem;
  }
  
  .back-header {
    font-size: 1.4rem;
    color: white;
    margin-bottom: 0.3rem;
    font-weight: 600;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
  }
  
  .back-stat {
    font-size: 1.1rem;
    color: rgba(255, 255, 255, 0.95);
    padding: 0 1rem 0.5rem;
    font-weight: 500;
  }
  
  .back-content {
    font-size: 1.1rem;
    color: rgba(255, 255, 255, 0.95);
    line-height: 1.4;
  }
  
  .back-list {
    list-style-type: disc;
    padding-left: 1.5rem;
    text-align: left;
    margin: 0 0 0.5rem 0;
  }
  
  .back-list li {
    margin-bottom: 0.4rem;
  }
  
  .flip-prompt {
    font-size: 0.9rem;
    color: rgba(255, 255, 255, 0.8);
    text-align: center;
    margin-top: auto;
    padding-top: 0.5rem;
    text-decoration: underline;
    font-weight: 500;
  }
  
  .card-front .flip-prompt {
    margin-top: 0.5rem;
  }
  
  @media (max-width: 768px) {
    .content-section {
      padding: 1.5rem;
    }
    
    .mission-hero {
      padding: 1.5rem;
    }
    
    .mission-image {
      height: 350px;
    }
    
    .mission-quote-container {
      max-width: 100%;
      width: 100%;
      padding: 0.75rem;
    }
    
    .mission-quote {
      font-size: 1.2rem;
    }
    
    .flow-title {
      font-size: 1.3rem;
      padding: 0.85rem 1.25rem;
    }
    
    .flow-content {
      padding: 1.25rem;
    }
    
    .summary-icon {
      font-size: 2rem;
    }
    
    .flow-content p {
      font-size: 1.05rem;
    }
    
    .risk-timeline {
      flex-direction: column;
      padding: 1.25rem;
      gap: 1.25rem;
    }
    
    .risk-card {
      min-width: 100%;
      height: 240px;
    }
    
    .risk-phase {
      font-size: 1.2rem;
      padding: 0.75rem 0.75rem 0.4rem;
    }
    
    .card-front .flip-prompt {
      margin-top: 0.3rem;
    }
    
    .back-header {
      font-size: 1.3rem;
    }
    
    .back-stat {
      font-size: 1.1rem;
      padding: 0 1rem 0.5rem;
    }
    
    .back-content {
      font-size: 1.1rem;
    }
    
    .back-list li {
      margin-bottom: 0.4rem;
    }
  }
  
  @media (max-width: 480px) {
    .content-section {
      padding: 1.25rem;
      width: 95%;
    }
    
    .mission-hero {
      padding: 1.25rem;
    }
    
    .mission-image {
      height: 300px;
    }
    
    .mission-quote-container {
      max-width: 100%;
      width: 100%;
      padding: 0.5rem;
    }
    
    .mission-quote {
      font-size: 1rem;
    }
    
    .flow-title {
      font-size: 1.2rem;
      padding: 0.75rem 1rem;
    }
    
    .flow-content {
      padding: 1rem;
      flex-direction: column;
      align-items: flex-start;
    }
    
    .summary-icon {
      font-size: 1.8rem;
      margin-bottom: 0.5rem;
    }
    
    .flow-content p {
      font-size: 1rem;
    }
    
    .risk-timeline {
      padding: 1rem;
      gap: 1rem;
    }
    
    .risk-card {
      height: 220px;
    }
    
    .risk-header {
      padding: 0.85rem;
    }
    
    .risk-phase {
      font-size: 1.1rem;
      padding: 0.5rem 0.5rem 0.3rem;
    }
    
    .card-front .flip-prompt {
      margin-top: 0.2rem;
    }
    
    .back-header {
      font-size: 1.2rem;
      margin-bottom: 0.3rem;
    }
    
    .back-stat {
      font-size: 1.1rem;
      padding: 0 1rem 0.5rem;
    }
    
    .back-content {
      font-size: 1rem;
    }
    
    .back-list {
      padding-left: 1.2rem;
    }
    
    .back-list li {
      margin-bottom: 0.3rem;
    }
    
    .flip-prompt {
      font-size: 0.8rem;
      padding-top: 0.5rem;
    }
  }
</style> 