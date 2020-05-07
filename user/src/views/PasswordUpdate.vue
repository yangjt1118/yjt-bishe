<template>
  <div style="height:100%">
    <div>
      <van-nav-bar
        style=" background-color: white; color: white; font-size: 18px;;"
        title="修改密码"
        left-text="返回"
        left-arrow
        @click-left="onClickLeft"
        boder
        :fixed=true

      >
      </van-nav-bar>
    </div>
    <van-form @submit="onSubmit" v-model="user"  style="margin-top:46px">
      <van-field
        readonly
        clickable
        name="picker"
        :value="value"
        label="修改类型"
        placeholder="选择修改类型"
        @click="showPicker = true"
      />
      <van-popup v-model="showPicker" position="bottom">
        <van-picker
          show-toolbar
          :columns="columns"
          @confirm="onConfirm"
          @cancel="showPicker = false"
        />
      </van-popup>
      <van-field
        v-model="user.password"
        name="原密码"
        label="原密码"
        placeholder="输入原密码"
        type="password"
        :rules="[{ required: true, message: '请填写原密码' }]"
      />
      <van-field
        v-model="user.password2"
        name="新密码"
        label="新密码"
        placeholder="输入新密码"
        type="password"
        :rules="[{ required: true, message: '请填写新密码' }]"
      />
      <div style="margin: 16px;">
        <van-button round block type="info" native-type="submit">
          提交
        </van-button>
      </div>
    </van-form>
  </div>
</template>
<script>
//这里要俺需要引入，我不是一个对象
// import { isvalidPhone } from "../plugins/validate";
// //定义一个全局的变量，谁用谁知道
// var validPhone = (rule, value, callback) => {
//   if (!value) {
//     callback(new Error("请输入电话号码"));
//   } else if (!isvalidPhone(value)) {
//     callback(new Error("请输入正确的11位手机号码"));
//   } else {
//     callback();
//   }
// };
export default {
  data() {
    return {
            value: "",
      columns: ["修改登录密码","修改支付密码"],
      showPicker: false,
      user: {}
    };
  },
  mounted() {
    this.fench();
  },
  methods: {
    fench() {
      this.user2 = JSON.parse(sessionStorage.getItem("user"));
      // console.log("user2",this.user2)
      if (this.user2 == null) {
        this.$router.push("/login");
      }
    },
       onConfirm(value) {
      this.value = value;
      this.showPicker = false;
    },
    onSubmit(values) {
      // console.log("submit", this.user);
      if(this.value==="修改登录密码"){
        this.user.value="1"
      }else if(this.value==="修改支付密码"){
        this.user.value="2"
      }
      this.user.name = this.user2.name;

      // console.log(this.user,"user")
      this.$http.post("user/updatepassword", this.user).then(res => {
        if (res.data.code == 200) {
          // this.$notify({ type: "primary", message: "修改成功" });
          this.$toast.success('修改成功');
          this.user={}
          this.value=""
        } else {
          this.$toast({ icon: "cross", message: "修改失败，请重新输入" });
          this.user={}
          this.value=""
        }
      });
    },
      onClickLeft() {
        this.$router.push("/person1")
    },
  }
};
</script>
<style>
.header {
  height: 50px;
  background-color: teal;
  color: white;
  font-size: 18px;
  line-height: 50px;
}
</style>
