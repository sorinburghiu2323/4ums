import CommunitiesPage from "../views/CommunitiesPage.vue";
import CreateCommunity from "../views/CreateCommunity.vue";
import HomePage from "../views/HomePage.vue";
import Leaderboard from "../views/Leaderboard.vue";
import LoginPage from "../views/LoginPage.vue";
import PreviewCommunity from "../views/PreviewCommunity.vue";
import Profile from "../views/Profile.vue";
import RegisterPage from "../views/RegisterPage.vue";
import Community from "../views/Community.vue"
import Vue from "vue";
import VueRouter from "vue-router";
import Post from "@/views/Post";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
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
    path: "/communities/:id/posts/:postId",
    name: "Post",
    component: Post,
  },
  {
    path: '/community/:id',
    name: 'Community',
    component: Community,
  }
];

const router = new VueRouter({
  routes,
});

export default router;
