<template>
  <div class="app1">
    <!-- <div style="height:8%;background-color:white"><heade1></heade1></div> -->
    <div class="box2">
      <div class="box3" >
        <img src="../assets/logo.png" class="box4" alt="">
        <div class="divider"></div>
      <el-form ref="user" :model="user" label-width="80px">
  <el-form-item label="账号">
    <el-input v-model="user.name"></el-input>
  </el-form-item>
  <el-form-item label="密码">
    <el-input v-model="user.password" show-password></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="login1">登录</el-button>
    <el-button @click="register">初始化账号</el-button>
  </el-form-item>
</el-form>
    </div>
    </div>
    <div style="height:7%"></div>
  </div>
</template>
<script>
// import heade1 from "../components/header"
import { mapMutations } from "vuex";
export default {
  // components:{
  //   heade1
  // },
  data() {
    return {
      activeName: "first",
      labelPosition: "right",
      user: {
        name: "",
        password: ""
      },
      userToken: ""
    };
  },
  methods: {
    ...mapMutations(["changeLogin"]),
    handleClick(tab, event) {
      console.log(tab, event);
    },
    login() {
      let _this = this;
      console.log(_this.user);
      this.$http
        .post("user/login", _this.user)
        .then(res => {
          if (res.data.code == 200) {
            sessionStorage.setItem("user", JSON.stringify(res.data.data));
            this.$message({
              message: "登录成功",
              type: "success"
            });
            // console.log(res.data.data.token)
            _this.userToken = "Bearer " + res.data.data.token;
            console.log(_this.userToken, 111); //获取到的token
            _this.changeLogin({ Authorization: _this.userToken });
            this.$router.push("/userquery");
          } else {
            console.log(res.data.data)
            this.$message({
              message: res.data.msg,
              type: "error"
            });
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
     login1() {
      let _this = this;
      console.log(_this.user,1111);
      this.$http
        .post("admin/login", _this.user)
        .then(res => {
          if (res.data.code == 200) {
            sessionStorage.setItem("admin", JSON.stringify(res.data.data));
            this.$message({
              message: "登录成功",
              type: "success"
            });
            // console.log(res.data.data.token)
            _this.userToken = "Bearer " + res.data.data.token;
            console.log(_this.userToken, 111); //获取到的token
            _this.changeLogin({ Authorization: _this.userToken });
            this.$router.push("/adminopuser");
          } else {
            console.log(res.data.data)
            this.$message({
              message: res.data.msg,
              type: "error"
            });
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    register() {
      this.$http.get("admin/init").then(res=>{
        if(res.data.code==200){
          this.$message({
              message: "初始化管理员成功，账号密码分别为admin default",
              type: "success"
            });
        }else{
          this.$message({
              message: "已初始化，账号密码分别为admin default",
              type: "success"
            });
        }
      })
      // console.log(222);
      // this.user.name = "";
      // this.user.password = "";
      // this.$router.push("/register");
    }
  }
};
</script>

<style>
html,
body {
  padding: 0px;
  margin: 0px;
  height: 100%;
  width: 100%;
  background: url("../assets/666.jpg") no-repeat center center;
  background-size:100% 100%;
}

.box {
  /* position: absolute; */
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
    width:400px;
    height: 320px;
    background:rgba(0,0,0,.5);
	box-sizing:border-box;
	box-shadow:0 15px 25px rgba(0,0,0,.5);
	border-radius: 10px;/*登录窗口边角圆滑*/
}
.box .inputBox input
{
	width: 100%;
	padding: 10px 0;
	/* font-side:16px; */
	color: #fff;
	/* letter-spacing: 1px; */
	margin-bottom:10px;
	border:none;
	border-bottom:1px solid #fff;
	outline:none;
	background:transparent;
}
.box .inputBox label
{
    /* position: absolute; */
    top: 0;
    left: 0;
    padding: 10px 0;
    font-size: 16px;
    color: #fff;
    pointer-events: none;
    transition: .5s;
}
.app1{
  height: 100%;
}
.box2{
  width: 100%;
  /* background-color: teal; */
  height: 85%;
  position: relative;
}
.box3 {
    position: absolute;
    padding: 20px;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
    width:400px;
    /* height: 600px; */
    background:rgb(229, 233, 233);
	box-sizing:border-box;
	box-shadow:0 15px 25px rgba(0,0,0,.5);
	border-radius: 10px;/*登录窗口边角圆滑*/
}
.box4 {
  width: 300px;
}
.divider {
      display: block;
    height: 1px;
    width: 100%;
    margin-bottom: 10px;
    background-color: rgb(190, 207, 247)
}
</style>
