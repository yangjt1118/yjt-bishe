import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import axios from 'axios';
import store from './store'
import moment from 'moment';
import echarts from 'echarts'
Vue.prototype.$echarts = echarts
//引入mock
// require("./axios/mock")
Vue.config.productionTip = false
Vue.prototype.$http=axios.create({
  baseURL:'http://localhost:5000'
  // baseURL:'api'
})
Vue.prototype.$moment = moment;
//异步请求前在header里加入token


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
//异步请求前在header里加入token
axios.interceptors.request.use(
  config => {
    if(config.url==='/login'||config.url==='/'){  //如果是登录和注册操作，则不需要携带header里面的token
    }else{
      if (localStorage.getItem('Authorization')) {
        config.headers.Authorizatior = localStorage.getItem('Authorization');
      }
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  });
//异步请求后，判断token是否过期
axios.interceptors.response.use(
  response =>{
    return response;
  },
  error => {
    if(error.response){
      switch (error.response.status) {
        case 401:
          localStorage.removeItem('Authorization');
          this.$router.push('/');
      }
    }
  }
)
//异步请求前判断请求的连接是否需要token
router.beforeEach((to, from, next) => {
  if (to.path === '/userindex') {
    next();
  } else {
    let token = localStorage.getItem('Authorization');
    console.log("我是浏览器本地缓存的token: "+token);
    if (token === 'null' || token === '') {
      next('/');
    } else {
      next();
    }
  }
});