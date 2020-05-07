<template>
  <div class="about">
    <van-row style="height:10%;background-color: rgba(0, 128, 128, 0.158);">
        <img src="../assets/logo.png" alt="" style="width:214.5px;height:54px;top:10px">
</van-row>
    <div style="height:80%">
      <van-form @submit="onSubmit" v-model="user">
       
        
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
          name="登录密码"
          label="登录密码"
          placeholder="请输入不小于六位的密码"
          :rules="[{ required: true, message: '请填写不少于六位的登录密码' }]"
        />
        <van-field
          v-model="user.paypassword"
          type="password"
          name="支付密码"
          label="支付密码"
          placeholder="请输入不小于六位的密码"
          :rules="[{ required: true, message: '请填写不少于六位的支付密码' }]"
        />
        <van-field name="user.gender" label="单选框">
          <template #input>
            <van-radio-group v-model="user.gender" direction="horizontal">
              <van-radio name="男">男</van-radio>
              <van-radio name="女">女</van-radio>
            </van-radio-group>
          </template>
        </van-field>
        <van-field
          v-model="user.phone"
          name="电话"
          label="电话"
          placeholder="电话"
          type="tel"
          :rules="[{ required: true, message: '请填写电话，电话格式是11位数字' }]"
        />
        <van-field
          v-model="user.address"
          name="地址"
          label="地址"
          placeholder="地址"
          :rules="[{ required: true, message: '请填写地址' }]"
        />
        <div style="margin: 16px;">
          <van-button
            round
            block
            type="info"
            native-type="submit"
            @click="dialog"
          >
            立即注册
          </van-button>
           <van-button
            round
            block
            type="primary"
            native-type="submit"
            style="margin-top:10px"
            to="/login"
          >
            返回登录页面
          </van-button>
          <!-- <van-button round block type="primary" color="linear-gradient(to right, #4bb0ff, #6149f6)" style="margin-top:10px" @click="register">
      注册
    </van-button> -->
        </div>
      </van-form>
    </div>
    
  </div>
</template>
<script>
export default {
  data() {
    return {
      user: {}
    };
  },
  methods: {
    onSubmit(values) {
      this.$http.post("user/register", this.user).then(res => {
        if (res.data.code == 200) {
          // this.$notify({ type: 'primary', message: '注册成功' });
          this.$dialog
            .confirm({
              title: "注册成功",
              message: "是否返回登录页面"
            })
            .then(() => {
              this.$router.push("/login");
            })
            .catch(() => {
              // on cancel
            });
          // this.$router.push("/index")
        } else {
          this.$notify({ type: "warning", message: res.data.msg });
        }
      });
    },
    dialog() {}
  }
};
</script>
<style>
.about {
  height: 100%;
}
</style>
