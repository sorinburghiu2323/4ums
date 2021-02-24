import Vue from "vue";
import App from "./App.vue";
import router from "./router/router.js";
// Fontawesome documentation: https://www.npmjs.com/package/@fortawesome/vue-fontawesome

// Regular style icons
import { library } from "@fortawesome/fontawesome-svg-core";
// Brand style icons
import { faFontAwesome } from "@fortawesome/free-brands-svg-icons";
// Solid style icons
import {
  faUserSecret,
  faSort, 
  faSearch,
  faCog,
  faTrophy,
  faUser,
  faUsers,
  faHome,
  faQuestion,
  faAlignLeft,
  faTimesCircle,
  faCommentDots,
  faArrowLeft,
  faThumbsUp,
} from "@fortawesome/free-solid-svg-icons";

import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

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
);

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.component("font-awesome-icon", FontAwesomeIcon);

Vue.config.productionTip = false;

// Cookie library
var VueCookie = require('vue-cookie');
Vue.use(VueCookie);

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
