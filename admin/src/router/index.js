import Vue from 'vue'
import VueRouter from 'vue-router'
import UserIndex from '../views/UserIndex.vue'
import AdminIndex from '../views/AdminIndex.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import UserCard from '../views/UserCard.vue'
import UserQuery from '../views/UserQuery.vue'
import Userpwdupd from '../views/Userpwdupd.vue'
import UserUpdata from '../views/UserUpdata.vue'
import Transfer from '../views/Transfer.vue'
import TransferHistory from '../views/TransferHistory.vue'
import UserArticle from '../views/UserArticle.vue'
import UserArticleList from '../views/UserArticleList.vue'
import UserGoods from '../views/UserGoods.vue'
import UserOrderList from '../views/UserOrderList.vue'
import AdminOpUser from '../views/AdminOpUser.vue'
import AdminArticleList from '../views/AdminArticleList.vue'
import AdminArticleAdd from '../views/AdminArticleAdd.vue'
import AdminGoodList from '../views/AdminGoodList.vue'
import AdminGoodAdd from '../views/AdminGoodAdd.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect:'/login'
  },
  {
    path: '/login',
    component:Login
  },
  {
    path: '/register',
    component:Register
  },
  {
    path: '/userindex',
    name: 'UserIndex',
    component:UserIndex,
    meta: {
      requireAuth: true,  // 添加该字段，表示进入这个路由是需要登录的
    },
    children:[
      {
        path: '/userquery',
        name: 'UserQuery',
        component: UserQuery
      },
      {
        path: '/userupdata',
        name: 'UserUpdata',
        component: UserUpdata
      },
      {
        path: '/userpwdupd',
        name: 'Userpwdupd',
        component: Userpwdupd
      },
      {
        path: '/usercard',
        name: 'UserCard',
        component: UserCard
      },
      {
        path: '/transfer',
        name: 'Transfer',
        component: Transfer
      },
      {
        path: '/transferhistory',
        name: 'TransferHistory',
        component: TransferHistory
      },
      {
        path:'/userarticlelist',
        name:'UserArticleList',
        component:UserArticleList,
      },
      {
        path:'/userarticle',
        name:'UserArticle',
        component:UserArticle,
      },
      {
        path:'/usergoods',
        name:'UserGoods',
        component:UserGoods,
      },
      {
        path:'/userorderlist',
        name:'UserOrderList',
        component:UserOrderList,
      },
    ]
  },
  {
    path: '/adminindex',
    name: 'AdminIndex',
    component:AdminIndex,
    meta: {
      requireAuth: true,  // 添加该字段，表示进入这个路由是需要登录的
    },
    children:[
     {
       path:'/adminopuser',
       name: 'AdminOpUser',
       component:AdminOpUser,
     },
     {
      path:'/adminarticlelist',
      name: 'AdminArticleList',
      component:AdminArticleList,
    },
    {
      path:'/adminarticleadd',
      name: 'AdminArticleAdd',
      component:AdminArticleAdd,
    },
    {
      path:'/admingoodlist',
      name: 'AdminGoodList',
      component:AdminGoodList,
    },
    {
      path:'/admingoodadd',
      name: 'AdminGoodAdd',
      component:AdminGoodAdd,
    }
    ]
  },
]
// 使用 router.beforeEach 注册一个全局前置守卫，判断用户是否登陆
// router.beforeEach((to, from, next) => {
//   if (to.path === '/login') {
//     next();
//   } else {
//     let token = localStorage.getItem('Authorization');
 
//     if (token === 'null' || token === '') {
//       next('/login');
//     } else {
//       next();
//     }
//   }
// });
const router = new VueRouter({
  routes
})

export default router
