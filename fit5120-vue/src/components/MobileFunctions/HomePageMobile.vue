<template> 
  <div class="container">
    <h2>Mobile Menu</h2>
    <ul class="menu">
      <li @click="activeComponent = 'BeachSafetyMobile'">1. Beach Safety</li>
      <li @click="activeComponent = 'RipCurrentDetectionMobile'">2. Rip Current Detection</li>
      <li @click="activeComponent = 'RiverImpactForecast'">3. River Impact Forecast</li>
    </ul>

    <div class="content">
      <BeachSafetyMobile v-if="activeComponent === 'BeachSafetyMobile'" />
      <RipCurrentDetectionMobile v-else-if="activeComponent === 'RipCurrentDetectionMobile'" />
      <RiverImpactForecast v-else-if="activeComponent === 'RiverImpactForecast'" />
    </div>
  </div>

  <AddToHomeScreenButton/>
</template>

<script setup>
import { ref } from 'vue'

import BeachSafetyMobile from './BeachSafetyMobile.vue'
import RipCurrentDetectionMobile from './RipCurrentDetectionMobile.vue'
import RiverImpactForecast from './RiverImpactForecast.vue'
import AddToHomeScreenButton from './AddToHomeScreenButton.vue'

const activeComponent = ref('BeachSafety') // Set initial view correctly
</script>

  
<style scoped>
  .container {
    padding: 1rem;
    font-family: Arial, sans-serif;
    text-align: center;
  }
  
  .menu {
    list-style: none;
    padding: 0;
    margin-bottom: 1rem;
  }
  
  .menu li {
    padding: 0.75rem;
    margin: 0.5rem 0;
    background-color: #007BFF;
    color: white;
    border-radius: 8px;
    cursor: pointer;
  }
  
  .menu li:hover {
    background-color: #0056b3;
  }
  
  .content {
    margin-top: 1rem;
  }
  </style>
  