import { createRouter, createWebHistory } from 'vue-router'
import LoadingPage from '../Loading.vue'
import LandingPage from '../Landing.vue'
import HomePage from '../HomePage.vue'
import BeachSafety from '../BeachSafety.vue'
import PoolSafety from '../PoolSafety.vue'
import PoolSupervision from '../PoolSupervision.vue'
import BackyardPool from '../BackyardPool.vue'
import BeachData from '../BeachData.vue'
import RipSafety from '../RipSafety.vue'
import SpotRipCurrents from '../SpotRipCurrents.vue'
import SurviveRipCurrents from '../SurviveRipCurrents.vue'
import SafetyTool from '../SafetyTool.vue'
import RipEscapeSimulation from '../RipEscapeSimulation.vue'
import BeachSafetyPractices from '../BeachSafetyPractices.vue'
// Import new components
import BeachSafetyRescue from '../BeachSafetyRescue.vue'
import WaterSafetySimulation from '../WaterSafetySimulation.vue'
import OffshoreRescue from '../OffshoreRescue.vue'

const routes = [
  {
    path: '/',
    name: 'Landing',
    component: LandingPage
  },
  {
    path: '/loading',
    name: 'Loading',
    component: LoadingPage
  },
  {
    path: '/home',
    name: 'Home',
    component: HomePage
  },
  {
    path: '/beach-safety',
    name: 'BeachSafety',
    component: BeachSafety
  },
  {
    path: '/pool-safety',
    name: 'PoolSafety',
    component: PoolSafety
  },
  {
    path: '/pool-supervision',
    name: 'PoolSupervision',
    component: PoolSupervision
  },
  {
    path: '/backyard-pool',
    name: 'BackyardPool',
    component: BackyardPool
  },
  {
    path: '/beach-data',
    name: 'BeachData',
    component: BeachData
  },
  {
    path: '/rip-safety',
    name: 'RipSafety',
    component: RipSafety
  },
  {
    path: '/spot-rip-currents',
    name: 'SpotRipCurrents',
    component: SpotRipCurrents
  },
  {
    path: '/survive-rip-currents',
    name: 'SurviveRipCurrents',
    component: SurviveRipCurrents
  },
  {
    path: '/safety-tool',
    name: 'SafetyTool',
    component: SafetyTool
  },
  {
    path: '/rip-escape-simulation',
    name: 'RipEscapeSimulation',
    component: RipEscapeSimulation
  },
  {
    path: '/water-safety-simulation',
    name: 'WaterSafetySimulation',
    component: WaterSafetySimulation
  },
  {
    path: '/beach-safety-practices',
    name: 'BeachSafetyPractices',
    component: BeachSafetyPractices
  },
  // Add new routes for the beach safety progress path
  {
    path: '/beach-safety-rescue',
    name: 'BeachSafetyRescue',
    component: BeachSafetyRescue
  },
  {
    path: '/offshore-rescue',
    name: 'OffshoreRescue',
    component: OffshoreRescue
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router 