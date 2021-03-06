import Vue from "vue";
import App from "./App.vue";
import router from "./router/router.js";
// Fontawesome documentation: https://www.npmjs.com/package/@fortawesome/vue-fontawesome
// Regular style icons
import {library} from "@fortawesome/fontawesome-svg-core";
// Brand style icons
import {faFontAwesome} from "@fortawesome/free-brands-svg-icons";
// Solid style icons
import {
  faAlignLeft,
  faArrowLeft,
  faCheckCircle,
  faCog,
  faCommentDots,
  faHome,
  faPaperPlane,
  faQuestion,
  faQuestionCircle,
  faSearch,
  faSort,
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
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";

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
);
Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.component("font-awesome-icon", FontAwesomeIcon);
Vue.config.devtools = true;
Vue.config.productionTip = false;

// Cookie library
var VueCookie = require('vue-cookie');
Vue.use(VueCookie);
new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
