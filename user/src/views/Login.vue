<template>
  <div class="about">
      <van-row style="height:10%;background-color: rgba(0, 128, 128, 0.158);">
        <img src="../assets/logo.png" alt="" style="width:214.5px;height:54px;top:10px">
</van-row>
 <div class="loginMain">
      <van-form @submit="onSubmit" v-model="user" class="form" >
  <van-field
    v-model="user.name"
    name="用户名"
    label="用户名"
    placeholder="用户名"
    :rules="[{ required: true, message: '请填写用户名' }]"
  />
  <van-field
    v-model="user.password"
    type="password"
    name="密码"
    label="密码"
    placeholder="密码"
    :rules="[{ required: true, message: '请填写密码' }]"
  />
  <div style="margin: 16px;">
    <van-button round block type="info" native-type="submit">
      登录
    </van-button>
    <div class="tozhuce">没有账号？立即注册</div>
    <van-button round block type="primary" style="margin-top:10px" @click="register">
      注册
    </van-button>
  </div>
</van-form>
<!-- <div><img src="" alt=""> </div> -->
 </div>
 

  </div>
</template>
<script>
export default {
  data() {
    return {
      user:{}
    };
  },
  methods: {
    onSubmit(values) {
      this.$http.post("user/login",this.user)
      .then(res=>{
        if (res.data.code == 200) {
            sessionStorage.setItem("user", JSON.stringify(res.data.data));
            this.$notify({ type: 'primary', message: '登录成功' });
            this.$router.push("/shouye")
            // console.log('submit', values);
        }else {
            this.$notify({ type: 'warning', message: res.data.msg });
          }
      })
    },
    register(){
        this.$router.push("/register")
    }
  },
};
</script>
<style>
  .about{
    height:100%
  }
  .van-cell {
    background-color: brown;
  }
  .form {
    /* background-color: brown; */
    /* position: absolute; */
    /* opacity:0.5 */
  }
  .loginMain {
    height: 84%;
    /* background-color: aqua; */
    /* background: url("../assets/loginBg.jpg") no-repeat center center; */
  }
  .footerrr {
    background-color: rgba(0, 128, 128, 0.158);
    height: 10%;
  }
  .tozhuce {
    color: grey;
    font-size: 12px;
  }
</style>