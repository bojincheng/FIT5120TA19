<template>
  <div class="p-6 max-w-4xl mx-auto">
    <h1 class="text-3xl font-bold mb-6">Pool Safety Knowledge Check</h1>

    <!-- Navigation Tabs -->
    <div class="flex space-x-4 mb-8">
      <button
        v-for="(tab, index) in tabs"
        :key="index"
        @click="currentTab = index"
        :class="[
          'px-4 py-2 rounded-xl',
          currentTab === index ? 'bg-blue-600 text-white' : 'bg-gray-200'
        ]"
      >
        {{ tab.title }}
      </button>
    </div>

    <!-- Tab Content -->
    <div v-if="currentTab === null" class="text-center text-gray-600 mt-10">
      <p>Please select a pool safety topic to explore.</p>
    </div>
    <div v-else>
      <component :is="tabs[currentTab].component" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import SilentSeconds from './SilentSeconds.vue'
import FenceRegulations from './FenceRegulations.vue'
import HazardWalkthrough from './HazardWalkthrough.vue'
import SafetyRoutine from './SafetyRoutine.vue'

const tabs = [
  { title: 'Silent Seconds', component: SilentSeconds },
  { title: 'Fence Laws', component: FenceRegulations },
  { title: 'Drowning Hazards', component: HazardWalkthrough },
  { title: 'Daily Routine', component: SafetyRoutine }
]

const currentTab = ref(null)
</script>

<style scoped>
button {
  transition: background-color 0.3s;
}
</style>


  