import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import axios from "axios";
import VueAxios from "vue-axios";

Vue.config.productionTip = false;

Vue.use(VueAxios, axios);
axios.defaults.baseURL = "http://127.0.0.1:5000/api";

new Vue({
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
