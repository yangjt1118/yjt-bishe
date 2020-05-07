<template>
	<div class="app-wrapper">
  <el-container style="height:100%">
	<el-aside :width="asideWidth" style="height:100%;background:#2B3141"><sidebar :isCollapse='isCollapse'></sidebar></el-aside>

  <el-container v-if="but">
    <el-header height="50px" class="backcol"><heade  @changehead="changehead" ></heade></el-header>

    <el-main class="pad"><router-view/><navbar  :isCollapse='isCollapse'></navbar></el-main>
  </el-container>
  <el-container v-else>
	<el-header height="50px" class="backcol"><heade @changehead="changehead" ></heade></el-header>
    <el-main class="pad"><router-view/><navbar  :isCollapse='isCollapse'></navbar></el-main>
  </el-container>
</el-container>
</div>
</template>

<script>
/* eslint-disable */
import Sidebar from "./components/Sidebar";
import Sidebar1 from "./components/Sidebar1";

import Navbar from "./components/Navbar";
import heade from "./components/heade";/*  */
export default{
	data() {
	    return {
	      isCollapse: false,
		  asideWidth:'200px',
		  but:true,
		  leftright:''
	    }
    },
	components: {
	    Sidebar,
		Navbar,
		heade,
	    Sidebar1,
	},
	mounted(){
		// this.rolepermission()
	},
  	methods: {
	//    changeSidebar(data){
	//    		this.isCollapse = data
	//    		if(data == true){
	//    			this.asideWidth = '64px'
	//    		}else{
	//    			this.asideWidth = '200px'
	//    		}
	//    },
	   changehead(data){
		   if(data==true||data==false){
		   this.but =data
		   this.$router.push({path:'/layout'});
		   }else{
			   if(data=='right'){
				   this.isCollapse=true
				   this.asideWidth = '64px'
			   }else{
				   this.isCollapse=false
	   				this.asideWidth = '200px'
			   }
		   }
	   },
	   //角色权限管理接口
	//    rolepermission(){
    //     let data={
	// 			"head":{
	// 				"userId":"00000001",
	// 				"orgId":"1",
	// 				"channelId":"1",
	// 				"ip":"127.0.0.1"
	// 			},
	// 			"body":{
	// 				"roleNum":"7",
	// 				"permissionGrade":"0",
	// 				"menuChannel":"0",
	// 				"routeId":"4"
	// 			}
	// 		}
    //     this.$axios({
    //           url:'./api/manage/select/rolepermission.do',
    //           method: 'post',
    //           data: data,
    //           headers:{
    //             'Content-Type':'application/json',
    //             'token':sessionStorage.getItem('token')
    //           }
    //           })
    //           .then(respanse=>{
    //           console.log(respanse);
    //           console.log(respanse.data.code)
    //             if(respanse.data.code=='0'){
    //                     this.$message({
    //                     message: '操作成功',
    //                     type: 'success'
    //                   });
    //           }else if(respanse.data.code=='20002') {
    //                     this.$message.error(
    //                     '账号不存在或密码错误',
    //                   );
    //           }
    //           })
    //   },
	}
}
</script>
<style type="text/css" scoped>
	.app-wrapper{
		height: 100%
	}
	/* .pad{
		padding: 0px!important
	} */
	.backcol{
		 background: #FFFFFF;
    height:50px;
    box-shadow:0px 2px 12px 0px rgba(188,188,188,0.5);
	}
	.el-main {
    display: block;
    -webkit-box-flex: 1;
    /* -ms-flex: 1; */
    flex: 1;
    /* -ms-flex-preferred-size: auto; */
    flex-basis: auto;
    overflow: auto;
    /* -webkit-box-sizing: border-box; */
    box-sizing: border-box;
    padding: 20px;
	padding-bottom:0px !important;
    background: #f8f8f8;
}

</style>