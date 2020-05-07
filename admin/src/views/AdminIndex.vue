<template>
  <div style="height:100%;width:100%;background-color:">
    <el-container style="height:100%">
      <el-header class="hearbg" style="background-color:#2B3141" >
        <el-row  :gutter="20">
  <el-col :span="22" style="margin-top:8px">
    
         <img src="../assets/logo.png" style="width:200px" alt=""></el-col>
  <el-col :span="2">
    <img src="../assets/touxiang.png" style="margin-top:20px;margin-right:5px" alt="">
    <img src="../assets/exit.png" alt="" style="margin-top:10px" @click="exit" /></el-col>
</el-row>
        
        
      </el-header>
      <el-container style="height:100%;background-color:#F8F8F8">
        <el-aside style="height:100%;width:210px" class="aside">
          <el-menu
            default-active="1"
            class="el-menu-vertical-demo"
            router
            background-color="#2B3141"
            text-color="#fff"
            active-text-color="#ffd04b"
          >
            <el-submenu index="1">
              <template slot="title">
                <i class="el-icon-user"></i>
                <span>用户管理</span>
              </template>
              <el-menu-item index="/adminopuser">用户管理</el-menu-item>
            </el-submenu>
            <el-submenu index="2">
              <template slot="title">
                <i class="el-icon-document"></i>
                <span>银行资讯管理</span>
              </template>
              <el-menu-item index="/adminarticlelist">资讯列表</el-menu-item>
              <el-menu-item index="/adminarticleadd">资讯发表</el-menu-item>
            </el-submenu>
            <el-submenu index="3">
              <template slot="title">
                <i class="el-icon-document"></i>
                <span>理财产品</span>
              </template>
              <el-menu-item index="/admingoodlist">理财产品列表</el-menu-item>
              <el-menu-item index="/admingoodadd">新增理财产品</el-menu-item>
            </el-submenu>
          </el-menu>
        </el-aside>
        <el-main
          ><el-card><router-view></router-view></el-card
        ></el-main>
      </el-container>
    </el-container>
  </div>
</template>
<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
.aside {
}
.headbg {
  background-color: rgb(97, 90, 90);
}
.aside ul {
  height: 100%;
}
</style>

<script>
export default {
  data() {
    return {
      user: {
        name: "",
      },
      user2: {},
    };
  },
  mounted() {
    this.fench();
  },
  methods: {
    fench() {
      this.user2 = JSON.parse(sessionStorage.getItem("admin"));
      if (this.user2 == null) {
        this.$router.push("/login");
      }
    },
    exit() {
      console.log(222);
      sessionStorage.clear();
      this.fench();
    },
    // handleOpen(key, keyPath) {
    //   console.log(key, keyPath);
    // },
    // handleClose(key, keyPath) {
    //   console.log(key, keyPath);
    // }
  },
};
</script>
