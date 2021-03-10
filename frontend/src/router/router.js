import CommunitiesPage from "../views/CommunitiesPage.vue";
import Community from "../views/Community.vue";
import CreateCommunity from "../views/CreateCommunity.vue";
import CreatePost from "../views/CreatePost.vue";
import DeleteCommunity from "@/views/DeleteCommunity";
import EditProfile from "@/views/EditProfile";
import EnterNewPassword from "../views/EnterNewPassword";
import Feed from "../views/Feed.vue";
import ForgotPassword from "@/views/ForgotPassword";
import Leaderboard from "../views/Leaderboard.vue";
import LeaveCommunity from "@/views/LeaveCommunity";
import LoginPage from "../views/LoginPage.vue";
import ManageCommunities from "../views/ManageCommunities.vue";
import NotFound from "@/views/NotFound";
import PostPage from "@/views/PostPage";
import PreviewCommunity from "../views/PreviewCommunity.vue";
import Profile from "../views/Profile.vue";
import RegisterPage from "../views/RegisterPage.vue";
import Settings from "@/views/Settings";
import User from "@/views/User";
import Vue from "vue";
import VueRouter from "vue-router";
import axios from "axios";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Feed",
    component: Feed,
  },
  {
    path: "/communities/:id/post/:type",
    name: "CreatePost",
    component: CreatePost,
  },
  {
    path: "/login",
    name: "LoginPage",
    component: LoginPage,
  },
  {
    path: "/login/forgot",
    name: "ForgotPassword",
    component: ForgotPassword,
  },
  {
    path: "/login/passwordreset",
    name: "EnterNewPassword",
    component: EnterNewPassword,
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
    name: "PostPage",
    component: PostPage,
  },
  {
    path: "/communities/:id",
    name: "Community",
    component: Community,
  },
  {
    path: "/users/:id",
    name: "User",
    component: User,
  },
  {
    path: "/manage",
    name: "Manage",
    component: ManageCommunities,
  },
  {
    path: "/settings",
    name: "Settings",
    component: Settings,
  },
  {
    path: "/users/me/edit",
    name: "EditProfile",
    component: EditProfile,
  },
  {
    path: "/leave/:id",
    name: "Leave",
    component: LeaveCommunity,
  },
  {
    path: "/delete/:id",
    name: "Delete",
    component: DeleteCommunity,
  },
  {
    path: "*",
    name: "NotFound",
    component: NotFound,
  },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.name !== from.name) {
    // Direct user to login if they are not authenticated
    axios.get("/api/users/me").catch(() => {
      if (to.path !== "/register" && !to.path.includes("/login")) {
        return next({
          path: "/login",
        });
      }
    });
  }
  next();
});
export default router;
