<!-- <template>
  <router-view></router-view>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
body {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
}
</style>  -->

# Mobile device check
<template>
  <div>
    <BeachSafety v-if="isMobile" />
    <router-view v-else />
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import BeachSafety from './BeachSafety.vue'

const isMobile = ref(false)

const checkDevice = () => {
  isMobile.value = window.innerWidth < 768
}

onMounted(() => {
  checkDevice()
  window.addEventListener('resize', checkDevice)
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', checkDevice)
})
</script>

<style>
body {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
}
</style>
