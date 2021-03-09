import App from "./App.vue";
import Vue from "vue";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {library} from "@fortawesome/fontawesome-svg-core";
import router from "./router/router.js";
Vue.component("font-awesome-icon", FontAwesomeIcon);

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
  faShareSquare,
  faSort,
  faStar,
  faThumbsUp,
  faTimesCircle,
  faTrophy,
  faUser,
  faUserSecret,
  faMedal,
  faCrown,
  faTimes,
  faPlus,
  faChalkboardTeacher,
  faHandPeace,
  faUsers,
  faShare,
} from "@fortawesome/free-solid-svg-icons";

// Add icons here after import
library.add(
    faUserSecret,
    faSort,
    faFontAwesome,
    faSearch,
    faCog,
    faTrophy,
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
    faPaperPlane,
    faTimes,
    faMedal,
    faCrown,
    faPlus,
    faChalkboardTeacher,
    faHandPeace,
    faUsers,
    faShare,
 )



Vue.config.devtools = true;
Vue.config.productionTip = false;

// Cookie library
var VueCookie = require("vue-cookie");
Vue.use(VueCookie);
new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
