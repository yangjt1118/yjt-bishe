<template>
  <div class="hello">
    <div align="center" class="logoheight"><img class="imgmargin" src="@/assets/sunyard.png"></div>
    
<el-scrollbar wrap-class="scrollbar-wrapper">
<el-menu default-active="1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" :collapse="isCollapse"  text-color="#798197" active-text-color="#FFFFFF" background-color="#2B3141">
  <el-submenu index="1">
        <template slot="title" >
          <i class="el-icon-user-solid"></i>
          <span style="color:#FFFFFF">权限管理</span>
        </template>
          <el-menu-item index="1-1" @click="jigou()">机构管理</el-menu-item>
          <el-menu-item index="1-2" @click="yonghu()">用户管理</el-menu-item>
          <el-menu-item index="1-3" @click="jiaose()">角色管理</el-menu-item>
        <el-submenu index="1-4">
                  <template slot="title" style="color:#FFFFFF">菜单管理</template>
                  <el-menu-item index="1-4-1" @click="caidan()">模板管理</el-menu-item>
                  <el-menu-item index="1-4-2" @click="yemian()">页面管理</el-menu-item>
                  <el-menu-item index="1-4-3" @click="anniu()">按钮管理</el-menu-item>
        </el-submenu>
      </el-submenu>
      <el-submenu index="2">
        <template slot="title">
          <i class="el-icon-setting"></i>
          <span style="color:#FFFFFF">参数管理</span>
        </template>
        <el-menu-item index="2-1" @click="quanju()">全局参数</el-menu-item>
          <el-menu-item index="2-2" @click="moban()">模板管理</el-menu-item>
          <el-menu-item index="2-3" @click="renwu()">任务管理</el-menu-item>
          <el-menu-item index="2-4" @click="zidian()">字典维护</el-menu-item>
      </el-submenu>
</el-menu>
</el-scrollbar>
  </div>
</template>

<script>
/* eslint-disable */
// import imgUrl from 'src/assets/sunyard.png'
export default {
	props:['isCollapse'],
	data() {
      return {
        //  imgUrl:require("src/assets/sunyard2.png"),
        // imgUrl:imgUrl,
        menuData:[{
        	title_p : '导航一'
        },{
        	title_p : '用户管理',
        	menuItemData:[{
        		title_c : '会员管理',
        		path : '/user/userManage'
        	},{
        		title_c : '收获地址',
        		path : '/user/address'
        	}]
        }],
        index:''
      };
    },
    created(){
      console.log('111')
      localStorage.setItem('index',this.index)
    },
    methods: {
      handleOpen() {
      },
      handleClose() {
      },
      jigou(e){
        
        // localStorage.setItem('index','1-1')
        this.$router.push({path:'/user/userManage'});
      },
      yonghu(){
        this.$router.push({path:'/user/yonghu'});
      },
      jiaose(){
        this.$router.push({path:'/user/jiaose'});
      },
      caidan(){
        this.$router.push({path:'/user/caidan'});
      },
      yemian(){
        this.$router.push({path:'/user/yemian'});
      },
      anniu(){
        this.$router.push({path:'/user/anniu'});
      },
      quanju(){
        this.$router.push({path:'/user/quanju'});
      },
      moban(){
        this.$router.push({path:'/user/moban'});
      },
      renwu(){
        this.$router.push({path:'/user/renwu'});

      },
      zidian(){
        this.$router.push({path:'/user/zidian'});
      }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
  }
.hello{
  background: #2B3141
}
.logoheight{
  height: 50px;
  
}
.imgmargin{
    margin: 13px 0px;
}
.el-submenu .el-menu-item {
    height: 40px;
    line-height: 40px;
    padding: 0 45px;
    min-width: 200px;
}
.el-submenu__title {
    font-size: 14px;
    padding: 0 20px;
    cursor: pointer;
    transition: border-color .3s,background-color .3s,color .3s;
    box-sizing: border-box;
    height: 40px!important;
    line-height: 40px!important;
    position: relative;
    white-space: nowrap;
    list-style: none;
}
/* .el-menu{
	border-right: none; 
    list-style: none;
    position: relative;
    margin: 0;
    padding-left: 0;
    background-color: #FFF;
}
.el-menu-vertical-demo{
  width: 200px;
}
.el-menu-item {
  padding-left: 50px!important;
} */
</style>
