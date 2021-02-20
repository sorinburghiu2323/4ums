import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from '../views/HomePage.vue'
import Communities from '../components/Communities.vue'
import Profile from '../components/Profile.vue'
import Leaderboard from '../components/Leaderboard.vue'

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