import Vue from 'vue'
import VueRouter from 'vue-router'
// import HomePage from '../views/HomePage.vue'
import HomePage2 from '../views/HomePage2.vue'
import HomePage3 from '../views/HomePage3.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'HomePage2',
        component: HomePage2
    },
    {
      path: '/homepage3',
      name: 'HomePage3',
      component: HomePage3
  },
]

const router = new VueRouter({
    routes
  })
  
export default router