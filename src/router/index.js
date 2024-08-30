import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/user/LoginView.vue'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'LoginView',
      component: LoginView
    }
  ]
})

export default router
