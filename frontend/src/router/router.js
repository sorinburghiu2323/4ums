import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from '../views/HomePage.vue'
import IndividualCommunitiesPage from '../views/IndividualCommunitiesPage.vue'
import Profile from '../views/Profile.vue'
import Leaderboard from '../views/Leaderboard.vue'
import LoginPage from '../views/LoginPage.vue'
import RegisterPage from '../views/RegisterPage.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'HomePage',
        component: HomePage
    },
    {
        path: '/login',
        name: 'LoginPage',
        component: LoginPage
    },
    {
        path: '/register',
        name: 'RegisterPage',
        component: RegisterPage,
    },
    {
        path: '/communities',
        name: 'Communities',
        component: IndividualCommunitiesPage
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