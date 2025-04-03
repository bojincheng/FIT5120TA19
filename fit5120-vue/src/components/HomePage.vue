<template>
    <div>
      <h1>Welcome to Drowning Statistics</h1>
      <p>Explore drowning statistics, search for specific data, and learn more about water safety.</p>
      
      <router-link to="/DrowningSearch">
        <button>Go to Drowning Search</button>
      </router-link>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HomePage'
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
