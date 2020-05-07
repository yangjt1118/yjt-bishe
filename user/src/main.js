import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Vant from 'vant';
import 'vant/lib/index.css';
import axios from 'axios';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// import Qs from 'qs'

// import VeeValidate, { Validator } from 'vee-validate'
// import zh_CN from 'vee-validate/dist/locale/zh_CN'


// Validator.localize('zh_CN', zh_CN)
// Vue.use(VeeValidate)

Vue.use(Vant,ElementUI);

Vue.config.productionTip = false
// Vue.prototype.$axios = axios;
Vue.prototype.$http=axios.create({
  baseURL:'http://localhost:5000',
  // transformRequest: [function (data, headers) {
  //   // Do whatever you want to transform the data
  //   return Qs.stringify(data);
  // }],
  // baseURL:'api'
})
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
