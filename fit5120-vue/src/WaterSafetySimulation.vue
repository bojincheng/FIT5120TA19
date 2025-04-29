<template>
  <div id="container" ref="container" class="water-safety-container fullscreen-container">
    <canvas id="simulation" ref="canvas"></canvas>
    
    <div id="title" class="title">
      <h2 id="titleText">{{ currentStepTitle }}</h2>
    </div>
    
    <div id="message" class="message">
      <p>{{ messageText }}</p>
      <div class="indicator"></div>
    </div>
    
    <div class="back-button" @click="goBack">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M19 12H5"></path>
        <path d="M12 19l-7-7 7-7"></path>
      </svg>
      <span>Back to Safety Guide</span>
    </div>
    
    <div class="scenario-selector">
      <h3>Scenarios</h3>
      <button 
        id="scenarioIncorrect" 
        :class="['scenario-button', { active: currentScenario === 'incorrect' }]" 
        @click="changeScenario('incorrect')"
      >
        Incorrect Response
      </button>
      <button 
        id="scenarioCorrect" 
        :class="['scenario-button', { active: currentScenario === 'correct' }]" 
        @click="changeScenario('correct')"
      >
        Correct Response
      </button>
    </div>
    
    <div class="legend">
      <div class="legend-item">
        <div class="legend-color safe"></div>
        <div class="legend-text">Safe Swimming Area</div>
      </div>
      <div class="legend-item">
        <div class="legend-color danger"></div>
        <div class="legend-text">Dangerous Area</div>
      </div>
    </div>
    
    <div class="control-panel">
      <button id="resetBtn" class="button" title="Reset" @click="resetSimulation">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M23 4v6h-6"></path>
          <path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"></path>
        </svg>
      </button>
      
      <button id="nextStepBtn" class="button next-step" title="Next Step" @click="nextStep" :disabled="isTransitioning">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="9 18 15 12 9 6"></polyline>
        </svg>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WaterSafetySimulation',
  data() {
    return {
      // State variables
      animationTime: 0,
      animationFrame: null,
      currentScenario: 'incorrect', // Start with incorrect scenario
      ctx: null,
      
      // Step-based animation variables
      currentStep: 0,
      maxSteps: 5,
      
      // Character positions with smooth transitions
      childPosition: { x: 0.5, y: 0.35 }, // Start in water
      parentPosition: { x: 0.3, y: 0.22 }, // Start on beach
      lifeguardPosition: { x: 0.8, y: 0.22 }, // Start at lifeguard tower
      
      // Target positions for smooth transitions
      targetChildPosition: { x: 0.5, y: 0.35 },
      targetParentPosition: { x: 0.3, y: 0.22 },
      targetLifeguardPosition: { x: 0.8, y: 0.22 },
      
      // Animation state
      childInDistress: false,
      parentCalling: false,
      lifeguardRescuing: false,
      parentEnteringWater: false, // For incorrect scenario
      rescueComplete: false,
      
      // Transition animation variables
      isTransitioning: false,
      transitionProgress: 0,
      transitionDuration: 1000, // 1 second transition
      transitionStartTime: 0,
      
      // Message text
      messageText: "Learn the proper response when a child is in trouble in the water",
      
      // Step titles for each scenario and step
      correctStepTitles: [
        "Water Safety Protocol - Initial State",
        "Step 1: Identify Child in Distress",
        "Step 2: Stay on Shore, Call for Help",
        "Step 3: Lifeguard Responds",
        "Step 4: Rescue in Progress",
        "Step 5: Rescue Complete - Everyone Safe"
      ],
      incorrectStepTitles: [
        "Water Safety Protocol - Initial State",
        "Step 1: Identify Child in Distress",
        "Step 2: INCORRECT - Parent Enters Water",
        "Step 3: Both Need Rescue Now",
        "Step 4: Lifeguard Must Rescue Two People",
        "Step 5: Rescue Complete - Added Risk"
      ],
      
      // Step-specific messages
      correctMessages: [
        "Child swimming in the water while parent watches from shore",
        "Child begins to struggle in the water",
        "Parent stays on shore and calls for help",
        "Lifeguard responds to the call for help",
        "Lifeguard reaches child and begins rescue",
        "Rescue successful - everyone safe on shore"
      ],
      incorrectMessages: [
        "Child swimming in the water while parent watches from shore",
        "Child begins to struggle in the water",
        "INCORRECT: Parent enters water to attempt rescue",
        "INCORRECT: Now both parent and child need rescue",
        "INCORRECT: Lifeguard now has to rescue two people",
        "Entering water created additional risk"
      ],

      colors: {
        // Sky colors
        skyTop: "#87CEEB",
        skyBottom: "#ADD8E6",

        // Water colors
        shallowWater: "#64B5F6",
        midWater: "#1976D2",
        deepWater: "#0D47A1",

        // Beach colors
        beach: "#F5DEB3",
        beachDark: "#E6C99F",

        // Character colors
        skin: "#FFD0A9",
        hair: "#8B4513",
        swimsuit: "#FF5252",
        lifeguardRed: "#FF0000",

        // Flag colors
        flagRed: "#FF0000",
        flagYellow: "#FFFF00"
      }
    };
  },
  computed: {
    // Get the current step title based on scenario and step
    currentStepTitle() {
      if (this.currentScenario === 'correct') {
        return this.correctStepTitles[this.currentStep];
      } else {
        return this.incorrectStepTitles[this.currentStep];
      }
    }
  },
  mounted() {
    // Initialize canvas
    this.ctx = this.$refs.canvas.getContext('2d');
    
    // Set up event listeners - use passive: true to improve scrolling performance
    window.addEventListener('resize', this.resizeCanvas, { passive: true });
    
    // Initialize
    this.resizeCanvas();
    
    // Start animation loop for continuous rendering
    this.startAnimationLoop();
    
    // Update the scene for the initial step
    this.updateSceneForStep();
    
    // Prevent body scrolling when simulation is shown
    document.body.style.overflow = 'hidden';
  },
  beforeUnmount() {
    // Clean up event listeners
    window.removeEventListener('resize', this.resizeCanvas);
    
    // Cancel animation frame if running
    if (this.animationFrame) {
      cancelAnimationFrame(this.animationFrame);
      this.animationFrame = null;
    }
    
    // Restore body scrolling
    document.body.style.overflow = '';
  },
  methods: {
    // Navigate back to previous page
    goBack() {
      this.$router.back();
    },
    
    // Resize canvas to fill container
    resizeCanvas() {
      const canvas = this.$refs.canvas;
      const container = this.$refs.container;
      
      if (!canvas || !container) return;
      
      canvas.width = container.clientWidth;
      canvas.height = container.clientHeight;
      
      // Redraw
      this.drawSimulation();
    },
    
    // Reset simulation
    resetSimulation() {
      this.animationTime = 0;
      this.messageText = "Learn the proper response when a child is in trouble in the water";
      
      // Reset animation state
      this.childInDistress = false;
      this.parentCalling = false;
      this.lifeguardRescuing = false;
      this.parentEnteringWater = false;
      this.rescueComplete = false;
      this.currentStep = 0;
      
      // Reset character positions
      this.childPosition = { x: 0.5, y: 0.35 };
      this.parentPosition = { x: 0.3, y: 0.22 };
      this.lifeguardPosition = { x: 0.8, y: 0.22 };
      
      this.targetChildPosition = { ...this.childPosition };
      this.targetParentPosition = { ...this.parentPosition };
      this.targetLifeguardPosition = { ...this.lifeguardPosition };
      
      // Update the scene for the initial step
      this.updateSceneForStep();
      
      // Update message text
      if (this.currentScenario === 'correct') {
        this.messageText = this.correctMessages[0];
      } else {
        this.messageText = this.incorrectMessages[0];
      }
    },
    
    // Move to next step
    nextStep(event) {
      // Prevent event from propagating to parent elements
      if (event) {
        event.preventDefault();
        event.stopPropagation();
      }
      
      if (this.isTransitioning) return; // Don't allow clicking during transition
      
      if (this.currentStep < this.maxSteps) {
        this.currentStep++;
        this.updateSceneForStep();
      } else {
        // Loop back to beginning when reaching the end
        this.resetSimulation();
      }
    },
    
    // Update scene based on current step
    updateSceneForStep() {
      // Update message text
      if (this.currentScenario === 'correct') {
        this.messageText = this.correctMessages[this.currentStep];
      } else {
        this.messageText = this.incorrectMessages[this.currentStep];
      }
      
      // Update animation state based on step
      switch (this.currentStep) {
        case 0: // Initial state - child swimming
          this.childInDistress = false;
          this.parentCalling = false;
          this.lifeguardRescuing = false;
          this.parentEnteringWater = false;
          this.rescueComplete = false;
          
          // Set target positions
          this.targetChildPosition = { x: 0.5, y: 0.35 };
          this.targetParentPosition = { x: 0.3, y: 0.22 };
          this.targetLifeguardPosition = { x: 0.8, y: 0.22 };
          
          // Start transition
          this.startTransition();
          break;
          
        case 1: // Child starts to struggle
          this.childInDistress = true;
          this.parentCalling = false;
          this.lifeguardRescuing = false;
          this.parentEnteringWater = false;
          
          // Set target positions - child starts struggling
          this.targetChildPosition = { x: 0.5, y: 0.35 };
          
          // Start transition
          this.startTransition();
          break;
          
        case 2: // Parent notices and reacts
          this.childInDistress = true;
          
          if (this.currentScenario === 'correct') {
            // Parent stays on shore
            this.parentCalling = true;
            this.parentEnteringWater = false;
            
            this.targetParentPosition = { x: 0.3, y: 0.22 };
          } else {
            // Parent starts to enter water (incorrect)
            this.parentCalling = false;
            this.parentEnteringWater = true;
            
            const progress = 0.5; // Midway to child
            this.targetParentPosition = {
              x: 0.3 + (0.5 - 0.3) * progress,
              y: 0.22 + (0.35 - 0.22) * progress
            };
          }
          
          // Start transition
          this.startTransition();
          break;
          
        case 3: // Lifeguard responds
          this.childInDistress = true;
          this.lifeguardRescuing = true;
          
          // Lifeguard starts moving
          const progress = 0.5; // Midway to child
          this.targetLifeguardPosition = {
            x: 0.8 - (0.8 - 0.5) * progress,
            y: 0.22 + (0.35 - 0.22) * progress
          };
          
          if (this.currentScenario === 'correct') {
            // Parent stays on shore and calls
            this.parentCalling = true;
            this.parentEnteringWater = false;
          } else {
            // Parent fully in water
            this.parentCalling = false;
            this.parentEnteringWater = true;
            
            this.targetParentPosition = {
              x: 0.5,
              y: 0.35
            };
          }
          
          // Start transition
          this.startTransition();
          break;
          
        case 4: // Rescue in progress
          this.childInDistress = true;
          this.lifeguardRescuing = true;
          
          // Lifeguard reaches child
          this.targetLifeguardPosition = { x: 0.5, y: 0.35 };
          
          if (this.currentScenario === 'correct') {
            // Parent stays on shore and calls
            this.parentCalling = true;
            this.parentEnteringWater = false;
          } else {
            // Both parent and child in trouble (incorrect)
            this.parentCalling = false;
            this.parentEnteringWater = true;
          }
          
          // Start transition
          this.startTransition();
          break;
          
        case 5: // Rescue complete
          this.rescueComplete = true;
          this.childInDistress = false;
          this.parentCalling = false;
          this.lifeguardRescuing = false;
          this.parentEnteringWater = false;
          
          // Everyone safe on shore
          this.targetChildPosition = { x: 0.4, y: 0.22 };
          this.targetParentPosition = { x: 0.3, y: 0.22 };
          this.targetLifeguardPosition = { x: 0.5, y: 0.22 };
          
          // Start transition
          this.startTransition();
          break;
      }
    },
    
    // Easing function for smooth transitions
    easeInOutCubic(t) {
      return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
    },
    
    // Start animation loop for continuous rendering
    startAnimationLoop() {
      const animate = () => {
        this.animationTime += 16; // ~60fps
        
        // Handle transition animation
        if (this.isTransitioning) {
          const now = Date.now();
          const elapsed = now - this.transitionStartTime;
          this.transitionProgress = Math.min(elapsed / this.transitionDuration, 1);
          
          // Apply easing function for smoother motion
          const easedProgress = this.easeInOutCubic(this.transitionProgress);
          
          // Interpolate character positions
          this.childPosition.x = this.childPosition.x + (this.targetChildPosition.x - this.childPosition.x) * easedProgress;
          this.childPosition.y = this.childPosition.y + (this.targetChildPosition.y - this.childPosition.y) * easedProgress;
          
          this.parentPosition.x = this.parentPosition.x + (this.targetParentPosition.x - this.parentPosition.x) * easedProgress;
          this.parentPosition.y = this.parentPosition.y + (this.targetParentPosition.y - this.parentPosition.y) * easedProgress;
          
          this.lifeguardPosition.x = this.lifeguardPosition.x + (this.targetLifeguardPosition.x - this.lifeguardPosition.x) * easedProgress;
          this.lifeguardPosition.y = this.lifeguardPosition.y + (this.targetLifeguardPosition.y - this.lifeguardPosition.y) * easedProgress;
          
          // Check if transition is complete
          if (this.transitionProgress >= 1) {
            this.isTransitioning = false;
            this.childPosition = { ...this.targetChildPosition };
            this.parentPosition = { ...this.targetParentPosition };
            this.lifeguardPosition = { ...this.targetLifeguardPosition };
          }
        }
        
        // Add small continuous movement for characters based on their state
        this.addCharacterMovement();
        
        this.drawSimulation();
        this.animationFrame = requestAnimationFrame(animate);
      };
      
      this.animationFrame = requestAnimationFrame(animate);
    },
    
    // Start transition animation between steps
    startTransition() {
      this.isTransitioning = true;
      this.transitionProgress = 0;
      this.transitionStartTime = Date.now();
    },
    
    // Add small continuous movement for characters based on their state
    addCharacterMovement() {
      const time = this.animationTime / 1000; // Convert to seconds
      
      // Only add movement if not transitioning
      if (!this.isTransitioning) {
        // Child movement
        if (this.childInDistress) {
          // Struggling motion
          this.childPosition.x += Math.sin(time * 3) * 0.0005;
          this.childPosition.y += Math.sin(time * 4) * 0.0003;
        } else {
          // Normal swimming motion
          this.childPosition.x += Math.sin(time * 0.5) * 0.0002;
          this.childPosition.y += Math.cos(time * 0.5) * 0.0001;
        }
        
        // Parent movement
        if (this.parentCalling) {
          // Calling for help
          this.parentPosition.x += Math.sin(time * 5) * 0.0001;
        } else if (this.parentEnteringWater) {
          // Struggling in water
          this.parentPosition.x += Math.sin(time * 3) * 0.0004;
          this.parentPosition.y += Math.cos(time * 4) * 0.0003;
        }
        
        // Lifeguard movement
        if (this.lifeguardRescuing) {
          // Swimming motion
          this.lifeguardPosition.x += Math.sin(time * 2) * 0.0002;
          this.lifeguardPosition.y += Math.cos(time * 2) * 0.0001;
        }
      }
    },
    
    // Draw the simulation
    drawSimulation() {
      const canvas = this.$refs.canvas;
      if (!canvas) return;
      
      const width = canvas.width;
      const height = canvas.height;
      const ctx = this.ctx;
      
      if (!ctx) return;
      
      // Clear canvas
      ctx.clearRect(0, 0, width, height);
      
      // Set up time variables
      const time = this.animationTime / 1000; // Convert to seconds
      
      // Enhanced color palette
      const colors = this.colors;
      
      // Shoreline position (constant)
      const baseShoreLineValue = height * 0.25;
      const shoreLineValue = baseShoreLineValue;
      
      // Draw sky with enhanced gradient and sun
      const skyGradient = ctx.createLinearGradient(0, 0, 0, height * 0.2);
      skyGradient.addColorStop(0, colors.skyTop);
      skyGradient.addColorStop(1, colors.skyBottom);
      ctx.fillStyle = skyGradient;
      ctx.fillRect(0, 0, width, height * 0.2);
      
      // Draw sun
      const sunX = width * 0.8;
      const sunY = height * 0.1;
      const sunRadius = Math.min(20, width * 0.03);
      
      // Sun glow
      const sunGlow = ctx.createRadialGradient(sunX, sunY, 0, sunX, sunY, sunRadius * 3);
      sunGlow.addColorStop(0, "rgba(255, 255, 200, 0.8)");
      sunGlow.addColorStop(0.2, "rgba(255, 255, 150, 0.4)");
      sunGlow.addColorStop(1, "rgba(255, 255, 100, 0)");
      
      ctx.fillStyle = sunGlow;
      ctx.beginPath();
      ctx.arc(sunX, sunY, sunRadius * 3, 0, Math.PI * 2);
      ctx.fill();
      
      // Sun itself
      ctx.fillStyle = "#FFFFA0";
      ctx.beginPath();
      ctx.arc(sunX, sunY, sunRadius, 0, Math.PI * 2);
      ctx.fill();
      
      // Draw beach with enhanced gradient and texture
      const beachGradient = ctx.createLinearGradient(0, height * 0.2, 0, height * 0.25);
      beachGradient.addColorStop(0, colors.beach);
      beachGradient.addColorStop(1, colors.beachDark);
      ctx.fillStyle = beachGradient;
      ctx.fillRect(0, height * 0.2, width, height * 0.05);
      
      // Add beach texture - using subtle gradient and lines
      for (let i = 0; i < 15; i++) {
        const y = height * 0.2 + (i / 15) * (height * 0.05);
        const lineWidth = 0.5 + Math.random() * 0.5;
        const alpha = 0.05 + Math.random() * 0.05;
        
        ctx.strokeStyle = `rgba(160, 140, 110, ${alpha})`;
        ctx.lineWidth = lineWidth;
        ctx.beginPath();
        ctx.moveTo(0, y + Math.sin(y * 0.1) * 2);
        
        // Create wavy line
        for (let x = 0; x < width; x += 20) {
          const waveHeight = Math.sin(x * 0.01 + i) * 1.5;
          ctx.lineTo(x, y + waveHeight);
        }
        
        ctx.stroke();
      }
      
      // Draw water with enhanced effects
      // Deep water base with more realistic gradient
      const waterGradient = ctx.createLinearGradient(0, shoreLineValue, 0, height);
      waterGradient.addColorStop(0, colors.shallowWater);
      waterGradient.addColorStop(0.3, colors.midWater);
      waterGradient.addColorStop(1, colors.deepWater);
      ctx.fillStyle = waterGradient;
      ctx.fillRect(0, shoreLineValue, width, height - shoreLineValue);
      
      // Draw underwater sand gradient at the shore
      const sandGradient = ctx.createLinearGradient(0, shoreLineValue, 0, shoreLineValue + height * 0.1);
      sandGradient.addColorStop(0, "rgba(245, 222, 179, 0.7)");
      sandGradient.addColorStop(1, "rgba(245, 222, 179, 0)");
      ctx.fillStyle = sandGradient;
      ctx.fillRect(0, shoreLineValue, width, height * 0.1);
      
      // Draw safe swimming area (between flags)
      const flagLeftX = width * 0.4;
      const flagRightX = width * 0.6;
      
      // Safe zone
      ctx.fillStyle = "rgba(76, 175, 80, 0.1)";
      ctx.beginPath();
      ctx.moveTo(flagLeftX, shoreLineValue);
      ctx.lineTo(flagRightX, shoreLineValue);
      ctx.lineTo(flagRightX, height * 0.6);
      ctx.lineTo(flagLeftX, height * 0.6);
      ctx.closePath();
      ctx.fill();
      
      // Border for safe zone
      ctx.strokeStyle = "rgba(76, 175, 80, 0.7)";
      ctx.lineWidth = 2;
      ctx.setLineDash([5, 5]);
      ctx.beginPath();
      ctx.moveTo(flagLeftX, shoreLineValue);
      ctx.lineTo(flagLeftX, height * 0.6);
      ctx.stroke();
      
      ctx.beginPath();
      ctx.moveTo(flagRightX, shoreLineValue);
      ctx.lineTo(flagRightX, height * 0.6);
      ctx.stroke();
      
      ctx.setLineDash([]);
      
      // Draw flags
      this.drawFlag(ctx, flagLeftX, shoreLineValue, colors.flagRed, colors.flagYellow);
      this.drawFlag(ctx, flagRightX, shoreLineValue, colors.flagRed, colors.flagYellow);
      
      // Draw lifeguard tower
      this.drawLifeguardTower(ctx, width * 0.8, height * 0.2, colors);
      
      // Draw breaking waves
      this.drawBreakingWaves(ctx, width, height, shoreLineValue, time);
      
      // Draw characters
      
      // Draw child
      const childX = width * this.childPosition.x;
      const childY = height * this.childPosition.y;
      this.drawChild(ctx, childX, childY, time, colors, this.childInDistress);
      
      // Draw parent
      const parentX = width * this.parentPosition.x;
      const parentY = height * this.parentPosition.y;
      this.drawParent(ctx, parentX, parentY, time, colors, this.parentCalling, this.parentEnteringWater);
      
      // Draw lifeguard
      const lifeguardX = width * this.lifeguardPosition.x;
      const lifeguardY = height * this.lifeguardPosition.y;
      this.drawLifeguard(ctx, lifeguardX, lifeguardY, time, colors, this.lifeguardRescuing);
      
      // Draw speech bubbles if needed
      if (this.parentCalling) {
        this.drawSpeechBubble(ctx, parentX, parentY - 40, "HELP!", 30);
      }
      
      if (this.childInDistress) {
        this.drawSpeechBubble(ctx, childX, childY - 30, "HELP!", 30);
      }
      
      // Draw rescue tube if lifeguard is rescuing
      if (this.lifeguardRescuing) {
        this.drawRescueTube(ctx, lifeguardX, lifeguardY, colors.lifeguardRed);
      }
    },
    
    // Draw breaking waves
    drawBreakingWaves(ctx, width, height, shoreLine, time) {
      // Draw multiple layers of breaking waves
      const waveY = shoreLine + 5;
      
      // Draw waves
      for (let x = 0; x < width; x += 10) {
        const waveHeight = 8 + Math.sin(x * 0.05 + time * 2) * 4;
        const waveFoam = 3 + Math.sin(x * 0.1 + time) * 2;
        
        // Wave
        ctx.fillStyle = "#FFFFFF";
        ctx.beginPath();
        ctx.ellipse(x, waveY, waveFoam, waveHeight, 0, 0, Math.PI * 2);
        ctx.fill();
      }
      
      // Draw foam particles in the water
      for (let i = 0; i < 60; i++) {
        const x = Math.random() * width;
        const yOffset = Math.sin(x * 0.05 + time * 2) * 5;
        const y = shoreLine + 10 + yOffset;
        const size = Math.random() * 3 + 1;
        const alpha = Math.random() * 0.5 + 0.3;
        
        ctx.fillStyle = `rgba(255, 255, 255, ${alpha})`;
        ctx.beginPath();
        ctx.arc(x, y, size, 0, Math.PI * 2);
        ctx.fill();
      }
    },
    
    // Draw a flag
    drawFlag(ctx, x, y, poleColor, flagColor) {
      const poleColorLocal = poleColor;
      const flagColorLocal = flagColor;
      // Flag pole
      ctx.fillStyle = "#8B4513";
      ctx.fillRect(x - 2, y - 60, 4, 60);
      
      // Flag
      ctx.fillStyle = poleColorLocal;
      ctx.beginPath();
      ctx.moveTo(x, y - 60);
      ctx.lineTo(x + 30, y - 50);
      ctx.lineTo(x, y - 40);
      ctx.closePath();
      ctx.fill();
      
      // Yellow stripe
      ctx.fillStyle = flagColorLocal;
      ctx.beginPath();
      ctx.moveTo(x, y - 55);
      ctx.lineTo(x + 20, y - 50);
      ctx.lineTo(x, y - 45);
      ctx.closePath();
      ctx.fill();
    },
    
    // Draw lifeguard tower
    drawLifeguardTower(ctx, x, y, colors) {
      // Tower base
      ctx.fillStyle = "#D2B48C";
      ctx.beginPath();
      ctx.moveTo(x - 30, y);
      ctx.lineTo(x + 30, y);
      ctx.lineTo(x + 20, y - 40);
      ctx.lineTo(x - 20, y - 40);
      ctx.closePath();
      ctx.fill();
      
      // Tower roof
      ctx.fillStyle = "#8B0000";
      ctx.beginPath();
      ctx.moveTo(x - 25, y - 40);
      ctx.lineTo(x + 25, y - 40);
      ctx.lineTo(x, y - 60);
      ctx.closePath();
      ctx.fill();
      
      // Tower window
      ctx.fillStyle = "#87CEEB";
      ctx.fillRect(x - 10, y - 30, 20, 15);
      
      // Tower sign
      ctx.fillStyle = "#FFFFFF";
      ctx.fillRect(x - 15, y - 55, 30, 10);
      
      ctx.fillStyle = "#FF0000";
      ctx.font = "bold 8px Arial";
      ctx.textAlign = "center";
      ctx.fillText("LIFEGUARD", x, y - 47);
      ctx.textAlign = "start";
    },
    
    // Draw child
    drawChild(ctx, x, y, time, colors, inDistress) {
      const inDistressLocal = inDistress;
      const baseSize = 15; // Smaller than adult
      
      // Draw shadow under water
      ctx.fillStyle = "rgba(0, 0, 0, 0.2)";
      ctx.beginPath();
      ctx.ellipse(x, y + baseSize * 0.5, baseSize, baseSize * 0.3, 0, 0, Math.PI * 2);
      ctx.fill();
      
      if (inDistressLocal) {
        // Struggling motion
        const struggleX = Math.sin(time * 8) * baseSize * 0.2;
        const struggleY = Math.cos(time * 10) * baseSize * 0.2;
        
        // Draw arms flailing
        ctx.strokeStyle = colors.skin;
        ctx.lineWidth = baseSize * 0.2;
        
        // Left arm
        ctx.beginPath();
        ctx.moveTo(x - baseSize * 0.4, y - baseSize * 0.3);
        ctx.lineTo(x - baseSize * 0.8 + struggleX, y - baseSize * 0.6 + struggleY);
        ctx.stroke();
        
        // Right arm
        ctx.beginPath();
        ctx.moveTo(x + baseSize * 0.4, y - baseSize * 0.3);
        ctx.lineTo(x + baseSize * 0.8 - struggleX, y - baseSize * 0.6 - struggleY);
        ctx.stroke();
        
        // Draw legs kicking
        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.lineTo(x - baseSize * 0.5 - struggleX, y + baseSize * 0.8);
        ctx.stroke();
        
        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.lineTo(x + baseSize * 0.5 + struggleX, y + baseSize * 0.8);
        ctx.stroke();
      } else {
        // Normal swimming motion
        const swimCycle = time * 4;
        const legKick = Math.sin(swimCycle) * baseSize * 0.3;
        const armStroke = Math.cos(swimCycle) * baseSize * 0.3;
        
        // Draw legs with kicking motion
        ctx.strokeStyle = colors.skin;
        ctx.lineWidth = baseSize * 0.2;
        
        // Left leg
        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.lineTo(x - baseSize * 0.4 - legKick, y + baseSize * 0.6);
        ctx.stroke();
        
        // Right leg
        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.lineTo(x + baseSize * 0.4 + legKick, y + baseSize * 0.6);
        ctx.stroke();
        
        // Draw arms with swimming motion
        // Left arm
        ctx.beginPath();
        ctx.moveTo(x - baseSize * 0.4, y - baseSize * 0.3);
        ctx.lineTo(x - baseSize * 0.6 - armStroke, y - baseSize * 0.1);
        ctx.stroke();
        
        // Right arm
        ctx.beginPath();
        ctx.moveTo(x + baseSize * 0.4, y - baseSize * 0.3);
        ctx.lineTo(x + baseSize * 0.6 + armStroke, y - baseSize * 0.1);
        ctx.stroke();
      }
      
      // Draw swimsuit
      ctx.fillStyle = "#00BCD4"; // Different color from parent
      ctx.beginPath();
      ctx.ellipse(x, y, baseSize * 0.5, baseSize * 0.3, 0, 0, Math.PI * 2);
      ctx.fill();
      
      // Draw torso
      ctx.fillStyle = colors.skin;
      ctx.beginPath();
      ctx.ellipse(x, y - baseSize * 0.3, baseSize * 0.4, baseSize * 0.3, 0, 0, Math.PI * 2);
      ctx.fill();
      
      // Draw head
      ctx.fillStyle = colors.skin;
      ctx.beginPath();
      ctx.arc(x, y - baseSize * 0.7, baseSize * 0.35, 0, Math.PI * 2);
      ctx.fill();
      
      // Draw hair
      ctx.fillStyle = colors.hair;
      ctx.beginPath();
      ctx.arc(x, y - baseSize * 0.85, baseSize * 0.35, Math.PI, 0);
      ctx.fill();
      
      // Draw face
      if (inDistressLocal) {
        // Distressed face
        ctx.fillStyle = "#000";
        ctx.beginPath();
        ctx.ellipse(x - baseSize * 0.1, y - baseSize * 0.7, baseSize * 0.05, baseSize * 0.03, 0, 0, Math.PI * 2);
        ctx.fill();
        
        ctx.beginPath();
        ctx.ellipse(x + baseSize * 0.1, y - baseSize * 0.7, baseSize * 0.05, baseSize * 0.03, 0, 0, Math.PI * 2);
        ctx.fill();
        
        // Mouth - distressed
        ctx.beginPath();
        ctx.arc(x, y - baseSize * 0.55, baseSize * 0.1, 0, Math.PI, false);
        ctx.stroke();
      } else {
        // Normal face
        ctx.fillStyle = "#000";
        ctx.beginPath();
        ctx.ellipse(x - baseSize * 0.1, y - baseSize * 0.7, baseSize * 0.05, baseSize * 0.03, 0, 0, Math.PI * 2);
        ctx.fill();
        
        ctx.beginPath();
        ctx.ellipse(x + baseSize * 0.1, y - baseSize * 0.7, baseSize * 0.05, baseSize * 0.03, 0, 0, Math.PI * 2);
        ctx.fill();
        
        // Mouth - happy
        ctx.beginPath();
        ctx.arc(x, y - baseSize * 0.55, baseSize * 0.1, 0.1, Math.PI - 0.1, false);
        ctx.stroke();
      }
      
      // Water splash effects around child if in distress
      if (inDistressLocal) {
        for (let i = 0; i < 8; i++) {
          const splashX = x + (Math.random() - 0.5) * baseSize * 4;
          const splashY = y + (Math.random() - 0.5) * baseSize * 3;
          const splashSize = Math.random() * baseSize * 0.3 + baseSize * 0.1;
          
          ctx.fillStyle = "rgba(255, 255, 255, 0.7)";
          ctx.beginPath();
          ctx.arc(splashX, splashY, splashSize, 0, Math.PI * 2);
          ctx.fill();
        }
      }
    },
    
    // Draw parent
    drawParent(ctx, x, y, time, colors, calling, inWater) {
      const baseSize = 20;
      
      if (inWater) {
        // Parent in water
        // Draw shadow under water
        ctx.fillStyle = "rgba(0, 0, 0, 0.2)";
        ctx.beginPath();
        ctx.ellipse(x, y + baseSize * 0.5, baseSize, baseSize * 0.3, 0, 0, Math.PI * 2);
        ctx.fill();
        
        // Struggling motion
        const struggleX = Math.sin(time * 6) * baseSize * 0.2;
        const struggleY = Math.cos(time * 8) * baseSize * 0.2;
        
        // Draw arms flailing
        ctx.strokeStyle = colors.skin;
        ctx.lineWidth = baseSize * 0.2;
        
        // Left arm
        ctx.beginPath();
        ctx.moveTo(x - baseSize * 0.4, y - baseSize * 0.3);
        ctx.lineTo(x - baseSize * 0.8 + struggleX, y - baseSize * 0.6 + struggleY);
        ctx.stroke();
        
        // Right arm
        ctx.beginPath();
        ctx.moveTo(x + baseSize * 0.4, y - baseSize * 0.3);
        ctx.lineTo(x + baseSize * 0.8 - struggleX, y - baseSize * 0.6 - struggleY);
        ctx.stroke();
        
        // Draw legs kicking
        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.lineTo(x - baseSize * 0.5 - struggleX, y + baseSize * 0.8);
        ctx.stroke();
        
        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.lineTo(x + baseSize * 0.5 + struggleX, y + baseSize * 0.8);
        ctx.stroke();
        
        // Draw swimsuit
        ctx.fillStyle = colors.swimsuit;
        ctx.beginPath();
        ctx.ellipse(x, y, baseSize * 0.5, baseSize * 0.3, 0, 0, Math.PI * 2);
        ctx.fill();
        
        // Draw torso
        ctx.fillStyle = colors.skin;
        ctx.beginPath();
        ctx.ellipse(x, y - baseSize * 0.3, baseSize * 0.4, baseSize * 0.3, 0, 0, Math.PI * 2);
        ctx.fill();
        
        // Draw head
        ctx.fillStyle = colors.skin;
        ctx.beginPath();
        ctx.arc(x, y - baseSize * 0.7, baseSize * 0.35, 0, Math.PI * 2);
        ctx.fill();
        
        // Draw hair
        ctx.fillStyle = colors.hair;
        ctx.beginPath();
        ctx.arc(x, y - baseSize * 0.85, baseSize * 0.35, Math.PI, 0);
        ctx.fill();
        
        // Draw distressed face
        ctx.fillStyle = "#000";
        ctx.beginPath();
        ctx.ellipse(x - baseSize * 0.1, y - baseSize * 0.7, baseSize * 0.05, baseSize * 0.03, 0, 0, Math.PI * 2);
        ctx.fill();
        
        ctx.beginPath();
        ctx.ellipse(x + baseSize * 0.1, y - baseSize * 0.7, baseSize * 0.05, baseSize * 0.03, 0, 0, Math.PI * 2);
        ctx.fill();
        
        // Mouth - distressed
        ctx.beginPath();
        ctx.arc(x, y - baseSize * 0.55, baseSize * 0.1, 0, Math.PI, false);
        ctx.stroke();
        
        // Water splash effects around parent
        for (let i = 0; i < 8; i++) {
          const splashX = x + (Math.random() - 0.5) * baseSize * 4;
          const splashY = y + (Math.random() - 0.5) * baseSize * 3;
          const splashSize = Math.random() * baseSize * 0.3 + baseSize * 0.1;
          
          ctx.fillStyle = "rgba(255, 255, 255, 0.7)";
          ctx.beginPath();
          ctx.arc(splashX, splashY, splashSize, 0, Math.PI * 2);
          ctx.fill();
        }
      } else {
        // Parent on beach
        // Draw shadow
        ctx.fillStyle = "rgba(0, 0, 0, 0.2)";
        ctx.beginPath();
        ctx.ellipse(x, y + baseSize * 1.8, baseSize, baseSize * 0.3, 0, 0, Math.PI * 2);
        ctx.fill();
        
        // Draw legs
        ctx.strokeStyle = colors.skin;
        ctx.lineWidth = baseSize * 0.25;
        
        // Left leg
        ctx.beginPath();
        ctx.moveTo(x - baseSize * 0.3, y + baseSize * 0.8);
        ctx.lineTo(x - baseSize * 0.5, y + baseSize * 1.7);
        ctx.stroke();
        
        // Right leg
        ctx.beginPath();
        ctx.moveTo(x + baseSize * 0.3, y + baseSize * 0.8);
        ctx.lineTo(x + baseSize * 0.5, y + baseSize * 1.7);
        ctx.stroke();
        
        // Draw shorts
        ctx.fillStyle = "#3F51B5"; // Blue shorts
        ctx.beginPath();
        ctx.rect(x - baseSize * 0.5, y + baseSize * 0.4, baseSize, baseSize * 0.4);
        ctx.fill();
        
        // Draw torso
        ctx.fillStyle = colors.skin;
        ctx.beginPath();
        ctx.ellipse(x, y, baseSize * 0.5, baseSize * 0.6, 0, 0, Math.PI * 2);
        ctx.fill();
        
        // Draw head
        ctx.fillStyle = colors.skin;
        ctx.beginPath();
        ctx.arc(x, y - baseSize * 0.8, baseSize * 0.4, 0, Math.PI * 2);
        ctx.fill();
        
        // Draw hair
        ctx.fillStyle = colors.hair;
        ctx.beginPath();
        ctx.arc(x, y - baseSize * 0.9, baseSize * 0.42, Math.PI, 0);
        ctx.fill();
        
        if (calling) {
          // Arms waving for help
          const waveOffset = Math.sin(time * 5) * baseSize * 0.3;
          
          ctx.strokeStyle = colors.skin;
          ctx.lineWidth = baseSize * 0.2;
          
          // Left arm waving
          ctx.beginPath();
          ctx.moveTo(x - baseSize * 0.4, y);
          ctx.lineTo(x - baseSize * 0.6, y - baseSize * 0.5 - waveOffset);
          ctx.stroke();
          
          // Right arm waving
          ctx.beginPath();
          ctx.moveTo(x + baseSize * 0.4, y);
          ctx.lineTo(x + baseSize * 0.6, y - baseSize * 0.5 - waveOffset);
          ctx.stroke();
          
          // Draw worried face
          ctx.fillStyle = "#000";
          ctx.beginPath();
          ctx.ellipse(x - baseSize * 0.1, y - baseSize * 0.8, baseSize * 0.05, baseSize * 0.03, 0, 0, Math.PI * 2);
          ctx.fill();
          
          ctx.beginPath();
          ctx.ellipse(x + baseSize * 0.1, y - baseSize * 0.8, baseSize * 0.05, baseSize * 0.03, 0, 0, Math.PI * 2);
          ctx.fill();
          
          // Mouth - worried
          ctx.beginPath();
          ctx.arc(x, y - baseSize * 0.55, baseSize * 0.1, 0, Math.PI, false);
          ctx.stroke();
        } else {
          // Normal standing pose
          ctx.strokeStyle = colors.skin;
          ctx.lineWidth = baseSize * 0.2;
          
          // Left arm (down)
          ctx.beginPath();
          ctx.moveTo(x - baseSize * 0.4, y);
          ctx.lineTo(x - baseSize * 0.6, y + baseSize * 0.5);
          ctx.stroke();
          
          // Right arm (down)
          ctx.beginPath();
          ctx.moveTo(x + baseSize * 0.4, y);
          ctx.lineTo(x + baseSize * 0.6, y + baseSize * 0.5);
          ctx.stroke();
          
          // Draw face - normal
          ctx.fillStyle = "#000";
          ctx.beginPath();
          ctx.ellipse(x - baseSize * 0.1, y - baseSize * 0.8, baseSize * 0.05, baseSize * 0.03, 0, 0, Math.PI * 2);
          ctx.fill();
          
          ctx.beginPath();
          ctx.ellipse(x + baseSize * 0.1, y - baseSize * 0.8, baseSize * 0.05, baseSize * 0.03, 0, 0, Math.PI * 2);
          ctx.fill();
          
          // Mouth - neutral
          ctx.beginPath();
          ctx.moveTo(x - baseSize * 0.1, y - baseSize * 0.65);
          ctx.lineTo(x + baseSize * 0.1, y - baseSize * 0.65);
          ctx.stroke();
        }
      }
    },
    
    // Draw lifeguard
    drawLifeguard(ctx, x, y, time, colors, rescuing) {
      const baseSize = 20;
      
      if (rescuing) {
        // Lifeguard in water
        // Draw shadow under water
        ctx.fillStyle = "rgba(0, 0, 0, 0.2)";
        ctx.beginPath();
        ctx.ellipse(x, y + baseSize * 0.5, baseSize, baseSize * 0.3, 0, 0, Math.PI * 2);
        ctx.fill();
        
        // Swimming motion
        const swimCycle = time * 4;
        const legKick = Math.sin(swimCycle) * baseSize * 0.3;
        const armStroke = Math.cos(swimCycle) * baseSize * 0.3;
        
        // Draw legs with kicking motion
        ctx.strokeStyle = colors.skin;
        ctx.lineWidth = baseSize * 0.2;
        
        // Left leg
        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.lineTo(x - baseSize * 0.4 - legKick, y + baseSize * 0.6);
        ctx.stroke();
        
        // Right leg
        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.lineTo(x + baseSize * 0.4 + legKick, y + baseSize * 0.6);
        ctx.stroke();
        
        // Draw arms with swimming motion
        // Left arm
        ctx.beginPath();
        ctx.moveTo(x - baseSize * 0.4, y - baseSize * 0.3);
        ctx.lineTo(x - baseSize * 0.6 - armStroke, y - baseSize * 0.1);
        ctx.stroke();
        
        // Right arm
        ctx.beginPath();
        ctx.moveTo(x + baseSize * 0.4, y - baseSize * 0.3);
        ctx.lineTo(x + baseSize * 0.6 + armStroke, y - baseSize * 0.1);
        ctx.stroke();
        
        // Draw swimsuit - lifeguard red
        ctx.fillStyle = colors.lifeguardRed;
        ctx.beginPath();
        ctx.ellipse(x, y, baseSize * 0.5, baseSize * 0.3, 0, 0, Math.PI * 2);
        ctx.fill();
        
        // Draw torso
        ctx.fillStyle = colors.skin;
        ctx.beginPath();
        ctx.ellipse(x, y - baseSize * 0.3, baseSize * 0.4, baseSize * 0.3, 0, 0, Math.PI * 2);
        ctx.fill();
        
        // Draw head
        ctx.fillStyle = colors.skin;
        ctx.beginPath();
        ctx.arc(x, y - baseSize * 0.7, baseSize * 0.35, 0, Math.PI * 2);
        ctx.fill();
        
        // Draw hair
        ctx.fillStyle = colors.hair;
        ctx.beginPath();
        ctx.arc(x, y - baseSize * 0.85, baseSize * 0.35, Math.PI, 0);
        ctx.fill();
        
        // Draw face - determined
        ctx.fillStyle = "#000";
        ctx.beginPath();
        ctx.ellipse(x - baseSize * 0.1, y - baseSize * 0.7, baseSize * 0.05, baseSize * 0.03, 0, 0, Math.PI * 2);
        ctx.fill();
        
        ctx.beginPath();
        ctx.ellipse(x + baseSize * 0.1, y - baseSize * 0.7, baseSize * 0.05, baseSize * 0.03, 0, 0, Math.PI * 2);
        ctx.fill();
        
        // Mouth - determined
        ctx.beginPath();
        ctx.moveTo(x - baseSize * 0.1, y - baseSize * 0.6);
        ctx.lineTo(x + baseSize * 0.1, y - baseSize * 0.6);
        ctx.stroke();
        
        // Water splash effects around lifeguard
        for (let i = 0; i < 5; i++) {
          const splashX = x + (Math.random() - 0.5) * baseSize * 3;
          const splashY = y + (Math.random() - 0.5) * baseSize * 2;
          const splashSize = Math.random() * baseSize * 0.2 + baseSize * 0.1;
          
          ctx.fillStyle = "rgba(255, 255, 255, 0.6)";
          ctx.beginPath();
          ctx.arc(splashX, splashY, splashSize, 0, Math.PI * 2);
          ctx.fill();
        }
      } else {
        // Lifeguard on beach
        // Draw shadow
        ctx.fillStyle = "rgba(0, 0, 0, 0.2)";
        ctx.beginPath();
        ctx.ellipse(x, y + baseSize * 1.8, baseSize, baseSize * 0.3, 0, 0, Math.PI * 2);
        ctx.fill();
        
        // Draw legs
        ctx.strokeStyle = colors.skin;
        ctx.lineWidth = baseSize * 0.25;
        
        // Left leg
        ctx.beginPath();
        ctx.moveTo(x - baseSize * 0.3, y + baseSize * 0.8);
        ctx.lineTo(x - baseSize * 0.5, y + baseSize * 1.7);
        ctx.stroke();
        
        // Right leg
        ctx.beginPath();
        ctx.moveTo(x + baseSize * 0.3, y + baseSize * 0.8);
        ctx.lineTo(x + baseSize * 0.5, y + baseSize * 1.7);
        ctx.stroke();
        
        // Draw shorts - lifeguard red
        ctx.fillStyle = colors.lifeguardRed;
        ctx.beginPath();
        ctx.rect(x - baseSize * 0.5, y + baseSize * 0.4, baseSize, baseSize * 0.4);
        ctx.fill();
        
        // Draw torso with "LIFEGUARD" text
        ctx.fillStyle = colors.lifeguardRed;
        ctx.beginPath();
        ctx.ellipse(x, y, baseSize * 0.5, baseSize * 0.6, 0, 0, Math.PI * 2);
        ctx.fill();
        
        // "LIFEGUARD" text
        ctx.fillStyle = "#FFFFFF";
        ctx.font = "bold 6px Arial";
        ctx.textAlign = "center";
        ctx.fillText("LIFE", x, y - baseSize * 0.1);
        ctx.fillText("GUARD", x, y + baseSize * 0.1);
        ctx.textAlign = "start";
        
        // Draw head
        ctx.fillStyle = colors.skin;
        ctx.beginPath();
        ctx.arc(x, y - baseSize * 0.8, baseSize * 0.4, 0, Math.PI * 2);
        ctx.fill();
        
        // Draw hair
        ctx.fillStyle = colors.hair;
        ctx.beginPath();
        ctx.arc(x, y - baseSize * 0.9, baseSize * 0.42, Math.PI, 0);
        ctx.fill();
        
        // Draw arms
        ctx.strokeStyle = colors.skin;
        ctx.lineWidth = baseSize * 0.2;
        
        // Left arm (down)
        ctx.beginPath();
        ctx.moveTo(x - baseSize * 0.4, y);
        ctx.lineTo(x - baseSize * 0.6, y + baseSize * 0.5);
        ctx.stroke();
        
        // Right arm (down)
        ctx.beginPath();
        ctx.moveTo(x + baseSize * 0.4, y);
        ctx.lineTo(x + baseSize * 0.6, y + baseSize * 0.5);
        ctx.stroke();
        
        // Draw face - alert
        ctx.fillStyle = "#000";
        ctx.beginPath();
        ctx.ellipse(x - baseSize * 0.1, y - baseSize * 0.8, baseSize * 0.05, baseSize * 0.03, 0, 0, Math.PI * 2);
        ctx.fill();
        
        ctx.beginPath();
        ctx.ellipse(x + baseSize * 0.1, y - baseSize * 0.8, baseSize * 0.05, baseSize * 0.03, 0, 0, Math.PI * 2);
        ctx.fill();
        
        // Mouth - alert
        ctx.beginPath();
        ctx.moveTo(x - baseSize * 0.1, y - baseSize * 0.65);
        ctx.lineTo(x + baseSize * 0.1, y - baseSize * 0.65);
        ctx.stroke();
      }
    },
    
    // Draw speech bubble
    drawSpeechBubble(ctx, x, y, text, size) {
      // Bubble
      ctx.fillStyle = "rgba(255, 255, 255, 0.9)";
      ctx.beginPath();
      ctx.ellipse(x, y, size, size / 2, 0, 0, Math.PI * 2);
      ctx.fill();
      
      // Pointer
      ctx.beginPath();
      ctx.moveTo(x, y + size / 2);
      ctx.lineTo(x - 10, y + size);
      ctx.lineTo(x + 10, y + size / 2 + 5);
      ctx.closePath();
      ctx.fill();
      
      // Text
      ctx.fillStyle = "#FF0000";
      ctx.font = "bold 16px Arial";
      ctx.textAlign = "center";
      ctx.fillText(text, x, y + 5);
      ctx.textAlign = "start";
    },
    
    // Draw rescue tube
    drawRescueTube(ctx, x, y, color) {
      // Draw rescue tube
      ctx.fillStyle = color;
      ctx.beginPath();
      ctx.ellipse(x + 30, y, 40, 10, 0, 0, Math.PI * 2);
      ctx.fill();
      
      // Draw rope
      ctx.strokeStyle = "#FFFFFF";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(x, y);
      ctx.lineTo(x + 30, y);
      ctx.stroke();
    },
    
    // Change scenario
    changeScenario(scenario, event) {
      // Prevent event from propagating to parent elements
      if (event) {
        event.preventDefault();
        event.stopPropagation();
      }
      
      this.currentScenario = scenario;
      
      // Reset simulation
      this.resetSimulation();
    }
  }
}
</script>

<style>
/* Scoped styles to prevent affecting parent page */
.water-safety-container {
  position: relative;
  overflow: hidden;
  background-color: #000;
  /* Important: prevent affecting parent page scrolling */
  touch-action: none;
  -ms-touch-action: none;
}

.fullscreen-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 9999;
  border-radius: 0;
}

.water-safety-container canvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.water-safety-container .title {
  position: absolute;
  top: 5%;
  left: 50%;
  transform: translateX(-50%);
  padding: 10px 16px;
  background: rgba(0,0,0,0.7);
  border-radius: 8px;
  text-align: center;
  border-bottom: 3px solid #22d3ee;
  box-shadow: 0 4px 10px rgba(0,0,0,0.2);
  max-width: 400px;
  z-index: 10;
  transition: all 0.3s ease;
}

.water-safety-container .title h2 {
  font-size: 18px;
  font-weight: bold;
  color: white;
  margin: 0;
  letter-spacing: 0.5px;
  transition: all 0.3s ease;
}

.water-safety-container .message {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 12px 20px;
  background: rgba(0,0,0,0.8);
  border-radius: 8px;
  text-align: center;
  max-width: 300px;
  border: none;
  border-left: 3px solid #22d3ee;
  box-shadow: 0 4px 10px rgba(0,0,0,0.2);
  z-index: 10;
  transition: all 0.3s ease;
}

.water-safety-container .message p {
  font-size: 16px;
  font-weight: 500;
  margin: 0;
  letter-spacing: 0.3px;
}

.water-safety-container .message .indicator {
  height: 4px;
  width: 80px;
  background-color: #22d3ee;
  margin: 8px auto 0;
  border-radius: 9999px;
}

.water-safety-container .control-panel {
  position: absolute;
  bottom: 16px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px;
  background-color: rgba(0,0,0,0.7);
  border-radius: 9999px;
  z-index: 10;
}

.water-safety-container .button {
  background-color: transparent;
  color: white;
  border: none;
  width: 36px;
  height: 36px;
  border-radius: 9999px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color 0.2s;
}

.water-safety-container .button:hover:not(:disabled) {
  background-color: rgba(255,255,255,0.2);
}

.water-safety-container .button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.water-safety-container .button svg {
  width: 18px;
  height: 18px;
}

.water-safety-container .button.next-step {
  background-color: #2563eb;
  width: 42px;
  height: 42px;
}

.water-safety-container .button.next-step:hover:not(:disabled) {
  background-color: #1d4ed8;
}

.water-safety-container .legend {
  position: absolute;
  bottom: 16px;
  right: 16px;
  background-color: rgba(0,0,0,0.7);
  border-radius: 8px;
  padding: 8px 12px;
  z-index: 10;
  font-size: 12px;
}

.water-safety-container .legend-item {
  display: flex;
  align-items: center;
  margin-bottom: 6px;
}

.water-safety-container .legend-item:last-child {
  margin-bottom: 0;
}

.water-safety-container .legend-color {
  width: 16px;
  height: 16px;
  margin-right: 6px;
  border-radius: 4px;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.water-safety-container .legend-color.safe {
  background-color: rgba(76, 175, 80, 0.5);
}

.water-safety-container .legend-color.danger {
  background-color: rgba(244, 67, 54, 0.5);
}

.water-safety-container .legend-text {
  font-size: 12px;
  color: white;
}

.water-safety-container .scenario-selector {
  position: absolute;
  top: 10px;
  right: 10px;
  background-color: rgba(0,0,0,0.7);
  border-radius: 8px;
  padding: 10px;
  z-index: 10;
  font-size: 12px;
}

.water-safety-container .scenario-selector h3 {
  margin-top: 0;
  margin-bottom: 6px;
  font-size: 14px;
  color: white;
}

.water-safety-container .scenario-button {
  display: block;
  width: 100%;
  padding: 6px 10px;
  margin-bottom: 6px;
  background-color: rgba(255,255,255,0.1);
  border: none;
  border-radius: 4px;
  color: white;
  text-align: left;
  cursor: pointer;
  transition: background-color 0.2s;
  font-size: 12px;
}

.water-safety-container .scenario-button:hover {
  background-color: rgba(255,255,255,0.2);
}

.water-safety-container .scenario-button.active {
  background-color: #2563eb;
}

.water-safety-container .scenario-button:last-child {
  margin-bottom: 0;
}

/* Responsive adjustments */
@media (max-width: 640px) {
  .water-safety-container .title {
    top: 60px;
    max-width: 90%;
  }
  
  .water-safety-container .title h2 {
    font-size: 14px;
  }
  
  .water-safety-container .message {
    max-width: 90%;
    padding: 8px 12px;
  }
  
  .water-safety-container .message p {
    font-size: 14px;
  }
  
  .water-safety-container .legend {
    bottom: 70px;
    right: 10px;
  }
  
  .water-safety-container .scenario-selector {
    top: 10px;
  }
  
  .back-button {
    top: 10px;
    left: 10px;
    padding: 6px 12px;
    font-size: 12px;
  }
  
  .back-button svg {
    width: 18px;
    height: 18px;
  }
}

.back-button {
  position: absolute;
  top: 20px;
  left: 20px;
  display: flex;
  align-items: center;
  background: rgba(0, 0, 0, 0.6);
  color: white;
  padding: 8px 16px;
  border-radius: 30px;
  cursor: pointer;
  z-index: 100;
  transition: all 0.2s ease;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
}

.back-button:hover {
  background: rgba(52, 152, 219, 0.8);
  transform: translateY(-2px);
}

.back-button svg {
  margin-right: 8px;
}
</style>