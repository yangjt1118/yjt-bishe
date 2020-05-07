<template>
  <div style="height:100%">
    <div>
      <van-nav-bar
        style=" background-color: white; color: white; font-size: 18px;;"
        title="修改基本信息"
        left-text="返回"
        left-arrow
        @click-left="onClickLeft"
        boder
                :fixed=true

      >
      </van-nav-bar>
    </div>
    <van-form @submit="onSubmit" v-model="user" style="margin-top:46px">
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
        :rules="[{ required: true, message: '请填写电话' }]"
      />
      <van-field
        v-model="user.address"
        name="地址"
        label="地址"
        placeholder="地址"
        :rules="[{ required: true, message: '请填写地址' }]"
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
import { isvalidPhone } from "../plugins/validate";
//定义一个全局的变量，谁用谁知道
var validPhone = (rule, value, callback) => {
  if (!value) {
    callback(new Error("请输入电话号码"));
  } else if (!isvalidPhone(value)) {
    callback(new Error("请输入正确的11位手机号码"));
  } else {
    callback();
  }
};
export default {
  data() {
    return {
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
      this.user.name = this.user2.name;
      // console.log(this.user);
      this.$http.post("user/query", this.user).then(res => {
        if (res.data.code == 200) {
          this.user = res.data.data;
        }
      });
    },
    onSubmit(values) {
      // console.log("submit", this.user);
      this.user.name = this.user2.name;

      this.$http.post("user/update", this.user).then(res => {
        if (res.data.code == 200) {
          // this.$notify({ type: "primary", message: "修改成功" });
          this.$toast.success('修改成功');
        } else {
          // console.log(res.data.data)
          this.$toast.success('修改失败');
          // this.user=this.user2
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
