import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import DrowningSearch from '../components/beach/DrowningSearch.vue';
import BeachData from '../components/beach/BeachData.vue';
import PoolSafetyKnowledgeCheck from '../components/pool/PoolSafetyKnowledgeCheck.vue';
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
    path: '/BeachData',
    name: 'BeachData',
    component: BeachData
  },
  {
    path: '/PoolSafetyKnowledgeCheck',
    name: 'PoolSafetyKnowledgeCheck',
    component: PoolSafetyKnowledgeCheck
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
