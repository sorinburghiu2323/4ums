import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from '../views/HomePage.vue'
import Communities from '../views/Communities.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'HomePage',
        component: HomePage
    },
    {
        path: '/communities',
        name: 'Communities',
        component: Communities
    },
]

const router = new VueRouter({
    routes
  })
  
export default router