import CommunitiesPage from "../views/CommunitiesPage.vue";
import CreateCommunity from "../views/CreateCommunity.vue";
import Leaderboard from "../views/Leaderboard.vue";
import LoginPage from "../views/LoginPage.vue";
import PreviewCommunity from "../views/PreviewCommunity.vue";
import Profile from "../views/Profile.vue";
import RegisterPage from "../views/RegisterPage.vue";
import Community from "../views/Community.vue"
import Vue from "vue";
import VueRouter from "vue-router";
import Feed from '../views/Feed.vue'
import axios from 'axios'


Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "Feed",
    component: Feed,
  },
  {
    path: "/login",
    name: "LoginPage",
    component: LoginPage,
  },
  {
    path: "/register",
    name: "RegisterPage",
    component: RegisterPage,
  },
  {
    path: "/communities",
    name: "Communities",
    component: CommunitiesPage,
  },
  {
    path: "/profile",
    name: "Profile",
    component: Profile,
  },
  {
    path: "/leaderboard",
    name: "Leaderboard",
    component: Leaderboard,
  },
  {
    path: "/communities/create",
    name: "CreateCommunity",
    component: CreateCommunity,
  },
  {
    path: "/communities/create/preview",
    name: "PreviewCommunity",
    component: PreviewCommunity,
  },
  {
    path: '/community/:id',
    name: 'Community',
    component: Community,
  }
];

const router = new VueRouter({
    routes
})

router.beforeEach((to, from, next) => {
    if (to.name !== from.name) {
        // Direct user to login if they are not authenticated
        axios.get('api/communities?type=all')
        .catch((err)=> {
            console.error(err);
            if(to.path !== '/login' && to.path !== '/register') {
                return next({
                    path: '/login',
                });
            }
        });
    }
    next();
});
export default router
