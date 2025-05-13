<!-- components/MobileFunctions/BottomNavBar.vue -->
<template>
  <nav class="bottom-nav">
    <router-link to="/mobile/home">Home</router-link>
    <router-link to="/mobile/beach">Beach</router-link>
    <router-link to="/mobile/rip">Rip</router-link>
  </nav>
</template>

<style scoped>
.bottom-nav {
  position: fixed;
  bottom: 0;
  width: 100%;
  display: flex;
  justify-content: space-around;
  background-color: #4CAF50;
  color: white;
  padding: 10px 0;
}

.bottom-nav a {
  color: white;
  font-weight: bold;
  text-decoration: none;
}

.bottom-nav a.router-link-active {
  border-bottom: 2px solid white;
}
</style>
