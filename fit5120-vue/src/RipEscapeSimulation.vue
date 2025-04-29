<template>
    <div class="simulation-wrapper">
      <div id="container" ref="container" class="container-small">
        <canvas id="simulation" ref="canvas"></canvas>
        
        <div class="scenario-tabs">
          <button id="incorrectTab" :class="['scenario-tab', { active: currentScenario === 'incorrect' }]" @click="switchScenario('incorrect')">
            Incorrect Response
          </button>
          <button id="correctTab" :class="['scenario-tab', { active: currentScenario === 'correct' }]" @click="switchScenario('correct')">
            Correct Response
          </button>
        </div>
        
        <div id="storyTitle" class="story-title">
          <h2 id="titleText">{{ currentStepTitle }}</h2>
        </div>
        
        <div id="correctIndicator" :class="['approach-indicator', 'correct', { visible: showCorrectIndicator, pulse: pulseCorrectIndicator }]">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="20 6 9 17 4 12"></polyline>
          </svg>
          <span>Correct Approach</span>
        </div>
        
        <div id="incorrectIndicator" :class="['approach-indicator', 'incorrect', { visible: showIncorrectIndicator, pulse: pulseIncorrectIndicator }]">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
          <span>Incorrect Approach</span>
        </div>
        
        <div class="control-panel">
          <button id="resetBtn" class="button" title="Reset" @click="resetSimulation">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M23 4v6h-6"></path>
              <path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"></path>
            </svg>
          </button>
          
          <button id="nextStepBtn" class="button next-step" title="Next Step" @click="nextStep">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </button>
          
          <button id="fullscreenBtn" class="button" title="Fullscreen" @click="toggleFullscreen">
            <svg v-if="!isFullscreen" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"></path>
            </svg>
            <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M8 3v3a2 2 0 0 1-2 2H3m18 0h-3a2 2 0 0 1-2-2V3m0 18v-3a2 2 0 0 1 2-2h3M3 16h3a2 2 0 0 1 2 2v3"></path>
            </svg>
          </button>
        </div>
  
        <!-- Step indicator -->
        <div class="step-indicator">
          <div v-for="i in totalSteps" :key="i" 
               :class="['step-dot', { active: currentStep >= i, current: currentStep === i }]">
          </div>
        </div>
  
        <!-- Area labels -->
        <div id="safeLabel1" class="area-label safe">SAFE ZONE</div>
        <div id="safeLabel2" class="area-label safe">SAFE ZONE</div>
        <div id="dangerLabel" class="area-label danger">RIP CURRENT</div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'RipCurrentSimulation',
    data() {
      return {
        // State variables
        isFullscreen: false,
        daytime: 0.5, // Fixed at noon
        currentScenario: 'incorrect', // 'correct' or 'incorrect'
        showCorrectIndicator: false,
        showIncorrectIndicator: false,
        pulseCorrectIndicator: false,
        pulseIncorrectIndicator: false,
        ctx: null,
        
        // Step-based animation variables
        currentStep: 0,
        totalSteps: 4, // Each scenario has 4 steps (0-3)
        animationTime: 0, // Used for wave animations
        animationFrame: null,
        
        // Transition animation variables
        isTransitioning: false,
        transitionProgress: 0,
        transitionDuration: 1000, // 1 second transition
        transitionStartTime: 0,
        
        // Swimmer position tracking for smooth transitions
        currentSwimmerPos: { x: 0, y: 0 },
        targetSwimmerPos: { x: 0, y: 0 },
        
        // Step titles for each scenario
        correctStepTitles: [
          "Starting at the Beach",
          "Caught in a Rip Current",
          "Swimming Parallel to Shore",
          "Safely Returning to Beach"
        ],
        incorrectStepTitles: [
          "Starting at the Beach",
          "Caught in a Rip Current",
          "Swimming Against the Current",
          "Exhausted and Pulled Further Out"
        ]
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
      
      // Set up event listeners
      window.addEventListener('resize', this.resizeCanvas);
      document.addEventListener('fullscreenchange', this.handleFullscreenChange);
      
      // Initialize
      this.resizeCanvas();
      
      // Start animation loop for background elements
      this.startBackgroundAnimation();
      
      // Initialize swimmer position
      const canvas = this.$refs.canvas;
      const width = canvas.width;
      const shoreLineY = canvas.height * 0.2;
      this.currentSwimmerPos = { 
        x: width * 0.5, 
        y: shoreLineY 
      };
      this.targetSwimmerPos = { ...this.currentSwimmerPos };
    },
    beforeUnmount() {
      // Clean up event listeners
      window.removeEventListener('resize', this.resizeCanvas);
      document.removeEventListener('fullscreenchange', this.handleFullscreenChange);
      
      // Cancel animation frame if running
      if (this.animationFrame) {
        cancelAnimationFrame(this.animationFrame);
        this.animationFrame = null;
      }
    },
    methods: {
      // Resize canvas to fill container
      resizeCanvas() {
        const canvas = this.$refs.canvas;
        const container = this.$refs.container;
        
        canvas.width = container.clientWidth;
        canvas.height = container.clientHeight;
        
        // Redraw
        this.drawSimulation();
        
        // Position area labels
        this.positionAreaLabels();
        
        // Update swimmer position for new canvas size
        this.updateSwimmerPositionForStep();
      },
      
      // Position area labels based on canvas size
      positionAreaLabels() {
        const canvas = this.$refs.canvas;
        const safeLabel1 = document.getElementById('safeLabel1');
        const safeLabel2 = document.getElementById('safeLabel2');
        const dangerLabel = document.getElementById('dangerLabel');
        
        if (safeLabel1 && safeLabel2 && dangerLabel) {
          safeLabel1.style.left = `${canvas.width * 0.25 - 50}px`;
          safeLabel1.style.top = `${canvas.height * 0.35}px`;
          
          safeLabel2.style.left = `${canvas.width * 0.75 - 50}px`;
          safeLabel2.style.top = `${canvas.height * 0.35}px`;
          
          dangerLabel.style.left = `${canvas.width * 0.5}px`;
          dangerLabel.style.top = `${canvas.height * 0.25}px`;
          dangerLabel.style.transform = 'translateX(-50%)';
        }
      },
      
      // Reset simulation
      resetSimulation() {
        this.currentStep = 0;
        
        // Hide approach indicators
        this.showCorrectIndicator = false;
        this.showIncorrectIndicator = false;
        this.pulseCorrectIndicator = false;
        this.pulseIncorrectIndicator = false;
        
        // Update swimmer position
        this.updateSwimmerPositionForStep();
        
        // Draw initial state
        this.drawSimulation();
      },
      
      // Move to next step in the animation
      nextStep() {
        if (this.isTransitioning) return; // Don't allow clicking during transition
        
        if (this.currentStep < this.totalSteps - 1) {
          this.currentStep++;
          this.updateIndicators();
          this.startTransition();
        } else {
          // Loop back to beginning when reaching the end
          this.resetSimulation();
        }
      },
      
      // Start transition animation between steps
      startTransition() {
        this.isTransitioning = true;
        this.transitionProgress = 0;
        this.transitionStartTime = Date.now();
        
        // Set target position for the swimmer based on new step
        this.updateSwimmerPositionForStep();
      },
      
      // Update swimmer position based on current step
      updateSwimmerPositionForStep() {
        const canvas = this.$refs.canvas;
        const width = canvas.width;
        const height = canvas.height;
        const shoreLineY = height * 0.2;
        const ripCenterX = width * 0.5;
        
        // Set target position based on scenario and step
        if (this.currentScenario === 'correct') {
          switch (this.currentStep) {
            case 0: // Initial state
              this.targetSwimmerPos = { 
                x: ripCenterX, 
                y: shoreLineY 
              };
              break;
            case 1: // Getting caught in the rip
              this.targetSwimmerPos = { 
                x: ripCenterX, 
                y: shoreLineY + height * 0.3 
              };
              break;
            case 2: // Swimming parallel to shore
              this.targetSwimmerPos = { 
                x: ripCenterX - width * 0.25, 
                y: shoreLineY + height * 0.3 
              };
              break;
            case 3: // Swimming back to shore
              this.targetSwimmerPos = { 
                x: ripCenterX - width * 0.35, 
                y: shoreLineY + height * 0.1 
              };
              break;
          }
        } else { // Incorrect scenario
          switch (this.currentStep) {
            case 0: // Initial state
              this.targetSwimmerPos = { 
                x: ripCenterX, 
                y: shoreLineY 
              };
              break;
            case 1: // Getting caught in the rip
              this.targetSwimmerPos = { 
                x: ripCenterX, 
                y: shoreLineY + height * 0.3 
              };
              break;
            case 2: // Swimming against the current
              this.targetSwimmerPos = { 
                x: ripCenterX, 
                y: shoreLineY + height * 0.3 
              };
              break;
            case 3: // Getting pulled further out
              this.targetSwimmerPos = { 
                x: ripCenterX, 
                y: shoreLineY + height * 0.5 
              };
              break;
          }
        }
        
        // If not transitioning, immediately set current position to target
        if (!this.isTransitioning) {
          this.currentSwimmerPos = { ...this.targetSwimmerPos };
        }
      },
      
      // Update indicators based on current step and scenario
      updateIndicators() {
        if (this.currentScenario === 'correct') {
          if (this.currentStep === 2) {
            this.showCorrectIndicator = true;
            this.pulseCorrectIndicator = true;
          } else if (this.currentStep === 3) {
            this.showCorrectIndicator = true;
            this.pulseCorrectIndicator = false;
          } else {
            this.showCorrectIndicator = false;
            this.pulseCorrectIndicator = false;
          }
        } else {
          if (this.currentStep === 2) {
            this.showIncorrectIndicator = true;
            this.pulseIncorrectIndicator = true;
          } else if (this.currentStep === 3) {
            this.showIncorrectIndicator = true;
            this.pulseIncorrectIndicator = false;
          } else {
            this.showIncorrectIndicator = false;
            this.pulseIncorrectIndicator = false;
          }
        }
      },
      
      // Toggle fullscreen
      toggleFullscreen() {
        if (!document.fullscreenElement) {
          this.$refs.container.requestFullscreen().catch(err => {
            console.error(`Error attempting to enable fullscreen: ${err.message}`);
          });
        } else {
          document.exitFullscreen();
        }
      },
      
      // Handle fullscreen change
      handleFullscreenChange() {
        this.isFullscreen = !!document.fullscreenElement;
      },
      
      // Switch scenario
      switchScenario(scenario) {
        this.currentScenario = scenario;
        
        // Reset animation
        this.resetSimulation();
      },
      
      // Easing function for smooth transitions
      easeInOutCubic(t) {
        return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
      },
      
      // Start background animation loop (waves, clouds, etc.)
      startBackgroundAnimation() {
        const animate = () => {
          this.animationTime += 16; // ~60fps
          
          // Handle transition animation
          if (this.isTransitioning) {
            const now = Date.now();
            const elapsed = now - this.transitionStartTime;
            this.transitionProgress = Math.min(elapsed / this.transitionDuration, 1);
            
            // Apply easing function for smoother motion
            const easedProgress = this.easeInOutCubic(this.transitionProgress);
            
            // Interpolate swimmer position
            this.currentSwimmerPos.x = this.currentSwimmerPos.x + (this.targetSwimmerPos.x - this.currentSwimmerPos.x) * easedProgress;
            this.currentSwimmerPos.y = this.currentSwimmerPos.y + (this.targetSwimmerPos.y - this.currentSwimmerPos.y) * easedProgress;
            
            // Check if transition is complete
            if (this.transitionProgress >= 1) {
              this.isTransitioning = false;
              this.currentSwimmerPos = { ...this.targetSwimmerPos };
            }
          }
          
          this.drawSimulation();
          this.animationFrame = requestAnimationFrame(animate);
        };
        
        this.animationFrame = requestAnimationFrame(animate);
      },
      
      // Draw the simulation
      drawSimulation() {
        const canvas = this.$refs.canvas;
        const width = canvas.width;
        const height = canvas.height;
        const ctx = this.ctx;
        
        // Clear canvas
        ctx.clearRect(0, 0, width, height);
        
        // Set up time variables
        const time = this.animationTime / 1000; // Convert to seconds
        
        // Enhanced color palette
        const colors = {
          // Sky colors
          skyTop: "#87CEEB",
          skyBottom: "#ADD8E6",
          
          // Water colors
          shallowWater: "#60a5fa",
          midWater: "#2563eb",
          deepWater: "#1d4ed8",
          
          // Beach colors
          beach: "#fcd34d",
          beachDark: "#f59e0b",
          
          // Rip current and zones
          ripCurrent: "var(--rip-current)",
          safeZone: "rgba(16, 185, 129, 0.1)", // green tint
          dangerZone: "rgba(239, 68, 68, 0.1)", // red tint
        };
        
        // Shoreline position (constant)
        const shoreLineY = height * 0.2;
        
        // Draw sky with gradient
        const skyGradient = ctx.createLinearGradient(0, 0, 0, shoreLineY);
        skyGradient.addColorStop(0, colors.skyTop);
        skyGradient.addColorStop(1, colors.skyBottom);
        ctx.fillStyle = skyGradient;
        ctx.fillRect(0, 0, width, shoreLineY);
        
        // Draw sun with glow
        const sunX = width * 0.8;
        const sunY = height * 0.1;
        const sunRadius = Math.min(20, width * 0.03); // Scale sun size based on container width
        
        // Sun glow
        const sunGlow = ctx.createRadialGradient(sunX, sunY, 0, sunX, sunY, sunRadius * 3);
        sunGlow.addColorStop(0, "rgba(255, 255, 200, 0.8)");
        sunGlow.addColorStop(0.3, "rgba(255, 255, 150, 0.4)");
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
        
        // Draw some clouds
        this.drawClouds(ctx, width, shoreLineY, time);
        
        // Draw beach with gradient
        const beachGradient = ctx.createLinearGradient(0, 0, 0, shoreLineY);
        beachGradient.addColorStop(0, colors.beach);
        beachGradient.addColorStop(1, colors.beachDark);
        ctx.fillStyle = beachGradient;
        ctx.fillRect(0, 0, width, shoreLineY * 0.3);
        
        // Add beach texture
        this.drawBeachTexture(ctx, width, shoreLineY);
        
        // Draw water with gradient
        const waterGradient = ctx.createLinearGradient(0, shoreLineY, 0, height);
        waterGradient.addColorStop(0, colors.shallowWater);
        waterGradient.addColorStop(0.3, colors.midWater);
        waterGradient.addColorStop(1, colors.deepWater);
        ctx.fillStyle = waterGradient;
        ctx.fillRect(0, shoreLineY, width, height - shoreLineY);
        
        // Draw rip current zone
        const ripWidth = width * 0.3;
        const ripCenterX = width * 0.5;
        
        // Draw safe zones with clear green borders
        // Left safe zone
        ctx.fillStyle = colors.safeZone;
        ctx.fillRect(0, shoreLineY, ripCenterX - ripWidth/2, height - shoreLineY);
        
        // Right safe zone
        ctx.fillRect(ripCenterX + ripWidth/2, shoreLineY, width - (ripCenterX + ripWidth/2), height - shoreLineY);
        
        // Draw green borders for safe zones
        ctx.strokeStyle = "rgba(16, 185, 129, 0.7)"; // green
        ctx.lineWidth = 3;
        ctx.setLineDash([10, 10]);
        
        // Left safe zone border
        ctx.beginPath();
        ctx.moveTo(0, shoreLineY);
        ctx.lineTo(ripCenterX - ripWidth/2, shoreLineY);
        ctx.lineTo(ripCenterX - ripWidth/2, height);
        ctx.lineTo(0, height);
        ctx.closePath();
        ctx.stroke();
        
        // Right safe zone border
        ctx.beginPath();
        ctx.moveTo(ripCenterX + ripWidth/2, shoreLineY);
        ctx.lineTo(width, shoreLineY);
        ctx.lineTo(width, height);
        ctx.lineTo(ripCenterX + ripWidth/2, height);
        ctx.closePath();
        ctx.stroke();
        
        // Draw danger zone with clear red border and darker water
        ctx.fillStyle = colors.ripCurrent;
        ctx.fillRect(ripCenterX - ripWidth/2, shoreLineY, ripWidth, height - shoreLineY);
  
        // Add a subtle gradient to the rip current to make it look more realistic
        const ripGradient = ctx.createLinearGradient(0, shoreLineY, 0, height);
        ripGradient.addColorStop(0, "rgba(12, 74, 110, 0.6)"); // Lighter at top
        ripGradient.addColorStop(1, "rgba(7, 54, 92, 0.9)"); // Darker at bottom
        ctx.fillStyle = ripGradient;
        ctx.fillRect(ripCenterX - ripWidth/2, shoreLineY, ripWidth, height - shoreLineY);
        
        // Draw red border for danger zone
        ctx.strokeStyle = "rgba(239, 68, 68, 0.7)"; // red
        ctx.beginPath();
        ctx.moveTo(ripCenterX - ripWidth/2, shoreLineY);
        ctx.lineTo(ripCenterX + ripWidth/2, shoreLineY);
        ctx.lineTo(ripCenterX + ripWidth/2, height);
        ctx.lineTo(ripCenterX - ripWidth/2, height);
        ctx.closePath();
        ctx.stroke();
        
        // Reset line dash
        ctx.setLineDash([]);
        
        // Draw rip current flow arrows
        this.drawRipCurrentFlow(ctx, ripCenterX, ripWidth, shoreLineY, height, time);
        
        // Draw waves
        this.drawWaves(ctx, shoreLineY, width, time);
        
        // Draw swimmer based on scenario and current step
        if (this.currentScenario === 'correct') {
          this.drawCorrectScenarioStep(ctx, ripCenterX, ripWidth, shoreLineY, width, height, time);
        } else {
          this.drawIncorrectScenarioStep(ctx, ripCenterX, ripWidth, shoreLineY, width, height, time);
        }
      },
      
      // Draw clouds
      drawClouds(ctx, width, shoreLineY, time) {
        const cloudPositions = [
          { x: width * 0.2 + time * 5 % width, y: shoreLineY * 0.4, size: Math.min(15, width * 0.025) },
          { x: width * 0.5 + time * 3 % width, y: shoreLineY * 0.3, size: Math.min(20, width * 0.03) },
          { x: width * 0.8 + time * 7 % width, y: shoreLineY * 0.5, size: Math.min(12, width * 0.02) }
        ];
        
        cloudPositions.forEach(cloud => {
          const cloudX = cloud.x % (width * 1.2) - width * 0.1;
          
          ctx.fillStyle = "rgba(255, 255, 255, 0.9)";
          
          // Draw cloud as a collection of circles
          for (let i = 0; i < 5; i++) {
            const offsetX = (i - 2) * cloud.size * 0.6;
            const offsetY = Math.sin(i * 1.5) * cloud.size * 0.2;
            const size = cloud.size * (0.7 + Math.sin(i * 2) * 0.3);
            
            ctx.beginPath();
            ctx.arc(cloudX + offsetX, cloud.y + offsetY, size, 0, Math.PI * 2);
            ctx.fill();
          }
        });
      },
      
      // Draw beach texture
      drawBeachTexture(ctx, width, shoreLineY) {
        // Add subtle horizontal texture lines to the beach
        for (let i = 0; i < 15; i++) {
          const y = shoreLineY * 0.3 * (i / 15);
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
      },
      
      // Draw the correct scenario step by step
      drawCorrectScenarioStep(ctx, ripCenterX, ripWidth, shoreLineY, width, height, time) {
        let swimDirection, isStruggling;
        
        // Get current swimmer position (with smooth transitions)
        const swimmerX = this.currentSwimmerPos.x;
        const swimmerY = this.currentSwimmerPos.y;
        
        // Determine swimmer state based on current step
        switch (this.currentStep) {
          case 0: // Initial state - not in water yet
            swimDirection = 0; // neutral
            isStruggling = false;
            break;
            
          case 1: // Getting caught in the rip
            swimDirection = 2; // trying to swim up/toward shore
            isStruggling = true;
            
            // Show realization
            ctx.fillStyle = "#FFFFFF";
            ctx.beginPath();
            ctx.ellipse(swimmerX + 40, swimmerY - 30, 30, 20, 0, 0, Math.PI * 2);
            ctx.fill();
            
            ctx.beginPath();
            ctx.moveTo(swimmerX + 15, swimmerY - 15);
            ctx.lineTo(swimmerX + 25, swimmerY - 25);
            ctx.lineTo(swimmerX + 10, swimmerY - 25);
            ctx.fill();
            
            // Draw arrow in thinking bubble
            ctx.strokeStyle = "#10b981";
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(swimmerX + 30, swimmerY - 30);
            ctx.lineTo(swimmerX + 50, swimmerY - 30);
            ctx.stroke();
            
            ctx.beginPath();
            ctx.moveTo(swimmerX + 45, swimmerY - 35);
            ctx.lineTo(swimmerX + 50, swimmerY - 30);
            ctx.lineTo(swimmerX + 45, swimmerY - 25);
            ctx.stroke();
            break;
            
          case 2: // Swimming parallel to shore
            swimDirection = -1; // swimming left
            isStruggling = false;
            
            // Draw correct approach indicator
            ctx.fillStyle = "rgba(16, 185, 129, 0.1)";
            ctx.beginPath();
            ctx.ellipse(swimmerX, swimmerY, 100, 50, 0, 0, Math.PI * 2);
            ctx.fill();
            
            // Correct direction arrow
            ctx.strokeStyle = "#10b981";
            ctx.lineWidth = 4;
            ctx.beginPath();
            ctx.moveTo(swimmerX - 60, swimmerY);
            ctx.lineTo(swimmerX - 20, swimmerY);
            ctx.stroke();
            
            // Arrow head
            ctx.beginPath();
            ctx.moveTo(swimmerX - 60, swimmerY);
            ctx.lineTo(swimmerX - 45, swimmerY - 10);
            ctx.lineTo(swimmerX - 45, swimmerY + 10);
            ctx.closePath();
            ctx.fillStyle = "#10b981";
            ctx.fill();
            break;
            
          case 3: // Swimming back to shore
            swimDirection = 2; // swimming up/toward shore
            isStruggling = false;
            
            // Draw path arrow
            ctx.strokeStyle = "#10b981";
            ctx.lineWidth = 2;
            ctx.setLineDash([5, 5]);
            ctx.beginPath();
            ctx.moveTo(ripCenterX - width * 0.4, shoreLineY + height * 0.3);
            ctx.lineTo(ripCenterX - width * 0.3, shoreLineY + height * 0.05);
            ctx.stroke();
            ctx.setLineDash([]);
            
            // Draw arrow head
            ctx.beginPath();
            ctx.moveTo(ripCenterX - width * 0.3, shoreLineY + height * 0.05);
            ctx.lineTo(ripCenterX - width * 0.3 - 10, shoreLineY + height * 0.05 + 10);
            ctx.lineTo(ripCenterX - width * 0.3 + 10, shoreLineY + height * 0.05 + 15);
            ctx.closePath();
            ctx.fillStyle = "#10b981";
            ctx.fill();
            break;
            
          default:
            swimDirection = 0;
            isStruggling = false;
        }
        
        // Draw the swimmer
        this.drawSwimmer(ctx, swimmerX, swimmerY, time, swimDirection, isStruggling);
      },
      
      // Draw the incorrect scenario step by step
      drawIncorrectScenarioStep(ctx, ripCenterX, ripWidth, shoreLineY, width, height, time) {
        let swimDirection, isStruggling;
        
        // Get current swimmer position (with smooth transitions)
        const swimmerX = this.currentSwimmerPos.x;
        const swimmerY = this.currentSwimmerPos.y;
        
        // Add side-to-side motion for struggling in step 2 and 3
        let adjustedX = swimmerX;
        if (this.currentStep === 2) {
          adjustedX += Math.sin(time * 8) * 15; // struggling side to side
        } else if (this.currentStep === 3) {
          adjustedX += Math.sin(time * 4) * 20; // weaker struggling
        }
        
        // Determine swimmer state based on current step
        switch (this.currentStep) {
          case 0: // Initial state - not in water yet
            swimDirection = 0; // neutral
            isStruggling = false;
            break;
            
          case 1: // Getting caught in the rip
            swimDirection = 2; // trying to swim up/toward shore
            isStruggling = true;
            
            // Show realization
            ctx.fillStyle = "#FFFFFF";
            ctx.beginPath();
            ctx.ellipse(adjustedX + 40, swimmerY - 30, 30, 20, 0, 0, Math.PI * 2);
            ctx.fill();
            
            ctx.beginPath();
            ctx.moveTo(adjustedX + 15, swimmerY - 15);
            ctx.lineTo(adjustedX + 25, swimmerY - 25);
            ctx.lineTo(adjustedX + 10, swimmerY - 25);
            ctx.fill();
            
            // Draw question mark in thinking bubble
            ctx.fillStyle = "#ef4444";
            ctx.font = "bold 20px Arial";
            ctx.textAlign = "center";
            ctx.textBaseline = "middle";
            ctx.fillText("?", adjustedX + 40, swimmerY - 30);
            ctx.textAlign = "start";
            ctx.textBaseline = "alphabetic";
            break;
            
          case 2: // Swimming against the current
            swimDirection = 2; // trying to swim up/toward shore
            isStruggling = true;
            
            // Draw wrong approach indicator
            ctx.fillStyle = "rgba(239, 68, 68, 0.15)";
            ctx.beginPath();
            ctx.arc(adjustedX, swimmerY, 70, 0, Math.PI * 2);
            ctx.fill();
            
            // Wrong direction arrow
            ctx.strokeStyle = "#ef4444";
            ctx.lineWidth = 4;
            ctx.beginPath();
            ctx.moveTo(adjustedX, swimmerY - 60);
            ctx.lineTo(adjustedX, swimmerY - 20);
            ctx.stroke();
            
            // Arrow head
            ctx.beginPath();
            ctx.moveTo(adjustedX, swimmerY - 60);
            ctx.lineTo(adjustedX - 10, swimmerY - 45);
            ctx.lineTo(adjustedX + 10, swimmerY - 45);
            ctx.closePath();
            ctx.fillStyle = "#ef4444";
            ctx.fill();
            
            // Add exhaustion indicators (sweat drops)
            for (let i = 0; i < 5; i++) {
              const angle = Math.PI * 0.5 + (Math.random() - 0.5) * 1;
              const distance = 30 + Math.random() * 20;
              const dropX = adjustedX + Math.cos(angle) * distance;
              const dropY = swimmerY - Math.sin(angle) * distance;
              
              // Draw sweat drop
              ctx.fillStyle = "rgba(200, 240, 255, 0.8)";
              ctx.beginPath();
              ctx.arc(dropX, dropY, 3 + Math.random() * 2, 0, Math.PI * 2);
              ctx.fill();
              
              // Draw drop trail
              ctx.beginPath();
              ctx.moveTo(dropX, dropY - 5);
              ctx.lineTo(dropX, dropY);
              ctx.strokeStyle = "rgba(200, 240, 255, 0.6)";
              ctx.lineWidth = 2;
              ctx.stroke();
            }
            break;
            
          case 3: // Getting pulled further out
            swimDirection = 2; // still trying to swim up/toward shore
            isStruggling = true;
            
            // Danger indicator
            ctx.fillStyle = "rgba(239, 68, 68, 0.1)";
            ctx.beginPath();
            ctx.arc(adjustedX, swimmerY, 100, 0, Math.PI * 2);
            ctx.fill();
            break;
            
          default:
            swimDirection = 0;
            isStruggling = false;
        }
        
        // Draw the swimmer
        this.drawSwimmer(ctx, adjustedX, swimmerY, time, swimDirection, isStruggling);
      },
      
      // Draw a swimmer
      drawSwimmer(ctx, x, y, time, swimDirection, isStruggling) {
        // Calculate perspective scale based on y position
        const perspectiveScale = Math.max(0.7, Math.min(1.2, 1 - (y - 125) / 400));
        const baseSize = 25 * perspectiveScale;
        
        // Swimming animation parameters
        const swimCycle = time * (isStruggling ? 8 : 4);
        const legKick = Math.sin(swimCycle) * baseSize * 0.8;
        const armStroke = Math.cos(swimCycle) * baseSize * 0.8;
        
        // Determine if swimmer is face down or face up based on direction
        const faceDown = swimDirection !== 2; // Face up when swimming toward shore
        
        // Draw shadow
        ctx.fillStyle = "rgba(0, 0, 0, 0.3)";
        ctx.beginPath();
        ctx.ellipse(x, y + baseSize * 0.8, baseSize * 1.5, baseSize * 0.4, 0, 0, Math.PI * 2);
        ctx.fill();
        
        // Draw legs
        ctx.strokeStyle = "#FFD0A9"; // skin color
        ctx.lineWidth = baseSize * 0.3;
        
        // Left leg
        ctx.beginPath();
        ctx.moveTo(x, y + baseSize * 0.3);
        if (faceDown) {
          ctx.lineTo(x - baseSize * 0.5 - legKick, y + baseSize * 1.2);
        } else {
          ctx.lineTo(x - baseSize * 0.5 - legKick, y - baseSize * 0.8);
        }
        ctx.stroke();
        
        // Right leg
        ctx.beginPath();
        ctx.moveTo(x, y + baseSize * 0.3);
        if (faceDown) {
          ctx.lineTo(x + baseSize * 0.5 + legKick, y + baseSize * 1.2);
        } else {
          ctx.lineTo(x + baseSize * 0.5 + legKick, y - baseSize * 0.8);
        }
        ctx.stroke();
        
        // Draw swimsuit
        ctx.fillStyle = "#3b82f6"; // blue swimsuit
        ctx.beginPath();
        ctx.ellipse(x, y, baseSize * 0.6, baseSize * 0.4, 0, 0, Math.PI * 2);
        ctx.fill();
        
        // Draw torso
        ctx.fillStyle = "#FFD0A9"; // skin color
        ctx.beginPath();
        if (faceDown) {
          ctx.ellipse(x, y - baseSize * 0.3, baseSize * 0.5, baseSize * 0.3, 0, 0, Math.PI * 2);
        } else {
          ctx.ellipse(x, y + baseSize * 0.3, baseSize * 0.5, baseSize * 0.3, 0, 0, Math.PI * 2);
        }
        ctx.fill();
        
        // Draw head
        ctx.fillStyle = "#FFD0A9"; // skin color
        ctx.beginPath();
        if (faceDown) {
          ctx.arc(x, y - baseSize * 0.7, baseSize * 0.4, 0, Math.PI * 2);
        } else {
          ctx.arc(x, y + baseSize * 0.7, baseSize * 0.4, 0, Math.PI * 2);
        }
        ctx.fill();
        
        // Draw hair
        ctx.fillStyle = "#8B4513"; // brown hair
        if (faceDown) {
          // Hair on top of head when face down
          ctx.beginPath();
          ctx.ellipse(x, y - baseSize * 0.9, baseSize * 0.45, baseSize * 0.25, 0, 0, Math.PI * 2);
          ctx.fill();
        } else {
          // Hair visible from behind when face up
          ctx.beginPath();
          ctx.ellipse(x, y + baseSize * 0.5, baseSize * 0.45, baseSize * 0.25, 0, 0, Math.PI * 2);
          ctx.fill();
        }
        
        // Draw arms with swimming motion
        ctx.strokeStyle = "#FFD0A9"; // skin color
        ctx.lineWidth = baseSize * 0.25;
        
        if (isStruggling) {
          // Struggling arms - more frantic and uncoordinated
          const struggleOffset1 = Math.sin(time * 15) * baseSize * 0.6;
          const struggleOffset2 = Math.cos(time * 12) * baseSize * 0.6;
          
          // Left arm - more exaggerated movement
          ctx.beginPath();
          ctx.moveTo(x - baseSize * 0.4, y);
          ctx.lineTo(x - baseSize * 1.2 + struggleOffset1, y - baseSize * 0.8 + struggleOffset2);
          ctx.stroke();
          
          // Right arm - more exaggerated movement
          ctx.beginPath();
          ctx.moveTo(x + baseSize * 0.4, y);
          ctx.lineTo(x + baseSize * 1.2 + struggleOffset2, y - baseSize * 0.8 - struggleOffset1);
          ctx.stroke();
          
          // Add splashing effect around swimmer when struggling
          for (let i = 0; i < 12; i++) {
            const splashAngle = Math.random() * Math.PI * 2;
            const splashDist = baseSize * (1 + Math.random() * 2);
            const splashX = x + Math.cos(splashAngle) * splashDist;
            const splashY = y + Math.sin(splashAngle) * splashDist;
            const splashSize = baseSize * (0.1 + Math.random() * 0.2);
            
            ctx.fillStyle = "rgba(255, 255, 255, 0.7)";
            ctx.beginPath();
            ctx.arc(splashX, splashY, splashSize, 0, Math.PI * 2);
            ctx.fill();
          }
        } else if (swimDirection === -1) {
          // Swimming left
          ctx.beginPath();
          ctx.moveTo(x - baseSize * 0.4, y);
          ctx.lineTo(x - baseSize * 1.2 - armStroke, y);
          ctx.stroke();
          
          ctx.beginPath();
          ctx.moveTo(x + baseSize * 0.4, y);
          ctx.lineTo(x + baseSize * 1.2 + armStroke, y);
          ctx.stroke();
        } else if (swimDirection === 1) {
          // Swimming right
          ctx.beginPath();
          ctx.moveTo(x - baseSize * 0.4, y);
          ctx.lineTo(x - baseSize * 1.2 - armStroke, y);
          ctx.stroke();
          
          ctx.beginPath();
          ctx.moveTo(x + baseSize * 0.4, y);
          ctx.lineTo(x + baseSize * 1.2 + armStroke, y);
          ctx.stroke();
        } else if (swimDirection === 2) {
          // Swimming up/toward shore
          ctx.beginPath();
          ctx.moveTo(x - baseSize * 0.4, y);
          ctx.lineTo(x - baseSize - armStroke, y - baseSize * 0.5);
          ctx.stroke();
          
          ctx.beginPath();
          ctx.moveTo(x + baseSize * 0.4, y);
          ctx.lineTo(x + baseSize + armStroke, y - baseSize * 0.5);
          ctx.stroke();
        } else {
          // Neutral/floating
          ctx.beginPath();
          ctx.moveTo(x - baseSize * 0.4, y);
          ctx.lineTo(x - baseSize * 0.9, y);
          ctx.stroke();
          
          ctx.beginPath();
          ctx.moveTo(x + baseSize * 0.4, y);
          ctx.lineTo(x + baseSize * 0.9, y);
          ctx.stroke();
        }
        
        // Draw face details if large enough
        if (baseSize > 10 && faceDown) {
          // Face details
          ctx.fillStyle = "#000";
          
          // Eyes
          ctx.beginPath();
          ctx.ellipse(x - baseSize * 0.15, y - baseSize * 0.7, baseSize * 0.05, baseSize * 0.08, 0, 0, Math.PI * 2);
          ctx.fill();
          
          ctx.beginPath();
          ctx.ellipse(x + baseSize * 0.15, y - baseSize * 0.7, baseSize * 0.05, baseSize * 0.08, 0, 0, Math.PI * 2);
          ctx.fill();
          
          // Mouth - changes based on struggling
          ctx.beginPath();
          if (isStruggling) {
            // Open mouth when struggling
            ctx.ellipse(x, y - baseSize * 0.55, baseSize * 0.1, baseSize * 0.08, 0, 0, Math.PI * 2);
          } else {
            // Smile when not struggling
            ctx.arc(x, y - baseSize * 0.55, baseSize * 0.15, 0.1, Math.PI - 0.1, false);
          }
          ctx.stroke();
        }
        
        // Water splash effects around swimmer
        if (isStruggling || Math.abs(swimDirection) > 0) {
          for (let i = 0; i < 5; i++) {
            const splashX = x + (Math.random() - 0.5) * baseSize * 3;
            const splashY = y + (Math.random() - 0.5) * baseSize * 2;
            const splashSize = Math.random() * baseSize * 0.3 + baseSize * 0.1;
            
            ctx.fillStyle = "rgba(255, 255, 255, 0.6)";
            ctx.beginPath();
            ctx.arc(splashX, splashY, splashSize, 0, Math.PI * 2);
            ctx.fill();
          }
        }
      },
      
      // Helper function to draw waves
      drawWaves(ctx, shoreLineY, width, time) {
        // Draw multiple layers of waves
        for (let i = 0; i < 8; i++) {
          const y = shoreLineY + i * 50;
          const amplitude = 8 - i * 0.8;
          const speed = 0.5 - i * 0.05;
          const alpha = 0.7 - i * 0.08;
          
          ctx.strokeStyle = `rgba(255, 255, 255, ${alpha})`;
          ctx.lineWidth = 2 - i * 0.2;
          ctx.beginPath();
          
          for (let x = 0; x < width; x += 10) {
            const waveY = y + Math.sin(x * 0.02 + time * speed) * amplitude;
            
            if (x === 0) {
              ctx.moveTo(x, waveY);
            } else {
              ctx.lineTo(x, waveY);
            }
          }
          
          ctx.stroke();
        }
      },
      
      // Helper function to draw rip current flow
      drawRipCurrentFlow(ctx, ripCenterX, ripWidth, shoreLineY, height, time) {
        // Draw rip current flow arrows
        ctx.strokeStyle = "#FFFFFF";
        ctx.lineWidth = 2;
        
        // Draw red arrows in the rip current
        const arrowCount = 3;
        const arrowSpacing = height * 0.2;
        
        for (let i = 0; i < arrowCount; i++) {
          const y = shoreLineY + arrowSpacing * (i + 1);
          const arrowLength = 40;
          
          // Draw arrow shaft
          ctx.strokeStyle = "#ef4444";
          ctx.lineWidth = 3;
          ctx.beginPath();
          ctx.moveTo(ripCenterX, y - arrowLength/2);
          ctx.lineTo(ripCenterX, y + arrowLength/2);
          ctx.stroke();
          
          // Draw arrow head
          ctx.fillStyle = "#ef4444";
          ctx.beginPath();
          ctx.moveTo(ripCenterX, y + arrowLength/2);
          ctx.lineTo(ripCenterX - 10, y + arrowLength/2 - 15);
          ctx.lineTo(ripCenterX + 10, y + arrowLength/2 - 15);
          ctx.closePath();
          ctx.fill();
        }
        
        // Draw flow particles
        ctx.strokeStyle = "#FFFFFF";
        ctx.lineWidth = 1.5;
        
        for (let i = 0; i < 8; i++) {
          const xOffset = ((i - 4) / 4) * (ripWidth * 0.8);
          const x = ripCenterX + xOffset;
          const flowSpeed = 1.5 - Math.abs(xOffset) / (ripWidth * 0.4); // Faster in center
          
          // Create multiple particles flowing down the current
          for (let j = 0; j < 3; j++) {
            const flowOffset = (time * flowSpeed + j * 0.33) % 1;
            const yStart = shoreLineY + flowOffset * (height - shoreLineY);
            const yEnd = Math.min(yStart + 20, height);
            
            // Adjust x position to follow the narrowing current
            const progress = (yStart - shoreLineY) / (height - shoreLineY);
            const narrowingFactor = 1 - progress * 0.4;
            const adjustedX = ripCenterX + xOffset * narrowingFactor;
            
            const alpha = 0.7 - flowOffset * 0.5;
            
            // Draw flow particle
            ctx.globalAlpha = alpha;
            ctx.beginPath();
            ctx.moveTo(adjustedX, yStart);
            ctx.lineTo(adjustedX, yEnd);
            ctx.stroke();
          }
        }
        
        ctx.globalAlpha = 1;
      }
    }
  }
  </script>
  
  <style>
  :root {
    --primary: #3b82f6;
    --primary-dark: #2563eb;
    --success: #10b981;
    --danger: #ef4444;
    --light: #f3f4f6;
    --dark: #1f2937;
    --water-light: #60a5fa;
    --water-mid: #2563eb;
    --water-dark: #1d4ed8;
    --rip-current: #0c4a6e; /* Darker blue for rip current */
    --sand: #fcd34d;
    --sand-dark: #f59e0b;
  }
  
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  
  body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: var(--dark);
    color: var(--light);
    line-height: 1.5;
  }
  
  .simulation-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
    width: 100%;
  }
  
  .container-small {
    position: relative;
    width: 800px;
    height: 500px;
    overflow: hidden;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    border: 1px solid rgba(255, 255, 255, 0.1);
    background-color: var(--dark);
  }
  
  canvas {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }
  
  .scenario-tabs {
    position: absolute;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 10px;
    z-index: 20;
    background: rgba(0,0,0,0.5);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 8px;
    border-radius: 8px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    width: auto;
    min-width: 300px;
  }
  
  .scenario-tab {
    flex: 1;
    padding: 10px 15px;
    background-color: rgba(255,255,255,0.1);
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 500;
    transition: all 0.2s;
    white-space: nowrap;
    text-align: center;
  }
  
  .scenario-tab.active {
    background-color: var(--primary);
    box-shadow: 0 0 15px rgba(59, 130, 246, 0.3);
  }
  
  .story-title {
    position: absolute;
    top: 80px;
    left: 50%;
    transform: translateX(-50%);
    padding: 10px 20px;
    background: rgba(0,0,0,0.7);
    border-radius: 8px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    width: 80%;
    z-index: 10;
    border-left: 4px solid var(--primary);
    transition: all 0.3s ease;
  }
  
  .story-title h2 {
    font-size: 16px;
    font-weight: 600;
    margin: 0;
    line-height: 1.4;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    transition: all 0.3s ease;
  }
  
  .step-indicator {
    position: absolute;
    bottom: 70px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 10px;
    z-index: 20;
  }
  
  .step-dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background-color: rgba(255, 255, 255, 0.3);
    border: 2px solid rgba(255, 255, 255, 0.5);
    transition: all 0.3s ease;
  }
  
  .step-dot.active {
    background-color: var(--primary);
    border-color: var(--primary-dark);
  }
  
  .step-dot.current {
    transform: scale(1.3);
    box-shadow: 0 0 10px rgba(59, 130, 246, 0.5);
  }
  
  .control-panel {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 8px 15px;
    background-color: rgba(0,0,0,0.75);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-radius: 30px;
    z-index: 10;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    border: 1px solid rgba(255,255,255,0.1);
  }
  
  .button {
    background-color: rgba(255,255,255,0.1);
    color: white;
    border: none;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s ease;
  }
  
  .button:hover {
    background-color: rgba(255,255,255,0.2);
    transform: translateY(-2px);
  }
  
  .button:active {
    transform: translateY(0);
  }
  
  .button svg {
    width: 16px;
    height: 16px;
  }
  
  .button.next-step {
    background-color: var(--primary);
    width: 48px;
    height: 48px;
  }
  
  .button.next-step:hover {
    background-color: var(--primary-dark);
    box-shadow: 0 0 15px rgba(59, 130, 246, 0.5);
  }
  
  .area-label {
    position: absolute;
    font-size: 14px;
    font-weight: 600;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
    pointer-events: none;
    z-index: 5;
    background: rgba(0,0,0,0.4);
    padding: 4px 8px;
    border-radius: 4px;
    letter-spacing: 1px;
    text-transform: uppercase;
  }
  
  .area-label.safe {
    color: var(--success);
    border: 2px solid var(--success);
  }
  
  .area-label.danger {
    color: var(--danger);
    border: 2px solid var(--danger);
    transform: translateX(-45%) !important; /* Adjust horizontal position */
  }
  
  .approach-indicator {
    position: absolute;
    bottom: 130px;
    left: 50%;
    transform: translateX(-50%);
    padding: 8px 16px;
    border-radius: 30px;
    font-weight: 600;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1px;
    z-index: 15;
    display: flex;
    align-items: center;
    gap: 8px;
    opacity: 0;
    transition: opacity 0.3s ease;
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 80%;
  }
  
  .approach-indicator.correct {
    background-color: rgba(16, 185, 129, 0.2);
    color: var(--success);
    border: 2px solid var(--success);
    box-shadow: 0 0 20px rgba(16, 185, 129, 0.2);
  }
  
  .approach-indicator.incorrect {
    background-color: rgba(239, 68, 68, 0.2);
    color: var(--danger);
    border: 2px solid var(--danger);
    box-shadow: 0 0 20px rgba(239, 68, 68, 0.2);
  }
  
  .approach-indicator.visible {
    opacity: 1;
  }
  
  @keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
  }
  
  .pulse {
    animation: pulse 2s infinite ease-in-out;
  }
  
  /* Responsive adjustments */
  @media (max-width: 850px) {
    .container-small {
      width: 100%;
      height: 400px;
    }
    
    .scenario-tabs {
      top: 15px;
      width: 90%;
      min-width: unset;
      flex-direction: row;
      gap: 6px;
      padding: 6px;
    }
  
    .scenario-tab {
      width: 100%;
      padding: 8px 12px;
      font-size: 12px;
      white-space: normal;
    }
  
    .story-title {
      top: 70px;
      width: 90%;
      padding: 8px 15px;
    }
  
    .story-title h2 {
      font-size: 14px;
      white-space: normal;
    }
  
    .approach-indicator {
      bottom: 120px;
      font-size: 12px;
      padding: 6px 12px;
      width: 90%;
    }
    
    .button {
      width: 32px;
      height: 32px;
    }
    
    .button svg {
      width: 14px;
      height: 14px;
    }
    
    .button.next-step {
      width: 42px;
      height: 42px;
    }
    
    .step-dot {
      width: 10px;
      height: 10px;
    }
  }
  </style>