import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import DrowningSearch from '../components/DrowningSearch.vue';
import BeachData from '../components/BeachData.vue';
import KidFallSim from '@/components/KidPoolSim.vue';

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage
  },
  {
    path: '/DrowningSearch',
    name: 'DrowningSearch',
    component: DrowningSearch
  },
  {
    path: '/Beachdata',
    name: 'Beachdata',
    component: BeachData
  },
  {
    path: '/KidFallSim',
    name: 'KidFallSim',
    component: KidFallSim
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
