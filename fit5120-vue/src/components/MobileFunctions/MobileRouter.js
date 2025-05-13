// src/components/MobileFunctions/MobileRouter.js
import { createRouter, createWebHistory } from 'vue-router'
import MobileHomePage from './HomePageMobile.vue'
import BeachSafetyPage from './BeachSafetyMobile.vue'
import RipCurrentDetectionPage from './RipCurrentDetectionMobile.vue'

const routes = [
  { path: '/mobile', redirect: '/mobile/home' },
  { path: '/mobile/home', component: MobileHomePage },
  { path: '/mobile/beach', component: BeachSafetyPage },
  { path: '/mobile/rip', component: RipCurrentDetectionPage }
]

export const mobileRouter = createRouter({
  history: createWebHistory(),
  routes
})
