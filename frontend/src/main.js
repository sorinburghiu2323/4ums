import App from "./App.vue";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import Vue from "vue";
import router from "./router/router.js";

import {
  library,
} from "@fortawesome/fontawesome-svg-core";

// Regular style icons
import {
  faThumbsUp as farThumbsUp,
} from '@fortawesome/free-regular-svg-icons'
// Brand style icons
import {faFontAwesome} from "@fortawesome/free-brands-svg-icons";
// Solid style icons
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
  faMedal,
  faCrown,
  faTimes,
  faPlus,
  faChalkboardTeacher,
  faHandPeace,
} from "@fortawesome/free-solid-svg-icons";

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
    farThumbsUp,
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
    faPlus,
    faChalkboardTeacher,
    faHandPeace,
);
Vue.component("font-awesome-icon", FontAwesomeIcon);

Vue.component("font-awesome-icon", FontAwesomeIcon);
Vue.config.devtools = true;
Vue.config.productionTip = false;

// Cookie library
var VueCookie = require("vue-cookie");
Vue.use(VueCookie);
new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
