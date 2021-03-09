import App from "./App.vue";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import Vue from "vue";
import {faFontAwesome} from "@fortawesome/free-brands-svg-icons";
import {library} from "@fortawesome/fontawesome-svg-core";
import router from "./router/router.js";

Vue.component("font-awesome-icon", FontAwesomeIcon);

import {
    faAlignLeft,
    faArrowLeft,
    faCheckCircle,
    faCog,
    faCommentDots,
    faCrown,
    faEdit,
    faHome,
    faMedal,
    faPaperPlane,
    faPencilAlt,
    faQuestion,
    faQuestionCircle,
    faSearch,
    faShareSquare,
    faSort,
    faStar,
    faThumbsUp,
    faTimes,
    faTimesCircle,
    faTrophy,
    faUser,
    faUserSecret,
    faUsers,
    faShare,
    faLink,
} from "@fortawesome/free-solid-svg-icons";

// Fontawesome documentation: https://www.npmjs.com/package/@fortawesome/vue-fontawesome
// Regular style icons

// Brand style icons

// Solid style icons

// Add icons here after import
library.add(
    faUserSecret,
    faSort,
    faFontAwesome,
    faSearch,
    faCog,
    faTrophy,
    faUsers,
    faUser,
    faHome,
    faQuestion,
    faAlignLeft,
    faTimesCircle,
    faCommentDots,
    faArrowLeft,
    faThumbsUp,
    faQuestionCircle,
    faCheckCircle,
    faPaperPlane,
    faTimes,
    faMedal,
    faCrown,
    faEdit,
    faShareSquare,
    faStar,
    faPencilAlt,
    faShare,
    faLink,
);


Vue.config.devtools = true;
Vue.config.productionTip = false;

import Clipboard from 'v-clipboard';
Vue.use(Clipboard);
// Cookie library
var VueCookie = require("vue-cookie");
Vue.use(VueCookie);
new Vue({
    router,
    render: (h) => h(App),
}).$mount("#app");
