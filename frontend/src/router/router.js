import Communities from "../views/Communities.vue";
import Community from "../views/Community.vue";
import CreatePost from "../views/CreatePost.vue";
import HomePage from "../views/HomePage.vue";
import Leaderboard from "../components/Leaderboard.vue";
import LoginPage from "../views/LoginPage.vue";
import Profile from "../components/Profile.vue";
import RegisterPage from "../views/RegisterPage.vue";
import Vue from "vue";
import VueRouter from "vue-router";

//import Communities from '../components/Communities.vue'

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
  },
  {
    path: "/communities/post/:type",
    name: "CreatePost",
    component: CreatePost,
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
    path: "/communities/:id",
    name: "Communities",
    component: Communities,
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
    path: "/communities/:id",
    name: "Community",
    component: Community,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
