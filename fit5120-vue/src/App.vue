<template>
  <div id="app">
    <BHeader />
    <router-view />
  </div>
</template>

<script>
import BHeader from './components/BHeader.vue';

export default {
  name: 'App',
  components: {
    BHeader
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

