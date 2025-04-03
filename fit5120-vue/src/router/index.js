import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import DrowningSearch from '../components/DrowningSearch.vue';

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
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
