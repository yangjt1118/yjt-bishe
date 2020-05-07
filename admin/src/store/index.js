
import Vue from 'vue';
import Vuex from 'vuex';
Vue.use(Vuex);
 
export default new Vuex.Store({
 
  state: {
    // 存储token
    Authorization: localStorage.getItem('Authorization') ? localStorage.getItem('Authorization') : ''
  },
/* actions: {
   changeLogin(ctx,Authorization){
     ctx.commit('changeLogin',Authorization);
   }
 },*/
  mutations: {
    // 修改token，并将token存入localStorage
    changeLogin (state,user) {
     state.Authorization = user.Authorization;
     console.log("store/index.js---到这里了!");
      localStorage.setItem('Authorization', user.Authorization);
    }
  }
});