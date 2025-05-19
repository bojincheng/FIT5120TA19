<template>
    <div class="container">
      <h1 v-if="!isVerySmallScreen">Beach Rip Current Safety</h1>
      
      <div class="scene" :class="{ 'small-scene': isSmallScreen, 'very-small-scene': isVerySmallScreen }">
        <!-- Beach environment with weather conditions -->
        <div class="sky" :class="{ 'stormy': currentStep >= 2 }"></div>
        <div class="beach"></div>
        <div class="ocean" :class="{ 'rough': currentStep >= 2 }">
          <div class="water">
            <!-- Wave animations -->
            <div v-for="n in 4" :key="`wave-${n}`" class="wave" 
                 :style="{ 
                   animationDelay: `${n * 0.3}s`,
                   top: `${5 + n * 18}%`,
                   animationDuration: `${currentStep >= 2 ? 4 : 8}s`
                 }"></div>
            
            <!-- Multiple rip currents -->
            <div class="rip-current main-rip" :class="{ 'active': currentStep >= 1 }">
              <div v-for="n in 6" :key="`rip-main-${n}`" class="rip-line"
                   :style="{ 
                     top: `${n * 15}%`,
                     animationDuration: `${2 + n * 0.3}s`
                   }"></div>
            </div>
            
            <div class="rip-current secondary-rip" :class="{ 'active': currentStep >= 2 }">
              <div v-for="n in 6" :key="`rip-sec-${n}`" class="rip-line"
                   :style="{ 
                     top: `${n * 15}%`,
                     animationDuration: `${2 + n * 0.3}s`
                   }"></div>
            </div>
            
            <!-- Foam patterns -->
            <div class="foam-pattern" :class="{ 'active': currentStep >= 1 }"></div>
          </div>
        </div>
        
        <!-- Beach elements -->
        <div v-if="!isVerySmallScreen" class="umbrella left-umbrella"></div>
        <div v-if="!isVerySmallScreen" class="umbrella right-umbrella"></div>
        <div class="beach-ball" :class="{ 'floating': currentStep === 2, 'drifting': currentStep >= 3 }"></div>
        
        <!-- Sandbar visualization -->
        <div class="sandbar" :class="{ 'visible': currentStep >= 1 }"></div>
        
        <!-- Safety flags -->
        <div class="safety-flag red-flag" :class="{ 'flag-highlighted': currentStep === 0 }">
          <div class="flag-pole"></div>
          <div class="flag red"></div>
        </div>
        
        <div class="safety-flag yellow-flag" :class="{ 'visible': currentStep >= 1 }">
          <div class="flag-pole"></div>
          <div class="flag yellow"></div>
        </div>
        
        <!-- Lifeguard tower -->
        <div class="lifeguard-tower" :class="{ 'tower-active': currentStep === 4 }">
          <div class="tower-base"></div>
          <div class="tower-top"></div>
          <div class="lifeguard" v-if="currentStep >= 3"></div>
        </div>
        
        <!-- Other beachgoers -->
        <div class="beachgoers" v-if="currentStep >= 1">
          <div class="beachgoer one"></div>
          <div class="beachgoer two"></div>
          <div class="beachgoer three"></div>
        </div>
        
        <!-- Parent character -->
        <div class="parent" :class="{ 
          onshore: currentStep === 0,
          watching: currentStep === 1,
          alerting: currentStep === 2,
          rescuing: currentStep === 3,
          teaching: currentStep === 4
        }">
          <div class="head">
            <div class="face">
              <div class="eyes" :class="{
                scanning: currentStep === 0,
                focused: currentStep === 1,
                alarmed: currentStep === 2,
                determined: currentStep === 3,
                teaching: currentStep === 4
              }"></div>
              <div class="mouth" :class="{
                neutral: currentStep === 0,
                concerned: currentStep === 1,
                shouting: currentStep === 2,
                strained: currentStep === 3,
                talking: currentStep === 4
              }"></div>
            </div>
          </div>
          <div class="body"></div>
          <div class="arm left"></div>
          <div class="arm right"></div>
          <div class="leg left"></div>
          <div class="leg right"></div>
          
          <!-- Parent speech bubble -->
          <div class="speech-bubble parent-bubble" v-if="currentStep === 2">Swim parallel!</div>
        </div>
        
        <!-- Child character -->
        <div class="child" :class="{ 
          playing: currentStep === 0,
          swimming: currentStep === 1,
          drifting: currentStep === 2,
          floating: currentStep === 3,
          learning: currentStep === 4
        }">
          <div class="head">
            <div class="face">
              <div class="eyes" :class="{
                happy: currentStep === 0,
                curious: currentStep === 1,
                scared: currentStep === 2,
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
          
          <!-- Child thought bubble -->
          <div class="thought-bubble child-bubble" v-if="currentStep === 2">Help!</div>
          
          <!-- Splash effect -->
          <div class="splash" v-if="currentStep === 2"></div>
        </div>
        
        <!-- Second child -->
        <div class="second-child" v-if="currentStep >= 2" :class="{
          drifting: currentStep === 2,
          struggling: currentStep === 3,
          rescued: currentStep === 4
        }">
          <div class="head"></div>
          <div class="body"></div>
          <div class="arm left"></div>
          <div class="arm right"></div>
          <div class="leg left"></div>
          <div class="leg right"></div>
          
          <div class="splash" v-if="currentStep === 2"></div>
        </div>
        
        <!-- Rescue equipment -->
        <div class="rescue-tube" v-if="currentStep >= 3" :class="{ 'in-use': currentStep === 3 }"></div>
        
        <!-- Weather effects -->
        <div class="wind" v-if="currentStep >= 2"></div>
        <div class="rain" v-if="currentStep >= 3"></div>
        
        <!-- Quiz result indicator -->
        <div class="quiz-result" v-if="showResults && !quizActive && !quizCompleted">
          <div v-if="lastAnswerCorrect" class="correct-indicator">✓</div>
          <div v-else class="incorrect-indicator">✗</div>
        </div>
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
          Start Quiz
        </button>
      </div>
      
      <div class="quiz-container" v-if="quizActive && !quizCompleted">
        <div class="timer">
          <div class="timer-bar" :style="{ width: `${timeRemaining * (isSmallScreen ? 10 : 5)}%` }"></div>
          <div class="timer-text">{{ timeRemaining }}s</div>
        </div>
        
        <div class="question">
          <h3>Scenario:</h3>
          <p>{{ currentQuestion.scenario }}</p>
        </div>
        
        <!-- Thinking phase -->
        <div v-if="quizPhase === 'thinking'" class="thinking-phase">
          <p>Analyze this situation...</p>
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
          </div>
          <div v-else class="incorrect-feedback">
            <h3>Incorrect</h3>
            <p>{{ currentQuestion.explanation }}</p>
          </div>
          <button @click="continueAfterQuestion" class="next-button">
            Continue
          </button>
        </div>
      </div>
      
      <!-- Quiz completion summary -->
      <div class="quiz-summary" v-if="quizCompleted">
        <div class="summary-header">
          <h2>Quiz Complete</h2>
          <div class="score-display">
            <div class="score">
              <span class="score-number">{{ correctAnswers }}</span>
              <span class="score-total">/ {{ totalQuestions }}</span>
            </div>
            <div class="score-label">Correct</div>
          </div>
        </div>
        
        <div class="key-learnings">
          <h3>Key Safety Points:</h3>
          <ul>
            <li v-for="(takeaway, index) in keyTakeaways" :key="index">
              {{ takeaway }}
            </li>
          </ul>
        </div>
        
        <div class="rip-identification">
          <h3>How to Spot Rip Currents:</h3>
          <div class="rip-indicators">
            <div class="indicator">
              <div class="indicator-icon color-diff"></div>
              <p>Darker water color</p>
            </div>
            <div class="indicator">
              <div class="indicator-icon calm-water"></div>
              <p>Calm patch between waves</p>
            </div>
            <div class="indicator">
              <div class="indicator-icon foam-line"></div>
              <p>Foam moving seaward</p>
            </div>
            <div class="indicator">
              <div class="indicator-icon wave-break"></div>
              <p>Gap in breaking waves</p>
            </div>
          </div>
        </div>
        
        <div class="family-plan">
          <h3>Family Beach Safety Plan:</h3>
          <ol>
            <li>Check conditions before visiting</li>
            <li>Establish clear supervision roles</li>
            <li>Create a meeting point</li>
            <li>Practice rip current escape techniques</li>
            <li>Position near lifeguards when possible</li>
          </ol>
        </div>
        
        <div class="final-message">
          <p>Remember: Rip current strength varies with tides. Always stay alert and adjust plans as conditions change.</p>
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
        quizPhase: 'thinking',
        currentQuestionIndex: 0,
        selectedAnswer: null,
        showResults: false,
        timeRemaining: 25,
        timerInterval: null,
        lastAnswerCorrect: false,
        isInIframe: false,
        windowHeight: window.innerHeight,
        windowWidth: window.innerWidth,
        quizCompleted: false,
        correctAnswers: 0,
        totalQuestions: 5,
        keyTakeaways: [
          "Rip currents form at breaks in sandbars and near structures",
          "Multiple rips can form during changing tides or after storms",
          "Strongest rips occur during outgoing tides",
          "Calm water between waves often signals a rip current",
          "Weather changes can intensify existing rips",
          "Float first, then swim parallel to shore if caught"
        ],
        steps: [
          {
            title: "Beach Hazard Assessment",
            description: "Multiple warning flags indicate various hazards including rip currents. Different sections of the beach have different conditions.",
            tip: "Look beyond flags for natural warning signs like unusual water patterns and changes in water color."
          },
          {
            title: "Multiple Rip Currents",
            description: "As the tide changes, primary and secondary rip currents form at different points along the beach.",
            tip: "Rips often form at breaks in sandbars, near jetties, and adjacent to headlands. They intensify during falling tides."
          },
          {
            title: "Changing Conditions",
            description: "Weather deteriorates with increasing wind. Multiple children are caught in different rip currents simultaneously.",
            tip: "Offshore winds can make water appear calm while masking strong underwater currents."
          },
          {
            title: "Multi-Person Rescue",
            description: "With multiple people in distress, proper prioritization becomes critical. The lifeguard needs assistance from capable adults.",
            tip: "Prioritize victims showing panic or fatigue. Remember: reach, throw, row, go. Only enter water as last resort with flotation."
          },
          {
            title: "Safety Planning",
            description: "The family learns about comprehensive beach safety planning that accounts for changing conditions and multiple hazards.",
            tip: "Monitor conditions continuously, establish clear communication, designate meeting points, and conduct regular headcounts."
          }
        ],
        questions: [
          {
            // Question 1: Flag system
            scenario: "You see a red flag at the main lifeguard tower and a yellow flag with black diamond 200 yards away. The tide is falling and offshore wind is picking up. What's happening?",
            options: [
              "Red area closed, yellow area safe for experienced swimmers",
              "Entire beach unsafe, yellow area has marine hazards",
              "Yellow area is a designated surfing zone",
              "Both sections have hazards, but conditions vary along the beach"
            ],
            correctAnswer: 3,
            explanation: "Different flags indicate varying conditions along the beach, but both signal hazards. Red flags indicate high danger, while yellow with black diamond shows medium hazard with specific dangers. Falling tide and offshore wind increase rip current risk by exposing sandbar breaks and masking surface indicators."
          },
          {
            // Question 2: Rip current identification
            scenario: "You notice a gap in breaking waves, different colored water, and foam moving seaward. Your children are playing 50 yards away. What's your best action?",
            options: [
              "Relocate to a different beach entirely",
              "Let them continue playing in shallow water with vigilant watch",
              "Call them back, explain the rip indicators, and move to a safer section",
              "Alert lifeguard but let children continue playing"
            ],
            correctAnswer: 2,
            explanation: "You've spotted multiple classic rip current signs. While your children aren't in immediate danger in the shallows, their proximity to these hazards warrants relocation. Use this as a teaching moment to help them identify these dangers themselves."
          },
          {
            // Question 3: Multiple victims
            scenario: "Two children are caught in a rip current 60 yards offshore. One is struggling and calling for help, the other is floating on their back. A lifeguard is helping someone else 100 yards away. What's your best response?",
            options: [
              "Swim out to rescue the struggling child first",
              "Enter water with flotation to help the struggling child while someone alerts the lifeguard",
              "Organize nearby adults to form a human chain while someone alerts the lifeguard",
              "Direct someone to alert the lifeguard while shouting instructions to both children"
            ],
            correctAnswer: 3,
            explanation: "The most effective response prioritizes alerting professional help while providing guidance from shore. The floating child is using the correct survival technique. Entering water creates additional risk, and human chains are dangerous in rip currents. Shouting instructions to 'float, don't fight' helps the struggling child conserve energy until help arrives."
          },
          {
            // Question 4: Complex rescue
            scenario: "Your teenager and their friend are caught in a rip current as weather deteriorates. Your teen is swimming parallel to shore, but their friend is panicking and swimming directly back. You have a boogie board and there's a rescue ring nearby. What's your best action?",
            options: [
              "Throw the boogie board to your teenager, then get the rescue ring for their friend",
              "Use the boogie board yourself to paddle out to the panicking friend",
              "Direct another adult to get the rescue ring while you enter with the boogie board along the rip's edge",
              "Signal your teenager to stay with their friend and share the boogie board"
            ],
            correctAnswer: 2,
            explanation: "Direct another adult to get the rescue ring while you use the boogie board for flotation to approach along the edge of the rip current. This provides immediate assistance while maintaining your safety. The panicking swimmer needs help first, while your teenager is using proper technique and can likely maintain themselves longer."
          },
          {
            // Question 5: Safety planning
            scenario: "After a close call, you want to create a beach safety plan for your family with children ages 5, 10, and 15. Which approach is most effective?",
            options: [
              "Assign each child a buddy and only allow swimming in designated areas",
              "Create a tiered system where older children have more freedom after passing swim tests",
              "Use colored swimwear, hand signals, meeting points, and age-appropriate boundaries that adjust with conditions",
              "Only visit lifeguarded beaches and require flotation for all children"
            ],
            correctAnswer: 2,
            explanation: "The most effective approach creates multiple safety layers. Distinctive colored swimwear increases visibility; hand signals enable communication across distances; designated meeting points prevent separation; and age-appropriate, condition-based boundaries acknowledge different capabilities while adapting to changing hazards."
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
        this.timeRemaining = this.isSmallScreen ? 20 : 25;
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
            this.selectedAnswer = -1;
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
        if (this.currentStep < this.steps.length - 1) {
          this.currentStep++;
        }
        
        this.quizActive = false;
        
        setTimeout(() => {
          if (this.currentQuestionIndex < this.questions.length - 1) {
            this.currentQuestionIndex++;
            this.startQuiz();
          } else {
            this.completeQuiz();
          }
        }, 2000);
      },
      completeQuiz() {
        this.quizCompleted = true;
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
        if (event.data && event.data.type === 'close-quiz') {
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
          if (this.isInIframe) {
            this.startQuiz();
            window.parent.postMessage({ 
              type: 'quiz-loaded', 
              status: 'success' 
            }, '*');
          }
        } catch (e) {
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
      this.checkIfInIframe();
      window.addEventListener('message', this.handleMessage);
      window.addEventListener('resize', this.handleResize);
      
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
    color: #0277BD;
    margin: 0 0 15px 0;
    font-size: 1.8rem;
  }
  
  /* Beach scene styling */
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
  
  /* Beach environment */
  .sky {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 40%;
    background: linear-gradient(to bottom, #81D4FA, #B3E5FC);
    z-index: 1;
    transition: all 1.5s ease;
  }
  
  .sky.stormy {
    background: linear-gradient(to bottom, #546E7A, #78909C);
  }
  
  .beach {
    position: absolute;
    top: 40%;
    left: 0;
    width: 100%;
    height: 20%;
    background-color: #FFECB3;
    z-index: 2;
  }
  
  .ocean {
    position: absolute;
    top: 60%;
    left: 0;
    width: 100%;
    height: 40%;
    overflow: hidden;
    z-index: 3;
    transition: all 1.5s ease;
  }
  
  .ocean.rough {
    background-color: rgba(0, 77, 128, 0.2);
  }
  
  .water {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to bottom, #039BE5, #0277BD);
    position: relative;
  }
  
  /* Wave animations */
  .wave {
    position: absolute;
    width: 200%;
    height: 10px;
    background: rgba(255, 255, 255, 0.3);
    border-radius: 50%;
    left: -50%;
    animation: waveMotion 8s infinite linear;
    transition: all 1s ease;
  }
  
  @keyframes waveMotion {
    0% {
      transform: translateX(-30%) scaleX(0.8);
    }
    50% {
      transform: translateX(0%) scaleX(1);
    }
    100% {
      transform: translateX(30%) scaleX(0.8);
    }
  }
  
  /* Rip current visualization */
  .rip-current {
    position: absolute;
    width: 60px;
    height: 100%;
    opacity: 0;
    transition: opacity 1s ease;
  }
  
  .rip-current.main-rip {
    left: 50%;
    transform: translateX(-50%);
  }
  
  .rip-current.secondary-rip {
    left: 25%;
    transform: translateX(-50%);
    width: 40px;
  }
  
  .rip-current.active {
    opacity: 1;
  }
  
  .rip-line {
    position: absolute;
    width: 100%;
    height: 3px;
    background-color: rgba(0, 77, 128, 0.4);
    animation: ripFlow 4s infinite linear;
  }
  
  @keyframes ripFlow {
    0% {
      transform: translateY(0);
    }
    100% {
      transform: translateY(-100%);
    }
  }
  
  /* Foam pattern */
  .foam-pattern {
    position: absolute;
    width: 100%;
    height: 100%;
    opacity: 0;
    transition: opacity 1s ease;
    pointer-events: none;
  }
  
  .foam-pattern.active {
    opacity: 1;
  }
  
  .foam-pattern:before {
    content: '';
    position: absolute;
    width: 60px;
    height: 5px;
    background-color: rgba(255, 255, 255, 0.5);
    top: 20%;
    left: 50%;
    transform: translateX(-50%);
    animation: foamMove 6s infinite linear;
  }
  
  .foam-pattern:after {
    content: '';
    position: absolute;
    width: 40px;
    height: 5px;
    background-color: rgba(255, 255, 255, 0.5);
    top: 40%;
    left: 25%;
    transform: translateX(-50%);
    animation: foamMove 5s infinite linear;
  }
  
  @keyframes foamMove {
    0% {
      transform: translateY(0) translateX(-50%);
    }
    100% {
      transform: translateY(-100%) translateX(-50%);
    }
  }
  
  /* Sandbar visualization */
  .sandbar {
    position: absolute;
    width: 80%;
    height: 10px;
    background-color: rgba(255, 236, 179, 0.3);
    top: 70%;
    left: 10%;
    border-radius: 50%;
    z-index: 4;
    opacity: 0;
    transition: opacity 1s ease;
  }
  
  .sandbar.visible {
    opacity: 1;
  }
  
  .sandbar:before, .sandbar:after {
    content: '';
    position: absolute;
    width: 20px;
    height: 100%;
    background-color: rgba(255, 236, 179, 0);
    top: 0;
  }
  
  .sandbar:before {
    left: 40%;
  }
  
  .sandbar:after {
    right: 20%;
  }
  
  /* Beach elements */
  .umbrella {
    position: absolute;
    z-index: 4;
    width: 40px;
    height: 40px;
  }
  
  .umbrella:before {
    content: '';
    position: absolute;
    width: 40px;
    height: 20px;
    background-color: #EF5350;
    border-radius: 50% 50% 0 0;
    top: 0;
  }
  
  .umbrella:after {
    content: '';
    position: absolute;
    width: 4px;
    height: 30px;
    background-color: #8D6E63;
    top: 20px;
    left: 18px;
  }
  
  .left-umbrella {
    top: 35%;
    left: 15%;
  }
  
  .right-umbrella {
    top: 35%;
    right: 15%;
  }
  
  .beach-ball {
    position: absolute;
    width: 20px;
    height: 20px;
    background: radial-gradient(circle, #FFEB3B 0%, #FFC107 100%);
    border-radius: 50%;
    top: 45%;
    left: 70%;
    z-index: 4;
    transition: all 2s ease;
  }
  
  .beach-ball.floating {
    top: 65%;
    left: 55%;
    animation: ballFloat 3s infinite;
  }
  
  .beach-ball.drifting {
    top: 65%;
    left: 25%;
    animation: ballDrift 4s infinite;
  }
  
  @keyframes ballFloat {
    0%, 100% {
      transform: translateY(0);
    }
    50% {
      transform: translateY(-10px);
    }
  }
  
  @keyframes ballDrift {
    0% {
      transform: translateY(0) translateX(0);
    }
    50% {
      transform: translateY(-5px) translateX(-20px);
    }
    100% {
      transform: translateY(0) translateX(-40px);
    }
  }
  
  /* Safety flags */
  .safety-flag {
    position: absolute;
    top: 30%;
    z-index: 5;
    transition: transform 0.3s ease;
  }
  
  .red-flag {
    right: 20%;
  }
  
  .yellow-flag {
    right: 30%;
    opacity: 0;
    transition: opacity 1s ease;
  }
  
  .yellow-flag.visible {
    opacity: 1;
  }
  
  .flag-pole {
    position: absolute;
    width: 4px;
    height: 40px;
    background-color: #8D6E63;
    left: 0;
  }
  
  .flag {
    position: absolute;
    width: 20px;
    height: 15px;
    top: 5px;
    left: 4px;
  }
  
  .flag.red {
    background-color: #F44336;
    animation: flagWave 2s infinite;
  }
  
  .flag.yellow {
    background-color: #FFEB3B;
    animation: flagWave 2.5s infinite;
  }
  
  .flag.yellow:after {
    content: '';
    position: absolute;
    width: 10px;
    height: 10px;
    background-color: #000;
    top: 2.5px;
    left: 5px;
    transform: rotate(45deg);
  }
  
  @keyframes flagWave {
    0%, 100% {
      transform: skewX(0deg);
    }
    50% {
      transform: skewX(-10deg);
    }
  }
  
  .flag-highlighted {
    transform: scale(1.2);
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
  
  /* Lifeguard tower */
  .lifeguard-tower {
    position: absolute;
    top: 30%;
    left: 10%;
    z-index: 4;
    transition: all 0.5s ease;
  }
  
  .tower-base {
    position: absolute;
    width: 30px;
    height: 20px;
    background-color: #FFECB3;
    border: 2px solid #8D6E63;
  }
  
  .tower-top {
    position: absolute;
    width: 40px;
    height: 15px;
    background-color: #F44336;
    top: -15px;
    left: -5px;
    border-radius: 5px 5px 0 0;
  }
  
  .lifeguard {
    position: absolute;
    width: 10px;
    height: 15px;
    background-color: #FFCC80;
    top: -10px;
    left: 10px;
    animation: lifeguardWatch 3s infinite;
  }
  
  @keyframes lifeguardWatch {
    0%, 100% {
      transform: translateX(-2px);
    }
    50% {
      transform: translateX(2px);
    }
  }
  
  .tower-active {
    transform: scale(1.1);
  }
  
  /* Beachgoers */
  .beachgoers {
    position: absolute;
    top: 40%;
    left: 0;
    width: 100%;
    height: 20%;
    z-index: 4;
    opacity: 0;
    animation: fadeIn 1s forwards;
  }
  
  @keyframes fadeIn {
    0% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
  }
  
  .beachgoer {
    position: absolute;
    width: 8px;
    height: 15px;
    background-color: #FFCC80;
    border-radius: 3px;
  }
  
  .beachgoer:before {
    content: '';
    position: absolute;
    width: 6px;
    height: 6px;
    background-color: #FFCC80;
    border-radius: 50%;
    top: -6px;
    left: 1px;
  }
  
  .beachgoer.one {
    top: 10%;
    left: 80%;
  }
  
  .beachgoer.two {
    top: 30%;
    left: 60%;
  }
  
  .beachgoer.three {
    top: 50%;
    left: 40%;
  }
  
  /* Parent character */
  .parent {
    position: absolute;
    height: 80px;
    width: 40px;
    z-index: 10;
    transition: all 1.5s ease;
  }
  
  .parent .head {
    position: absolute;
    top: 0;
    left: 10px;
    width: 20px;
    height: 20px;
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
    top: 6px;
    width: 100%;
    height: 4px;
  }
  
  .parent .eyes:before, .parent .eyes:after {
    content: '';
    position: absolute;
    width: 4px;
    height: 4px;
    background-color: #5D4037;
    border-radius: 50%;
  }
  
  .parent .eyes:before {
    left: 4px;
  }
  
  .parent .eyes:after {
    right: 4px;
  }
  
  .parent .eyes.scanning {
    animation: scanBeach 3s infinite;
  }
  
  @keyframes scanBeach {
    0%, 100% {
      transform: translateX(-2px);
    }
    50% {
      transform: translateX(2px);
    }
  }
  
  .parent .eyes.alarmed:before, .parent .eyes.alarmed:after {
    height: 5px;
    width: 5px;
  }
  
  .parent .mouth {
    position: absolute;
    bottom: 4px;
    left: 6px;
    width: 8px;
    height: 3px;
    background-color: #5D4037;
    border-radius: 1px;
  }
  
  .parent .mouth.concerned {
    width: 8px;
    height: 4px;
    border-radius: 4px 4px 0 0;
    transform: translateY(1px);
  }
  
  .parent .mouth.shouting {
    height: 5px;
    width: 5px;
    border-radius: 50%;
    animation: shout 0.7s infinite;
  }
  
  @keyframes shout {
    0%, 100% {
      height: 3px;
      border-radius: 1px;
    }
    50% {
      height: 5px;
      border-radius: 50%;
    }
  }
  
  .parent .mouth.strained {
    width: 10px;
    height: 3px;
  }
  
  .parent .mouth.talking {
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
  
  .parent .body {
    position: absolute;
    top: 20px;
    left: 13px;
    width: 14px;
    height: 30px;
    background-color: #26A69A;
    border-radius: 4px;
  }
  
  .parent .arm {
    position: absolute;
    width: 4px;
    height: 20px;
    background-color: #FFCC80;
    transition: transform 0.5s ease;
  }
  
  .parent .arm.left {
    top: 24px;
    left: 8px;
    transform-origin: top center;
  }
  
  .parent .arm.right {
    top: 24px;
    right: 8px;
    transform-origin: top center;
  }
  
  .parent.alerting .arm.right {
    transform: rotate(-45deg);
    animation: waveArm 1s infinite;
  }
  
  @keyframes waveArm {
    0%, 100% {
      transform: rotate(-45deg);
    }
    50% {
      transform: rotate(-60deg);
    }
  }
  
  .parent.rescuing .arm.right {
    transform: rotate(-90deg);
  }
  
  .parent .leg {
    position: absolute;
    width: 4px;
    height: 24px;
    background-color: #FFCC80;
  }
  
  .parent .leg.left {
    top: 50px;
    left: 12px;
  }
  
  .parent .leg.right {
    top: 50px;
    right: 12px;
  }
  
  .parent.onshore {
    top: 40%;
    left: 30%;
  }
  
  .parent.watching {
    top: 45%;
    left: 35%;
  }
  
  .parent.alerting {
    top: 45%;
    left: 40%;
    animation: parentAlert 0.5s infinite;
  }
  
  @keyframes parentAlert {
    0%, 100% {
      transform: translateY(0);
    }
    50% {
      transform: translateY(-3px);
    }
  }
  
  .parent.rescuing {
    top: 50%;
    left: 45%;
  }
  
  .parent.teaching {
    top: 45%;
    left: 25%;
  }
  
  /* Child character */
  .child {
    position: absolute;
    height: 60px; /* Smaller than parent */
    width: 30px;
    z-index: 10;
    transition: all 1.5s ease;
  }
  
  .child .head {
    position: absolute;
    top: 0;
    left: 7.5px;
    width: 15px;
    height: 15px;
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
    top: 4px;
    width: 100%;
    height: 3px;
  }
  
  .child .eyes:before, .child .eyes:after {
    content: '';
    position: absolute;
    width: 3px;
    height: 3px;
    background-color: #5D4037;
    border-radius: 50%;
  }
  
  .child .eyes:before {
    left: 3px;
  }
  
  .child .eyes:after {
    right: 3px;
  }
  
  .child .eyes.happy:before, .child .eyes.happy:after {
    height: 2px;
    border-radius: 2px 2px 0 0;
    transform: translateY(-1px);
  }
  
  .child .eyes.scared:before, .child .eyes.scared:after {
    height: 4px;
    width: 4px;
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
  
  .child .mouth {
    position: absolute;
    bottom: 3px;
    left: 4.5px;
    width: 6px;
    height: 2px;
    background-color: #5D4037;
    border-radius: 1px;
  }
  
  .child .mouth.smiling {
    height: 3px;
    width: 6px;
    border-radius: 0 0 3px 3px;
    transform: translateY(-1px);
  }
  
  .child .mouth.gasping {
    height: 4px;
    width: 4px;
    border-radius: 50%;
    animation: gasp 0.7s infinite;
  }
  
  @keyframes gasp {
    0%, 100% {
      height: 2px;
      border-radius: 1px;
    }
    50% {
      height: 4px;
      border-radius: 50%;
    }
  }
  
  .child .body {
    position: absolute;
    top: 15px;
    left: 10px;
    width: 10px;
    height: 22px;
    background-color: #FFA726;
    border-radius: 3px;
  }
  
  .child .arm {
    position: absolute;
    width: 3px;
    height: 15px;
    background-color: #FFCC80;
    transition: transform 0.5s ease;
  }
  
  .child .arm.left {
    top: 18px;
    left: 6px;
    transform-origin: top center;
  }
  
  .child .arm.right {
    top: 18px;
    right: 6px;
    transform-origin: top center;
  }
  
  .child.drifting .arm.left, .child.drifting .arm.right {
    animation: armFlail 0.5s infinite alternate;
  }
  
  @keyframes armFlail {
    0% {
      transform: rotate(-30deg);
    }
    100% {
      transform: rotate(30deg);
    }
  }
  
  .child .leg {
    position: absolute;
    width: 3px;
    height: 18px;
    background-color: #FFCC80;
  }
  
  .child .leg.left {
    top: 37px;
    left: 9px;
  }
  
  .child .leg.right {
    top: 37px;
    right: 9px;
  }
  
  .child.drifting .leg.left, .child.drifting .leg.right {
    animation: legKick 0.7s infinite alternate;
  }
  
  @keyframes legKick {
    0% {
      transform: rotate(-15deg);
    }
    100% {
      transform: rotate(15deg);
    }
  }
  
  .child.playing {
    top: 45%;
    left: 60%;
    animation: childPlay 2s infinite;
  }
  
  @keyframes childPlay {
    0%, 100% {
      transform: translateY(0);
    }
    50% {
      transform: translateY(-5px);
    }
  }
  
  .child.swimming {
    top: 65%;
    left: 50%;
    animation: swimming 3s infinite;
  }
  
  @keyframes swimming {
    0%, 100% {
      transform: translateY(0) rotate(0deg);
    }
    25% {
      transform: translateY(-3px) rotate(-5deg);
    }
    75% {
      transform: translateY(-3px) rotate(5deg);
    }
  }
  
  .child.drifting {
    top: 65%;
    left: 55%;
    animation: drifting 2s infinite;
  }
  
  @keyframes drifting {
    0%, 100% {
      transform: translateY(0) rotate(0deg);
    }
    25% {
      transform: translateY(-5px) rotate(-10deg);
    }
    75% {
      transform: translateY(-5px) rotate(10deg);
    }
  }
  
  .child.floating {
    top: 60%;
    left: 45%;
    animation: floating 3s infinite;
  }
  
  @keyframes floating {
    0%, 100% {
      transform: translateY(0);
    }
    50% {
      transform: translateY(-3px);
    }
  }
  
  .child.learning {
    top: 45%;
    left: 20%;
  }
  
  /* Second child */
  .second-child {
    position: absolute;
    height: 50px; /* Smaller than first child */
    width: 25px;
    z-index: 10;
    transition: all 1.5s ease;
    opacity: 0;
    animation: fadeIn 1s forwards;
  }
  
  .second-child .head {
    position: absolute;
    top: 0;
    left: 6px;
    width: 13px;
    height: 13px;
    background-color: #FFCC80;
    border-radius: 50%;
  }
  
  .second-child .body {
    position: absolute;
    top: 13px;
    left: 8.5px;
    width: 8px;
    height: 18px;
    background-color: #FF7043;
    border-radius: 3px;
  }
  
  .second-child .arm {
    position: absolute;
    width: 2.5px;
    height: 12px;
    background-color: #FFCC80;
  }
  
  .second-child .arm.left {
    top: 15px;
    left: 5px;
  }
  
  .second-child .arm.right {
    top: 15px;
    right: 5px;
  }
  
  .second-child .leg {
    position: absolute;
    width: 2.5px;
    height: 15px;
    background-color: #FFCC80;
  }
  
  .second-child .leg.left {
    top: 31px;
    left: 7.5px;
  }
  
  .second-child .leg.right {
    top: 31px;
    right: 7.5px;
  }
  
  .second-child.drifting {
    top: 65%;
    left: 25%;
    animation: childDrifting 2.5s infinite;
  }
  
  @keyframes childDrifting {
    0%, 100% {
      transform: translateY(0) rotate(0deg);
    }
    25% {
      transform: translateY(-3px) rotate(-5deg);
    }
    75% {
      transform: translateY(-3px) rotate(5deg);
    }
  }
  
  .second-child.struggling {
    top: 65%;
    left: 30%;
    animation: struggling 0.7s infinite;
  }
  
  @keyframes struggling {
    0%, 100% {
      transform: translateY(0) rotate(-5deg);
    }
    50% {
      transform: translateY(-2px) rotate(5deg);
    }
  }
  
  .second-child.rescued {
    top: 45%;
    left: 15%;
  }
  
  /* Rescue equipment */
  .rescue-tube {
    position: absolute;
    width: 30px;
    height: 10px;
    background-color: #F44336;
    border-radius: 5px;
    top: 45%;
    left: 35%;
    z-index: 9;
    opacity: 0;
    animation: fadeIn 1s forwards;
  }
  
  .rescue-tube.in-use {
    top: 55%;
    left: 40%;
    animation: tubeInUse 2s infinite;
  }
  
  @keyframes tubeInUse {
    0%, 100% {
      transform: translateY(0) rotate(0deg);
    }
    50% {
      transform: translateY(-3px) rotate(5deg);
    }
  }
  
  /* Splash effect */
  .splash {
    position: absolute;
    top: -10px;
    left: -10px;
    width: 50px;
    height: 15px;
    z-index: 9;
  }
  
  .splash:before, .splash:after {
    content: '';
    position: absolute;
    background-color: rgba(255, 255, 255, 0.7);
    width: 12px;
    height: 15px;
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
  
  /* Weather effects */
  .wind {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 40%;
    z-index: 6;
    pointer-events: none;
    opacity: 0;
    animation: fadeIn 1s forwards;
  }
  
  .wind:before, .wind:after {
    content: '';
    position: absolute;
    height: 2px;
    background-color: rgba(255, 255, 255, 0.3);
    animation: windGust 3s infinite linear;
  }
  
  .wind:before {
    width: 30px;
    top: 30%;
    left: 20%;
  }
  
  .wind:after {
    width: 50px;
    top: 60%;
    left: 60%;
    animation-delay: 1.5s;
  }
  
  @keyframes windGust {
    0% {
      transform: translateX(-100%) scaleX(0.5);
      opacity: 0;
    }
    50% {
      transform: translateX(0%) scaleX(1);
      opacity: 0.5;
    }
    100% {
      transform: translateX(100%) scaleX(0.5);
      opacity: 0;
    }
  }
  
  .rain {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 40%;
    z-index: 7;
    pointer-events: none;
    opacity: 0;
    animation: fadeIn 1s forwards;
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
  
  /* Speech and thought bubbles */
  .speech-bubble, .thought-bubble {
    position: absolute;
    top: -25px;
    left: 0;
    min-width: 40px;
    height: 25px;
    background-color: white;
    border-radius: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    font-size: 0.7rem;
    z-index: 20;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    padding: 0 5px;
    animation: bobUpDown 2s infinite;
  }
  
  .speech-bubble:after {
    content: '';
    position: absolute;
    bottom: -5px;
    left: 10px;
    width: 10px;
    height: 10px;
    background-color: white;
    transform: rotate(45deg);
    z-index: -1;
  }
  
  @keyframes bobUpDown {
    0%, 100% {
      transform: translateY(0);
    }
    50% {
      transform: translateY(-3px);
    }
  }
  
  .parent-bubble {
    left: -10px;
    min-width: 60px;
  }
  
  .child-bubble {
    left: -5px;
    min-width: 30px;
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
    background-color: #E1F5FE;
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
    background-color: #E1F5FE;
  }
  
  .option-button.selected {
    background-color: #B3E5FC;
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
  
  /* Quiz completion summary */
  .quiz-summary {
    background-color: white;
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    width: 100%;
    max-width: 800px;
    margin-bottom: 20px;
    animation: fadeIn 0.5s ease-in;
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
    color: #0277BD;
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
    color: #0277BD;
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
    color: #0277BD;
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
  
  /* Rip current identification section */
  .rip-identification {
    margin-bottom: 25px;
    background-color: #E1F5FE;
    padding: 15px;
    border-radius: 8px;
  }
  
  .rip-identification h3 {
    color: #0277BD;
    margin: 0 0 15px 0;
    font-size: 1.3rem;
  }
  
  .rip-indicators {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 15px;
  }
  
  .indicator {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }
  
  .indicator-icon {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    margin-right: 10px;
    flex-shrink: 0;
  }
  
  .color-diff {
    background: linear-gradient(to right, #81D4FA, #01579B);
  }
  
  .calm-water {
    background-color: #0277BD;
    position: relative;
  }
  
  .calm-water:after {
    content: '';
    position: absolute;
    top: 50%;
    left: 0;
    width: 100%;
    height: 2px;
    background-color: rgba(255, 255, 255, 0.3);
  }
  
  .foam-line {
    background-color: #B3E5FC;
    position: relative;
  }
  
  .foam-line:after {
    content: '';
    position: absolute;
    top: 30%;
    left: 0;
    width: 100%;
    height: 2px;
    background-color: white;
    animation: foamMove 2s infinite linear;
  }
  
  @keyframes foamMove {
    0% {
      transform: translateX(-100%);
    }
    100% {
      transform: translateX(100%);
    }
  }
  
  .wave-break {
    background-color: #0277BD;
    position: relative;
    overflow: hidden;
  }
  
  .wave-break:before, .wave-break:after {
    content: '';
    position: absolute;
    height: 5px;
    background-color: white;
    border-radius: 50%;
    animation: waveBreak 2s infinite;
  }
  
  .wave-break:before {
    width: 20px;
    left: -5px;
    top: 5px;
  }
  
  .wave-break:after {
    width: 20px;
    right: -5px;
    top: 20px;
  }
  
  @keyframes waveBreak {
    0% {
      transform: translateX(-100%);
    }
    100% {
      transform: translateX(100%);
    }
  }
  
  .indicator p {
    margin: 0;
    font-size: 0.9rem;
  }
  
  /* Family plan section */
  .family-plan {
    margin-bottom: 25px;
    background-color: #FFF9C4;
    padding: 15px;
    border-radius: 8px;
    border-left: 5px solid #FFC107;
  }
  
  .family-plan h3 {
    color: #F57F17;
    margin: 0 0 15px 0;
    font-size: 1.3rem;
  }
  
  .family-plan ol {
    margin: 0;
    padding-left: 20px;
  }
  
  .family-plan li {
    margin-bottom: 8px;
    line-height: 1.5;
  }
  
  .final-message {
    background-color: #E1F5FE;
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 20px;
    border-left: 5px solid #0277BD;
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
    background-color: #0277BD;
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 1.1rem;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .restart-button:hover {
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
    
    .summary-header {
      flex-direction: column;
      text-align: center;
    }
    
    .summary-header h2 {
      margin-bottom: 15px;
      font-size: 1.4rem;
    }
    
    .rip-indicators {
      grid-template-columns: 1fr;
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
    
    .step-info, .quiz-container, .quiz-summary {
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
    
    .key-learnings h3, .rip-identification h3, .family-plan h3 {
      font-size: 1.2rem;
    }
    
    .score-number {
      font-size: 2rem;
    }
    
    .score-total {
      font-size: 1.2rem;
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
    
    .step-info, .quiz-container, .quiz-summary {
      padding: 10px;
      margin-bottom: 12px;
    }
    
    .key-learnings li {
      margin-bottom: 5px;
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
  </style>