import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/HomePage.vue'
import Drowningsearch from '../components/DrowningSearch.vue'
import RipCurrentDetection from '../components/RipCurrentDetection.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Drowningsearch',
    name: 'Drowningsearch',
    component: Drowningsearch
  },
  {
    path: '/ripcurrent',
    name: 'RipCurrentDetection',
    component: RipCurrentDetection
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router