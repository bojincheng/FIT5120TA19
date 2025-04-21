<template>
  <div class="space-y-4 max-w-xl">
    <h2 class="text-2xl font-semibold">Daily Pool Safety Routine</h2>
    <p>Select the steps you'd like to include in your daily checklist:</p>

    <!-- Checklist options -->
    <div v-for="(step, index) in checklistOptions" :key="index">
      <label class="flex items-center space-x-2">
        <input type="checkbox" v-model="selectedSteps" :value="step.text" />
        <span :title="step.tip">{{ step.text }}</span>
      </label>
    </div>

    <!-- Toggle Button for Remembering Checklist -->
    <button 
      @click="toggleRemember"
      :class="rememberChecklist ? 'bg-green-500' : 'bg-gray-300'"
      class="text-white py-1 px-3 rounded focus:outline-none transition w-full"
    >
      {{ rememberChecklist ? '✔ Checklist has been remembered' : 'Remember my checklist' }}
    </button>

    <!-- Email Input Field on its own line -->
    <div class="mt-2">
      <input 
        v-model="email" 
        type="email" 
        placeholder="Enter your email" 
        class="w-full p-2 border rounded"
      />
    </div>

    <!-- Separate Container for the 'Email Me My Checklist' Button -->
    <div class="mt-2">
      <button 
        @click="sendChecklist" 
        class="bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded w-full"
      >
        Email Me My Checklist
      </button>
    </div>

    <!-- Status/Error Messages -->
    <p v-if="statusMessage" class="text-green-600">{{ statusMessage }}</p>
    <p v-if="errorMessage" class="text-red-600">{{ errorMessage }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'

const checklistOptions = [
  { text: 'Check pool gate is latched', tip: 'Ensure the gate locks securely and closes automatically.' },
  { text: 'Remove toys from pool', tip: 'Toys can tempt children to enter the pool area unsupervised.' },
  { text: 'Store chemicals safely', tip: 'Keep chemicals in a locked cabinet out of reach of children.' },
  { text: 'Ensure CPR sign is visible', tip: 'A CPR sign is required by law and can save lives in emergencies.' },
  { text: 'Keep phone nearby for emergencies', tip: 'Being able to call emergency services quickly is critical.' }
]

const selectedSteps = ref([])
const email = ref('')
const rememberChecklist = ref(false) // Default state should be false (unchecked)
const statusMessage = ref('')
const errorMessage = ref('')

// Load saved checklist from localStorage on component mount
onMounted(() => {
  const saved = localStorage.getItem('savedChecklist')
  const savedRemember = localStorage.getItem('rememberChecklist')
  
  // If the checklist was previously remembered, restore saved items
  if (savedRemember === 'true') {
    selectedSteps.value = JSON.parse(saved) // Restore the saved checklist items
    rememberChecklist.value = true // Set the "remember" status to true
  } else {
    rememberChecklist.value = false // Ensure the button starts in the default state
  }
})

// Watch for changes in selectedSteps and update localStorage accordingly
watch(selectedSteps, (newSelectedSteps) => {
  if (rememberChecklist.value) {
    localStorage.setItem('savedChecklist', JSON.stringify(newSelectedSteps))
  }
})

// Toggle remember setting
const toggleRemember = () => {
  rememberChecklist.value = !rememberChecklist.value
  if (rememberChecklist.value) {
    localStorage.setItem('savedChecklist', JSON.stringify(selectedSteps.value))
    localStorage.setItem('rememberChecklist', 'true')
  } else {
    localStorage.removeItem('savedChecklist')
    localStorage.removeItem('rememberChecklist')
  }
}

const sendChecklist = async () => {
  statusMessage.value = ''
  errorMessage.value = ''

  if (!email.value || selectedSteps.value.length === 0) {
    errorMessage.value = 'Please enter an email and select at least one step.'
    return
  }

  try {
    await axios.post('http://localhost:5000/send-checklist', {
      email: email.value,
      checklist: selectedSteps.value
    })
    statusMessage.value = 'Email sent successfully, please check your mailbox!'
    selectedSteps.value = []
    email.value = ''
  } catch (err) {
    errorMessage.value = 'Something went wrong. Please try again later.'
  }
}
</script>











