import {
  faAlignLeft,
  faArrowLeft,
  faCheckCircle,
  faCog,
  faCommentDots,
  faEdit,
  faHome,
  faPaperPlane,
  faPencilAlt,
  faQuestion,
  faQuestionCircle,
  faSearch,
  faShare,
  faShareSquare,
  faSort,
  faStar,
  faThumbsUp,
  faTimesCircle,
  faTrophy,
  faUser,
  faUsers,
  faUserSecret,
  faTimes,
  faMedal,
  faCrown,
} from "@fortawesome/free-solid-svg-icons";

import App from "./App.vue";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import Vue from "vue";
import {faFontAwesome} from "@fortawesome/free-brands-svg-icons";
import {library} from "@fortawesome/fontawesome-svg-core";
import router from "./router/router.js";

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
    faEdit,
    faStar,
    faShareSquare,
    faPaperPlane,
    faPencilAlt,
    faShare,
    faPaperPlane,
    faTimes,
    faMedal,
    faCrown,
);
Vue.component("font-awesome-icon", FontAwesomeIcon);

Vue.component("font-awesome-icon", FontAwesomeIcon);
Vue.config.devtools = true;
Vue.config.productionTip = false;

// Cookie library
var VueCookie = require("vue-cookie");
Vue.use(VueCookie);
//Particles
import Particles from "particles.vue";
Vue.use(Particles);
new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
