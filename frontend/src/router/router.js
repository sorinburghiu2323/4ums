import Communities from "../components/Communities.vue";
import CreateCommunity from "../views/CreateCommunity.vue";
import HomePage from "../views/HomePage.vue";
import Leaderboard from "../components/Leaderboard.vue";
import LoginPage from "../views/LoginPage.vue";
import PreviewCommunity from "../views/PreviewCommunity.vue";
import Profile from "../components/Profile.vue";
import RegisterPage from "../views/RegisterPage.vue";
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
  }
];

const router = new VueRouter({
  routes,
});

export default router;
