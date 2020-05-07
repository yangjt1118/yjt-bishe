<template>
  <div style="height:100%">
    <el-container style="height:100%; border: 1px solid #eee">
      <el-header class="header1" style="background:#88ada6">
        <!-- <Heade></Heade> -->
      </el-header>
      <el-container>
        <el-aside
          width="202px"
          style="height:100%;background-color: #299ecc11"
        >
          <el-menu
            router
            default-active="/userquery"
            class="el-menu-vertical-demo"
          >
            <el-submenu index="1">
              <template slot="title">
                <i class="el-icon-user"></i>
                <span>个人信息</span>
              </template>
              <el-menu-item index="/userquery">信息查看</el-menu-item>
              <el-menu-item index="/userupdata">信息修改</el-menu-item>
              <el-menu-item index="/userpwdupd">密码更改</el-menu-item>
              <el-menu-item index="/usercard">银行卡管理</el-menu-item>
            </el-submenu>
            <el-submenu index="2">
              <template slot="title">
                <i class="el-icon-document"></i>
                <span>转账</span>
              </template>
              <el-menu-item index="/transfer">转账</el-menu-item>
              <el-menu-item index="/transferhistory">转账历史</el-menu-item>
            </el-submenu>
            <el-submenu index="3">
              <template slot="title">
                <i class="el-icon-document"></i>
                <span>文章</span>
              </template>
              <el-menu-item index="/userarticlelist">文章列表</el-menu-item>
              <!-- <el-menu-item index="/userarticle">文章详情</el-menu-item> -->
            </el-submenu>
            <el-submenu index="4">
              <template slot="title">
                <i class="el-icon-document"></i>
                <span>商品</span>
              </template>
              <el-menu-item index="/usergoods">商品列表</el-menu-item>
              <el-menu-item index="/userorderlist">历史订单</el-menu-item>
            </el-submenu>
          </el-menu>
        </el-aside>
        <el-main style="padding:20px;height:100%">
          <div class="main"><router-view></router-view></div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>
<script>
// import Heade from "../components/header"
export default {
  // component:{
  //   Heade
  // },
  data(){
    return {
      user:{
        name:""
      },
      user2:{
        
      }
    }
  },
  mounted() {
    this.fench()
  },
  methods: {
    fench(){
      this.user2 = JSON.parse(sessionStorage.getItem("user"));
      this.user.name = this.user2.name;
      if (this.user2==null){
            this.$router.push("/login")
        }
    }
  },
}
</script>
<style>
html,
body {
  padding: 0px;
  margin: 0px;
    height: 100%;
  width: 100%;
  background: white;
}
.el-header {
  background-color: #b3c0d1;
  color: #333;
  /* line-height: 60px; */
}

.el-aside {
  color: #333;
}
.main{
  background-color: #299ecc11;
  height: 100%;
  padding: 20px;
}
</style>

<script>
export default {
  // isCollapse: true
};
</script>
