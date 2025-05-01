<template>
  <div class="rip-safety-page">
    <div class="bg-image"></div>
    <div class="overlay"></div>
    
    <!-- Beach Menu Component -->
    <BeachMenu :menuOpen="menuOpen" @toggle-menu="toggleMenu" />
    
    <div class="content-wrapper">
      <div class="main-content">
        <div class="rip-progress-nav">
          <div class="progress-bar">
            <div class="progress-step">
              <router-link to="/beach-safety-rescue" class="step-link">
                <div class="step-number">1</div>
                <div class="step-label">Signs of Trouble</div>
              </router-link>
            </div>
            <div class="progress-connector"></div>
            <div class="progress-step">
              <router-link to="/survive-rip-currents" class="step-link">
                <div class="step-number">2</div>
                <div class="step-label">Survive Rip Currents</div>
              </router-link>
            </div>
            <div class="progress-connector"></div>
            <div class="progress-step active">
              <div class="step-number">3</div>
              <div class="step-label">Safety Tools</div>
            </div>
          </div>
        </div>
        
        <div class="title-section">
          <h1>Beach Safety Tools</h1>
          <div class="statistic-banner">
          </div>
        </div>

        <div class="content-section">
          <h2 class="section-title">🔄 Rip Current Escape Simulation</h2>
          
          <div class="section-body">
            <p>Our interactive simulation helps you and your children understand the proper techniques for escaping rip currents. Visualize and practice the correct response in a safe, virtual environment.</p>
            
            <div v-if="!simulationActive" class="simulation-image-container">
              <img 
                src="./assets/Swimmer-in-a-rip.jpg" 
                alt="Swimmer caught in a rip current" 
                class="simulation-image"
                @error="handleImageError"
              >
              <div class="image-overlay-button">
                <button @click="activateSimulation" class="simulation-btn">
                  <span class="btn-icon">▶</span>
                  <span class="btn-text">Start Simulation</span>
                </button>
              </div>
            </div>
            
            <div v-if="simulationActive" class="simulation-container">
              <div class="simulation-active">
                <div class="simulation-content">
                  <!-- Simulation content goes here -->
                  <RipEscapeSimulation />
                  
                  <!-- Fullscreen prompt -->
                  <div v-if="showFullscreenPrompt" class="fullscreen-prompt">
                    <div class="prompt-content">
                      <svg class="arrow-pointer left" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="19" y1="12" x2="5" y2="12"></line>
                        <polyline points="12 5 5 12 12 19"></polyline>
                      </svg>
                      <span>Click fullscreen for best experience</span>
                    </div>
                  </div>
                </div>
                <div class="back-button-container">
                  <button @click="deactivateSimulation" class="back-btn">
                    <span class="btn-text">Back to Safety Tools</span>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="content-section">
          <h2 class="section-title">🧒 Child-Friendly Teaching Resources</h2>
          
          <div class="section-body">
            <p>Use these resources to teach children about rip current safety in an age-appropriate way:</p>
            
            <div class="teaching-resources">
              <div class="teaching-resource">
                <div class="resource-header">
                  <div class="resource-age">Children</div>
                  <h4>Rip Current Safety Quiz</h4>
                </div>
                <p>Age-appropriate quiz helping children identify rip currents and learn essential beach safety actions.</p>
                <button @click="startQuiz('child')" class="download-link">Take Quiz</button>
              </div>
              
              <div class="teaching-resource">
                <div class="resource-header">
                  <div class="resource-age">Parents</div>
                  <h4>Family Beach Safety Quiz</h4>
                </div>
                <p>Advanced quiz covering rip current identification, rescue techniques, and family safety planning.</p>
                <button @click="startQuiz('parent')" class="download-link">Take Quiz</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Child Quiz Popup -->
    <div class="quiz-overlay" v-if="showChildQuiz" @click.self="closeQuiz">
      <div class="quiz-container child-quiz">
        <div class="quiz-header">
          <h3>Rip Current Safety Quiz for Children</h3>
          <button class="close-btn" @click="closeQuiz">&times;</button>
        </div>
        
        <div v-if="!quizCompleted" class="quiz-content">
          <div class="quiz-progress">
            <span>Question {{ quizStep + 1 }} of {{ totalQuizQuestions }}</span>
            <div class="quiz-progress-bar">
              <div class="quiz-progress-fill" :style="{ width: `${(quizStep / totalQuizQuestions) * 100}%` }"></div>
            </div>
          </div>
          
          <div class="question-container">
            <h4 class="question">{{ currentQuizQuestion.question }}</h4>
            <div class="options">
              <button 
                v-for="(option, index) in currentQuizQuestion.options" 
                :key="index" 
                class="option-btn"
                :class="{ 'correct': currentQuizQuestion.correctAnswer === index && selectedOption === index,
                          'incorrect': currentQuizQuestion.correctAnswer !== index && selectedOption === index }"
                @click="selectedOption = index"
                :disabled="selectedOption !== null">
                {{ option }}
              </button>
            </div>
          </div>
          
          <div v-if="selectedOption !== null" class="feedback">
            <div :class="['feedback-content', selectedOption === currentQuizQuestion.correctAnswer ? 'correct-feedback' : 'incorrect-feedback']">
              <div class="feedback-icon">
                <svg v-if="selectedOption === currentQuizQuestion.correctAnswer" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
                <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <line x1="18" y1="6" x2="6" y2="18"></line>
                  <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>
              </div>
              <p>{{ currentQuizQuestion.explanation }}</p>
              <button @click="nextQuizStep(selectedOption === currentQuizQuestion.correctAnswer); selectedOption = null" class="next-btn">Next Question</button>
            </div>
          </div>
        </div>
        
        <div v-else class="quiz-results">
          <div class="results-container">
            <h4>Quiz Complete!</h4>
            <div class="score">
              <div class="score-circle">
                <span class="score-text">{{ quizScore }}/{{ totalQuizQuestions }}</span>
              </div>
              <p v-if="quizScore === totalQuizQuestions">Perfect score! You're a beach safety expert!</p>
              <p v-else-if="quizScore >= totalQuizQuestions * 0.7">Great job! You know a lot about beach safety!</p>
              <p v-else>Good effort! Keep learning about beach safety!</p>
            </div>
            <div class="result-actions">
              <button @click="restartQuiz" class="restart-btn">Take Quiz Again</button>
              <button @click="closeQuiz" class="close-quiz-btn">Close Quiz</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Parent Quiz Popup -->
    <div class="quiz-overlay" v-if="showParentQuiz" @click.self="closeQuiz">
      <div class="quiz-container parent-quiz">
        <div class="quiz-header">
          <h3>Family Beach Safety Quiz for Parents</h3>
          <button class="close-btn" @click="closeQuiz">&times;</button>
        </div>
        
        <div v-if="!quizCompleted" class="quiz-content">
          <div class="quiz-progress">
            <span>Question {{ quizStep + 1 }} of {{ totalQuizQuestions }}</span>
            <div class="quiz-progress-bar">
              <div class="quiz-progress-fill" :style="{ width: `${(quizStep / totalQuizQuestions) * 100}%` }"></div>
            </div>
          </div>
          
          <div class="question-container">
            <h4 class="question">{{ currentQuizQuestion.question }}</h4>
            <div class="options">
              <button 
                v-for="(option, index) in currentQuizQuestion.options" 
                :key="index" 
                class="option-btn"
                :class="{ 'correct': currentQuizQuestion.correctAnswer === index && selectedOption === index,
                          'incorrect': currentQuizQuestion.correctAnswer !== index && selectedOption === index }"
                @click="selectedOption = index"
                :disabled="selectedOption !== null">
                {{ option }}
              </button>
            </div>
          </div>
          
          <div v-if="selectedOption !== null" class="feedback">
            <div :class="['feedback-content', selectedOption === currentQuizQuestion.correctAnswer ? 'correct-feedback' : 'incorrect-feedback']">
              <div class="feedback-icon">
                <svg v-if="selectedOption === currentQuizQuestion.correctAnswer" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
                <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <line x1="18" y1="6" x2="6" y2="18"></line>
                  <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>
              </div>
              <p>{{ currentQuizQuestion.explanation }}</p>
              <button @click="nextQuizStep(selectedOption === currentQuizQuestion.correctAnswer); selectedOption = null" class="next-btn">Next Question</button>
            </div>
          </div>
        </div>
        
        <div v-else class="quiz-results">
          <div class="results-container">
            <h4>Quiz Complete!</h4>
            <div class="score">
              <div class="score-circle">
                <span class="score-text">{{ quizScore }}/{{ totalQuizQuestions }}</span>
              </div>
              <p v-if="quizScore === totalQuizQuestions">Perfect score! You're a beach safety expert!</p>
              <p v-else-if="quizScore >= totalQuizQuestions * 0.7">Great job! You know a lot about beach safety!</p>
              <p v-else>Good effort! Keep learning about beach safety!</p>
            </div>
            <div class="result-actions">
              <button @click="restartQuiz" class="restart-btn">Take Quiz Again</button>
              <button @click="closeQuiz" class="close-quiz-btn">Close Quiz</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import BeachMenu from './components/BeachMenu.vue'
import RipEscapeSimulation from './RipEscapeSimulation.vue'

export default {
  name: 'SafetyTool',
  components: {
    BeachMenu,
    RipEscapeSimulation
  },
  data() {
    return {
      menuOpen: false,
      simulationActive: false,
      showFullscreenPrompt: false,
      showChildQuiz: false,
      showParentQuiz: false,
      currentQuizType: null,
      quizStep: 0,
      childScore: 0,
      parentScore: 0,
      quizCompleted: false,
      selectedOption: null
    }
  },
  mounted() {
    // Set the active navigation link for this page
    this.setActiveNavLink();
  },
  beforeDestroy() {
    // No scroll event listeners to remove
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
      
      // Add active class to Beach Safety links
      const desktopBeachLink = document.querySelector('.nav-link[href="/beach-safety-rescue"]');
      const mobileBeachLink = document.querySelector('.mobile-nav-link[href="/beach-safety-rescue"]');
      
      if (desktopBeachLink) desktopBeachLink.classList.add('active');
      if (mobileBeachLink) mobileBeachLink.classList.add('active');
    },
    activateSimulation() {
      this.simulationActive = true;
      
      // Show fullscreen prompt
      this.showFullscreenPrompt = true;
      
      // Hide prompt after 7 seconds
      setTimeout(() => {
        this.showFullscreenPrompt = false;
      }, 7000);
    },
    deactivateSimulation() {
      this.simulationActive = false;
      this.showFullscreenPrompt = false;
    },
    
    startQuiz(type) {
      this.currentQuizType = type;
      this.quizStep = 0;
      this.quizCompleted = false;
      
      if (type === 'child') {
        this.showChildQuiz = true;
        this.childScore = 0;
      } else {
        this.showParentQuiz = true;
        this.parentScore = 0;
      }
    },
    
    closeQuiz() {
      this.showChildQuiz = false;
      this.showParentQuiz = false;
      this.currentQuizType = null;
      this.quizStep = 0;
      this.selectedOption = null;
    },
    
    nextQuizStep(isCorrect) {
      if (isCorrect) {
        if (this.currentQuizType === 'child') {
          this.childScore++;
        } else {
          this.parentScore++;
        }
      }
      
      // Move to next question
      this.quizStep++;
      
      // Check if quiz is complete
      if (this.currentQuizType === 'child' && this.quizStep >= this.childQuizQuestions.length) {
        this.quizCompleted = true;
      } else if (this.currentQuizType === 'parent' && this.quizStep >= this.parentQuizQuestions.length) {
        this.quizCompleted = true;
      }
    },
    
    restartQuiz() {
      this.quizStep = 0;
      this.quizCompleted = false;
      
      if (this.currentQuizType === 'child') {
        this.childScore = 0;
      } else {
        this.parentScore = 0;
      }
    },
    handleResourceImageError(e) {
      // Add a fallback class to show a styled message
      e.target.classList.add('image-error');
      // Clear the source to prevent further error attempts
      e.target.src = '';
      // Add an error container with a message
      const container = e.target.closest('.resource-image-container');
      if (container) {
        container.classList.add('error-container');
      }
    },
    handleImageError(e) {
      // Add a fallback class to show a styled message
      e.target.classList.add('image-error');
      // Clear the source to prevent further error attempts
      e.target.src = '';
      // Add an error container with a message
      const container = e.target.closest('.simulation-image-container');
      if (container) {
        container.classList.add('error-container');
      }
    }
  },
  computed: {
    childQuizQuestions() {
      return [
        {
          question: "What color flag at the beach means it's dangerous to swim?",
          options: ["Green", "Yellow", "Red", "Blue"],
          correctAnswer: 2, // Red
          explanation: "A red flag means dangerous conditions like strong rip currents are present. Never swim when red flags are up!"
        },
        {
          question: "What should you do if caught in a rip current?",
          options: [
            "Swim straight back to shore",
            "Swim parallel to the shore",
            "Try to touch the bottom",
            "Wave for help while swimming toward shore"
          ],
          correctAnswer: 1, // Swim parallel
          explanation: "Swimming parallel to the shore is the best way to escape a rip current. Once you're out of the current, you can swim back to shore."
        },
        {
          question: "How can you identify a rip current?",
          options: [
            "Water that looks calm",
            "A line of foam moving away from shore",
            "Waves that look bigger than others",
            "Water that has lots of seaweed"
          ],
          correctAnswer: 1, // line of foam
          explanation: "Rip currents often appear as a line of foam, discolored water, or a break in the incoming wave pattern moving away from shore."
        },
        {
          question: "What should you NEVER do in a rip current?",
          options: [
            "Float on your back",
            "Signal for help",
            "Panic and fight against the current",
            "Swim parallel to shore"
          ],
          correctAnswer: 2, // Panic and fight
          explanation: "Never panic or fight against the current - this will tire you out quickly. Stay calm and swim parallel to shore."
        },
        {
          question: "Where is the safest place to swim at the beach?",
          options: [
            "Between the flags at a patrolled beach",
            "Where there are no waves",
            "Where the water looks calmest",
            "Far away from other swimmers"
          ],
          correctAnswer: 0, // Between flags
          explanation: "Always swim between the flags at a patrolled beach. Lifeguards place these flags in the safest areas."
        }
      ];
    },
    parentQuizQuestions() {
      return [
        {
          question: "Which of the following is NOT a common indicator of a rip current?",
          options: [
            "A gap in the breaking waves",
            "Discolored water extending beyond the surf zone",
            "Churning, choppy surface water",
            "Water that appears brighter and more colorful than surrounding water"
          ],
          correctAnswer: 3, // Brighter water
          explanation: "Rip currents typically appear as darker, not brighter water. Other signs include gaps in breaking waves, sandy/discolored water, and debris moving seaward."
        },
        {
          question: "Approximately what percentage of beach rescues are related to rip currents?",
          options: ["Around 20%", "Around 40%", "Around 60%", "Around 80%"],
          correctAnswer: 3, // 80%
          explanation: "Rip currents account for approximately 80% of beach rescues performed by lifeguards."
        },
        {
          question: "What is the most effective strategy if you see someone caught in a rip current?",
          options: [
            "Immediately swim out to rescue them",
            "Throw them a flotation device if possible and call for help",
            "Shout instructions to swim directly back to shore",
            "Wait to see if they can get out on their own"
          ],
          correctAnswer: 1, // Throw flotation device
          explanation: "Never enter the water to rescue someone unless trained. Throw them a flotation device if possible and get help from lifeguards. Many would-be rescuers drown."
        },
        {
          question: "At what time of year can rip currents occur?",
          options: [
            "Only during summer months",
            "Only during stormy weather",
            "Only during high tide",
            "Any time of year in the right conditions"
          ],
          correctAnswer: 3, // Any time
          explanation: "Rip currents can occur at any time of year when the right conditions exist, regardless of season or weather."
        },
        {
          question: "What is the most dangerous misconception about rip currents?",
          options: [
            "That they pull you under water",
            "That they only occur during storms",
            "That they are easy to spot",
            "That they only affect poor swimmers"
          ],
          correctAnswer: 0, // Pull under
          explanation: "Rip currents don't pull you under water; they pull you away from shore. Many drownings occur when people exhaust themselves swimming against the current."
        },
        {
          question: "What should be included in a family beach safety plan?",
          options: [
            "Just telling children to stay close",
            "A designated meeting point, identification of nearest lifeguard, and water entry rules",
            "Allowing children to swim anywhere as long as they're with friends",
            "Focusing only on sun protection"
          ],
          correctAnswer: 1, // Meeting point, lifeguard, rules
          explanation: "A comprehensive beach safety plan should include a meeting point if separated, identifying the nearest lifeguard, establishing clear rules about water entry, and educating all family members about beach flags and hazards."
        }
      ];
    },
    currentQuizQuestion() {
      if (this.currentQuizType === 'child') {
        return this.quizStep < this.childQuizQuestions.length ? this.childQuizQuestions[this.quizStep] : null;
      } else {
        return this.quizStep < this.parentQuizQuestions.length ? this.parentQuizQuestions[this.quizStep] : null;
      }
    },
    quizScore() {
      return this.currentQuizType === 'child' ? this.childScore : this.parentScore;
    },
    totalQuizQuestions() {
      return this.currentQuizType === 'child' ? this.childQuizQuestions.length : this.parentQuizQuestions.length;
    }
  }
}
</script>

<style scoped>
.rip-safety-page {
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

.section-body {
  font-size: clamp(0.95rem, 1.5vw, 1.05rem);
  line-height: 1.6;
  width: 100%;
  margin: 0 auto;
}

.section-body p {
  margin-bottom: 1rem;
}

.resource-image-container {
  width: 70%;
  max-width: 600px;
  margin: 0 auto 1.5rem;
  border-radius: 0.8rem;
  overflow: hidden;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.resource-header-image {
  width: 100%;
  height: auto;
  display: block;
  object-fit: cover;
}

.image-error {
  min-height: 200px;
  background-color: rgba(1, 54, 92, 0.7);
  position: relative;
}

.image-error::after {
  content: "Image not available";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: rgba(255, 255, 255, 0.8);
  font-style: italic;
  font-size: 1.1rem;
}

.error-container {
  background-color: rgba(1, 54, 92, 0.7);
  position: relative;
}

.context-text {
  background: rgba(0, 0, 0, 0.2);
  padding: 1rem 1.5rem;
  border-radius: 0.8rem;
  border-left: 4px solid #f39c12;
  font-style: italic;
  margin-bottom: 1.5rem;
  font-size: clamp(0.95rem, 1.5vw, 1.05rem);
  line-height: 1.6;
}

.simulation-image-container {
  width: 100%;
  max-width: 800px;
  margin: 0 auto 1.5rem;
  border-radius: 0.8rem;
  overflow: hidden;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
  position: relative;
}

.simulation-image {
  width: 100%;
  height: auto;
  display: block;
  object-fit: cover;
}

.image-overlay-button {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.4);
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.3s ease;
}

.image-overlay-button:hover {
  background: rgba(0, 0, 0, 0.6);
}

.image-overlay-button .simulation-btn {
  transform: scale(1);
  transition: transform 0.3s ease, background-color 0.3s ease, box-shadow 0.3s ease;
}

.image-overlay-button:hover .simulation-btn {
  transform: scale(1.1);
  background: #e67e22;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.5);
}

.simulation-container {
  margin: 1.5rem 0;
}

.rip-progress-nav {
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
  flex: 1;
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
  width: 100%;
  height: 2px;
  background: rgba(255, 255, 255, 0.3);
  margin: 0 0.5rem;
  position: relative;
  top: -8px;
  flex: 1;
  max-width: 100px;
}

/* Simulation container styles */
.simulation-container {
  margin: 1.5rem 0;
}

.simulation-buttons {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 2rem 0;
  gap: 1.5rem;
}

.simulation-btn {
  background: #f39c12;
  color: white;
  font-weight: 700;
  font-size: 1.4rem;
  padding: 1.2rem 2.5rem;
  border-radius: 2rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  text-decoration: none;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
  transition: all 0.3s ease;
  border: none;
  cursor: pointer;
}

.simulation-btn:hover {
  background: #e67e22;
  transform: translateY(-5px);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
}

.btn-icon {
  font-size: 1.6rem;
}

.back-button-container {
  display: flex;
  justify-content: center;
  padding: 1.5rem 0;
  width: 100%;
}

.back-btn {
  background: #3498db;
  color: white;
  text-decoration: none;
  padding: 0.8rem 1.5rem;
  border-radius: 2rem;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1rem;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.back-btn:hover {
  background: #2980b9;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
}

/* Active simulation styles */
.simulation-active {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  width: 100%;
}

.simulation-content {
  background: rgba(1, 54, 92, 0.8);
  border-radius: 1rem;
  padding: 0;
  min-height: 600px;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.4);
  animation: expandSimulation 0.5s ease-out both;
  width: 100%;
  overflow: hidden;
}

.simulation-content :deep(.simulation-wrapper) {
  width: 100%;
  height: 100%;
  padding: 0;
}

.simulation-content :deep(.container-small) {
  border-radius: 0;
  width: 100%;
  height: 600px;
  box-shadow: none;
  border: none;
}

@keyframes expandSimulation {
  from { transform: scale(0.9); opacity: 0; }
  to { transform: scale(1); opacity: 1; }
}

.simulation-placeholder {
  text-align: center;
  color: white;
}

.simulation-placeholder h3 {
  font-size: 1.8rem;
  margin-bottom: 1rem;
  color: #f39c12;
}

.simulation-placeholder p {
  font-size: 1.2rem;
  color: rgba(255, 255, 255, 0.9);
}

/* Teaching resources styles */
.teaching-resources {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 1.5rem 0;
}

.teaching-resource {
  background: rgba(1, 54, 92, 0.7);
  border-radius: 0.75rem;
  padding: 1.5rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  height: 100%;
}

.resource-header {
  margin-bottom: 1rem;
}

.resource-age {
  background: #f39c12;
  color: white;
  font-weight: 700;
  font-size: 1.2rem;
  padding: 0.5rem 1.2rem;
  border-radius: 2rem;
  display: inline-block;
  margin-bottom: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.teaching-resource h4 {
  color: white;
  margin: 0 0 0.75rem;
  font-size: 1.1rem;
  font-weight: 600;
}

.teaching-resource p {
  margin: 0 0 1.5rem;
  flex-grow: 1;
  font-size: 0.95rem;
}

.download-link {
  background: #3498db;
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 2rem;
  font-weight: 600;
  display: inline-block;
  transition: all 0.2s ease;
  align-self: flex-start;
  border: none;
  cursor: pointer;
}

.download-link:hover {
  background: #2980b9;
  transform: translateY(-2px);
}

/* Quiz styles */
.quiz-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  backdrop-filter: blur(5px);
  padding: 1rem;
}

.quiz-container {
  background: linear-gradient(to bottom, rgba(1, 54, 92, 0.95), rgba(1, 54, 92, 0.85));
  border-radius: 1rem;
  width: 100%;
  max-width: 800px;
  max-height: 80vh;
  overflow-y: auto;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: white;
  animation: fadeIn 0.3s ease-out;
}

.child-quiz {
  border-top: 5px solid #f39c12;
}

.parent-quiz {
  border-top: 5px solid #3498db;
}

.quiz-header {
  padding: 1.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.quiz-header h3 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 600;
}

.close-btn {
  background: none;
  border: none;
  color: white;
  font-size: 1.8rem;
  cursor: pointer;
  line-height: 1;
  padding: 0;
  margin: 0;
  opacity: 0.7;
  transition: opacity 0.2s;
}

.close-btn:hover {
  opacity: 1;
}

.quiz-content {
  padding: 1.5rem;
}

.quiz-progress {
  margin-bottom: 1.5rem;
}

.quiz-progress span {
  display: block;
  margin-bottom: 0.5rem;
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.8);
}

.quiz-progress-bar {
  height: 8px;
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 4px;
  overflow: hidden;
}

.quiz-progress-fill {
  height: 100%;
  background-color: #f39c12;
  transition: width 0.3s ease;
}

.parent-quiz .quiz-progress-fill {
  background-color: #3498db;
}

.question-container {
  background: rgba(0, 0, 0, 0.2);
  padding: 1.5rem;
  border-radius: 0.8rem;
  margin-bottom: 1.5rem;
}

.question {
  font-size: 1.2rem;
  font-weight: 600;
  margin-top: 0;
  margin-bottom: 1.5rem;
  line-height: 1.4;
}

.options {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.option-btn {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: white;
  padding: 1rem;
  text-align: left;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 0.2s;
  font-size: 1rem;
}

.option-btn:hover:not(:disabled) {
  background: rgba(255, 255, 255, 0.2);
  transform: translateX(5px);
}

.option-btn.correct {
  background-color: rgba(16, 185, 129, 0.2);
  border-color: #10b981;
}

.option-btn.incorrect {
  background-color: rgba(239, 68, 68, 0.2);
  border-color: #ef4444;
}

.feedback {
  margin-top: 1.5rem;
  animation: fadeIn 0.3s ease-out;
}

.feedback-content {
  border-radius: 0.8rem;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.correct-feedback {
  background: rgba(16, 185, 129, 0.15);
  border: 1px solid rgba(16, 185, 129, 0.3);
}

.incorrect-feedback {
  background: rgba(239, 68, 68, 0.15);
  border: 1px solid rgba(239, 68, 68, 0.3);
}

.feedback-icon {
  width: 40px;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50%;
  margin-bottom: 1rem;
}

.correct-feedback .feedback-icon {
  background-color: rgba(16, 185, 129, 0.2);
  color: #10b981;
}

.incorrect-feedback .feedback-icon {
  background-color: rgba(239, 68, 68, 0.2);
  color: #ef4444;
}

.feedback-icon svg {
  width: 24px;
  height: 24px;
}

.next-btn {
  background: #f39c12;
  color: white;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 2rem;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  margin-top: 1.5rem;
  transition: all 0.2s;
}

.next-btn:hover {
  background: #e67e22;
  transform: translateY(-2px);
}

.parent-quiz .next-btn {
  background: #3498db;
}

.parent-quiz .next-btn:hover {
  background: #2980b9;
}

.quiz-results {
  padding: 2rem;
  text-align: center;
}

.results-container {
  max-width: 500px;
  margin: 0 auto;
}

.quiz-results h4 {
  font-size: 1.8rem;
  margin-bottom: 1.5rem;
  color: #f39c12;
}

.parent-quiz .quiz-results h4 {
  color: #3498db;
}

.score {
  margin-bottom: 2rem;
}

.score-circle {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 auto 1.5rem;
  background: rgba(255, 255, 255, 0.1);
  border: 4px solid #f39c12;
}

.parent-quiz .score-circle {
  border-color: #3498db;
}

.score-text {
  font-size: 2rem;
  font-weight: 700;
}

.result-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.restart-btn, .close-quiz-btn {
  padding: 0.8rem 1.5rem;
  border-radius: 2rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  border: none;
  font-size: 1rem;
}

.restart-btn {
  background: #f39c12;
  color: white;
}

.restart-btn:hover {
  background: #e67e22;
  transform: translateY(-2px);
}

.parent-quiz .restart-btn {
  background: #3498db;
}

.parent-quiz .restart-btn:hover {
  background: #2980b9;
}

.close-quiz-btn {
  background: rgba(255, 255, 255, 0.1);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.close-quiz-btn:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: translateY(-2px);
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Fullscreen prompt */
.fullscreen-prompt {
  position: absolute;
  bottom: 30px;
  right: 100px;
  z-index: 100;
  animation: fadeInUp 0.5s ease-out forwards, fadeOut 0.5s ease-in forwards 6.5s;
}

.prompt-content {
  display: flex;
  align-items: center;
  background: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 10px 15px;
  border-radius: 20px;
  font-size: 0.9rem;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(5px);
  border: 2px solid #f39c12;
}

.arrow-pointer {
  width: 18px;
  height: 18px;
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeOut {
  from { opacity: 1; }
  to { opacity: 0; }
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
  
  .simulation-btn {
    font-size: 1.2rem;
    padding: 1rem 2rem;
  }
  
  .simulation-content {
    min-height: 450px;
    padding: 0;
  }
  
  .simulation-content :deep(.container-small) {
    height: 450px;
  }
  
  .simulation-placeholder h3 {
    font-size: 1.5rem;
  }
  
  .simulation-placeholder p {
    font-size: 1rem;
  }
  
  .rip-progress-nav {
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
  
  .back-button-container {
    padding: 1rem 0;
  }
  
  .back-btn {
    padding: 0.6rem 1.2rem;
    font-size: 0.9rem;
  }
  
  .fullscreen-prompt {
    bottom: 20px;
    right: 80px;
  }
  
  .prompt-content {
    font-size: 0.8rem;
    padding: 8px 12px;
  }
  
  .arrow-pointer {
    width: 20px;
    height: 20px;
  }
  
  /* Quiz responsive styles */
  .quiz-container {
    max-height: 85vh;
  }
  
  .quiz-header h3 {
    font-size: 1.3rem;
  }
  
  .question {
    font-size: 1.1rem;
  }
  
  .option-btn {
    padding: 0.8rem;
    font-size: 0.95rem;
  }
  
  .next-btn, .restart-btn, .close-quiz-btn {
    padding: 0.7rem 1.3rem;
    font-size: 0.95rem;
  }
  
  .score-circle {
    width: 100px;
    height: 100px;
  }
  
  .score-text {
    font-size: 1.7rem;
  }
  
  .quiz-results h4 {
    font-size: 1.5rem;
  }
  
  .resource-age {
    font-size: 1.1rem;
    padding: 0.4rem 1rem;
  }
  
  .context-text {
    padding: 0.9rem 1.2rem;
    margin-bottom: 1.2rem;
  }
  
  .resource-image-container {
    width: 80%;
    margin: 0 auto 1.2rem;
    border-radius: 0.8rem;
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
  
  .simulation-btn {
    font-size: 1.1rem;
    padding: 0.9rem 1.8rem;
  }
  
  .simulation-content {
    min-height: 350px;
    padding: 0;
  }
  
  .simulation-content :deep(.container-small) {
    height: 350px;
  }
  
  .simulation-placeholder h3 {
    font-size: 1.3rem;
  }
  
  .simulation-placeholder p {
    font-size: 0.9rem;
  }
  
  .feature-item {
    padding: 1rem;
  }
  
  .feature-icon {
    font-size: 1.5rem;
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
  
  .back-button-container {
    padding: 0.8rem 0;
  }
  
  .back-btn {
    padding: 0.5rem 1rem;
    font-size: 0.85rem;
  }
  
  .fullscreen-prompt {
    bottom: 15px;
    right: 60px;
  }
  
  .prompt-content {
    font-size: 0.75rem;
    padding: 6px 10px;
  }
  
  .arrow-pointer {
    width: 18px;
    height: 18px;
  }
  
  /* Quiz responsive styles */
  .quiz-overlay {
    padding: 0.5rem;
  }
  
  .quiz-container {
    max-height: 90vh;
    border-radius: 0.8rem;
  }
  
  .quiz-header {
    padding: 1rem;
  }
  
  .quiz-header h3 {
    font-size: 1.1rem;
  }
  
  .quiz-content {
    padding: 1rem;
  }
  
  .question-container {
    padding: 1rem;
  }
  
  .question {
    font-size: 1rem;
    margin-bottom: 1rem;
  }
  
  .option-btn {
    padding: 0.7rem;
    font-size: 0.9rem;
  }
  
  .feedback-content {
    padding: 1rem;
  }
  
  .feedback-icon {
    width: 32px;
    height: 32px;
  }
  
  .feedback-icon svg {
    width: 18px;
    height: 18px;
  }
  
  .next-btn, .restart-btn, .close-quiz-btn {
    padding: 0.6rem 1.2rem;
    font-size: 0.9rem;
  }
  
  .quiz-results {
    padding: 1.5rem 1rem;
  }
  
  .score-circle {
    width: 80px;
    height: 80px;
    border-width: 3px;
  }
  
  .score-text {
    font-size: 1.5rem;
  }
  
  .quiz-results h4 {
    font-size: 1.3rem;
    margin-bottom: 1rem;
  }
  
  .resource-age {
    font-size: 1rem;
    padding: 0.35rem 0.9rem;
  }
  
  .context-text {
    padding: 0.8rem 1rem;
    margin-bottom: 1rem;
    font-size: 0.9rem;
  }
  
  .resource-image-container {
    width: 90%;
    margin: 0 auto 1rem;
    border-radius: 0.6rem;
  }
}
</style> 