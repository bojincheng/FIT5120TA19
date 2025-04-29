<template>
  <div class="pool-safety-window" :style="{ width: width + 'px', height: height + 'px' }">
    <div ref="containerRef" class="window-container relative overflow-hidden bg-black text-white font-sans rounded-lg shadow-xl">
      <!-- Canvas container with fixed aspect ratio -->
      <div class="relative w-full h-full">
        <div ref="canvasContainerRef" class="relative w-full h-full" style="aspect-ratio: 2/1;">
          <canvas ref="canvasRef" class="absolute top-0 left-0 w-full h-full"></canvas>
        </div>
      </div>
      
      <!-- Start Button -->
      <div v-if="!isStarted" class="absolute inset-0 flex items-center justify-center bg-black/50 z-[50]">
        <button 
          class="bg-cyan-600 hover:bg-cyan-700 text-white py-3 px-6 rounded-lg text-xl font-bold transition-colors shadow-lg"
          @click="startSimulation"
        >
          Start Simulation
        </button>
      </div>

      <div class="absolute top-[10%] left-1/2 -translate-x-1/2 p-4 bg-black/70 rounded-lg text-center border-b-[3px] border-cyan-400 shadow-md max-w-[500px] z-[20]">
        <h2 class="text-xl sm:text-2xl font-bold tracking-tight">Pool Safety Simulation</h2>
      </div>

      <!-- Quiz Popup - 改为absolute定位 -->
      <div v-if="showQuiz" class="absolute inset-0 bg-black/80 flex items-center justify-center p-4 z-[100]">
        <div class="bg-gray-900 rounded-lg max-w-lg p-6 relative animate-fade-in">
          <div class="absolute top-2 right-2 bg-red-500 text-white rounded-full w-8 h-8 flex items-center justify-center font-bold">
            {{ timeLeft }}
          </div>

          <h2 class="text-xl font-bold text-cyan-400 mb-6">
            The child has fallen into the pool! What would you do?
          </h2>

          <div class="flex flex-col gap-3">
            <button 
              class="bg-blue-600 hover:bg-blue-700 text-white py-3 px-4 rounded-md text-left transition-colors"
              @click="handleOptionSelect('A')"
            >
              A. Jump into the water
            </button>

            <button 
              class="bg-blue-600 hover:bg-blue-700 text-white py-3 px-4 rounded-md text-left transition-colors"
              @click="handleOptionSelect('B')"
            >
              B. Call emergency services
            </button>

            <button 
              class="bg-blue-600 hover:bg-blue-700 text-white py-3 px-4 rounded-md text-left transition-colors"
              @click="handleOptionSelect('C')"
            >
              C. Shout for help
            </button>
          </div>
        </div>
      </div>

      <!-- Simplified Feedback Popup - 改为absolute定位 -->
      <div v-if="showFeedback" class="absolute inset-0 bg-black/80 flex items-center justify-center p-4 z-[100]">
        <div class="bg-gray-900 rounded-lg max-w-lg p-6 relative max-h-[90vh] overflow-y-auto">
          <h2 class="text-xl font-bold text-cyan-400 mb-4">Safety Response</h2>
          
          <!-- Simplified Feedback -->
          <div class="mb-4" :class="feedbackColorClass">
            <p :class="feedbackTextClass">
              <span class="font-bold">{{ feedbackTitle }}</span> {{ feedbackMessage }}
            </p>
          </div>

          <div class="mt-6 p-3 bg-blue-900/50 rounded-md">
            <p class="text-blue-200 text-sm">
              <span class="font-bold">Remember:</span> The best approach in a water emergency is to "Reach, Throw,
              Row, Go" - try to reach the person from land, throw something that floats, use a boat if available, and
              only enter the water as a last resort if you're trained.
            </p>
          </div>

          <button 
            class="mt-4 bg-cyan-600 hover:bg-cyan-700 text-white py-2 px-4 rounded-md transition-colors"
            @click="resetSimulation"
          >
            Restart Simulation
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch, computed } from 'vue';

// Props for component size
const props = defineProps({
  width: {
    type: Number,
    default: 600
  },
  height: {
    type: Number,
    default: 400
  }
});

// Canvas and container refs
const canvasRef = ref(null);
const containerRef = ref(null);
const canvasContainerRef = ref(null);

// State variables
const paused = ref(true);
const showLabels = ref(true);
const isStarted = ref(false);

// Quiz state
const showQuiz = ref(false);
const timeLeft = ref(10);
const selectedOption = ref(null);
const showFeedback = ref(false);

// Rescue animation state
const playingRescueAnimation = ref(false);
const rescueAnimationType = ref(null);
const rescueAnimationTime = ref(0);
const rescueAnimationCompleted = ref(false);

// Animation time tracking
const animationTimeRef = ref(0);
const lastCycleTimeRef = ref(0);

// Animation frame and other variables
let animationFrame = null;
let animationTime = 0;

// Simplified feedback content
const feedbackColorClass = computed(() => {
  if (selectedOption.value === 'C') return 'bg-green-900/50 p-4 rounded-md mb-4';
  if (selectedOption.value === 'timeout') return 'bg-red-900/50 p-4 rounded-md mb-4';
  return 'bg-yellow-900/50 p-4 rounded-md mb-4';
});

const feedbackTextClass = computed(() => {
  if (selectedOption.value === 'C') return 'text-green-200';
  if (selectedOption.value === 'timeout') return 'text-red-200';
  return 'text-yellow-200';
});

const feedbackTitle = computed(() => {
  if (selectedOption.value === 'A') return 'Risky choice:';
  if (selectedOption.value === 'B') return 'Important:';
  if (selectedOption.value === 'C') return 'Good choice:';
  if (selectedOption.value === 'timeout') return 'Time\'s up!';
  return '';
});

const feedbackMessage = computed(() => {
  if (selectedOption.value === 'A') {
    return 'Jumping into the water without proper training is dangerous. Without proper training and equipment, rescuers frequently become victims.';
  }
  if (selectedOption.value === 'B') {
    return 'Calling emergency services is crucial, but in a drowning situation, every second counts. Someone needs to take immediate action while waiting for help.';
  }
  if (selectedOption.value === 'C') {
    return 'Shouting for help alerts others, including lifeguards who are trained for water rescue. This is often the safest first response while you look for a reaching aid.';
  }
  if (selectedOption.value === 'timeout') {
    return 'In an emergency situation, quick action is essential. Every second counts when someone is drowning.';
  }
  return '';
});

// Start simulation
const startSimulation = () => {
  isStarted.value = true;
  paused.value = false;

  // Reset animation time
  animationTime = 0;

  // Ensure animation starts running
  if (animationFrame) {
    cancelAnimationFrame(animationFrame);
  }
  startAnimation();
};

// Reset simulation
const resetSimulation = () => {
  // Reset all state variables
  paused.value = true;
  showQuiz.value = false;
  selectedOption.value = null;
  timeLeft.value = 10;
  showFeedback.value = false;
  isStarted.value = false;

  // Reset animation state
  playingRescueAnimation.value = false;
  rescueAnimationType.value = null;
  rescueAnimationTime.value = 0;
  rescueAnimationCompleted.value = false;

  // Reset animation time and cycle variables
  animationTime = 0;
  animationTimeRef.value = 0;
  lastCycleTimeRef.value = 0;

  // Cancel current animation frame
  if (animationFrame) {
    cancelAnimationFrame(animationFrame);
    animationFrame = null;
  }

  // Redraw initial scene
  drawSimulation(0);

  // Delay one frame before drawing again to ensure all states are correctly applied
  requestAnimationFrame(() => {
    drawSimulation(0);
  });
};

// Handle quiz option selection
const handleOptionSelect = (option) => {
  selectedOption.value = option;
  showQuiz.value = false;
  // Start animation immediately
  playingRescueAnimation.value = true;
  rescueAnimationType.value = option;
  rescueAnimationTime.value = 0;
  paused.value = false; // Make sure animation plays immediately

  // Ensure animation continues running
  if (!animationFrame) {
    startAnimation();
  }
};

// Canvas drawing functions
const drawPerson = (ctx, x, y, baseSize, legSwing, armSwing, rotation, colors, inWater, falling) => {
  ctx.save();
  ctx.translate(x, y);
  ctx.rotate(rotation);

  // Clothes color - different from swimmer
  const clothesColor = "#3F51B5";

  // Draw legs if not fully submerged
  if (!inWater) {
    ctx.strokeStyle = colors.skin;
    ctx.lineWidth = baseSize * 0.25;

    // Left leg with swing
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(-baseSize * 0.3 - legSwing, baseSize * 0.8);
    ctx.stroke();

    // Right leg with opposite swing
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(baseSize * 0.3 - legSwing, baseSize * 0.8);
    ctx.stroke();
  }

  // Draw body
  ctx.fillStyle = clothesColor;
  ctx.beginPath();
  ctx.ellipse(0, -baseSize * 0.3, baseSize * 0.4, baseSize * 0.3, 0, 0, Math.PI * 2);
  ctx.fill();

  // Draw head
  ctx.fillStyle = colors.skin;
  ctx.beginPath();
  ctx.arc(0, -baseSize * 0.7, baseSize * 0.35, 0, Math.PI * 2);
  ctx.fill();

  // Draw hair
  ctx.fillStyle = colors.hair;
  ctx.beginPath();
  ctx.arc(0, -baseSize * 0.85, baseSize * 0.35, Math.PI, 0);
  ctx.fill();

  // Draw arms
  ctx.strokeStyle = colors.skin;
  ctx.lineWidth = baseSize * 0.2;

  // Left arm with swing
  ctx.beginPath();
  ctx.moveTo(-baseSize * 0.4, -baseSize * 0.3);
  ctx.lineTo(-baseSize * 0.7 - armSwing, -baseSize * 0.1);
  ctx.stroke();

  // Right arm with opposite swing
  ctx.beginPath();
  ctx.moveTo(baseSize * 0.4, -baseSize * 0.3);
  ctx.lineTo(baseSize * 0.7 - armSwing, -baseSize * 0.1);
  ctx.stroke();

  // Draw face - expression changes when falling or in water
  ctx.fillStyle = "#000";

  // Eyes
  ctx.beginPath();
  ctx.ellipse(-baseSize * 0.1, -baseSize * 0.7, baseSize * 0.05, baseSize * 0.03, 0, 0, Math.PI * 2);
  ctx.fill();

  ctx.beginPath();
  ctx.ellipse(baseSize * 0.1, -baseSize * 0.7, baseSize * 0.05, baseSize * 0.03, 0, 0, Math.PI * 2);
  ctx.fill();

  // Mouth - changes based on state
  if (falling || inWater) {
    // Surprised/worried mouth
    ctx.beginPath();
    ctx.arc(0, -baseSize * 0.55, baseSize * 0.1, 0, Math.PI, false);
    ctx.stroke();
  } else {
    // Normal mouth
    ctx.beginPath();
    ctx.arc(0, -baseSize * 0.55, baseSize * 0.1, 0.1, Math.PI - 0.1, false);
    ctx.stroke();
  }

  ctx.restore();
};

const drawLeisurePool = (ctx, width, height, time, colors) => {
  // Irregular shaped leisure pool
  ctx.fillStyle = colors.poolEdge;
  ctx.beginPath();
  ctx.moveTo(width * 0.2, height * 0.3);
  ctx.lineTo(width * 0.8, height * 0.3);
  ctx.lineTo(width * 0.8, height * 0.6);
  ctx.lineTo(width * 0.6, height * 0.7);
  ctx.lineTo(width * 0.2, height * 0.7);
  ctx.closePath();
  ctx.fill();

  // Water with gradient
  const waterColor = "rgba(79, 195, 247, 0.9)"; // Fixed water clarity

  ctx.fillStyle = waterColor;
  ctx.beginPath();
  ctx.moveTo(width * 0.21, height * 0.31);
  ctx.lineTo(width * 0.79, height * 0.31);
  ctx.lineTo(width * 0.79, height * 0.59);
  ctx.lineTo(width * 0.6, height * 0.69);
  ctx.lineTo(width * 0.21, height * 0.69);
  ctx.closePath();
  ctx.fill();

  // Draw water slide
  ctx.fillStyle = "#FF9800";
  ctx.beginPath();
  ctx.moveTo(width * 0.85, height * 0.2);
  ctx.lineTo(width * 0.8, height * 0.3);
  ctx.lineTo(width * 0.75, height * 0.3);
  ctx.lineTo(width * 0.8, height * 0.2);
  ctx.closePath();
  ctx.fill();

  // Draw water ripples
  for (let i = 0; i < 40; i++) {
    const x = width * (0.25 + Math.random() * 0.5);
    const y = height * (0.35 + Math.random() * 0.3);
    const size = Math.random() * 15 + 5;
    const alpha = Math.random() * 0.2 + 0.1;

    ctx.strokeStyle = `rgba(255, 255, 255, ${alpha})`;
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.arc(x, y, size, 0, Math.PI * 2);
    ctx.stroke();
  }

  // Draw splash zone
  ctx.fillStyle = "rgba(255, 255, 255, 0.3)";
  ctx.beginPath();
  ctx.arc(width * 0.75, height * 0.35, 20, 0, Math.PI * 2);
  ctx.fill();

  // Draw water features
  ctx.fillStyle = "#64B5F6";
  ctx.beginPath();
  ctx.arc(width * 0.3, height * 0.5, 15, 0, Math.PI * 2);
  ctx.fill();

  // Draw bubbles from water feature
  for (let i = 0; i < 5; i++) {
    const bubbleSize = 3 + Math.sin(time * 3 + i) * 2;
    const bubbleX = width * 0.3 + Math.sin(time * 2 + i * 0.5) * 10;
    const bubbleY = height * (0.5 - ((time * 0.2 + i * 0.1) % 0.15));

    ctx.fillStyle = "rgba(255, 255, 255, 0.6)";
    ctx.beginPath();
    ctx.arc(bubbleX, bubbleY, bubbleSize, 0, Math.PI * 2);
    ctx.fill();
  }
};

const drawSwimmer = (ctx, x, y, time, colors) => {
  const baseSize = 15;
  const swimCycle = time * 4;
  const legKick = Math.sin(swimCycle) * baseSize * 0.5;
  const armStroke = Math.cos(swimCycle) * baseSize * 0.5;

  // Draw shadow under water
  ctx.fillStyle = "rgba(0, 0, 0, 0.2)";
  ctx.beginPath();
  ctx.ellipse(x, y + baseSize * 0.5, baseSize, baseSize * 0.3, 0, 0, Math.PI * 2);
  ctx.fill();

  // Draw legs with kicking motion
  ctx.strokeStyle = colors.skin;
  ctx.lineWidth = baseSize * 0.25;

  // Left leg
  ctx.beginPath();
  ctx.moveTo(x, y);
  ctx.lineTo(x - baseSize * 0.5 - legKick, y + baseSize * 0.8);
  ctx.stroke();

  // Right leg
  ctx.beginPath();
  ctx.moveTo(x, y);
  ctx.lineTo(x + baseSize * 0.5 + legKick, y + baseSize * 0.8);
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

  // Draw arms with swimming motion
  ctx.strokeStyle = colors.skin;
  ctx.lineWidth = baseSize * 0.2;

  // Left arm
  ctx.beginPath();
  ctx.moveTo(x - baseSize * 0.4, y - baseSize * 0.3);
  ctx.lineTo(x - baseSize * 0.8 - armStroke, y - baseSize * 0.1);
  ctx.stroke();

  // Right arm
  ctx.beginPath();
  ctx.moveTo(x + baseSize * 0.4, y - baseSize * 0.3);
  ctx.lineTo(x + baseSize * 0.8 + armStroke, y - baseSize * 0.1);
  ctx.stroke();

  // Draw face
  if (baseSize > 10) {
    // Eyes
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

  // Water splash effects around swimmer
  for (let i = 0; i < 5; i++) {
    const splashX = x + (Math.random() - 0.5) * baseSize * 3;
    const splashY = y + (Math.random() - 0.5) * baseSize * 2;
    const splashSize = Math.random() * baseSize * 0.2 + baseSize * 0.1;

    ctx.fillStyle = "rgba(255, 255, 255, 0.6)";
    ctx.beginPath();
    ctx.arc(splashX, splashY, splashSize, 0, Math.PI * 2);
    ctx.fill();
  }
};

const drawLifeguard = (ctx, x, y, time, colors) => {
  const baseSize = 20;

  // Draw chair
  ctx.fillStyle = "#F44336";
  ctx.fillRect(x - baseSize * 0.5, y - baseSize * 2, baseSize, baseSize * 2);

  // Draw lifeguard
  // Body
  ctx.fillStyle = "#FFD54F";
  ctx.fillRect(x - baseSize * 0.4, y - baseSize * 1.8, baseSize * 0.8, baseSize * 0.8);

  // Head
  ctx.fillStyle = colors.skin;
  ctx.beginPath();
  ctx.arc(x, y - baseSize * 2, baseSize * 0.4, 0, Math.PI * 2);
  ctx.fill();

  // Hair
  ctx.fillStyle = colors.hair;
  ctx.beginPath();
  ctx.arc(x, y - baseSize * 2.2, baseSize * 0.3, Math.PI, 0);
  ctx.fill();

  // Arms
  ctx.strokeStyle = colors.skin;
  ctx.lineWidth = baseSize * 0.2;

  // Left arm - moving slightly
  const armMove = Math.sin(time) * 0.1;
  ctx.beginPath();
  ctx.moveTo(x - baseSize * 0.4, y - baseSize * 1.5);
  ctx.lineTo(x - baseSize * 0.8, y - baseSize * (1.3 + armMove));
  ctx.stroke();

  // Right arm - holding whistle
  ctx.beginPath();
  ctx.moveTo(x + baseSize * 0.4, y - baseSize * 1.5);
  ctx.lineTo(x + baseSize * 0.6, y - baseSize * 1.8);
  ctx.stroke();

  // Whistle
  ctx.fillStyle = "#FFC107";
  ctx.beginPath();
  ctx.arc(x + baseSize * 0.7, y - baseSize * 1.9, baseSize * 0.1, 0, Math.PI * 2);
  ctx.fill();

  // Legs
  ctx.strokeStyle = colors.skin;
  ctx.lineWidth = baseSize * 0.25;

  // Left leg
  ctx.beginPath();
  ctx.moveTo(x - baseSize * 0.2, y - baseSize);
  ctx.lineTo(x - baseSize * 0.3, y - baseSize * 0.5);
  ctx.stroke();

  // Right leg
  ctx.beginPath();
  ctx.moveTo(x + baseSize * 0.2, y - baseSize);
  ctx.lineTo(x + baseSize * 0.3, y - baseSize * 0.5);
  ctx.stroke();

  // Face
  // Eyes
  ctx.fillStyle = "#000";
  ctx.beginPath();
  ctx.ellipse(x - baseSize * 0.1, y - baseSize * 2, baseSize * 0.05, baseSize * 0.03, 0, 0, Math.PI * 2);
  ctx.fill();

  ctx.beginPath();
  ctx.ellipse(x + baseSize * 0.1, y - baseSize * 2, baseSize * 0.05, baseSize * 0.03, 0, 0, Math.PI * 2);
  ctx.fill();

  // Mouth
  ctx.beginPath();
  ctx.arc(x, y - baseSize * 1.85, baseSize * 0.1, 0.1, Math.PI - 0.1, false);
  ctx.stroke();

  // Lifeguard text
  if (showLabels.value) {
    ctx.font = "bold 12px Arial";
    ctx.fillStyle = "#000000";
    ctx.textAlign = "center";
    ctx.fillText("Lifeguard", x, y - baseSize * 1.4);
    ctx.textAlign = "start";
  }
};

const drawWalkingPerson = (ctx, width, height, time, colors) => {
  const baseSize = 18;
  const cycleTime = 15; // Total seconds for the full animation cycle
  let animationPhase = (time % cycleTime) / cycleTime;

  // Calculate position based on animation phase
  let x, y, rotation = 0, isInWater = false, isFalling = false;

  // Walking phase (0-0.6)
  if (animationPhase < 0.6) {
    const walkProgress = animationPhase / 0.6;
    x = width * (0.2 + walkProgress * 0.3); // Walk from 0.2 to 0.5 of width
    y = height * 0.29; // Just above the pool edge

    // Improved walking animation - use more natural gait
    const walkCycle = time * 2.5; // Slightly slow down walking speed

    // Leg swing - alternate left and right legs
    const leftLegSwing = Math.sin(walkCycle) * baseSize * 0.25;
    const rightLegSwing = Math.sin(walkCycle + Math.PI) * baseSize * 0.25;

    // Arm swing - coordinated with opposite leg (right arm with left leg)
    const leftArmSwing = Math.sin(walkCycle + Math.PI) * baseSize * 0.2;
    const rightArmSwing = Math.sin(walkCycle) * baseSize * 0.2;

    // Slight body bounce to simulate walking motion
    const bodyBounce = Math.abs(Math.sin(walkCycle * 2)) * baseSize * 0.05;

    // Save current state
    ctx.save();
    ctx.translate(x, y - bodyBounce); // Apply body bounce

    // Draw legs
    ctx.strokeStyle = colors.skin;
    ctx.lineWidth = baseSize * 0.25;

    // Left leg
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(-baseSize * 0.3 + leftLegSwing, baseSize * 0.8);
    ctx.stroke();

    // Right leg
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(baseSize * 0.3 + rightLegSwing, baseSize * 0.8);
    ctx.stroke();

    // Draw body
    ctx.fillStyle = "#3F51B5"; // Clothes color
    ctx.beginPath();
    ctx.ellipse(0, -baseSize * 0.3, baseSize * 0.4, baseSize * 0.3, 0, 0, Math.PI * 2);
    ctx.fill();

    // Draw head
    ctx.fillStyle = colors.skin;
    ctx.beginPath();
    ctx.arc(0, -baseSize * 0.7, baseSize * 0.35, 0, Math.PI * 2);
    ctx.fill();

    // Draw hair
    ctx.fillStyle = colors.hair;
    ctx.beginPath();
    ctx.arc(0, -baseSize * 0.85, baseSize * 0.35, Math.PI, 0);
    ctx.fill();

    // Draw arms
    ctx.strokeStyle = colors.skin;
    ctx.lineWidth = baseSize * 0.2;

    // Left arm
    ctx.beginPath();
    ctx.moveTo(-baseSize * 0.4, -baseSize * 0.3);
    ctx.lineTo(-baseSize * 0.7 + leftArmSwing, -baseSize * 0.1);
    ctx.stroke();

    // Right arm
    ctx.beginPath();
    ctx.moveTo(baseSize * 0.4, -baseSize * 0.3);
    ctx.lineTo(baseSize * 0.7 + rightArmSwing, -baseSize * 0.1);
    ctx.stroke();

    // Draw face
    ctx.fillStyle = "#000";

    // Eyes
    ctx.beginPath();
    ctx.ellipse(-baseSize * 0.1, -baseSize * 0.7, baseSize * 0.05, baseSize * 0.03, 0, 0, Math.PI * 2);
    ctx.fill();

    ctx.beginPath();
    ctx.ellipse(baseSize * 0.1, -baseSize * 0.7, baseSize * 0.05, baseSize * 0.03, 0, 0, Math.PI * 2);
    ctx.fill();

    // Mouth - normal expression
    ctx.beginPath();
    ctx.arc(0, -baseSize * 0.55, baseSize * 0.1, 0.1, Math.PI - 0.1, false);
    ctx.stroke();

    // Restore state
    ctx.restore();
  }
  // Slipping/falling phase (0.6-0.7)
  else if (animationPhase < 0.7) {
    const fallProgress = (animationPhase - 0.6) / 0.1;
    x = width * 0.5; // Position where person falls
    y = height * (0.29 + fallProgress * 0.1); // Start falling
    rotation = (fallProgress * Math.PI) / 4; // Rotate as falling
    isFalling = true;

    // Draw person falling
    drawPerson(ctx, x, y, baseSize, 0, 0, rotation, colors, false, true);

    // Draw "slip" effect
    ctx.strokeStyle = "rgba(255, 255, 255, 0.7)";
    ctx.lineWidth = 2;
    ctx.beginPath();
    for (let i = 0; i < 5; i++) {
      const slipX = x - baseSize * 0.5 + Math.random() * baseSize;
      const slipY = y - baseSize * 0.5 + Math.random() * baseSize;
      ctx.moveTo(slipX, slipY);
      ctx.lineTo(slipX + 5, slipY + 5);
    }
    ctx.stroke();
  }
  // Splash phase (0.7-0.8)
  else if (animationPhase < 0.8) {
    x = width * 0.5;
    y = height * 0.45; // In water
    isInWater = true;

    // Draw big splash
    const splashSize = baseSize * 2;
    for (let i = 0; i < 12; i++) {
      const angle = (i / 12) * Math.PI * 2;
      const splashX = x + Math.cos(angle) * splashSize * Math.random();
      const splashY = y + Math.sin(angle) * splashSize * Math.random() * 0.5;
      const dropSize = Math.random() * baseSize * 0.3 + baseSize * 0.1;

      ctx.fillStyle = "rgba(255, 255, 255, 0.8)";
      ctx.beginPath();
      ctx.arc(splashX, splashY, dropSize, 0, Math.PI * 2);
      ctx.fill();
    }

    // Draw person in water (partially submerged)
    drawPerson(ctx, x, y, baseSize, 0, 0, 0, colors, true, false);
  }
  // Swimming/struggling phase (0.8-1.0)
  else {
    x = width * 0.5; // Keep at the same position where they fell
    y = height * 0.45;
    isInWater = true;

    // Random arm movements for struggling
    const struggleIntensity = Math.sin(time * 10) * baseSize * 0.4;

    // Draw smaller splashes around
    for (let i = 0; i < 5; i++) {
      const splashX = x + (Math.random() - 0.5) * baseSize * 2;
      const splashY = y + (Math.random() - 0.5) * baseSize;
      const dropSize = Math.random() * baseSize * 0.15 + baseSize * 0.05;

      ctx.fillStyle = "rgba(255, 255, 255, 0.6)";
      ctx.beginPath();
      ctx.arc(splashX, splashY, dropSize, 0, Math.PI * 2);
      ctx.fill();
    }

    // Draw person struggling in water
    drawPerson(ctx, x, y, baseSize, struggleIntensity, struggleIntensity, 0, colors, true, false);
  }

  // Draw attention mark if falling or in water
  if (isFalling || isInWater) {
    ctx.fillStyle = "#FF5252";
    ctx.beginPath();
    ctx.moveTo(x, y - baseSize * 2);
    ctx.lineTo(x + baseSize * 0.5, y - baseSize * 2.5);
    ctx.lineTo(x - baseSize * 0.5, y - baseSize * 2.5);
    ctx.closePath();
    ctx.fill();

    ctx.font = "bold 16px Arial";
    ctx.fillStyle = "#FFFFFF";
    ctx.textAlign = "center";
    ctx.fillText("!", x, y - baseSize * 2.3);
  }
};

const drawRescueAnimation = (ctx, width, height, time, colors, type) => {
  // Child in water position (same as the fallen person)
  let childX = width * 0.5;
  let childY = height * 0.45;
  const baseSize = 18;

  // Animation phase (0-1)
  const animationPhase = Math.min(time / 8, 1); // 8 seconds total animation

  // Flag to indicate if animation is completed
  let isCompleted = false;

  // Check if animation is completed
  if (animationPhase >= 1) {
    isCompleted = true;
  }

  if (type === "A") {
    // Option A: Person jumps in but fails to rescue
    const rescuerBaseSize = 20;

    // Draw the child struggling in water (only if not rescued)
    const struggleIntensity = Math.sin(time * 10) * baseSize * 0.4;

    // Draw smaller splashes around child
    for (let i = 0; i < 5; i++) {
      const splashX = childX + (Math.random() - 0.5) * baseSize * 2;
      const splashY = childY + (Math.random() - 0.5) * baseSize;
      const dropSize = Math.random() * baseSize * 0.15 + baseSize * 0.05;

      ctx.fillStyle = "rgba(255, 255, 255, 0.6)";
      ctx.beginPath();
      ctx.arc(splashX, splashY, dropSize, 0, Math.PI * 2);
      ctx.fill();
    }

    // Draw child struggling in water
    drawPerson(ctx, childX, childY, baseSize, struggleIntensity, struggleIntensity, 0, colors, true, false);

    // Draw attention mark above child
    ctx.fillStyle = "#FF5252";
    ctx.beginPath();
    ctx.moveTo(childX, childY - baseSize * 2);
    ctx.lineTo(childX + baseSize * 0.5, childY - baseSize * 2.5);
    ctx.lineTo(childX - baseSize * 0.5, childY - baseSize * 2.5);
    ctx.closePath();
    ctx.fill();

    ctx.font = "bold 16px Arial";
    ctx.fillStyle = "#FFFFFF";
    ctx.textAlign = "center";
    ctx.fillText("!", childX, childY - baseSize * 2.3);

    // Calculate rescuer position
    let rescuerX, rescuerY, rescuerRotation = 0;
    let isInWater = false;
    let showSpeechBubble = false;

    // Starting position on the edge
    const startX = width * 0.3;
    const startY = height * 0.29;

    // Jumping phase (0-0.2)
    if (animationPhase < 0.2) {
      const jumpProgress = animationPhase / 0.2;
      rescuerX = startX + (childX - startX) * jumpProgress * 0.7;
      rescuerY = startY - Math.sin(jumpProgress * Math.PI) * height * 0.1; // Arc jump
      rescuerRotation = jumpProgress * Math.PI * 0.5; // Rotate during jump
    }
    // Splash phase (0.2-0.3)
    else if (animationPhase < 0.3) {
      rescuerX = startX + (childX - startX) * 0.7;
      rescuerY = height * 0.4;
      isInWater = true;

      // Draw splash
      const splashSize = rescuerBaseSize * 2;
      for (let i = 0; i < 12; i++) {
        const angle = (i / 12) * Math.PI * 2;
        const splashX = rescuerX + Math.cos(angle) * splashSize * Math.random();
        const splashY = rescuerY + Math.sin(angle) * splashSize * Math.random() * 0.5;
        const dropSize = Math.random() * rescuerBaseSize * 0.3 + rescuerBaseSize * 0.1;

        ctx.fillStyle = "rgba(255, 255, 255, 0.8)";
        ctx.beginPath();
        ctx.arc(splashX, splashY, dropSize, 0, Math.PI * 2);
        ctx.fill();
      }
    }
    // Swimming toward child (0.3-0.6)
    else if (animationPhase < 0.6) {
      const swimProgress = (animationPhase - 0.3) / 0.3;
      rescuerX = startX + (childX - startX) * (0.7 + swimProgress * 0.2);
      rescuerY = height * 0.45;
      isInWater = true;

      // Draw water splashes
      for (let i = 0; i < 3; i++) {
        const splashX = rescuerX - rescuerBaseSize * 0.5 + Math.random() * rescuerBaseSize;
        const splashY = rescuerY - rescuerBaseSize * 0.2 + Math.random() * rescuerBaseSize * 0.4;
        const splashSize = Math.random() * rescuerBaseSize * 0.15 + rescuerBaseSize * 0.05;

        ctx.fillStyle = "rgba(255, 255, 255, 0.6)";
        ctx.beginPath();
        ctx.arc(splashX, splashY, splashSize, 0, Math.PI * 2);
        ctx.fill();
      }
    }
    // Struggling and calling for help (0.6-1.0)
    else {
      rescuerX = startX + (childX - startX) * 0.9; // Close but not reaching child
      rescuerY = height * 0.45;
      isInWater = true;
      showSpeechBubble = true;

      // Draw smaller splashes around rescuer
      for (let i = 0; i < 5; i++) {
        const splashX = rescuerX + (Math.random() - 0.5) * rescuerBaseSize * 2;
        const splashY = rescuerY + (Math.random() - 0.5) * rescuerBaseSize;
        const dropSize = Math.random() * rescuerBaseSize * 0.15 + rescuerBaseSize * 0.05;

        ctx.fillStyle = "rgba(255, 255, 255, 0.6)";
        ctx.beginPath();
        ctx.arc(splashX, splashY, dropSize, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    // Draw the rescuer
    if (isInWater) {
      // Draw rescuer in water
      drawPerson(
        ctx,
        rescuerX,
        rescuerY,
        rescuerBaseSize,
        animationPhase > 0.6 ? Math.sin(time * 8) * rescuerBaseSize * 0.4 : 0,
        animationPhase > 0.6 ? Math.sin(time * 8) * rescuerBaseSize * 0.4 : 0,
        0,
        colors,
        true,
        false
      );
    } else {
      // Draw rescuer jumping
      drawPerson(ctx, rescuerX, rescuerY, rescuerBaseSize, 0, 0, rescuerRotation, colors, false, false);
    }

    // Draw speech bubble for help
    if (showSpeechBubble) {
      ctx.fillStyle = "white";
      ctx.beginPath();
      ctx.ellipse(
        rescuerX + rescuerBaseSize * 1.2,
        rescuerY - rescuerBaseSize * 1.2,
        rescuerBaseSize * 1.0, // Increased width
        rescuerBaseSize * 0.6, // Increased height
        0,
        0,
        Math.PI * 2
      );
      ctx.fill();

      // Speech bubble pointer
      ctx.beginPath();
      ctx.moveTo(rescuerX + rescuerBaseSize * 0.5, rescuerY - rescuerBaseSize * 0.8);
      ctx.lineTo(rescuerX + rescuerBaseSize * 0.8, rescuerY - rescuerBaseSize * 1);
      ctx.lineTo(rescuerX + rescuerBaseSize * 0.7, rescuerY - rescuerBaseSize * 0.7);
      ctx.closePath();
      ctx.fill();

      // Text
      ctx.font = "bold 16px Arial"; // Larger font
      ctx.fillStyle = "#FF0000";
      ctx.textAlign = "center";
      ctx.fillText("Help!", rescuerX + rescuerBaseSize * 1.2, rescuerY - rescuerBaseSize * 1.1);
    }
  } else if (type === "B") {
    // Option B: Person calls emergency services

    // Draw the child struggling in water (only if not rescued)
    const struggleIntensity = Math.sin(time * 10) * baseSize * 0.4;

    // Draw smaller splashes around child
    for (let i = 0; i < 5; i++) {
      const splashX = childX + (Math.random() - 0.5) * baseSize * 2;
      const splashY = childY + (Math.random() - 0.5) * baseSize;
      const dropSize = Math.random() * baseSize * 0.15 + baseSize * 0.05;

      ctx.fillStyle = "rgba(255, 255, 255, 0.6)";
      ctx.beginPath();
      ctx.arc(splashX, splashY, dropSize, 0, Math.PI * 2);
      ctx.fill();
    }

    // Draw child struggling in water
    drawPerson(ctx, childX, childY, baseSize, struggleIntensity, struggleIntensity, 0, colors, true, false);

    // Draw attention mark above child
    ctx.fillStyle = "#FF5252";
    ctx.beginPath();
    ctx.moveTo(childX, childY - baseSize * 2);
    ctx.lineTo(childX + baseSize * 0.5, childY - baseSize * 2.5);
    ctx.lineTo(childX - baseSize * 0.5, childY - baseSize * 2.5);
    ctx.closePath();
    ctx.fill();

    ctx.font = "bold 16px Arial";
    ctx.fillStyle = "#FFFFFF";
    ctx.textAlign = "center";
    ctx.fillText("!", childX, childY - baseSize * 2.3);

    const callerBaseSize = 20;
    const callerX = width * 0.25;
    const callerY = height * 0.29; // On the edge

    // Calculate animation phase
    let showPhone = false;
    let showSpeechBubble = false;

    // Appear and look concerned (0-0.3)
    if (animationPhase < 0.3) {
      // Just draw the person looking concerned
    }
    // Take out phone (0.3-0.5)
    else if (animationPhase < 0.5) {
      showPhone = true;
    }
    // Talk on phone (0.5-1.0)
    else {
      showPhone = true;
      showSpeechBubble = true;
    }

    // Draw the caller
    drawPerson(ctx, callerX, callerY, callerBaseSize, 0, 0, 0, colors, false, false);

    // Draw phone
    if (showPhone) {
      ctx.fillStyle = "#333333";
      ctx.fillRect(
        callerX + callerBaseSize * 0.5,
        callerY - callerBaseSize * 0.5,
        callerBaseSize * 0.3,
        callerBaseSize * 0.5
      );
    }

    // Draw speech bubble
    if (showSpeechBubble) {
      ctx.fillStyle = "white";
      ctx.beginPath();
      ctx.ellipse(
        callerX + callerBaseSize * 1.2,
        callerY - callerBaseSize * 1.2,
        callerBaseSize * 1.5, // Increased width
        callerBaseSize * 0.9, // Increased height
        0,
        0,
        Math.PI * 2
      );
      ctx.fill();

      // Speech bubble pointer
      ctx.beginPath();
      ctx.moveTo(callerX + callerBaseSize * 0.5, callerY - callerBaseSize * 0.8);
      ctx.lineTo(callerX + callerBaseSize * 0.8, callerY - callerBaseSize * 1);
      ctx.lineTo(callerX + callerBaseSize * 0.7, callerY - callerBaseSize * 0.7);
      ctx.closePath();
      ctx.fill();

      // Text with increased spacing
      ctx.font = "bold 13px Arial"; // Slightly larger font
      ctx.fillStyle = "#000";
      ctx.textAlign = "center";
      ctx.fillText("Someone fell in!", callerX + callerBaseSize * 1.2, callerY - callerBaseSize * 1.3); // Moved up
      ctx.fillText("Send help!", callerX + callerBaseSize * 1.2, callerY - callerBaseSize * 0.9); // More space between lines
    }
  } else if (type === "C") {
    // Option C: Person shouts for help, lifeguard rescues
    const shouterBaseSize = 20;
    const shouterX = width * 0.25;
    const shouterY = height * 0.29; // On the edge

    const lifeguardStartX = width * 0.85;
    const lifeguardStartY = height * 0.25;
    const lifeguardBaseSize = 20;

    // Shore position for returning
    const shoreX = width * 0.25;
    const shoreY = height * 0.29;

    // Calculate animation phases
    let showSpeechBubble = false;
    let lifeguardX = lifeguardStartX;
    let lifeguardY = lifeguardStartY;
    let lifeguardInWater = false;
    let lifeguardWithChild = false;

    // Draw the child struggling in water (only if not rescued yet)
    if (animationPhase < 0.6) {
      const struggleIntensity = Math.sin(time * 10) * baseSize * 0.4;

      // Draw smaller splashes around child
      for (let i = 0; i < 5; i++) {
        const splashX = childX + (Math.random() - 0.5) * baseSize * 2;
        const splashY = childY + (Math.random() - 0.5) * baseSize;
        const dropSize = Math.random() * baseSize * 0.15 + baseSize * 0.05;

        ctx.fillStyle = "rgba(255, 255, 255, 0.6)";
        ctx.beginPath();
        ctx.arc(splashX, splashY, dropSize, 0, Math.PI * 2);
        ctx.fill();
      }

      // Draw child struggling in water
      drawPerson(ctx, childX, childY, baseSize, struggleIntensity, struggleIntensity, 0, colors, true, false);

      // Draw attention mark above child
      ctx.fillStyle = "#FF5252";
      ctx.beginPath();
      ctx.moveTo(childX, childY - baseSize * 2);
      ctx.lineTo(childX + baseSize * 0.5, childY - baseSize * 2.5);
      ctx.lineTo(childX - baseSize * 0.5, childY - baseSize * 2.5);
      ctx.closePath();
      ctx.fill();

      ctx.font = "bold 16px Arial";
      ctx.fillStyle = "#FFFFFF";
      ctx.textAlign = "center";
      ctx.fillText("!", childX, childY - baseSize * 2.3);
    }

    // Person appears and shouts (0-0.15)
    if (animationPhase < 0.15) {
      showSpeechBubble = true;
    }
    // Lifeguard notices and jumps off chair (0.15-0.3)
    else if (animationPhase < 0.3) {
      showSpeechBubble = true;
      const jumpProgress = (animationPhase - 0.15) / 0.15;
      lifeguardX = lifeguardStartX - jumpProgress * width * 0.1;
      lifeguardY = lifeguardStartY + jumpProgress * height * 0.1;
    }
    // Lifeguard runs to pool edge (0.3-0.45)
    else if (animationPhase < 0.45) {
      const runProgress = (animationPhase - 0.3) / 0.15;
      lifeguardX = lifeguardStartX - width * 0.1 - runProgress * (lifeguardStartX - childX - width * 0.1);
      lifeguardY = lifeguardStartY + height * 0.1;
    }
    // Lifeguard jumps and swims to child (0.45-0.6)
    else if (animationPhase < 0.6) {
      const swimProgress = (animationPhase - 0.45) / 0.15;
      lifeguardX =
        lifeguardStartX -
        width * 0.1 -
        (lifeguardStartX - childX - width * 0.1) +
        swimProgress * (childX - (lifeguardStartX - width * 0.1 - (lifeguardStartX - childX - width * 0.1)));
      lifeguardY = height * 0.45;
      lifeguardInWater = true;

      // Draw splash
      if (swimProgress < 0.2) {
        const splashSize = lifeguardBaseSize * 2;
        for (let i = 0; i < 12; i++) {
          const angle = (i / 12) * Math.PI * 2;
          const splashX = lifeguardX + Math.cos(angle) * splashSize * Math.random();
          const splashY = lifeguardY + Math.sin(angle) * splashSize * Math.random() * 0.5;
          const dropSize = Math.random() * lifeguardBaseSize * 0.3 + lifeguardBaseSize * 0.1;

          ctx.fillStyle = "rgba(255, 255, 255, 0.8)";
          ctx.beginPath();
          ctx.arc(splashX, splashY, dropSize, 0, Math.PI * 2);
          ctx.fill();
        }
      }

      // Draw water splashes
      for (let i = 0; i < 3; i++) {
        const splashX = lifeguardX - lifeguardBaseSize * 0.5 + Math.random() * lifeguardBaseSize;
        const splashY = lifeguardY - lifeguardBaseSize * 0.2 + Math.random() * lifeguardBaseSize * 0.4;
        const splashSize = Math.random() * lifeguardBaseSize * 0.15 + lifeguardBaseSize * 0.05;

        ctx.fillStyle = "rgba(255, 255, 255, 0.6)";
        ctx.beginPath();
        ctx.arc(splashX, splashY, splashSize, 0, Math.PI * 2);
        ctx.fill();
      }
    }
    // Lifeguard rescues child (0.6-0.75)
    else if (animationPhase < 0.75) {
      lifeguardX = childX;
      lifeguardY = height * 0.45;
      lifeguardInWater = true;
      lifeguardWithChild = true;

      // Draw smaller splashes around
      for (let i = 0; i < 5; i++) {
        const splashX = lifeguardX + (Math.random() - 0.5) * lifeguardBaseSize * 2;
        const splashY = lifeguardY + (Math.random() - 0.5) * lifeguardBaseSize;
        const dropSize = Math.random() * lifeguardBaseSize * 0.15 + lifeguardBaseSize * 0.05;

        ctx.fillStyle = "rgba(255, 255, 255, 0.6)";
        ctx.beginPath();
        ctx.arc(splashX, splashY, dropSize, 0, Math.PI * 2);
        ctx.fill();
      }
    }
    // Lifeguard returns to shore with child (0.75-1.0)
    else {
      lifeguardWithChild = true;
      lifeguardInWater = true;

      // Calculate position moving back to shore
      const returnProgress = (animationPhase - 0.75) / 0.25;
      lifeguardX = childX + returnProgress * (shoreX - childX);

      // Gradually move up to shore level
      if (returnProgress > 0.8) {
        // Almost at shore, start moving up
        const exitProgress = (returnProgress - 0.8) / 0.2;
        lifeguardY = height * 0.45 - exitProgress * (height * 0.45 - shoreY);
        lifeguardInWater = returnProgress < 0.9; // Out of water in the last bit
      } else {
        lifeguardY = height * 0.45;
      }

      // Draw water splashes while swimming
      if (lifeguardInWater) {
        for (let i = 0; i < 3; i++) {
          const splashX = lifeguardX - lifeguardBaseSize * 0.5 + Math.random() * lifeguardBaseSize;
          const splashY = lifeguardY - lifeguardBaseSize * 0.2 + Math.random() * lifeguardBaseSize * 0.4;
          const splashSize = Math.random() * lifeguardBaseSize * 0.15 + lifeguardBaseSize * 0.05;

          ctx.fillStyle = "rgba(255, 255, 255, 0.6)";
          ctx.beginPath();
          ctx.arc(splashX, splashY, splashSize, 0, Math.PI * 2);
          ctx.fill();
        }
      }

      // Draw "safe" indicator when reaching shore
      if (returnProgress > 0.9) {
        ctx.fillStyle = "#4CAF50";
        ctx.beginPath();
        ctx.arc(
          lifeguardX + lifeguardBaseSize * 1.2,
          lifeguardY - lifeguardBaseSize * 0.5,
          lifeguardBaseSize * 0.3,
          0,
          Math.PI * 2
        );
        ctx.fill();

        ctx.font = "bold 16px Arial";
        ctx.fillStyle = "#FFFFFF";
        ctx.textAlign = "center";
        ctx.fillText("✓", lifeguardX + lifeguardBaseSize * 1.2, lifeguardY - lifeguardBaseSize * 0.4);
      }
    }

    // Draw the shouter
    drawPerson(ctx, shouterX, shouterY, shouterBaseSize, 0, 0, 0, colors, false, false);

    // Draw speech bubble
    if (showSpeechBubble) {
      ctx.fillStyle = "white";
      ctx.beginPath();
      ctx.ellipse(
        shouterX + shouterBaseSize * 1.2,
        shouterY - shouterBaseSize * 1.2,
        shouterBaseSize * 1.0, // Increased width
        shouterBaseSize * 0.6, // Increased height
        0,
        0,
        Math.PI * 2
      );
      ctx.fill();

      // Speech bubble pointer
      ctx.beginPath();
      ctx.moveTo(shouterX + shouterBaseSize * 0.5, shouterY - shouterBaseSize * 0.8);
      ctx.lineTo(shouterX + shouterBaseSize * 0.8, shouterY - shouterBaseSize * 1);
      ctx.lineTo(shouterX + shouterBaseSize * 0.7, shouterY - shouterBaseSize * 0.7);
      ctx.closePath();
      ctx.fill();

      // Text
      ctx.font = "bold 16px Arial"; // Larger font
      ctx.fillStyle = "#FF0000";
      ctx.textAlign = "center";
      ctx.fillText("Help!", shouterX + shouterBaseSize * 1.2, shouterY - shouterBaseSize * 1.1);
    }

    // Draw lifeguard
    if (!lifeguardInWater) {
      // Draw lifeguard running/jumping
      ctx.fillStyle = "#FFD54F"; // Lifeguard uniform
      ctx.fillRect(
        lifeguardX - lifeguardBaseSize * 0.4,
        lifeguardY - lifeguardBaseSize * 0.8,
        lifeguardBaseSize * 0.8,
        lifeguardBaseSize * 0.8
      );

      // Head
      ctx.fillStyle = colors.skin;
      ctx.beginPath();
      ctx.arc(lifeguardX, lifeguardY - lifeguardBaseSize, lifeguardBaseSize * 0.4, 0, Math.PI * 2);
      ctx.fill();

      // Arms and legs with running motion
      const runCycle = time * 5;
      const legSwing = Math.sin(runCycle) * lifeguardBaseSize * 0.3;
      const armSwing = Math.cos(runCycle) * lifeguardBaseSize * 0.3;

      ctx.strokeStyle = colors.skin;
      ctx.lineWidth = lifeguardBaseSize * 0.2;

      // Arms
      ctx.beginPath();
      ctx.moveTo(lifeguardX - lifeguardBaseSize * 0.4, lifeguardY - lifeguardBaseSize * 0.5);
      ctx.lineTo(lifeguardX - lifeguardBaseSize * 0.7 - armSwing, lifeguardY - lifeguardBaseSize * 0.3);
      ctx.stroke();

      ctx.beginPath();
      ctx.moveTo(lifeguardX + lifeguardBaseSize * 0.4, lifeguardY - lifeguardBaseSize * 0.5);
      ctx.lineTo(lifeguardX + lifeguardBaseSize * 0.7 - armSwing, lifeguardY - lifeguardBaseSize * 0.3);
      ctx.stroke();

      // Legs
      ctx.lineWidth = lifeguardBaseSize * 0.25;

      ctx.beginPath();
      ctx.moveTo(lifeguardX - lifeguardBaseSize * 0.2, lifeguardY);
      ctx.lineTo(lifeguardX - lifeguardBaseSize * 0.3 - legSwing, lifeguardY + lifeguardBaseSize * 0.5);
      ctx.stroke();

      ctx.beginPath();
      ctx.moveTo(lifeguardX + lifeguardBaseSize * 0.2, lifeguardY);
      ctx.lineTo(lifeguardX + lifeguardBaseSize * 0.3 - legSwing, lifeguardY + lifeguardBaseSize * 0.5);
      ctx.stroke();
    } else {
      // Draw lifeguard swimming/rescuing
      if (lifeguardWithChild) {
        // Don't draw the child separately anymore
        // Draw lifeguard holding child
        ctx.fillStyle = "#FFD54F"; // Lifeguard uniform
        ctx.fillRect(
          lifeguardX - lifeguardBaseSize * 0.4,
          lifeguardY - lifeguardBaseSize * 0.3,
          lifeguardBaseSize * 0.8,
          lifeguardBaseSize * 0.6
        );

        // Head
        ctx.fillStyle = colors.skin;
        ctx.beginPath();
        ctx.arc(lifeguardX, lifeguardY - lifeguardBaseSize * 0.7, lifeguardBaseSize * 0.4, 0, Math.PI * 2);
        ctx.fill();

        // Child (smaller, being held)
        ctx.fillStyle = "#3F51B5"; // Child's clothes
        ctx.fillRect(
          lifeguardX - lifeguardBaseSize * 0.3,
          lifeguardY - lifeguardBaseSize * 0.1,
          lifeguardBaseSize * 0.6,
          lifeguardBaseSize * 0.4
        );

        // Child's head
        ctx.fillStyle = colors.skin;
        ctx.beginPath();
        ctx.arc(lifeguardX, lifeguardY - lifeguardBaseSize * 0.3, lifeguardBaseSize * 0.25, 0, Math.PI * 2);
        ctx.fill();
      } else {
        // Draw lifeguard swimming
        const swimCycle = time * 4;
        const legKick = Math.sin(swimCycle) * lifeguardBaseSize * 0.3;
        const armStroke = Math.cos(swimCycle) * lifeguardBaseSize * 0.3;

        ctx.fillStyle = "#FFD54F"; // Lifeguard uniform
        ctx.fillRect(
          lifeguardX - lifeguardBaseSize * 0.4,
          lifeguardY - lifeguardBaseSize * 0.3,
          lifeguardBaseSize * 0.8,
          lifeguardBaseSize * 0.6
        );

        // Head
        ctx.fillStyle = colors.skin;
        ctx.beginPath();
        ctx.arc(lifeguardX, lifeguardY - lifeguardBaseSize * 0.7, lifeguardBaseSize * 0.4, 0, Math.PI * 2);
        ctx.fill();

        // Arms with swimming motion
        ctx.strokeStyle = colors.skin;
        ctx.lineWidth = lifeguardBaseSize * 0.2;

        ctx.beginPath();
        ctx.moveTo(lifeguardX - lifeguardBaseSize * 0.4, lifeguardY - lifeguardBaseSize * 0.3);
        ctx.lineTo(lifeguardX - lifeguardBaseSize * 0.8 - armStroke, lifeguardY - lifeguardBaseSize * 0.1);
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(lifeguardX + lifeguardBaseSize * 0.4, lifeguardY - lifeguardBaseSize * 0.3);
        ctx.lineTo(lifeguardX + lifeguardBaseSize * 0.8 + armStroke, lifeguardY - lifeguardBaseSize * 0.1);
        ctx.stroke();

        // Legs with kicking motion
        ctx.lineWidth = lifeguardBaseSize * 0.25;

        ctx.beginPath();
        ctx.moveTo(lifeguardX, lifeguardY + lifeguardBaseSize * 0.3);
        ctx.lineTo(lifeguardX - lifeguardBaseSize * 0.5 - legKick, lifeguardY + lifeguardBaseSize * 0.8);
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(lifeguardX, lifeguardY + lifeguardBaseSize * 0.3);
        ctx.lineTo(lifeguardX + lifeguardBaseSize * 0.5 + legKick, lifeguardY + lifeguardBaseSize * 0.8);
        ctx.stroke();
      }
    }
  } else if (type === "timeout") {
    // Child drowning animation
    const childX = width * 0.5;
    const childY = height * 0.45;
    const childBaseSize = 18;

    // Calculate animation phase
    const drowningPhase = animationPhase;

    // Struggling and sinking animation
    if (drowningPhase < 0.5) {
      // Intense struggling
      const struggleIntensity = Math.sin(time * 15) * childBaseSize * 0.5;

      // Draw more intense splashes
      for (let i = 0; i < 8; i++) {
        const splashX = childX + (Math.random() - 0.5) * childBaseSize * 3;
        const splashY = childY + (Math.random() - 0.5) * childBaseSize * 1.5;
        const dropSize = Math.random() * childBaseSize * 0.2 + childBaseSize * 0.1;

        ctx.fillStyle = "rgba(255, 255, 255, 0.7)";
        ctx.beginPath();
        ctx.arc(splashX, splashY, dropSize, 0, Math.PI * 2);
        ctx.fill();
      }

      // Draw child struggling more intensely
      drawPerson(ctx, childX, childY, childBaseSize, struggleIntensity, struggleIntensity, 0, colors, true, false);

      // Draw danger indicator
      ctx.fillStyle = "#FF0000";
      ctx.beginPath();
      ctx.arc(childX + childBaseSize * 1.5, childY - childBaseSize, childBaseSize * 0.4, 0, Math.PI * 2);
      ctx.fill();

      ctx.font = "bold 16px Arial";
      ctx.fillStyle = "#FFFFFF";
      ctx.textAlign = "center";
      ctx.fillText("!", childX + childBaseSize * 1.5, childY - childBaseSize * 0.9);
    }
    // Sinking phase
    else {
      const sinkProgress = (drowningPhase - 0.5) / 0.5;
      const sinkY = childY + sinkProgress * childBaseSize * 1.5;

      // Fewer, smaller bubbles as child sinks
      for (let i = 0; i < 5; i++) {
        const bubbleX = childX + (Math.random() - 0.5) * childBaseSize * 2;
        const bubbleY = sinkY - childBaseSize + Math.random() * childBaseSize * 2;
        const bubbleSize = Math.random() * childBaseSize * 0.15 + childBaseSize * 0.05;

        ctx.fillStyle = "rgba(255, 255, 255, 0.5)";
        ctx.beginPath();
        ctx.arc(bubbleX, bubbleY, bubbleSize, 0, Math.PI * 2);
        ctx.fill();
      }

      // Draw child sinking
      ctx.globalAlpha = Math.max(0, 1 - sinkProgress * 0.8); // Fade out as sinking
      drawPerson(ctx, childX, sinkY, childBaseSize, 0, 0, 0, colors, true, false);
      ctx.globalAlpha = 1.0;

      // Draw danger indicator
      ctx.fillStyle = "#FF0000";
      ctx.beginPath();
      ctx.arc(childX + childBaseSize * 1.5, childY - childBaseSize, childBaseSize * 0.4, 0, Math.PI * 2);
      ctx.fill();

      ctx.font = "bold 16px Arial";
      ctx.fillStyle = "#FFFFFF";
      ctx.textAlign = "center";
      ctx.fillText("!", childX + childBaseSize * 1.5, childY - childBaseSize * 0.9);
    }
  }

  return isCompleted;
};

// Draw the simulation
const drawSimulation = (time) => {
  const canvas = canvasRef.value;
  if (!canvas) return;

  const ctx = canvas.getContext("2d");
  if (!ctx) return;

  const width = canvas.width;
  const height = canvas.height;

  // Clear canvas
  ctx.clearRect(0, 0, width, height);

  // Set up time variables
  const animTime = time / 1000; // Convert to seconds
  animationTimeRef.value = animTime;

  // Enhanced color palette
  const colors = {
    // Background colors
    background: "#F5F5F5",
    poolDeck: "#E0E0E0",
    poolDeckLines: "#CCCCCC",

    // Water colors
    waterLight: "#81D4FA",
    waterMedium: "#4FC3F7",
    waterDeep: "#29B6F6",

    // Pool colors
    poolEdge: "#BBDEFB",
    poolLane: "#FFFFFF",
    poolBottom: "#B3E5FC",

    // Character colors
    skin: "#FFD0A9",
    hair: "#8B4513",
    swimsuit: "#FF5252",
  };

  // Draw background
  ctx.fillStyle = colors.background;
  ctx.fillRect(0, 0, width, height);

  // Draw pool deck
  ctx.fillStyle = colors.poolDeck;
  ctx.fillRect(0, height * 0.2, width, height * 0.8);

  // Add pool deck texture
  for (let i = 0; i < 20; i++) {
    const y = height * 0.2 + (i / 20) * (height * 0.8);
    ctx.strokeStyle = colors.poolDeckLines;
    ctx.lineWidth = 0.5;
    ctx.beginPath();
    ctx.moveTo(0, y);
    ctx.lineTo(width, y);
    ctx.stroke();
  }

  for (let i = 0; i < 20; i++) {
    const x = (i / 20) * width;
    ctx.strokeStyle = colors.poolDeckLines;
    ctx.lineWidth = 0.5;
    ctx.beginPath();
    ctx.moveTo(x, height * 0.2);
    ctx.lineTo(x, height);
    ctx.stroke();
  }

  // Draw leisure pool
  drawLeisurePool(ctx, width, height, animTime, colors);

  // Draw single swimmer
  const swimX = width * 0.4;
  const swimY = height * 0.45;
  drawSwimmer(ctx, swimX, swimY, animTime, colors);

  // Draw lifeguard
  drawLifeguard(ctx, width * 0.85, height * 0.25, animTime, colors);

  // Check if we're playing a rescue animation
  if (playingRescueAnimation.value) {
    const animationCompleted = drawRescueAnimation(
      ctx,
      width,
      height,
      rescueAnimationTime.value,
      colors,
      rescueAnimationType.value
    );

    // Check if animation is completed
    if (animationCompleted && !rescueAnimationCompleted.value) {
      rescueAnimationCompleted.value = true;
    }
  } else {
    // Draw person walking and falling
    const cycleTime = 15; // Total seconds for the full animation cycle
    const animationPhase = (animTime % cycleTime) / cycleTime;

    // Check if we've completed a cycle and should show the quiz
    if (animationPhase < (lastCycleTimeRef.value % cycleTime) / cycleTime) {
      // We've wrapped around to a new cycle
      if (!showQuiz.value && !showFeedback.value && !playingRescueAnimation.value) {
        showQuiz.value = true;
        timeLeft.value = 10;
        paused.value = true;
      }
    }
    lastCycleTimeRef.value = animTime;

    drawWalkingPerson(ctx, width, height, animTime, colors);
  }

  // Draw letterbox effect at bottom
  const letterboxHeight = height * 0.05;
  ctx.fillStyle = "#000";
  ctx.fillRect(0, height - letterboxHeight, width, letterboxHeight);
};

// Resize canvas to fill container
const resizeCanvas = () => {
  const canvas = canvasRef.value;
  const container = canvasContainerRef.value;
  if (!canvas || !container) return;

  // Get container dimensions
  const width = container.clientWidth;
  const height = container.clientHeight;

  // Set canvas dimensions to match container
  canvas.width = width;
  canvas.height = height;

  // Redraw if animation is not running
  if (!isStarted.value || paused.value) {
    drawSimulation(animationTime);
  }
};

// Animation loop
const startAnimation = () => {
  // If animation frame is already running, cancel it first
  if (animationFrame) {
    cancelAnimationFrame(animationFrame);
    animationFrame = null;
  }

  const animate = () => {
    if (!paused.value && isStarted.value) {
      animationTime += 16; // ~60fps
      if (playingRescueAnimation.value) {
        rescueAnimationTime.value += 0.016; // Increment rescue animation time
      }
    }

    // Always draw once regardless of pause state
    drawSimulation(animationTime);

    // Continue requesting next frame
    animationFrame = requestAnimationFrame(animate);
  };

  animationFrame = requestAnimationFrame(animate);
};

// Initialize
onMounted(() => {
  resizeCanvas();
  window.addEventListener("resize", resizeCanvas);

  // Initial draw
  drawSimulation(0);
});

// Cleanup
onUnmounted(() => {
  window.removeEventListener("resize", resizeCanvas);
  if (animationFrame) {
    cancelAnimationFrame(animationFrame);
  }
});

// Watch for rescue animation completion
watch(rescueAnimationCompleted, (newValue) => {
  if (newValue) {
    // Show feedback after animation completes
    showFeedback.value = true;
  }
});

// Timer for quiz
watch([showQuiz, timeLeft], ([isShowing, time]) => {
  if (isShowing && time > 0 && !selectedOption.value) {
    setTimeout(() => {
      timeLeft.value = time - 1;
    }, 1000);
  } else if (isShowing && time === 0 && !selectedOption.value) {
    // Time's up
    showQuiz.value = false;
    playingRescueAnimation.value = true;
    rescueAnimationType.value = "timeout";
    rescueAnimationTime.value = 0;
    selectedOption.value = "timeout";
    paused.value = false; // Make sure animation plays immediately
  }
});
</script>

<style>
@keyframes fade-in {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-fade-in {
  animation: fade-in 0.3s ease-out forwards;
}

.pool-safety-window {
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
}

.window-container {
  width: 100%;
  height: 100%;
  position: relative;
  overflow: hidden;
}
</style>