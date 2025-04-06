import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import DrowningSearch from '../components/DrowningSearch.vue';
import BeachData from '../components/BeachData.vue';

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
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
