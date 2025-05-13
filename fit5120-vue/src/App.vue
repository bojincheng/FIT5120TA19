# Two routes for different device types: 
# if the mobile device is detected, render the partial pages, else render all pages
<template>
  <div>
    <MobileRouterView v-if="isMobile" />
    <router-view v-else />
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
//import HomePageMobile from './components/MobileFunctions/HomePageMobile.vue'
import MobileRouterView from './components/MobileFunctions/MobileRouterView.vue'

const isMobile = ref(false)
const router = useRouter()

const checkDevice = () => {
  isMobile.value = window.innerWidth < 768 
}

onMounted(() => {
  checkDevice()
  window.addEventListener('resize', checkDevice)

  // if (window.innerWidth < 768 && !window.location.pathname.startsWith('/mobile')) {
  //   router.replace('/mobile/home')
  // }
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
