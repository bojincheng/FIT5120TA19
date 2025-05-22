import { createRouter, createWebHistory } from 'vue-router'
import NewLandingPage from '../NewLanding.vue'
import BeachHomePage from '../components/BeachHomePage.vue'
import RipEscapeSimulation from '../RipEscapeSimulation.vue'
import PoolSafetyQuiz from '../PoolSafetyQuiz.vue'
import PoolHomePage from '../components/PoolHomePage.vue'
import RiverHomePage from '../components/RiverHome.vue'
const routes = [
  {
    path: '/',
    name: 'Landing',
    component: NewLandingPage
  },
  {
    path: '/beach',
    name: 'Beach',
    component: BeachHomePage
  },
  {
    path: '/pool',
    name: 'Pool',
    component: PoolHomePage
  },
  {
    path: '/river',
    name: 'River',
    component: RiverHomePage
  },
  {
    path: '/rip-escape-simulation',
    name: 'RipEscapeSimulation',
    component: RipEscapeSimulation
  },
 
  {
    path: '/pool-safety-quiz',
    name: 'PoolSafetyQuiz',
    component: PoolSafetyQuiz
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router 