import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from '../views/HomePage.vue'
import CreatePost from '../views/CreatePost.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'HomePage',
        component: HomePage
    },
    {
        path: '/communities/:id/post',
        name: 'CreatePost',
        component: CreatePost
    }
]

const router = new VueRouter({
    routes
  })
  
export default router