<template>
  <div style="height:100%">
    <div>
      <van-nav-bar
        style=" background-color: white; color: white; font-size: 18px;;"
        title="转账汇款"
        left-text="返回"
        left-arrow
        @click-left="onClickLeft"
        boder
        :fixed="true"
      >
      </van-nav-bar>
    </div>
    <van-form @submit="onSubmit" v-model="form" style="margin-top:46px">
      <van-field
        readonly
        clickable
        name="picker"
        :value="value"
        label="卡号"
        placeholder="选择卡号"
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
        v-model="form.mount"
        name="转账金额"
        label="转账金额"
        placeholder="转账金额"
        type="number"
        :rules="[{ required: true, message: '请输入转账金额' }]"
      />
      <van-field
        v-model="form.dcard"
        name="对方卡号"
        label="对方卡号"
        placeholder="对方卡号"
        type="digit"
        :rules="[{ required: true, message: '请输入对方卡号' }]"
      />
      <van-field
        v-model="form.dname"
        name="对方姓名"
        label="对方姓名"
        placeholder="对方姓名"
        :rules="[{ required: true, message: '请对方姓名' }]"
      />
      <van-field
        v-model="form.paypassword"
        type="password"
        name="支付密码"
        label="支付密码"
        placeholder="支付密码"
        :rules="[{ required: true, message: '请输入支付密码' }]"
      />
      <div style="margin: 16px;">
        <van-button round block type="info" native-type="submit">
          立即转账
        </van-button>
        <van-button
          style="margin-top:10px"
          round
          block
          type="primary"
          native-type="submit"
          to="/transferhistory"
        >
          查看转账记录
        </van-button>
      </div>
    </van-form>
  </div>
</template>
<script>
export default {
  data() {
    return {
      form: {},
      value: "",
      columns: [],
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
      this.user.name = this.user2.name;
      this.$http.post("user/querycard", this.user).then(res => {
        if (res.data.code == 200) {
          this.na = res.data.data.map(function(v) {
            return v.card_id;
          });
          this.columns = this.na;
        }
      });
    },
    onSubmit(values) {
      this.form.name = this.user2.name;
      this.form.scard = this.value.toString();
      this.$http
        .post("user/transfer", this.form)
        .then(res => {
          if (res.data.code == 200) {
            this.$toast({ message: "转账成功", icon: "success" });
            this.form = {};
            this.value = "";
          } else {
            this.$toast({ message: res.data.msg, icon: "cross" });
            // this.form = {};
            // this.value = "";
          }
        })
        .catch(res => {
          this.$toast({ message: res.data.msg, icon: "cross" });
          this.form = {};
          this.value = "";
        });
    },
    onConfirm(value) {
      this.value = value;
      this.showPicker = false;
    },
    onClickLeft() {
      this.$router.push("/Shouye");
    }
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
