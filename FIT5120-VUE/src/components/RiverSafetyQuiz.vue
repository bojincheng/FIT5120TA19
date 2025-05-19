<template>
    <div class="container">
      <h1 v-if="!isVerySmallScreen">River Safety for Teens</h1>
      
      <div class="scene" :class="{ 'small-scene': isSmallScreen, 'very-small-scene': isVerySmallScreen }">
        <!-- River environment -->
        <div class="sky"></div>
        <div class="riverbank"></div>
        <div class="river">
          <div class="water">
            <!-- Current lines -->
            <div v-for="n in 5" :key="`current-${n}`" class="current-line" 
                 :style="{ top: `${n * 18}%` }"></div>
            
            <!-- Water ripples -->
            <div v-for="n in 3" :key="`ripple-${n}`" class="ripple"
                 :style="{ 
                   left: `${30 + n * 20}%`, 
                   animationDelay: `${n * 0.5}s`,
                   top: `${20 + n * 25}%`
                 }"></div>
          </div>
        </div>
        
        <!-- Trees and rocks - hide on very small screens -->
        <div v-if="!isVerySmallScreen" class="tree left-tree"></div>
        <div v-if="!isVerySmallScreen" class="tree right-tree"></div>
        <div class="rock big-rock"></div>
        <div class="rock small-rock"></div>
        
        <!-- Warning sign -->
        <div class="warning-sign" :class="{ 'sign-highlighted': currentStep === 0 }">
          <div class="sign-text">!</div>
        </div>
        
        <!-- Floating debris -->
        <div class="debris" v-if="currentStep >= 2"></div>
        
        <!-- Teenager character -->
        <div class="teen" :class="{ 
          onshore: currentStep === 0,
          wading: currentStep === 1,
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
          
          <!-- Thought bubble for teen -->
          <div class="thought-bubble" v-if="currentStep === 2">!</div>
          
          <!-- Splash effect -->
          <div class="splash" v-if="currentStep === 2"></div>
        </div>
        
        <!-- Friend character -->
        <div class="friend" :class="{ 
          cautious: currentStep === 0,
          warning: currentStep === 1,
          helping: currentStep === 2,
          rescuing: currentStep === 3,
          teaching: currentStep === 4
        }">
          <div class="head">
            <div class="face">
              <div class="eyes" :class="{
                attentive: currentStep === 0,
                concerned: currentStep === 1,
                alert: currentStep === 2,
                focused: currentStep === 3,
                attentive: currentStep === 4
              }"></div>
              <div class="mouth" :class="{
                neutral: currentStep === 0,
                frowning: currentStep === 1,
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
          
          <!-- Thought bubble for friend -->
          <div class="thought-bubble friend-bubble" v-if="currentStep === 1">Stop!</div>
        </div>
        
        <!-- Rescue stick/branch -->
        <div class="rescue-stick" v-if="currentStep === 3"></div>
        
        <!-- Quiz result indicator -->
        <div class="quiz-result" v-if="showResults && !quizActive && !quizCompleted">
          <div v-if="lastAnswerCorrect" class="correct-indicator">✓</div>
          <div v-else class="incorrect-indicator">✗</div>
        </div>
        
        <!-- Weather effects -->
        <div class="rain" v-if="currentStep === 2"></div>
      </div>
      
      <div class="step-info" :class="{ 'compact': isSmallScreen, 'very-compact': isVerySmallScreen }" v-if="!quizCompleted">
        <h2>{{ steps[currentStep].title }}</h2>
        <p>{{ steps[currentStep].description }}</p>
        <div class="stat-box">
          <strong>Tip:</strong> {{ steps[currentStep].tip }}
        </div>
      </div>
      
      <div v-if="!quizActive && currentStep === 0 && !quizCompleted" class="controls">
        <button @click="startQuiz" class="control-button">
          Start Safety Scenario
        </button>
      </div>
      
      <div class="quiz-container" v-if="quizActive && !quizCompleted">
        <div class="timer">
          <div class="timer-bar" :style="{ width: `${timeRemaining * (isSmallScreen ? 10 : 6.67)}%` }"></div>
          <div class="timer-text">{{ timeRemaining }} seconds</div>
        </div>
        
        <div class="question">
          <h3>{{ isSmallScreen ? 'Scenario:' : 'What would you do?' }}</h3>
          <p>{{ currentQuestion.scenario }}</p>
        </div>
        
        <!-- Thinking phase -->
        <div v-if="quizPhase === 'thinking'" class="thinking-phase">
          <p>{{ isSmallScreen ? 'Think about what you would do...' : 'Take a moment to think about what you would do in this situation...' }}</p>
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
      
      <!-- Quiz completion summary -->
      <div class="quiz-summary" v-if="quizCompleted">
        <div class="summary-header">
          <h2>River Safety Quiz Complete!</h2>
          <div class="score-display">
            <div class="score">
              <span class="score-number">{{ correctAnswers }}</span>
              <span class="score-total">/ {{ totalQuestions }}</span>
            </div>
            <div class="score-label">Correct Answers</div>
          </div>
        </div>
        
        <div class="key-learnings">
          <h3>Key Safety Takeaways:</h3>
          <ul>
            <li v-for="(takeaway, index) in keyTakeaways" :key="index">
              {{ takeaway }}
            </li>
          </ul>
        </div>
        
        <div class="scenario-summary">
          <h3>Remember These Scenarios:</h3>
          <div class="scenario-cards">
            <div v-for="(step, index) in steps" :key="index" class="scenario-card">
              <div class="scenario-number">{{ index + 1 }}</div>
              <h4>{{ step.title }}</h4>
              <p>{{ step.tip }}</p>
            </div>
          </div>
        </div>
        
        <div class="final-message">
          <p>Rivers can be unpredictable and dangerous. Always prioritize safety over fun, be aware of changing conditions, and look out for your friends.</p>
        </div>
        
        <button @click="restartQuiz" class="restart-button">
          Restart Quiz
        </button>
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
        timeRemaining: 20, // Increased time for scenario-based questions
        timerInterval: null,
        lastAnswerCorrect: false,
        isInIframe: false,
        windowHeight: window.innerHeight,
        windowWidth: window.innerWidth,
        quizCompleted: false,
        correctAnswers: 0,
        totalQuestions: 5,
        keyTakeaways: [
          "Always check for warning signs and assess river conditions before entering",
          "Strong currents can exist beneath calm-looking water surfaces",
          "Never swim alone - always have a buddy watching out for you",
          "If caught in a current, float on your back with feet downstream and angle toward shore",
          "Use 'Reach, Throw, Row, Go' for rescues - avoid entering dangerous water yourself"
        ],
        steps: [
          {
            title: "Recognizing Hazards",
            description: "The teens are at the riverbank, noticing warning signs. Rivers can have hidden dangers like strong currents, submerged objects, and sudden drop-offs that aren't visible from the surface.",
            tip: "Always check for posted warning signs and learn to identify natural warning signs like discolored water, debris, or unusual water patterns that may indicate dangerous conditions."
          },
          {
            title: "Peer Pressure Situation",
            description: "One teen is wading into potentially dangerous water while their friend warns them to stop. Peer pressure can lead to risky decisions around water.",
            tip: "Be the voice of reason in your friend group. It takes courage to speak up when someone is about to do something dangerous."
          },
          {
            title: "Underestimating Current",
            description: "The teen is now struggling in the current. Even strong swimmers can be overwhelmed by river currents, which can be much stronger than they appear on the surface.",
            tip: "River currents can be 3-4 times stronger than ocean currents of the same speed. Just 6 inches of fast-moving water can knock you off your feet."
          },
          {
            title: "Safe Rescue Techniques",
            description: "The friend is attempting a safe rescue by extending a branch. Never enter the water to save someone unless you're trained in water rescue.",
            tip: "Remember 'Reach, Throw, Row, Go' - try reaching or throwing something to the person before considering entering the water yourself."
          },
          {
            title: "River Safety Education",
            description: "Both teens are now safe and discussing what they've learned. Understanding river dynamics and having a safety plan can prevent dangerous situations.",
            tip: "Always go to rivers with friends, wear a life jacket when appropriate, and let someone know where you're going and when you'll return."
          }
        ],
        questions: [
          {
            // Question for Scenario 1: Recognizing Hazards
            scenario: "You and your friends arrive at a river on a hot summer day. The water looks calm on the surface, but you notice some unusual swirling patterns and a warning sign that's partially hidden by bushes. Your friends are eager to jump in right away. What would you do?",
            options: [
              "Join them immediately - the water looks calm enough and everyone's excited",
              "Suggest checking out the warning sign first and looking for a designated swimming area",
              "Test the water by wading in slowly before deciding if it's safe to swim",
              "Let your friends go first while you watch from the shore"
            ],
            correctAnswer: 1,
            explanation: "Always check warning signs and assess river conditions before entering. The unusual swirling patterns could indicate dangerous undercurrents that aren't visible from the surface. Designated swimming areas are chosen because they've been assessed for safety.",
            additionalInfo: "According to river safety experts, many drownings occur because people fail to recognize warning signs. Swirling patterns, discolored water, and debris are natural indicators of potentially dangerous conditions. Taking just a few minutes to properly assess a river can prevent tragedy."
          },
          {
            // Question for Scenario 2: Peer Pressure
            scenario: "Your group finds a spot where the river narrows and flows quickly between large rocks. One of your friends says, 'I bet I can swim across to the other side!' and starts preparing to jump in. Others are encouraging them. What would you do?",
            options: [
              "Join in - if they can do it, you can too",
              "Film it on your phone - it'll make a great social media post",
              "Point out the dangers and suggest finding a safer place to swim",
              "Stay quiet - it's not your place to tell others what to do"
            ],
            correctAnswer: 2,
            explanation: "Speaking up about safety concerns could save a life. Narrow sections with fast-flowing water are extremely dangerous as the current is concentrated and more powerful. The pressure to 'go along' with risky behavior is a major factor in teen drownings.",
            additionalInfo: "Research shows that in 75% of teen drowning incidents, other people were present who could have intervened. Having the courage to speak up against peer pressure is difficult but crucial. Practicing phrases like 'That doesn't seem worth the risk' or 'Let's find a safer spot' can help you be prepared to resist pressure in the moment."
          },
          {
            // Question for Scenario 3: Underestimating Current
            scenario: "While wading in what seemed like calm water, you suddenly feel the current pulling strongly at your legs and you're losing your footing. The shore seems far away now. What's your best immediate action?",
            options: [
              "Swim hard directly against the current to get back to where you started",
              "Float on your back with feet pointed downstream, then angle gradually toward shore",
              "Call loudly for help while trying to stand up against the current",
              "Swim with all your strength toward the nearest shore using a front crawl"
            ],
            correctAnswer: 1,
            explanation: "The defensive swimming position (floating on your back with feet downstream) protects your head from impacts with rocks while allowing you to see and navigate. Swimming at an angle with the current conserves energy while making progress toward shore.",
            additionalInfo: "River rescue experts teach that fighting directly against a current quickly leads to exhaustion. A moderate current of just 5 mph exerts about 250 pounds of force against an average person - impossible to overcome with swimming strength alone. The defensive swimming position uses the current's energy while protecting you from obstacles."
          },
          {
            // Question for Scenario 4: Safe Rescue
            scenario: "You're on the riverbank when you see someone struggling in the current about 15 feet from shore. They're panicking and calling for help. There's a long branch nearby and other people in the area. What should you do first?",
            options: [
              "Immediately jump in to swim to them - every second counts",
              "Shout instructions for them to swim harder toward shore",
              "Call for help from others while grabbing the branch to extend to the person",
              "Run downstream to try to intercept them when they float by"
            ],
            correctAnswer: 2,
            explanation: "The 'Reach, Throw, Row, Go' rescue hierarchy prioritizes your safety while helping others. Extending a branch (reach) allows you to help without entering dangerous water. Calling for help ensures additional resources if your first attempt fails.",
            additionalInfo: "Drowning statistics show that approximately 70% of drowning deaths occur during rescue attempts, creating multiple victims from a single incident. Even trained lifeguards use equipment and approach from behind to avoid being grabbed by panicking victims. The safest rescue is one where the rescuer stays on land while extending or throwing rescue aids."
          },
          {
            // Question for Scenario 5: River Safety Education
            scenario: "After a close call at the river, your friend group is discussing what they learned. Which combination of safety practices would create the most effective protection against future incidents?",
            options: [
              "Checking weather forecasts and bringing waterproof phone cases",
              "Swimming only in designated areas, wearing life jackets when appropriate, and always using the buddy system",
              "Bringing first aid kits and emergency whistles",
              "Swimming during daylight hours and avoiding alcohol"
            ],
            correctAnswer: 1,
            explanation: "The most effective approach combines multiple safety layers: swimming in designated areas (environmental protection), wearing appropriate life jackets (personal protection), and using the buddy system (supervision). This creates multiple barriers against drowning.",
            additionalInfo: "The concept of 'layers of protection' is endorsed by all major water safety organizations. If one layer fails (like a momentary lapse in supervision), other layers (like a proper life jacket) can prevent tragedy. While all the options contain good practices, the correct answer provides the most comprehensive protection through multiple safety layers."
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
        this.timeRemaining = this.isSmallScreen ? 15 : 20; // Longer time for scenario-based questions
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
        if (this.lastAnswerCorrect) {
          this.correctAnswers++;
        }
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
          } else {
            // Quiz is complete
            this.completeQuiz();
          }
        }, 2000);
      },
      completeQuiz() {
        this.quizCompleted = true;
        // Calculate final score
        this.totalQuestions = this.questions.length;
      },
      restartQuiz() {
        this.quizCompleted = false;
        this.currentStep = 0;
        this.currentQuestionIndex = 0;
        this.correctAnswers = 0;
        this.quizActive = false;
        this.selectedAnswer = null;
        this.showResults = false;
      },
      handleMessage(event) {
        // Handle messages from parent
        if (event.data && event.data.type === 'close-quiz') {
          // Reset quiz state if needed
          clearInterval(this.timerInterval);
          this.quizActive = false;
          this.currentStep = 0;
          this.currentQuestionIndex = 0;
          this.quizCompleted = false;
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
    min-height: auto;
    margin: 0;
    padding: 15px 25px;
    font-family: Arial, sans-serif;
    color: #333;
    background-color: #f5f5f5;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: center;
    overflow-x: hidden;
    overflow-y: auto; /* Allow vertical scrolling to see content */
    padding-bottom: 30px; /* Add bottom padding to ensure visibility */
  }
  
  h1 {
    text-align: center;
    color: #1565C0;
    margin: 0 0 10px 0;
    font-size: 1.8rem;
  }
  
  /* River scene styling - optimized for larger view */
  .scene {
    position: relative;
    width: 100%;
    max-width: 1000px;
    height: 38vh;
    min-height: 250px;
    max-height: 450px;
    border-radius: 10px;
    overflow: hidden;
    margin-bottom: 15px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }
  
  /* River environment */
  .sky {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 40%;
    background: linear-gradient(to bottom, #64B5F6, #90CAF9);
    z-index: 1;
  }
  
  .riverbank {
    position: absolute;
    top: 40%;
    left: 0;
    width: 100%;
    height: 20%;
    background-color: #8D6E63;
    z-index: 2;
  }
  
  .river {
    position: absolute;
    top: 60%;
    left: 0;
    width: 100%;
    height: 40%;
    overflow: hidden;
    z-index: 3;
  }
  
  .water {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to bottom, #1976D2, #0D47A1);
    animation: flow 8s linear infinite;
  }
  
  @keyframes flow {
    0% {
      background-position: 0 0;
    }
    100% {
      background-position: 100px 0;
    }
  }
  
  .current-line {
    position: absolute;
    left: 0;
    width: 100%;
    height: 2px;
    background-color: rgba(255, 255, 255, 0.2);
    animation: currentFlow 3s linear infinite;
  }
  
  @keyframes currentFlow {
    0% {
      transform: translateX(-100%);
    }
    100% {
      transform: translateX(100%);
    }
  }
  
  /* Water ripples */
  .ripple {
    position: absolute;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    border: 2px solid rgba(255, 255, 255, 0.3);
    animation: rippleEffect 3s infinite;
  }
  
  @keyframes rippleEffect {
    0% {
      transform: scale(0);
      opacity: 1;
    }
    100% {
      transform: scale(3);
      opacity: 0;
    }
  }
  
  /* Trees */
  .tree {
    position: absolute;
    z-index: 4;
  }
  
  .tree:before {
    content: '';
    position: absolute;
    width: 40px;
    height: 40px;
    background-color: #2E7D32;
    border-radius: 50%;
  }
  
  .tree:after {
    content: '';
    position: absolute;
    width: 10px;
    height: 20px;
    background-color: #5D4037;
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
  
  /* Rocks */
  .rock {
    position: absolute;
    background-color: #757575;
    border-radius: 50% 50% 25% 25%;
    z-index: 4;
  }
  
  .big-rock {
    width: 60px;
    height: 40px;
    top: 55%;
    left: 20%;
  }
  
  .small-rock {
    width: 30px;
    height: 20px;
    top: 58%;
    right: 25%;
  }
  
  /* Warning sign */
  .warning-sign {
    position: absolute;
    top: 45%;
    right: 15%;
    width: 30px;
    height: 30px;
    background-color: #FFC107;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 5;
    border: 3px solid #333;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  
  .sign-text {
    color: #333;
    font-weight: bold;
    font-size: 20px;
  }
  
  .sign-highlighted {
    transform: scale(1.2);
    box-shadow: 0 0 15px rgba(255, 255, 0, 0.8);
    animation: pulse 1.5s infinite;
  }
  
  @keyframes pulse {
    0%, 100% {
      transform: scale(1.2);
    }
    50% {
      transform: scale(1.3);
    }
  }
  
  /* Floating debris */
  .debris {
    position: absolute;
    width: 40px;
    height: 15px;
    background-color: #795548;
    border-radius: 10px;
    top: 65%;
    left: 70%;
    z-index: 6;
    animation: floatDebris 8s linear infinite;
  }
  
  @keyframes floatDebris {
    0% {
      transform: translateX(100%) rotate(0deg);
    }
    100% {
      transform: translateX(-200%) rotate(360deg);
    }
  }
  
  /* Teen character */
  .teen {
    position: absolute;
    height: 80px;
    width: 40px;
    z-index: 10;
    transition: all 1.5s ease;
  }
  
  .teen .head {
    position: absolute;
    top: 0;
    left: 10px;
    width: 20px;
    height: 20px;
    background-color: #FFCC80;
    border-radius: 50%;
    overflow: hidden;
  }
  
  .teen .face {
    position: relative;
    width: 100%;
    height: 100%;
  }
  
  .teen .eyes {
    position: absolute;
    top: 6px;
    width: 100%;
    height: 4px;
  }
  
  .teen .eyes:before, .teen .eyes:after {
    content: '';
    position: absolute;
    width: 4px;
    height: 4px;
    background-color: #5D4037;
    border-radius: 50%;
  }
  
  .teen .eyes:before {
    left: 4px;
  }
  
  .teen .eyes:after {
    right: 4px;
  }
  
  .teen .eyes.happy:before, .teen .eyes.happy:after {
    height: 3px;
    border-radius: 3px 3px 0 0;
    transform: translateY(-1px);
  }
  
  .teen .eyes.panicked:before, .teen .eyes.panicked:after {
    height: 5px;
    width: 5px;
    animation: blink 0.5s infinite;
  }
  
  @keyframes blink {
    0%, 100% {
      transform: scaleY(1);
    }
    50% {
      transform: scaleY(0.1);
    }
  }
  
  .teen .mouth {
    position: absolute;
    bottom: 4px;
    left: 6px;
    width: 8px;
    height: 3px;
    background-color: #5D4037;
    border-radius: 1px;
  }
  
  .teen .mouth.smiling {
    height: 4px;
    width: 8px;
    border-radius: 0 0 4px 4px;
    transform: translateY(-1px);
  }
  
  .teen .mouth.gasping {
    height: 5px;
    width: 5px;
    border-radius: 50%;
    animation: gasp 0.7s infinite;
  }
  
  .teen .mouth.calm {
    width: 6px;
  }
  
  @keyframes gasp {
    0%, 100% {
      height: 3px;
      border-radius: 1px;
    }
    50% {
      height: 5px;
      border-radius: 50%;
    }
  }
  
  .teen .body {
    position: absolute;
    top: 20px;
    left: 13px;
    width: 14px;
    height: 30px;
    background-color: #42A5F5;
    border-radius: 4px;
  }
  
  .teen .arm {
    position: absolute;
    width: 4px;
    height: 20px;
    background-color: #FFCC80;
    transition: transform 0.5s ease;
  }
  
  .teen .arm.left {
    top: 24px;
    left: 8px;
    transform-origin: top center;
  }
  
  .teen .arm.right {
    top: 24px;
    right: 8px;
    transform-origin: top center;
  }
  
  .teen.struggling .arm.left {
    animation: armFlail 0.5s infinite;
  }
  
  .teen.struggling .arm.right {
    animation: armFlail 0.5s infinite reverse;
  }
  
  @keyframes armFlail {
    0%, 100% {
      transform: rotate(-30deg);
    }
    50% {
      transform: rotate(30deg);
    }
  }
  
  .teen .leg {
    position: absolute;
    width: 4px;
    height: 24px;
    background-color: #FFCC80;
    transition: transform 0.5s ease;
  }
  
  .teen .leg.left {
    top: 50px;
    left: 12px;
    transform-origin: top center;
  }
  
  .teen .leg.right {
    top: 50px;
    right: 12px;
    transform-origin: top center;
  }
  
  .teen.struggling .leg.left {
    animation: legKick 0.7s infinite;
  }
  
  .teen.struggling .leg.right {
    animation: legKick 0.7s infinite reverse;
  }
  
  @keyframes legKick {
    0%, 100% {
      transform: rotate(-15deg);
    }
    50% {
      transform: rotate(15deg);
    }
  }
  
  .teen.onshore {
    top: 40%;
    left: 40%;
  }
  
  .teen.wading {
    top: 50%;
    left: 50%;
    animation: wade 3s infinite;
  }
  
  @keyframes wade {
    0%, 100% {
      transform: translateY(0);
    }
    50% {
      transform: translateY(-5px);
    }
  }
  
  .teen.struggling {
    top: 65%;
    left: 60%;
    animation: drowning 1s infinite;
  }
  
  @keyframes drowning {
    0%, 100% {
      transform: translateY(0) rotate(0deg);
    }
    25% {
      transform: translateY(-8px) rotate(-10deg);
    }
    75% {
      transform: translateY(-8px) rotate(10deg);
    }
  }
  
  .teen.rescued {
    top: 55%;
    left: 40%;
    transition: all 2s ease;
  }
  
  .teen.safe {
    top: 45%;
    left: 30%;
  }
  
  /* Splash effect */
  .splash {
    position: absolute;
    top: -10px;
    left: -10px;
    width: 60px;
    height: 20px;
    z-index: 9;
  }
  
  .splash:before, .splash:after {
    content: '';
    position: absolute;
    background-color: rgba(255, 255, 255, 0.7);
    width: 15px;
    height: 20px;
    border-radius: 50%;
    animation: splashEffect 0.8s infinite;
  }
  
  .splash:before {
    left: 0;
    animation-delay: 0s;
  }
  
  .splash:after {
    right: 0;
    animation-delay: 0.4s;
  }
  
  @keyframes splashEffect {
    0% {
      transform: scale(0) translateY(0);
      opacity: 0.8;
    }
    100% {
      transform: scale(1) translateY(-15px);
      opacity: 0;
    }
  }
  
  /* Friend character */
  .friend {
    position: absolute;
    height: 80px;
    width: 40px;
    z-index: 10;
    transition: all 1.5s ease;
  }
  
  .friend .head {
    position: absolute;
    top: 0;
    left: 10px;
    width: 20px;
    height: 20px;
    background-color: #FFCC80;
    border-radius: 50%;
    overflow: hidden;
  }
  
  .friend .face {
    position: relative;
    width: 100%;
    height: 100%;
  }
  
  .friend .eyes {
    position: absolute;
    top: 6px;
    width: 100%;
    height: 4px;
  }
  
  .friend .eyes:before, .friend .eyes:after {
    content: '';
    position: absolute;
    width: 4px;
    height: 4px;
    background-color: #5D4037;
    border-radius: 50%;
  }
  
  .friend .eyes:before {
    left: 4px;
  }
  
  .friend .eyes:after {
    right: 4px;
  }
  
  .friend .eyes.alert:before, .friend .eyes.alert:after {
    height: 5px;
    width: 5px;
  }
  
  .friend .mouth {
    position: absolute;
    bottom: 4px;
    left: 6px;
    width: 8px;
    height: 3px;
    background-color: #5D4037;
    border-radius: 1px;
  }
  
  .friend .mouth.frowning {
    width: 8px;
    height: 4px;
    border-radius: 4px 4px 0 0;
    transform: translateY(1px);
  }
  
  .friend .mouth.concerned {
    width: 8px;
    height: 4px;
    border-radius: 4px 4px 0 0;
    transform: translateY(1px);
  }
  
  .friend .mouth.determined {
    width: 10px;
    height: 3px;
  }
  
  .friend .mouth.talking {
    animation: talking 1s infinite;
  }
  
  @keyframes talking {
    0%, 100% {
      height: 3px;
      width: 7px;
    }
    50% {
      height: 4px;
      width: 8px;
    }
  }
  
  .friend .body {
    position: absolute;
    top: 20px;
    left: 13px;
    width: 14px;
    height: 30px;
    background-color: #EF5350;
    border-radius: 4px;
  }
  
  .friend .arm {
    position: absolute;
    width: 4px;
    height: 20px;
    background-color: #FFCC80;
    transition: transform 0.5s ease;
  }
  
  .friend .arm.left {
    top: 24px;
    left: 8px;
    transform-origin: top center;
  }
  
  .friend .arm.right {
    top: 24px;
    right: 8px;
    transform-origin: top center;
  }
  
  .friend.warning .arm.right {
    transform: rotate(-45deg);
  }
  
  .friend.helping .arm.right {
    transform: rotate(-30deg);
  }
  
  .friend.rescuing .arm.right {
    transform: rotate(-60deg);
  }
  
  .friend .leg {
    position: absolute;
    width: 4px;
    height: 24px;
    background-color: #FFCC80;
  }
  
  .friend .leg.left {
    top: 50px;
    left: 12px;
  }
  
  .friend .leg.right {
    top: 50px;
    right: 12px;
  }
  
  .friend.cautious {
    top: 40%;
    left: 25%;
  }
  
  .friend.warning {
    top: 45%;
    left: 35%;
    animation: warning 0.5s infinite;
  }
  
  @keyframes warning {
    0%, 100% {
      transform: rotate(0deg);
    }
    50% {
      transform: rotate(5deg);
    }
  }
  
  .friend.helping {
    top: 50%;
    left: 45%;
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
  
  .friend.rescuing {
    top: 50%;
    left: 50%;
  }
  
  .friend.teaching {
    top: 45%;
    left: 40%;
  }
  
  /* Rescue stick */
  .rescue-stick {
    position: absolute;
    top: 55%;
    left: 50%;
    width: 80px;
    height: 4px;
    background-color: #8D6E63;
    transform-origin: left center;
    transform: rotate(20deg);
    z-index: 9;
  }
  
  /* Thought bubbles */
  .thought-bubble {
    position: absolute;
    top: -30px;
    left: 0;
    width: 40px;
    height: 40px;
    background-color: white;
    border-radius: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    z-index: 20;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    animation: bobUpDown 2s infinite;
  }
  
  @keyframes bobUpDown {
    0%, 100% {
      transform: translateY(0);
    }
    50% {
      transform: translateY(-5px);
    }
  }
  
  .friend-bubble {
    left: auto;
    right: -25px;
  }
  
  /* Rain effect */
  .rain {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 40%;
    z-index: 7;
    pointer-events: none;
  }
  
  .rain:before {
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    background: linear-gradient(to bottom, transparent, rgba(255,255,255,0.2));
    animation: rainfall 0.5s linear infinite;
  }
  
  @keyframes rainfall {
    0% {
      background-position: 0 0;
    }
    100% {
      background-position: 0 20px;
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
  
  /* Step info - optimized for compact display */
  .step-info {
    background-color: #E3F2FD;
    padding: 12px 15px;
    border-radius: 8px;
    margin-bottom: 15px;
    border-left: 5px solid #1565C0;
    width: 100%;
    max-width: 1000px;
  }
  
  .step-info h2 {
    margin-top: 0;
    margin-bottom: 6px;
    color: #1565C0;
    font-size: 1.4rem;
  }
  
  .step-info p {
    line-height: 1.5;
    margin: 0 0 10px 0;
    font-size: 1rem;
  }
  
  .stat-box {
    margin-top: 10px;
    padding: 8px 10px;
    background-color: #fff;
    border-radius: 5px;
    border-left: 3px solid #F44336;
    font-size: 0.95rem;
  }
  
  /* Quiz container - optimized for better space usage */
  .quiz-container {
    background-color: #F5F5F5;
    padding: 15px 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    width: 100%;
    max-width: 1000px;
    margin-bottom: 15px;
    overflow-y: visible; /* Ensure content can be scrolled into view */
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
    background-color: #1565C0;
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
    color: #1565C0;
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
  
  /* Options grid - optimized for better display */
  .options {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 10px;
    margin-bottom: 15px;
    width: 100%;
  }
  
  .option-button {
    padding: 15px;
    background-color: white;
    border: 2px solid #1565C0;
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
  
  /* Feedback section styling - ensure visibility */
  .feedback {
    margin-top: 15px;
    width: 100%;
    padding-bottom: 15px; /* Add bottom padding for better visibility */
  }
  
  .correct-feedback, .incorrect-feedback {
    background-color: #C8E6C9;
    color: #2E7D32;
    padding: 18px;
    border-radius: 8px;
    margin-bottom: 15px;
    width: 100%;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); /* Add shadow for better visibility */
  }
  
  .incorrect-feedback {
    background-color: #FFCDD2;
    color: #C62828;
  }
  
  .feedback h3 {
    margin: 0 0 10px 0;
    font-size: 1.3rem; /* Increased size for better visibility */
    font-weight: 700;
  }
  
  .feedback p {
    font-size: 1.05rem; /* Increased size for better readability */
    line-height: 1.5;
    margin-bottom: 12px; /* Add margin for spacing */
  }
  
  .additional-info {
    margin-top: 15px;
    padding: 15px;
    background-color: rgba(21, 101, 192, 0.05); /* Lighter background */
    border-left: 3px solid #1565C0;
    border-radius: 0 8px 8px 0;
    width: 100%;
    box-shadow: 0 1px 5px rgba(0, 0, 0, 0.05); /* Subtle shadow */
  }
  
  .additional-info h4 {
    margin-top: 0;
    margin-bottom: 10px;
    color: #1565C0;
    font-size: 1.1rem; /* Increased size */
    font-weight: 600;
  }
  
  .additional-info p {
    margin: 0;
    font-size: 1rem; /* Increased size */
    line-height: 1.5;
    color: #333; /* Darker text for better contrast */
  }
  
  .next-button {
    display: block;
    margin: 18px auto 10px; /* Increased top margin */
    padding: 12px 28px; /* Larger button */
    background-color: #1565C0;
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 1.1rem; /* Larger text */
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Add shadow */
  }
  
  .next-button:hover {
    background-color: #0D47A1;
    transform: translateY(-2px); /* Slight lift effect */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
  }
  
  .controls {
    text-align: center;
    margin: 10px 0;
    flex-shrink: 0;
  }
  
  .control-button {
    padding: 12px 24px;
    background-color: #1565C0;
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 1rem;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .control-button:hover {
    background-color: #0D47A1;
  }
  
  /* Quiz completion summary - more compact */
  .quiz-summary {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    width: 100%;
    max-width: 1000px;
    margin-bottom: 15px;
    animation: fadeIn 0.5s ease-in;
  }
  
  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: translateY(20px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  .summary-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    padding-bottom: 15px;
    border-bottom: 1px solid #E0E0E0;
  }
  
  .summary-header h2 {
    color: #1565C0;
    margin: 0;
    font-size: 1.6rem;
  }
  
  .score-display {
    text-align: center;
  }
  
  .score {
    display: flex;
    align-items: baseline;
    justify-content: center;
  }
  
  .score-number {
    font-size: 2.5rem;
    font-weight: bold;
    color: #1565C0;
  }
  
  .score-total {
    font-size: 1.5rem;
    color: #757575;
    margin-left: 5px;
  }
  
  .score-label {
    font-size: 0.9rem;
    color: #757575;
    margin-top: 5px;
  }
  
  .key-learnings {
    margin-bottom: 25px;
  }
  
  .key-learnings h3 {
    color: #1565C0;
    margin: 0 0 15px 0;
    font-size: 1.3rem;
  }
  
  .key-learnings ul {
    margin: 0;
    padding-left: 20px;
  }
  
  .key-learnings li {
    margin-bottom: 10px;
    line-height: 1.5;
  }
  
  .scenario-summary {
    margin-bottom: 25px;
  }
  
  .scenario-summary h3 {
    color: #1565C0;
    margin: 0 0 15px 0;
    font-size: 1.3rem;
  }
  
  .scenario-cards {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 12px;
  }
  
  .scenario-card {
    background-color: #F5F5F5;
    border-radius: 8px;
    padding: 15px;
    position: relative;
    border-left: 4px solid #1565C0;
  }
  
  .scenario-number {
    position: absolute;
    top: -10px;
    right: -10px;
    width: 30px;
    height: 30px;
    background-color: #1565C0;
    color: white;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
  }
  
  .scenario-card h4 {
    margin: 0 0 10px 0;
    color: #1565C0;
  }
  
  .scenario-card p {
    margin: 0;
    font-size: 0.9rem;
    line-height: 1.4;
  }
  
  .final-message {
    background-color: #E3F2FD;
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 20px;
    border-left: 5px solid #1565C0;
  }
  
  .final-message p {
    margin: 0;
    line-height: 1.5;
    font-weight: bold;
  }
  
  .restart-button {
    display: block;
    margin: 0 auto;
    padding: 12px 30px;
    background-color: #1565C0;
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 1.1rem;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .restart-button:hover {
    background-color: #0D47A1;
  }
  
  /* Responsive adjustments for larger screens in popup */
  @media (min-width: 1400px) {
    .scene {
      max-width: 1200px;
      height: 40vh;
      max-height: 500px;
    }
    
    .step-info, .quiz-container, .quiz-summary {
      max-width: 1200px;
    }
    
    .options {
      grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
    }
  }
  
  /* More compact for very small screens */
  @media (max-height: 750px) {
    .scene {
      height: 35vh;
      min-height: 200px;
    }
    
    .step-info {
      padding: 10px 12px;
    }
    
    .step-info h2 {
      font-size: 1.2rem;
      margin-bottom: 5px;
    }
    
    .stat-box {
      margin-top: 8px;
      padding: 6px 8px;
    }
  }
  
  /* Ensure scrollability of quiz sections */
  .quiz-container, .options, .feedback, .additional-info {
    overflow: visible;
  }
  </style>