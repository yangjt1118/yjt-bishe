import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Home from '../views/Home.vue'
import PasswordUpdate from '../views/PasswordUpdate.vue'
import Person1 from '../views/Person1.vue'
import Shouye from '../views/Shouye.vue'

import UserUpdate from '../views/UserUpdate.vue'
import Index from '../views/Index.vue'
import Good from '../views/Good.vue'
import GoodBuy from '../views/GoodBuy.vue'
import Article from '../views/Article.vue'

import QueryCard from '../views/func/QueryCard.vue'
import AddCard from '../views/func/AddCard.vue'
import TransferHistory from '../views/func/TransferHistory.vue'
import Transfer from '../views/func/Transfer.vue'
import OrderHistory from '../views/func/OrderHistory.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Login.vue')
  },
  {
    path:'/login',
    name:"Login",
    component:Login
  },
  {
    path:'/register',
    name:"Register",
    component:Register
  },
  {
    path:'/index',
    name:"Index",
    component:Index,
    children:[
      {
        path:'/person1',
        name:"Person1",
        component:Person1,
        children:[
         
        ]
      },
      {
        path:'/shouye',
        name:"Shouye",
        component:Shouye,
      },
      {
        path:'/good',
        name:"Good",
        component:Good,
      }
    ]
  },
  {
    path:'/userupdate',
    name:"UserUpdate",
    component:UserUpdate,
  },
  {
    path:'/passwordupdate',
    name:"PasswordUpdate",
    component:PasswordUpdate,
  },
  {
    path:'/querycard',
    name:"QueryCard",
    component:QueryCard,
  },
  {
    path:'/addcard',
    name:"AddCard",
    component:AddCard,
  },
  {
    path:'/transferhistory',
    name:"TransferHistory",
    component:TransferHistory,
  },
  {
    path:'/orderhistory',
    name:"OrderHistory",
    component:OrderHistory,
  },
  {
    path:'/transfer',
    name:"Transfer",
    component:Transfer,
  },
  {
    path:'/article',
    name:"Article",
    component:Article,
  },
  {
    path:'/goodbuy',
    name:"GoodBuy",
    component:GoodBuy,
  },
  {
    path:'/home',
    name:"Home",
    component:Home,
  },
]

const router = new VueRouter({
  routes
})

export default router
