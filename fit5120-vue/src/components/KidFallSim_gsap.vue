<template>
  <div class="pool-safety-window" :style="{ width: width + 'px', height: height + 'px' }">
    <div ref="containerRef" class="window-container relative overflow-hidden bg-black text-white font-sans rounded-lg shadow-xl">
      
      <!-- Canvas container with fixed aspect ratio -->
      <div class="relative w-full h-[calc(100%-32px)]">
        <div ref="canvasContainerRef" class="relative w-full h-full" style="aspect-ratio: 2/1;">
          <canvas ref="canvasRef" class="absolute top-0 left-0 w-full h-full"></canvas>
        </div>
      </div>
      
      <!-- Start Button -->
      <div v-if="!isStarted" class="absolute inset-0 flex items-center justify-center bg-black/50 z-[100]">
        <button 
          class="bg-cyan-600 hover:bg-cyan-700 text-white py-2 px-4 rounded-lg text-sm font-bold transition-colors shadow-lg"
          @click="startSimulation"
        >
          Start Simulation
        </button>
      </div>

      <!-- Quiz Popup -->
      <div v-if="showQuiz" class="absolute inset-0 bg-black/80 flex items-center justify-center p-2 z-[200]">
        <div class="bg-gray-900 rounded-lg w-[90%] max-w-[300px] p-4 relative animate-fade-in">
          <div class="absolute top-2 right-2 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center font-bold text-xs">
            {{ timeLeft }}
          </div>

          <h2 class="text-sm font-bold text-cyan-400 mb-4">
            The child has fallen into the pool! What would you do?
          </h2>

          <div class="flex flex-col gap-2">
            <button 
              class="bg-blue-600 hover:bg-blue-700 text-white py-2 px-3 rounded-md text-left transition-colors text-xs"
              @click="handleOptionSelect('A')"
            >
              A. Jump into the water
            </button>

            <button 
              class="bg-blue-600 hover:bg-blue-700 text-white py-2 px-3 rounded-md text-left transition-colors text-xs"
              @click="handleOptionSelect('B')"
            >
              B. Call emergency services
            </button>

            <button 
              class="bg-blue-600 hover:bg-blue-700 text-white py-2 px-3 rounded-md text-left transition-colors text-xs"
              @click="handleOptionSelect('C')"
            >
              C. Use the life ring
            </button>
          </div>
        </div>
      </div>

      <!-- Feedback Popup -->
      <div v-if="showFeedback" class="absolute inset-0 bg-black/80 flex items-center justify-center p-2 z-[200]">
        <div class="bg-gray-900 rounded-lg w-[90%] max-w-[300px] p-4 relative max-h-[80%] overflow-y-auto text-xs">
          <h2 class="text-sm font-bold text-cyan-400 mb-3">Safety Feedback</h2>
          
          <!-- Simplified Feedback -->
          <div class="mb-3 p-3 rounded-md" :class="feedbackColorClass">
            <p :class="feedbackTextClass">
              <span class="font-bold">{{ feedbackTitle }}</span> {{ feedbackMessage }}
            </p>
          </div>

          <div class="mt-4 p-2 bg-blue-900/50 rounded-md">
            <p class="text-blue-200 text-xs">
              <span class="font-bold">Remember:</span> Water rescue sequence: "Reach, Throw, Row, Go"
            </p>
          </div>

          <button 
            class="mt-3 bg-cyan-600 hover:bg-cyan-700 text-white py-1 px-3 rounded-md transition-colors text-xs"
            @click="resetSimulation"
          >
            Restart
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

// Emit events for window controls
const emit = defineEmits(['minimize', 'maximize', 'close']);

// Window control functions
const minimizeWindow = () => emit('minimize');
const maximizeWindow = () => emit('maximize');
const closeWindow = () => emit('close');

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
  if (selectedOption.value === 'C') return 'bg-green-900/50';
  if (selectedOption.value === 'timeout') return 'bg-red-900/50';
  return 'bg-yellow-900/50';
});

const feedbackTextClass = computed(() => {
  if (selectedOption.value === 'C') return 'text-green-200';
  if (selectedOption.value === 'timeout') return 'text-red-200';
  return 'text-yellow-200';
});

const feedbackTitle = computed(() => {
  if (selectedOption.value === 'A') return 'Risky choice:';
  if (selectedOption.value === 'B') return 'Important note:';
  if (selectedOption.value === 'C') return 'Good choice:';
  if (selectedOption.value === 'timeout') return 'Time\'s up!';
  return '';
});

const feedbackMessage = computed(() => {
  if (selectedOption.value === 'A') {
    return 'Jumping into water without training is dangerous. A drowning person may pull rescuers underwater.';
  }
  if (selectedOption.value === 'B') {
    return 'Calling for help is important, but in drowning situations, every second counts.';
  }
  if (selectedOption.value === 'C') {
    return 'Using rescue equipment like a life ring is the safest and most effective option.';
  }
  if (selectedOption.value === 'timeout') {
    return 'In emergency situations, quick action is essential. Stay calm but act quickly.';
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

// Draw life ring
const drawLifeRing = (ctx, x, y, size, rotation = 0) => {
  ctx.save();
  ctx.translate(x, y);
  ctx.rotate(rotation);

  // Outer ring
  ctx.fillStyle = "#FF5252"; // Red color for visibility
  ctx.beginPath();
  ctx.arc(0, 0, size, 0, Math.PI * 2);
  ctx.fill();

  // Inner ring (hole)
  ctx.fillStyle = "#FFFFFF"; // White inner ring
  ctx.beginPath();
  ctx.arc(0, 0, size * 0.6, 0, Math.PI * 2);
  ctx.fill();

  // Draw stripes for visibility
  ctx.fillStyle = "#FFFFFF";

  // Top stripe
  ctx.beginPath();
  ctx.rect(-size * 0.15, -size, size * 0.3, size * 2);
  ctx.fill();

  // Side stripe
  ctx.beginPath();
  ctx.rect(-size, -size * 0.15, size * 2, size * 0.3);
  ctx.fill();

  // Draw rope
  ctx.strokeStyle = "#FFFFFF";
  ctx.lineWidth = size * 0.1;
  ctx.beginPath();

  // Draw rope in a wavy pattern around the ring
  for (let i = 0; i < 8; i++) {
    const angle = (i / 8) * Math.PI * 2;
    const nextAngle = ((i + 1) / 8) * Math.PI * 2;

    const x1 = Math.cos(angle) * size * 0.8;
    const y1 = Math.sin(angle) * size * 0.8;

    const x2 = Math.cos(nextAngle) * size * 0.8;
    const y2 = Math.sin(nextAngle) * size * 0.8;

    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
  }

  ctx.stroke();

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

  // Draw life ring on the pool edge
  drawLifeRing(ctx, width * 0.25, height * 0.28, 15);

  // Add a small label for the life ring if showLabels is true
  if (showLabels.value) {
    ctx.font = "bold 10px Arial";
    ctx.fillStyle = "#000000";
    ctx.textAlign = "center";
    ctx.fillText("Life Ring", width * 0.25, height * 0.24);
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

      // Swimming animation
      const swimCycle = time * 4;

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
    // Option C: Person uses life ring to rescue
    const rescuerBaseSize = 20;
    const rescuerX = width * 0.25;
    const rescuerY = height * 0.29; // On the edge

    // Life ring properties
    const lifeRingSize = 15;
    let lifeRingX, lifeRingY, lifeRingRotation = 0;

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

    // Person grabs life ring (0-0.2)
    if (animationPhase < 0.2) {
      // Draw person reaching for life ring
      const reachProgress = animationPhase / 0.2;
      
      // Draw person with arms reaching
      drawPerson(ctx, rescuerX, rescuerY, rescuerBaseSize, 0, reachProgress * 0.5, 0, colors, false, false);
      
      // Draw life ring at its original position
      lifeRingX = rescuerX;
      lifeRingY = rescuerY - 5;
      drawLifeRing(ctx, lifeRingX, lifeRingY, lifeRingSize);
    }
    // Person throws life ring (0.2-0.4)
    else if (animationPhase < 0.4) {
      const throwProgress = (animationPhase - 0.2) / 0.2;
      
      // Draw person in throwing pose
      const throwArmSwing = Math.sin(throwProgress * Math.PI) * rescuerBaseSize * 0.8;
      drawPerson(ctx, rescuerX, rescuerY, rescuerBaseSize, 0, throwArmSwing, 0, colors, false, false);
      
      // Calculate life ring trajectory (arc)
      lifeRingX = rescuerX + (childX - rescuerX) * throwProgress;
      lifeRingY = rescuerY - Math.sin(throwProgress * Math.PI) * height * 0.2; // Arc trajectory
      lifeRingRotation = throwProgress * Math.PI * 4; // Spin while flying
      
      // Draw life ring in flight
      drawLifeRing(ctx, lifeRingX, lifeRingY, lifeRingSize, lifeRingRotation);
    }
    // Life ring reaches child and splash (0.4-0.5)
    else if (animationPhase < 0.5) {
      // Draw person in post-throw pose
      drawPerson(ctx, rescuerX, rescuerY, rescuerBaseSize, 0, 0.3, 0, colors, false, false);
      
      // Life ring reaches child position
      lifeRingX = childX;
      lifeRingY = childY - baseSize * 0.5;
      
      // Draw splash around life ring
      const splashSize = lifeRingSize * 1.5;
      for (let i = 0; i < 10; i++) {
        const angle = (i / 10) * Math.PI * 2;
        const splashX = lifeRingX + Math.cos(angle) * splashSize * Math.random();
        const splashY = lifeRingY + Math.sin(angle) * splashSize * Math.random() * 0.5;
        const dropSize = Math.random() * lifeRingSize * 0.3 + lifeRingSize * 0.1;

        ctx.fillStyle = "rgba(255, 255, 255, 0.8)";
        ctx.beginPath();
        ctx.arc(splashX, splashY, dropSize, 0, Math.PI * 2);
        ctx.fill();
      }
      
      // Draw life ring at child position
      drawLifeRing(ctx, lifeRingX, lifeRingY, lifeRingSize);
    }
    // Child grabs life ring (0.5-0.6)
    else if (animationPhase < 0.6) {
      // Draw person pulling rope
      const pullArmSwing = Math.sin(time * 5) * rescuerBaseSize * 0.3;
      drawPerson(ctx, rescuerX, rescuerY, rescuerBaseSize, 0, pullArmSwing, 0, colors, false, false);
      
      // Life ring at child position
      lifeRingX = childX;
      lifeRingY = childY - baseSize * 0.5;
      
      // Draw life ring with child
      drawLifeRing(ctx, lifeRingX, lifeRingY, lifeRingSize);
      
      // Draw rope connecting rescuer to life ring
      ctx.strokeStyle = "#FFFFFF";
      ctx.lineWidth = 2;
      ctx.beginPath();
      
      // Wavy rope
      const segments = 10;
      for (let i = 0; i <= segments; i++) {
        const t = i / segments;
        const waveHeight = Math.sin(t * Math.PI * 3 + time * 5) * 5;
        const x = rescuerX + (lifeRingX - rescuerX) * t;
        const y = rescuerY + (lifeRingY - rescuerY) * t + waveHeight;
        
        if (i === 0) {
          ctx.moveTo(x, y);
        } else {
          ctx.lineTo(x, y);
        }
      }
      
      ctx.stroke();
    }
    // Pulling child to safety (0.6-1.0)
    else {
      const pullProgress = (animationPhase - 0.6) / 0.4;
      
      // Draw person pulling rope
      const pullArmSwing = Math.sin(time * 5) * rescuerBaseSize * 0.3;
      drawPerson(ctx, rescuerX, rescuerY, rescuerBaseSize, 0, pullArmSwing, 0, colors, false, false);
      
      // Life ring and child moving toward shore
      lifeRingX = childX - (childX - rescuerX) * pullProgress;
      lifeRingY = childY - (childY - rescuerY) * pullProgress;
      
      // Draw life ring
      drawLifeRing(ctx, lifeRingX, lifeRingY, lifeRingSize);
      
      // Draw child holding onto life ring
      // Adjust child position to appear holding the ring
      const childHoldingX = lifeRingX;
      const childHoldingY = lifeRingY + baseSize * 0.3;
      
      // Draw smaller splashes around child being pulled
      for (let i = 0; i < 5; i++) {
        const splashX = childHoldingX + (Math.random() - 0.5) * baseSize * 2;
        const splashY = childHoldingY + (Math.random() - 0.5) * baseSize;
        const dropSize = Math.random() * baseSize * 0.15 + baseSize * 0.05;

        ctx.fillStyle = "rgba(255, 255, 255, 0.6)";
        ctx.beginPath();
        ctx.arc(splashX, splashY, dropSize, 0, Math.PI * 2);
        ctx.fill();
      }
      
      // Draw child holding ring
      drawPerson(ctx, childHoldingX, childHoldingY, baseSize, 0, 0, 0, colors, true, false);
      
      // Draw rope connecting rescuer to life ring
      ctx.strokeStyle = "#FFFFFF";
      ctx.lineWidth = 2;
      ctx.beginPath();
      
      // Wavy rope
      const segments = 10;
      for (let i = 0; i <= segments; i++) {
        const t = i / segments;
        const waveHeight = Math.sin(t * Math.PI * 3 + time * 5) * 5;
        const x = rescuerX + (lifeRingX - rescuerX) * t;
        const y = rescuerY + (lifeRingY - rescuerY) * t + waveHeight;
        
        if (i === 0) {
          ctx.moveTo(x, y);
        } else {
          ctx.lineTo(x, y);
        }
      }
      
      ctx.stroke();
      
      // Draw "safe" indicator when reaching shore
      if (pullProgress > 0.9) {
        ctx.fillStyle = "#4CAF50";
        ctx.beginPath();
        ctx.arc(
          lifeRingX + lifeRingSize * 1.2,
          lifeRingY - lifeRingSize * 0.5,
          lifeRingSize * 0.3,
          0,
          Math.PI * 2
        );
        ctx.fill();

        ctx.font = "bold 16px Arial";
        ctx.fillStyle = "#FFFFFF";
        ctx.textAlign = "center";
        ctx.fillText("✓", lifeRingX + lifeRingSize * 1.2, lifeRingY - lifeRingSize * 0.4);
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

  // Draw window title bar
  const letterboxHeight = height * 0.05;
  ctx.fillStyle = "#000";
  ctx.fillRect(0, 0, width, letterboxHeight);
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

.window-header {
  user-select: none;
  cursor: move;
}

.window-button {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  margin-left: 4px;
  background-color: rgba(255, 255, 255, 0.1);
}

.window-button:hover {
  background-color: rgba(255, 255, 255, 0.2);
}
</style>