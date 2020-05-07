<template>
  <div class="hello">
<el-scrollbar wrap-class="scrollbar-wrapper">
<el-menu default-active="1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" :collapse="isCollapse"  text-color="#bfcbd9" active-text-color="#409EFF">
  <!-- <el-submenu index="1" >
    <template slot="title">
      <i class="el-icon-location"></i>
      <span slot="title">导航一</span>
    </template>
    <el-submenu index="1-4">
      <span slot="title">用户管理</span>
      <el-menu-item index="1-4-1">会员管理</el-menu-item>
      <el-menu-item index="1-4-1">收货地址</el-menu-item>
      <el-menu-item index="1-4-1">会员收藏</el-menu-item>
    </el-submenu>
  </el-submenu> -->
  
  <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-user-solid"></i>
          <span>权限管理1</span>
        </template>
        <el-menu-item-group>
          <!-- <template slot="title">分组一</template> -->
          <el-menu-item index="1-1" @click="jigou()">机构管理</el-menu-item>
          <el-menu-item index="1-2" @click="yonghu()">用户管理</el-menu-item>
          <el-menu-item index="1-3" @click="jiaose()">角色管理</el-menu-item>
          <el-menu-item index="1-4" @click="caidan()">菜单管理</el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <el-submenu index="2">
        <template slot="title">
          <i class="el-icon-setting"></i>
          <span>参数管理</span>
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
export default {
	props:['isCollapse'],
	data() {
      return {
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
</style>
