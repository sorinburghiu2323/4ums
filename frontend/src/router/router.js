import Communities from '../components/Communities.vue'
import Profile from '../components/Profile.vue'
import Leaderboard from '../components/Leaderboard.vue'
import Post from '../components/Post.vue'
import HomePage from "@/views/HomePage";
import LoginPage from "@/views/LoginPage";
import RegisterPage from "@/views/RegisterPage";
import CreateCommunity from "@/views/CreateCommunity";
import PreviewCommunity from "@/views/PreviewCommunity";


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
        path: '/communities/:id/posts:postId',
        name: 'Post',
        component: Post
    }
];

const router = new VueRouter({
    routes,
});

export default router;
