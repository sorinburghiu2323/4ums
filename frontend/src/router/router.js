import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from '../views/HomePage.vue'
import Communities from '../views/Communities.vue'
import Profile from '../views/Profile.vue'
import Leaderboard from '../views/Leaderboard.vue'

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
    {
        path: '/profile',
        name: 'Profile',
        component: Profile
    },
    {
        path: '/leaderboard',
        name: 'Leaderboard',
        component: Leaderboard
    }
]

const router = new VueRouter({
    routes
  })
  
export default router