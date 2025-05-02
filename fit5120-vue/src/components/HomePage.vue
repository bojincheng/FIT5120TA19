<template>
    <div>
      <h1>Welcome to Drowning Statistics</h1>
      <p>Explore drowning statistics, search for specific data, and learn more about water safety.</p>
      
      <router-link to="/KidPoolSim">
        <button>Go to Drowning Sim</button>
      </router-link>
    </div>
    <div class="simulation-wrapper">
      <PoolSafetySimulation :width="600" :height="400" />
    </div>
  </template>
  
  <script>
  import PoolSafetySimulation from './KidPoolSim.vue';


  export default {
    name: 'HomePage',
    components: {
      PoolSafetySimulation
    }
  };
  </script>
  
  <style scoped>
  div {
    text-align: center;
    padding: 20px;
  }
  
  button {
    background-color: #3e8e41;
    color: white;
    padding: 10px 20px;
    border: none;
    cursor: pointer;
    font-size: 16px;
    margin-top: 10px;
  }
  
  button:hover {
    background-color: #2e6b31;
  }
  </style>
