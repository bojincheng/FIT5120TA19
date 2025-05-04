<template>
  <div class="container">
    <h1 v-if="!isVerySmallScreen">Backyard Pool Safety</h1>
    
    <div class="scene" :class="{ 'small-scene': isSmallScreen, 'very-small-scene': isVerySmallScreen }">
      <!-- Backyard environment -->
      <div class="grass"></div>
      <div class="patio"></div>
      
      <!-- Simple trees - hide on very small screens -->
      <div v-if="!isVerySmallScreen" class="tree left-tree"></div>
      <div v-if="!isVerySmallScreen" class="tree right-tree"></div>
      
      <!-- Pool fence -->
      <div class="pool-fence">
        <!-- Fence sections -->
        <div class="fence-section top"></div>
        <div class="fence-section right"></div>
        <div class="fence-section bottom">
          <!-- Gate in the bottom section -->
          <div class="fence-gate" :class="{ 'gate-open': currentStep >= 3 }"></div>
        </div>
        <div class="fence-section left"></div>
        
        <!-- Fence posts -->
        <div class="fence-post top-left"></div>
        <div class="fence-post top-right"></div>
        <div class="fence-post bottom-right"></div>
        <div class="fence-post bottom-left"></div>
      </div>
      
      <!-- Clean, minimalist pool -->
      <div class="pool">
        <div class="water">
          <!-- Simple lane lines - reduced number for performance -->
          <div v-for="n in 4" :key="`lane-${n}`" class="lane-line" 
               :style="{ top: `${n * 20}%` }"></div>
        </div>
        
        <!-- Pool ladder -->
        <div class="pool-ladder"></div>
        
        <!-- Depth marker - hide on very small screens -->
        <div v-if="!isVerySmallScreen" class="depth-marker">4 FT</div>
      </div>
      
      <!-- Child character -->
      <div class="child" :class="{ 
        playing: currentStep === 0,
        unattended: currentStep === 1,
        struggling: currentStep === 2,
        rescued: currentStep === 3,
        safe: currentStep === 4
      }">
        <div class="head">
          <div class="face">
            <div class="eyes" :class="{
              happy: currentStep === 0,
              neutral: currentStep === 1,
              panicked: currentStep === 2,
              relieved: currentStep >= 3
            }"></div>
            <div class="mouth" :class="{
              smiling: currentStep === 0,
              neutral: currentStep === 1,
              gasping: currentStep === 2,
              calm: currentStep >= 3
            }"></div>
          </div>
        </div>
        <div class="body"></div>
        <div class="arm left"></div>
        <div class="arm right"></div>
        <div class="leg left"></div>
        <div class="leg right"></div>
        
        <!-- Thought bubble for child -->
        <div class="thought-bubble" v-if="currentStep === 2">!</div>
      </div>
      
      <!-- Parent character -->
      <div class="parent" :class="{ 
        watching: currentStep === 0,
        distracted: currentStep === 1,
        alert: currentStep === 2,
        rescuing: currentStep === 3,
        teaching: currentStep === 4
      }">
        <div class="head">
          <div class="face">
            <div class="eyes" :class="{
              attentive: currentStep === 0,
              'looking-away': currentStep === 1,
              alert: currentStep === 2,
              focused: currentStep === 3,
              attentive: currentStep === 4
            }"></div>
            <div class="mouth" :class="{
              smiling: currentStep === 0,
              neutral: currentStep === 1,
              concerned: currentStep === 2,
              determined: currentStep === 3,
              talking: currentStep === 4
            }"></div>
          </div>
        </div>
        <div class="body"></div>
        <div class="arm left"></div>
        <div class="arm right"></div>
        <div class="leg left"></div>
        <div class="leg right"></div>
        
        <!-- Phone distraction -->
        <div class="phone" v-if="currentStep === 1"></div>
        
        <!-- Thought bubble for parent -->
        <div class="thought-bubble parent-bubble" v-if="currentStep === 1">...</div>
      </div>
      
      <!-- Quiz result indicator -->
      <div class="quiz-result" v-if="showResults && !quizActive">
        <div v-if="lastAnswerCorrect" class="correct-indicator">✓</div>
        <div v-else class="incorrect-indicator">✗</div>
      </div>
    </div>
    
    <div class="step-info" :class="{ 'compact': isSmallScreen, 'very-compact': isVerySmallScreen }">
      <h2>{{ steps[currentStep].title }}</h2>
      <p>{{ steps[currentStep].description }}</p>
      <div class="stat-box">
        <strong>Tip:</strong> {{ steps[currentStep].tip }}
      </div>
    </div>
    
    <div v-if="!quizActive && currentStep === 0" class="controls">
      <button @click="startQuiz" class="control-button">
        Start Safety Scenario
      </button>
    </div>
    
    <div class="quiz-container" v-if="quizActive">
      <div class="timer">
        <div class="timer-bar" :style="{ width: `${timeRemaining * (isSmallScreen ? 10 : 6.67)}%` }"></div>
        <div class="timer-text">{{ timeRemaining }} seconds</div>
      </div>
      
      <div class="question">
        <h3>{{ isSmallScreen ? 'Question:' : 'Scenario Question:' }}</h3>
        <p>{{ currentQuestion.question }}</p>
      </div>
      
      <!-- Thinking phase -->
      <div v-if="quizPhase === 'thinking'" class="thinking-phase">
        <p>{{ isSmallScreen ? 'Think about this scenario...' : 'Take a moment to think about this scenario...' }}</p>
        <button @click="showOptions" class="next-button">Show Options</button>
      </div>
      
      <!-- Options phase -->
      <div v-if="quizPhase === 'options'" class="options">
        <button 
          v-for="(option, index) in currentQuestion.options" 
          :key="index"
          @click="selectAnswer(index)"
          :class="{ 
            'option-button': true,
            'selected': selectedAnswer === index,
            'correct': showResults && index === currentQuestion.correctAnswer,
            'incorrect': showResults && selectedAnswer === index && index !== currentQuestion.correctAnswer
          }"
          :disabled="showResults"
        >
          {{ option }}
        </button>
      </div>
      
      <!-- Results phase -->
      <div class="feedback" v-if="showResults">
        <div v-if="selectedAnswer === currentQuestion.correctAnswer" class="correct-feedback">
          <h3>Correct!</h3>
          <p>{{ currentQuestion.explanation }}</p>
          <div class="additional-info" v-if="!isVerySmallScreen">
            <h4>More Information:</h4>
            <p>{{ currentQuestion.additionalInfo }}</p>
          </div>
        </div>
        <div v-else class="incorrect-feedback">
          <h3>Incorrect</h3>
          <p>{{ currentQuestion.explanation }}</p>
          <div class="additional-info" v-if="!isVerySmallScreen">
            <h4>More Information:</h4>
            <p>{{ currentQuestion.additionalInfo }}</p>
          </div>
        </div>
        <button @click="continueAfterQuestion" class="next-button">
          Continue
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentStep: 0,
      quizActive: false,
      quizPhase: 'thinking', // 'thinking', 'options', 'results'
      currentQuestionIndex: 0,
      selectedAnswer: null,
      showResults: false,
      timeRemaining: 15, // Increased time for more complex questions
      timerInterval: null,
      lastAnswerCorrect: false,
      isInIframe: false,
      windowHeight: window.innerHeight,
      windowWidth: window.innerWidth,
      steps: [
        {
          title: "Active Supervision",
          description: "The parent is actively watching their child in the pool from outside the fence. For young children, active supervision means giving them 100% of your attention.",
          tip: "Always maintain 'touch supervision' for young children - staying within arm's reach at all times."
        },
        {
          title: "Distracted Supervision",
          description: "The parent has become distracted by their phone. Even a brief moment of distraction can be dangerous - drowning can happen in seconds.",
          tip: "Designate a responsible adult as a dedicated 'water watcher' who agrees not to use phones or other distractions."
        },
        {
          title: "Signs of Drowning",
          description: "The child is now in distress. Unlike in movies, real drowning is often quiet with little splashing or noise.",
          tip: "Drowning doesn't look like drowning. It's often silent and can happen in as little as 20-60 seconds."
        },
        {
          title: "Rescue Response",
          description: "The parent has noticed and is responding immediately, opening the gate to reach the child. For backyard pools, parents should be prepared to enter the water quickly if needed.",
          tip: "Keep a shepherd's hook (long pole with a hook) and life ring near your pool for emergencies."
        },
        {
          title: "Prevention Education",
          description: "The child is now safe and the parent is teaching water safety. Multiple layers of protection are essential for preventing drowning incidents.",
          tip: "Combine supervision with barriers (pool fences with self-closing gates), swimming lessons, life jackets, and CPR training."
        }
      ],
      questions: [
        {
          // Question for Scenario 1: Active Supervision
          question: "In the scene you just observed, the parent is actively supervising their child. What critical action should they take if they absolutely need to step away for a moment?",
          options: [
            "It's okay to step away briefly since the pool is fenced",
            "Ask the child to get out of the pool until they return",
            "Designate another responsible adult to take over supervision",
            "Tell the child to be careful while they're gone"
          ],
          correctAnswer: 2,
          explanation: "Even with a fence, a child should never be left alone in or near water. The only safe option is to ensure another responsible adult takes over supervision before stepping away.",
          additionalInfo: "The American Academy of Pediatrics reports that lapses in supervision are a factor in 70% of drowning incidents involving children. A proper handoff of supervision responsibility includes making eye contact with the new supervisor, verbally confirming they're taking over, and ensuring they understand the importance of undivided attention."
        },
        {
          // Question for Scenario 2: Distracted Supervision
          question: "In this scenario, the parent became distracted by their phone. What physiological factor makes phone use particularly dangerous around water?",
          options: [
            "Phones emit radiation that can cause drowsiness",
            "The blue light from phones can impair peripheral vision",
            "Phones trigger 'inattentional blindness' where you fail to notice unexpected objects",
            "Phone use slows reaction time by affecting motor neurons"
          ],
          correctAnswer: 2,
          explanation: "Phone use causes 'inattentional blindness' - a psychological phenomenon where you fail to notice unexpected objects or events when your attention is focused elsewhere, even if they're in your direct line of sight.",
          additionalInfo: "Studies at Western Washington University found that people using phones were 50% less likely to notice unusual activities happening right in front of them. For water safety, this means a parent could be looking directly at a pool where a child is drowning but not actually 'see' it because their attention is captured by the phone. This is why complete focus is essential for water supervision."
        },
        {
          // Question for Scenario 3: Signs of Drowning
          question: "Looking at the child's behavior in this scenario, which of these is NOT a typical sign of drowning?",
          options: [
            "Head low in water with mouth at water level",
            "Arms moving downward instead of waving",
            "Loud splashing and calls for help",
            "Vertical body position with minimal forward movement"
          ],
          correctAnswer: 2,
          explanation: "Contrary to popular belief and media portrayals, drowning victims rarely splash dramatically or call for help. The Instinctive Drowning Response prevents them from waving arms or calling out because their body prioritizes breathing over everything else.",
          additionalInfo: "Dr. Francesco Pia, who identified the Instinctive Drowning Response, found that drowning people physiologically cannot wave for help. Their arms instinctively extend laterally and press down on the water surface to try to leverage their mouths above water. The respiratory system prioritizes breathing over speech, making it impossible to call for help. This is why drowning is often called the 'silent killer' - it looks nothing like what most people expect."
        },
        {
          // Question for Scenario 4: Rescue Response
          question: "In the rescue scenario you just saw, the parent is rushing to help their child. If you needed to perform a water rescue but weren't a strong swimmer, what would be your best first action?",
          options: [
            "Jump in immediately - every second counts",
            "Call 000 first before doing anything else",
            "Use the 'reach, throw, don't go' approach - extend or throw something to the victim",
            "Run to find someone who's a better swimmer"
          ],
          correctAnswer: 2,
          explanation: "The 'reach, throw, don't go' principle is safest. Extend a pole, shepherd's hook, or throw a floating object while calling for help. Non-swimmers attempting rescues often become victims themselves.",
          additionalInfo: "The American Red Cross drowning chain of survival emphasizes that untrained rescuers should avoid direct contact with active drowning victims. A drowning person's survival instinct can cause them to climb on top of a rescuer, potentially drowning both. Using the pool fence gate properly (as shown in the animation) and having rescue equipment readily available near the pool are essential parts of a safe rescue plan."
        },
        {
          // Question for Scenario 5: Prevention Education
          question: "In the final scene, the parent is teaching water safety. Which approach would be most effective for teaching young children about pool safety?",
          options: [
            "Explaining the statistics and dangers of drowning",
            "Using fear-based warnings about the consequences of breaking rules",
            "Teaching simple, consistent rules with positive reinforcement",
            "Showing graphic videos of drowning incidents"
          ],
          correctAnswer: 2,
          explanation: "Young children learn best through simple, consistent rules with positive reinforcement. Complex statistics or fear-based approaches are less effective and can create anxiety around water rather than respect and safety.",
          additionalInfo: "Child development research shows that children under 7 typically cannot fully understand cause-and-effect relationships for complex dangers. The American Academy of Pediatrics recommends teaching water safety through simple rules (like 'never go near water without a grown-up'), consistent enforcement, positive reinforcement when rules are followed, and age-appropriate explanations. This builds a foundation of water respect rather than water fear, which is important for both safety and eventual swimming skill development."
        },
        {
          // Additional question about fence safety
          question: "Looking at the pool fence in this scenario, what critical feature should all pool gates have to prevent unsupervised access?",
          options: [
            "A lock that requires a key",
            "A self-closing, self-latching mechanism that's out of children's reach",
            "An alarm that sounds when opened",
            "A sign warning about the dangers of unsupervised swimming"
          ],
          correctAnswer: 1,
          explanation: "All pool gates should have self-closing, self-latching mechanisms positioned out of children's reach. This ensures the gate closes and secures automatically after someone passes through, preventing accidental access.",
          additionalInfo: "The U.S. Consumer Product Safety Commission found that properly functioning self-closing, self-latching gates could prevent up to 70% of child drownings in residential pools. Gates should open outward, away from the pool, and the latch should be at least 54 inches above the ground. Regular testing of the self-closing mechanism is essential, as hinges can weaken over time. Some jurisdictions legally require these features on all residential pool fences."
        },
        {
          // Additional question about multiple layers of protection
          question: "In the scenarios you've observed, which combination of safety measures represents the most effective 'layers of protection' approach?",
          options: [
            "Swimming lessons and pool toys designed for safety",
            "Pool fence, constant supervision, swimming ability, and emergency response knowledge",
            "Pool cover and alarm system",
            "Posted safety rules and first aid kit"
          ],
          correctAnswer: 1,
          explanation: "The most effective approach uses multiple layers: physical barriers (fence), constant supervision, swimming ability, and emergency response knowledge. No single prevention strategy is 100% effective, but when multiple layers are used together, the risk is significantly reduced.",
          additionalInfo: "The concept of 'layers of protection' is endorsed by all major water safety organizations. If one layer fails (like a momentary lapse in supervision), other layers (like a proper fence) can prevent tragedy. Research by the National Drowning Prevention Alliance shows that areas with mandatory pool fencing laws have up to 50% fewer drowning incidents. The animation demonstrates several of these layers: the fence as a physical barrier, supervision (when done properly), and education about water safety."
        }
      ]
    };
  },
  computed: {
    currentQuestion() {
      return this.questions[this.currentQuestionIndex];
    },
    isSmallScreen() {
      return this.windowWidth <= 768;
    },
    isVerySmallScreen() {
      return this.windowWidth <= 480 || this.windowHeight <= 667;
    }
  },
  methods: {
    startQuiz() {
      this.quizActive = true;
      this.quizPhase = 'thinking';
      this.selectedAnswer = null;
      this.showResults = false;
      this.timeRemaining = this.isSmallScreen ? 10 : 15; // Shorter time for small screens
    },
    showOptions() {
      this.quizPhase = 'options';
      this.startTimer();
    },
    startTimer() {
      clearInterval(this.timerInterval);
      this.timerInterval = setInterval(() => {
        if (this.timeRemaining > 0) {
          this.timeRemaining--;
        } else {
          this.timeUp();
        }
      }, 1000);
    },
    timeUp() {
      clearInterval(this.timerInterval);
      if (!this.showResults) {
        this.showResults = true;
        if (this.selectedAnswer === null) {
          this.selectedAnswer = -1; // No answer selected
          this.lastAnswerCorrect = false;
        }
      }
    },
    selectAnswer(index) {
      this.selectedAnswer = index;
      this.lastAnswerCorrect = (index === this.currentQuestion.correctAnswer);
      clearInterval(this.timerInterval);
      this.showResults = true;
    },
    continueAfterQuestion() {
      // Progress to the next step in the animation
      if (this.currentStep < this.steps.length - 1) {
        this.currentStep++;
      }
      
      this.quizActive = false;
      
      // Show the quiz result indicator briefly
      setTimeout(() => {
        // Move to the next question or end quiz if all questions answered
        if (this.currentQuestionIndex < this.questions.length - 1) {
          this.currentQuestionIndex++;
          this.startQuiz();
        }
      }, 2000);
    },
    handleMessage(event) {
      // Handle messages from parent
      if (event.data && event.data.type === 'close-quiz') {
        // Reset quiz state if needed
        clearInterval(this.timerInterval);
        this.quizActive = false;
        this.currentStep = 0;
        this.currentQuestionIndex = 0;
      }
    },
    checkIfInIframe() {
      try {
        this.isInIframe = window.self !== window.top;
        // If we're in an iframe, notify the parent
        if (this.isInIframe) {
          // Start the quiz automatically if in iframe
          this.startQuiz();
          // Notify parent frame that we're loaded
          window.parent.postMessage({ 
            type: 'quiz-loaded', 
            status: 'success' 
          }, '*');
        }
      } catch (e) {
        // If we can't access window.top due to same-origin policy,
        // we're definitely in an iframe from another domain
        this.isInIframe = true;
        this.startQuiz();
      }
    },
    handleResize() {
      this.windowHeight = window.innerHeight;
      this.windowWidth = window.innerWidth;
    }
  },
  mounted() {
    // Check if running in iframe
    this.checkIfInIframe();
    
    // Add message listener for iframe communication
    window.addEventListener('message', this.handleMessage);
    
    // Handle window resizing
    window.addEventListener('resize', this.handleResize);
    
    // Automatically start quiz for better user experience
    if (!this.isInIframe && !this.quizActive) {
      setTimeout(() => {
        this.startQuiz();
      }, 1000);
    }
  },
  beforeUnmount() {
    clearInterval(this.timerInterval);
    window.removeEventListener('message', this.handleMessage);
    window.removeEventListener('resize', this.handleResize);
  }
};
</script>

<style scoped>
body {
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  overflow-y: auto;
}

.container {
  max-width: none;
  width: 100%;
  min-height: 100vh;
  margin: 0;
  padding: 20px;
  font-family: Arial, sans-serif;
  color: #333;
  background-color: #f5f5f5;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow-x: hidden;
}

h1 {
  text-align: center;
  color: #0277bd;
  margin: 0 0 15px 0;
  font-size: 1.8rem;
}

/* Clean, minimalist scene styling */
.scene {
  position: relative;
  width: 100%;
  max-width: 800px;
  height: 40vh;
  min-height: 250px;
  max-height: 400px;
  border-radius: 10px;
  overflow: hidden;
  margin-bottom: 20px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

/* Backyard environment */
.grass {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #8BC34A;
  z-index: 1;
}

.patio {
  position: absolute;
  top: 70px;
  left: 70px;
  width: calc(100% - 140px);
  height: 100px;
  background-color: #E0E0E0;
  z-index: 2;
}

/* Simple trees */
.tree {
  position: absolute;
  z-index: 3;
}

.tree:before {
  content: '';
  position: absolute;
  width: 40px;
  height: 40px;
  background-color: #4CAF50;
  border-radius: 50%;
}

.tree:after {
  content: '';
  position: absolute;
  width: 10px;
  height: 20px;
  background-color: #795548;
}

.left-tree {
  top: 20px;
  left: 20px;
}

.left-tree:before {
  top: 0;
  left: 0;
}

.left-tree:after {
  top: 40px;
  left: 15px;
}

.right-tree {
  top: 20px;
  right: 20px;
}

.right-tree:before {
  top: 0;
  right: 0;
}

.right-tree:after {
  top: 40px;
  right: 15px;
}

/* Pool fence */
.pool-fence {
  position: absolute;
  top: 150px;
  left: 50px;
  width: calc(100% - 100px);
  height: 240px;
  z-index: 5;
}

.fence-section {
  position: absolute;
  background-color: #BDBDBD;
  z-index: 5;
}

.fence-section.top, .fence-section.bottom {
  left: 0;
  width: 100%;
  height: 5px;
}

.fence-section.left, .fence-section.right {
  top: 0;
  width: 5px;
  height: 100%;
}

.fence-section.top {
  top: 0;
}

.fence-section.bottom {
  bottom: 0;
}

.fence-section.left {
  left: 0;
}

.fence-section.right {
  right: 0;
}

/* Fence posts */
.fence-post {
  position: absolute;
  width: 10px;
  height: 10px;
  background-color: #757575;
  z-index: 6;
}

.fence-post.top-left {
  top: 0;
  left: 0;
  transform: translate(-50%, -50%);
}

.fence-post.top-right {
  top: 0;
  right: 0;
  transform: translate(50%, -50%);
}

.fence-post.bottom-right {
  bottom: 0;
  right: 0;
  transform: translate(50%, 50%);
}

.fence-post.bottom-left {
  bottom: 0;
  left: 0;
  transform: translate(-50%, 50%);
}

/* Fence gate */
.fence-gate {
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 60px;
  height: 5px;
  background-color: #9E9E9E;
  transform: translateX(-50%);
  transform-origin: center bottom;
  transition: transform 1s ease;
}

.fence-gate:before {
  content: '';
  position: absolute;
  top: -30px;
  left: 50%;
  width: 5px;
  height: 30px;
  background-color: #9E9E9E;
  transform: translateX(-50%);
}

.fence-gate.gate-open {
  transform: translateX(-50%) rotateZ(-90deg);
}

/* Clean, minimalist pool */
.pool {
  position: absolute;
  top: 170px;
  left: 70px;
  width: calc(100% - 140px);
  height: 200px;
  border-radius: 10px;
  overflow: hidden;
  z-index: 4;
  border: 10px solid #E0E0E0;
}

.water {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(180deg, #64B5F6 0%, #1976D2 100%);
}

.lane-line {
  position: absolute;
  left: 0;
  width: 100%;
  height: 1px;
  background-color: rgba(255, 255, 255, 0.3);
}

.pool-ladder {
  position: absolute;
  top: 0;
  right: 20px;
  width: 20px;
  height: 60px;
  background-color: #E0E0E0;
  z-index: 5;
}

.depth-marker {
  position: absolute;
  bottom: 10px;
  right: 10px;
  color: white;
  font-weight: bold;
  font-size: 16px;
  z-index: 5;
}

/* Child character - in the pool with expressions - MUCH LARGER SIZE */
.child {
  position: absolute;
  top: 270px;
  left: 350px;
  height: 80px; /* Increased from 60px */
  width: 40px; /* Increased from 30px */
  z-index: 10;
  transition: all 1.5s ease;
}

.child .head {
  position: absolute;
  top: 0;
  left: 10px; /* Adjusted for larger size */
  width: 20px; /* Increased from 16px */
  height: 20px; /* Increased from 16px */
  background-color: #FFCC80;
  border-radius: 50%;
  overflow: hidden;
}

.child .face {
  position: relative;
  width: 100%;
  height: 100%;
}

.child .eyes {
  position: absolute;
  top: 6px; /* Adjusted for larger size */
  width: 100%;
  height: 4px; /* Increased from 3px */
}

.child .eyes:before, .child .eyes:after {
  content: '';
  position: absolute;
  width: 4px; /* Increased from 3px */
  height: 4px; /* Increased from 3px */
  background-color: #5D4037;
  border-radius: 50%;
}

.child .eyes:before {
  left: 4px; /* Adjusted for larger size */
}

.child .eyes:after {
  right: 4px; /* Adjusted for larger size */
}

.child .eyes.happy:before, .child .eyes.happy:after {
  height: 3px; /* Increased from 2px */
  border-radius: 3px 3px 0 0;
  transform: translateY(-1px);
}

.child .eyes.panicked:before, .child .eyes.panicked:after {
  height: 5px; /* Increased from 4px */
  width: 5px; /* Increased from 4px */
}

.child .mouth {
  position: absolute;
  bottom: 4px; /* Adjusted for larger size */
  left: 6px; /* Adjusted for larger size */
  width: 8px; /* Increased from 6px */
  height: 3px; /* Increased from 2px */
  background-color: #5D4037;
  border-radius: 1px;
}

.child .mouth.smiling {
  height: 4px; /* Increased from 3px */
  width: 8px; /* Increased from 6px */
  border-radius: 0 0 4px 4px;
  transform: translateY(-1px);
}

.child .mouth.gasping {
  height: 5px; /* Increased from 4px */
  width: 5px; /* Increased from 4px */
  border-radius: 50%;
  animation: gasp 0.7s infinite;
}

.child .mouth.calm {
  width: 6px; /* Increased from 5px */
}

@keyframes gasp {
  0%, 100% {
    height: 3px; /* Increased from 2px */
    border-radius: 1px;
  }
  50% {
    height: 5px; /* Increased from 4px */
    border-radius: 50%;
  }
}

.child .body {
  position: absolute;
  top: 20px; /* Adjusted for larger size */
  left: 13px; /* Adjusted for larger size */
  width: 14px; /* Increased from 10px */
  height: 30px; /* Increased from 22px */
  background-color: #FFEB3B;
  border-radius: 4px;
}

.child .arm {
  position: absolute;
  width: 4px; /* Increased from 3px */
  height: 20px; /* Increased from 15px */
  background-color: #FFCC80;
}

.child .arm.left {
  top: 24px; /* Adjusted for larger size */
  left: 8px; /* Adjusted for larger size */
}

.child .arm.right {
  top: 24px; /* Adjusted for larger size */
  right: 8px; /* Adjusted for larger size */
}

.child .leg {
  position: absolute;
  width: 4px; /* Increased from 3px */
  height: 24px; /* Increased from 18px */
  background-color: #FFCC80;
}

.child .leg.left {
  top: 50px; /* Adjusted for larger size */
  left: 12px; /* Adjusted for larger size */
}

.child .leg.right {
  top: 50px; /* Adjusted for larger size */
  right: 12px; /* Adjusted for larger size */
}

.child.playing {
  animation: bobbing 2s infinite;
}

.child.unattended {
  left: 400px;
  animation: drifting 3s infinite;
}

.child.struggling {
  left: 450px;
  animation: drowning 1s infinite;
}

.child.rescued {
  left: 350px;
  top: 240px;
}

.child.safe {
  left: 300px;
  top: 270px;
}

/* Parent character - on the grass with expressions - MUCH LARGER SIZE */
.parent {
  position: absolute;
  top: 40px;
  left: 200px;
  height: 120px; /* Increased from 90px */
  width: 40px; /* Increased from 30px */
  z-index: 10;
  transition: all 1.5s ease;
}

.parent .head {
  position: absolute;
  top: 0;
  left: 10px; /* Adjusted for larger size */
  width: 20px; /* Increased from 16px */
  height: 20px; /* Increased from 16px */
  background-color: #FFCC80;
  border-radius: 50%;
  overflow: hidden;
}

.parent .face {
  position: relative;
  width: 100%;
  height: 100%;
}

.parent .eyes {
  position: absolute;
  top: 6px; /* Adjusted for larger size */
  width: 100%;
  height: 4px; /* Increased from 3px */
}

.parent .eyes:before, .parent .eyes:after {
  content: '';
  position: absolute;
  width: 4px; /* Increased from 3px */
  height: 4px; /* Increased from 3px */
  background-color: #5D4037;
  border-radius: 50%;
}

.parent .eyes:before {
  left: 4px; /* Adjusted for larger size */
}

.parent .eyes:after {
  right: 4px; /* Adjusted for larger size */
}

.parent .eyes.looking-away:before, .parent .eyes.looking-away:after {
  transform: translateX(3px); /* Increased from 2px */
}

.parent .eyes.alert:before, .parent .eyes.alert:after {
  height: 5px; /* Increased from 4px */
  width: 5px; /* Increased from 4px */
}

.parent .mouth {
  position: absolute;
  bottom: 4px; /* Adjusted for larger size */
  left: 6px; /* Adjusted for larger size */
  width: 8px; /* Increased from 6px */
  height: 3px; /* Increased from 2px */
  background-color: #5D4037;
  border-radius: 1px;
}

.parent .mouth.smiling {
  height: 4px; /* Increased from 3px */
  width: 8px; /* Increased from 6px */
  border-radius: 0 0 4px 4px;
  transform: translateY(-1px);
}

.parent .mouth.concerned {
  width: 8px; /* Increased from 6px */
  height: 4px; /* Increased from 3px */
  border-radius: 4px 4px 0 0;
  transform: translateY(1px);
}

.parent .mouth.determined {
  width: 10px; /* Increased from 8px */
  height: 3px; /* Increased from 2px */
}

.parent .mouth.talking {
  animation: talking 1s infinite;
}

@keyframes talking {
  0%, 100% {
    height: 3px; /* Increased from 2px */
    width: 7px; /* Increased from 5px */
  }
  50% {
    height: 4px; /* Increased from 3px */
    width: 8px; /* Increased from 6px */
  }
}

.parent .body {
  position: absolute;
  top: 20px; /* Adjusted for larger size */
  left: 13px; /* Adjusted for larger size */
  width: 14px; /* Increased from 10px */
  height: 50px; /* Increased from 38px */
  background-color: #9575CD;
  border-radius: 4px;
}

.parent .arm {
  position: absolute;
  width: 4px; /* Increased from 3px */
  height: 30px; /* Increased from 22px */
  background-color: #FFCC80;
}

.parent .arm.left {
  top: 30px; /* Adjusted for larger size */
  left: 8px; /* Adjusted for larger size */
}

.parent .arm.right {
  top: 30px; /* Adjusted for larger size */
  right: 8px; /* Adjusted for larger size */
}

.parent .leg {
  position: absolute;
  width: 4px; /* Increased from 3px */
  height: 40px; /* Increased from 30px */
  background-color: #FFCC80;
}

.parent .leg.left {
  top: 70px; /* Adjusted for larger size */
  left: 12px; /* Adjusted for larger size */
}

.parent .leg.right {
  top: 70px; /* Adjusted for larger size */
  right: 12px; /* Adjusted for larger size */
}

.parent.watching {
  left: 200px;
}

.parent.distracted {
  left: 150px;
}

.parent.alert {
  left: 250px;
  animation: alert 0.5s infinite;
}

@keyframes alert {
  0%, 100% {
    transform: rotate(0deg);
  }
  50% {
    transform: rotate(5deg);
  }
}

.parent.rescuing {
  top: 120px;
  left: 350px;
  animation: running 0.5s infinite;
}

@keyframes running {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-5px); /* Increased from -3px */
  }
}

.parent.teaching {
  top: 120px;
  left: 250px;
}

/* Phone */
.phone {
  position: absolute;
  top: 30px; /* Adjusted for larger size */
  right: -10px; /* Adjusted for larger size */
  width: 10px; /* Increased from 8px */
  height: 20px; /* Increased from 15px */
  background-color: #424242;
  border-radius: 1px;
}

/* Thought bubbles */
.thought-bubble {
  position: absolute;
  top: -30px; /* Adjusted for larger size */
  left: 0;
  width: 40px; /* Increased from 30px */
  height: 40px; /* Increased from 30px */
  background-color: white;
  border-radius: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  z-index: 20;
}

.parent-bubble {
  left: auto;
  right: -25px; /* Adjusted for larger size */
}

/* Animations */
@keyframes bobbing {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-7px); /* Increased from -5px */
  }
}

@keyframes drifting {
  0%, 100% {
    transform: translateX(0);
  }
  50% {
    transform: translateX(20px); /* Increased from 15px */
  }
}

@keyframes drowning {
  0%, 100% {
    transform: translateY(0) rotate(0deg);
  }
  25% {
    transform: translateY(-5px) rotate(-10deg); /* Increased from -3px and -8deg */
  }
  75% {
    transform: translateY(-5px) rotate(10deg); /* Increased from -3px and 8deg */
  }
}

/* Quiz result indicator */
.quiz-result {
  position: absolute;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 20;
  animation: fadeInOut 2s forwards;
}

.correct-indicator {
  background-color: rgba(76, 175, 80, 0.8);
  width: 100%;
  height: 100%;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-size: 24px;
  font-weight: bold;
}

.incorrect-indicator {
  background-color: rgba(244, 67, 54, 0.8);
  width: 100%;
  height: 100%;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-size: 24px;
  font-weight: bold;
}

@keyframes fadeInOut {
  0% {
    opacity: 0;
    transform: translateX(-50%) scale(0.5);
  }
  20% {
    opacity: 1;
    transform: translateX(-50%) scale(1);
  }
  80% {
    opacity: 1;
    transform: translateX(-50%) scale(1);
  }
  100% {
    opacity: 0;
    transform: translateX(-50%) scale(0.5);
  }
}

/* Step info */
.step-info {
  background-color: #E3F2FD;
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 20px;
  border-left: 5px solid #0277BD;
  width: 100%;
  max-width: 800px;
}

.step-info h2 {
  margin-top: 0;
  margin-bottom: 8px;
  color: #0277BD;
  font-size: 1.4rem;
}

.step-info p {
  line-height: 1.5;
  margin: 0 0 12px 0;
  font-size: 1rem;
}

.stat-box {
  margin-top: 12px;
  padding: 10px 12px;
  background-color: #fff;
  border-radius: 5px;
  border-left: 3px solid #F44336;
  font-size: 0.95rem;
}

/* Quiz styling */
.quiz-container {
  background-color: #F5F5F5;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  width: 100%;
  max-width: 800px;
  margin-bottom: 20px;
}

.timer {
  position: relative;
  height: 25px;
  background-color: #E0E0E0;
  border-radius: 15px;
  margin-bottom: 10px;
  overflow: hidden;
  flex-shrink: 0;
}

.timer-bar {
  height: 100%;
  background-color: #0277BD;
  transition: width 1s linear;
}

.timer-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: #000;
  font-weight: bold;
  font-size: 0.9rem;
}

.question {
  margin-bottom: 15px;
  flex-shrink: 0;
}

.question h3 {
  margin: 0 0 5px 0;
  color: #0277BD;
  font-size: 1.1rem;
}

.question p {
  font-size: 1rem;
  line-height: 1.4;
  margin: 0;
}

/* Thinking phase styling */
.thinking-phase {
  text-align: center;
  padding: 12px;
  background-color: #E8F5E9;
  border-radius: 8px;
  margin-bottom: 15px;
  flex-shrink: 0;
}

.thinking-phase p {
  font-size: 1rem;
  margin: 0 0 10px 0;
}

.options {
  display: grid;
  grid-template-columns: 1fr;
  gap: 10px;
  margin-bottom: 15px;
  width: 100%;
}

.option-button {
  padding: 15px;
  background-color: white;
  border: 2px solid #0277BD;
  border-radius: 8px;
  text-align: left;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s;
  width: 100%;
}

.option-button:hover:not(:disabled) {
  background-color: #E3F2FD;
}

.option-button.selected {
  background-color: #BBDEFB;
}

.option-button.correct {
  background-color: #C8E6C9;
  border-color: #4CAF50;
}

.option-button.incorrect {
  background-color: #FFCDD2;
  border-color: #F44336;
}

.feedback {
  margin-top: 15px;
  width: 100%;
}

.correct-feedback, .incorrect-feedback {
  background-color: #C8E6C9;
  color: #2E7D32;
  padding: 15px;
  border-radius: 5px;
  margin-bottom: 15px;
  width: 100%;
}

.incorrect-feedback {
  background-color: #FFCDD2;
  color: #C62828;
}

.feedback h3 {
  margin: 0 0 10px 0;
  font-size: 1.2rem;
}

.additional-info {
  margin-top: 15px;
  padding: 12px;
  background-color: #F5F5F5;
  border-left: 3px solid #0277BD;
  border-radius: 0 5px 5px 0;
  width: 100%;
}

.additional-info h4 {
  margin-top: 0;
  margin-bottom: 8px;
  color: #0277BD;
  font-size: 1rem;
}

.additional-info p {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.5;
}

.next-button {
  display: block;
  margin: 10px auto 0;
  padding: 10px 20px;
  background-color: #0277BD;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
  flex-shrink: 0;
}

.next-button:hover {
  background-color: #01579B;
}

.controls {
  text-align: center;
  margin: 10px 0;
  flex-shrink: 0;
}

.control-button {
  padding: 12px 24px;
  background-color: #0277BD;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.control-button:hover {
  background-color: #01579B;
}

/* Responsive design */
@media (min-width: 768px) {
  .options {
    grid-template-columns: 1fr 1fr;
  }
  
  .container {
    padding: 20px 30px;
  }
}

/* Responsive adjustments for smaller screens */
@media (max-width: 768px) {
  .container {
    padding: 15px;
  }
  
  h1 {
    font-size: 1.5rem;
    margin-bottom: 15px;
  }
  
  .scene {
    height: 35vh;
    min-height: 200px;
    margin-bottom: 15px;
  }
  
  .step-info {
    padding: 12px;
    margin-bottom: 15px;
  }
  
  .step-info h2 {
    font-size: 1.3rem;
  }
  
  .quiz-container {
    padding: 15px;
  }
  
  .option-button, .next-button, .control-button {
    font-size: 0.95rem;
    padding: 12px 15px;
  }
}

@media (max-width: 480px) {
  .container {
    padding: 10px;
  }
  
  h1 {
    font-size: 1.3rem;
    margin-bottom: 10px;
  }
  
  .scene {
    height: 30vh;
    min-height: 180px;
    margin-bottom: 12px;
  }
  
  .step-info h2 {
    font-size: 1.2rem;
  }
  
  .step-info, .quiz-container {
    padding: 10px;
  }
  
  .option-button {
    font-size: 0.9rem;
    padding: 10px;
  }
  
  .timer {
    height: 20px;
    margin-bottom: 10px;
  }
  
  .question h3 {
    font-size: 1.1rem;
  }
  
  .feedback h3 {
    font-size: 1.1rem;
  }
}

/* iPhone SE and other very small devices */
@media (max-height: 667px) {
  .scene {
    height: 28vh;
    min-height: 150px;
  }
  
  h1 {
    font-size: 1.2rem;
    margin-bottom: 8px;
  }
  
  .step-info, .quiz-container {
    padding: 10px;
    margin-bottom: 12px;
  }
}

/* Compact step info */
.step-info.compact {
  padding: 12px;
}

.step-info.compact h2 {
  font-size: 1.2rem;
  margin-bottom: 8px;
}

.step-info.compact p {
  font-size: 0.95rem;
  margin-bottom: 8px;
}

.step-info.compact .stat-box {
  padding: 8px;
  font-size: 0.9rem;
}

.step-info.very-compact {
  padding: 10px;
}

.step-info.very-compact h2 {
  font-size: 1.1rem;
  margin-bottom: 5px;
}

.step-info.very-compact p {
  font-size: 0.9rem;
  margin-bottom: 5px;
  line-height: 1.4;
}

.step-info.very-compact .stat-box {
  padding: 6px;
  font-size: 0.85rem;
  margin-top: 8px;
}

/* Remove fixed heights and scrollbars from elements */
.step-info, .quiz-container, .options, .feedback, .thinking-phase, .additional-info {
  max-height: none;
  overflow-y: visible;
}

/* Button styling */
.next-button {
  display: block;
  margin: 15px auto 0;
  padding: 12px 25px;
  background-color: #0277BD;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.next-button:hover {
  background-color: #01579B;
}

.controls {
  text-align: center;
  margin: 15px 0;
  width: 100%;
  max-width: 800px;
}

.control-button {
  padding: 12px 30px;
  background-color: #0277BD;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.control-button:hover {
  background-color: #01579B;
}
</style>