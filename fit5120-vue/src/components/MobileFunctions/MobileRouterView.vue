<!-- src/components/MobileFunctions/MobileRouterView.vue -->
<script setup>
import { RouterView } from 'vue-router'
import BottomNavBar from './BottomNavBar.vue'
import { mobileRouter } from './MobileRouter'
import { useRouter } from 'vue-router'

const globalRouter = useRouter()
globalRouter.addRoute({
  path: '/mobile/:catchAll(.*)*',
  component: {
    render() {
      return h(RouterView, { router: mobileRouter })
    }
  }
})
</script>

<template>
  <router-view />
  <BottomNavBar />
</template>

<style scoped>
.mobile-wrapper {
  padding-bottom: 1000px; 
}
</style>