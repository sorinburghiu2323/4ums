import ChangePassword from "../views/ChangePassword.vue";
import CommunitiesPage from "../views/CommunitiesPage.vue";
import Community from "../views/Community.vue";
import CreateCommunity from "../views/CreateCommunity.vue";
import CreatePost from "../views/CreatePost.vue";
import DeleteCheck from "../views/DeleteCheck.vue";
import Feed from "../views/Feed.vue";
import Leaderboard from "../views/Leaderboard.vue";
import LoginPage from "../views/LoginPage.vue";
import ManageCommunities from "../views/ManageCommunities.vue";
import EditProfile from "../views/EditProfile.vue";
import NotFound from "@/views/NotFound";
import PostPage from "@/views/PostPage";
import PreviewCommunity from "../views/PreviewCommunity.vue";
import Profile from "../views/Profile.vue";
import RegisterPage from "../views/RegisterPage.vue";
import Settings from "../views/Settings.vue";
import LeaveCommunity from "../views/LeaveCommunity.vue";
import DeleteCommunity from "@/views/DeleteCommunity";
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
    path: "/profile/delete",
    name: "DeleteCheck",
    component: DeleteCheck,
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
    path: "/changePassword",
    name: "ChangePassword",
    component: ChangePassword,
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
      path: '*',
      name: 'NotFound',
      component: NotFound,
  }
];

const router = new VueRouter({
  mode: "history",
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.name !== from.name) {
    // Direct user to login if they are not authenticated
    axios.get("/api/users/me").catch(() => {
      if (to.path !== "/login" && to.path !== "/register") {
        return next({
          path: "/login",
        });
      }
    });
  }
  next();
});
export default router;
