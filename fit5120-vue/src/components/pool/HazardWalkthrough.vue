<template> 
  <div class="max-w-xl mx-auto p-4">
    <div class="border p-4 rounded shadow-md">
      <div 
        ref="lottieContainer" 
        class="w-full mb-4 flex justify-center items-center"
        style="height: 220px; max-width: 100%;">
      </div>

      <h3 class="text-xl font-semibold mb-2">{{ hazards[currentIndex].title }}</h3>
      <p class="mb-2">{{ hazards[currentIndex].description }}</p>
      <p class="italic text-green-700">{{ hazards[currentIndex].prevention }}</p>

      <div class="flex justify-between mt-4">
        <button @click="prev" :disabled="currentIndex === 0" class="btn">Back</button>
        <button @click="next" :disabled="currentIndex === hazards.length - 1" class="btn">Next</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import lottie from 'lottie-web'

const currentIndex = ref(0)
const lottieContainer = ref(null)
let lottieInstance = null

const hazards = [
  {
    title: 'Unfenced Pools',
    animationPath: '/animations/unfenced.json',
    description: 'Unfenced or poorly secured pools pose a high drowning risk, especially to toddlers who may wander in unsupervised.',
    prevention: 'Install a compliant pool fence with a self-closing, self-latching gate. Always supervise children around water.',
  },
  {
    title: 'Bathtubs',
    animationPath: '/animations/bathtub.json',
    description: 'Bathtubs can become hazardous if a child slips or is left unsupervised, even for a short time.',
    prevention: 'Always stay within arm’s reach of children during bath time and empty the tub immediately after use.',
  },
  {
  title: 'Lack of Supervision',
  animationPath: '/animations/supervision.json',
  description: 'Children can quickly get into dangerous situations around water if left unsupervised, even for a moment.',
  prevention: 'Always maintain constant, active supervision when children are near water — never rely on older children or distractions like phones.',
}
]

// Load animation
const loadAnimation = () => {
  if (lottieInstance) {
    lottieInstance.destroy()
  }

  lottieInstance = lottie.loadAnimation({
    container: lottieContainer.value,
    renderer: 'svg',
    loop: true,
    autoplay: true,
    path: hazards[currentIndex.value].animationPath,
  })
}

// Watch currentIndex and reload animation
watch(currentIndex, () => {
  loadAnimation()
})

// Initialize animation on mount
onMounted(() => {
  loadAnimation()
})

const next = () => {
  if (currentIndex.value < hazards.length - 1) currentIndex.value++
}

const prev = () => {
  if (currentIndex.value > 0) currentIndex.value--
}
</script>

<style scoped>
.btn {
  background-color: #3b82f6;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  transition: background-color 0.2s;
}
.btn:disabled {
  background-color: #9ca3af;
  cursor: not-allowed;
}
</style>

  