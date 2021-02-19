import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from '../views/HomePage.vue'
import CreatePost from '../views/CreatePost.vue'
import Communities from '../views/Communities.vue'
import Community from '../views/Community.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'HomePage',
        component: HomePage
    },
    {
        path: '/communities/:id/post/:type',
        name: 'CreatePost',
        component: CreatePost
    },
    {
        path: '/communities',
        name: 'Communities',
        component: Communities
    },
    {
        path: '/communities/:id',
        name: 'Community',
        component: Community
    }
]

const router = new VueRouter({
    routes
  })
  
export default router