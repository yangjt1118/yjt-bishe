<template>
  <div style="height:100%;background-color:#f8f8f8;">
    <div>
      <van-nav-bar
        style=" background-color: white; color: white; font-size: 18px;;"
        title="新增银行卡"
        left-text="返回"
        left-arrow
        @click-left="onClickLeft"
        boder
        :fixed=true
      >
      </van-nav-bar>
      <van-form @submit="onSubmit" v-model="card" style="margin-top:46px">
        <!-- <van-field v-model="text" label="文本" /> -->
        <!-- 输入手机号，调起手机号键盘 -->
        <!-- <van-field v-model="tel" type="tel" label="手机号" /> -->
        <!-- 允许输入正整数，调起纯数字键盘 -->
        <van-field v-model="card.card_id" type="digit" label="卡号" :rules="[{ required: true, message: '请输入六位数的卡号' }]"  />
        <!-- <van-number-keyboard
v-model="card.card_id"
  :show="show"
  extra-key="."
  close-button-text="完成"
  @blur="show = false"
/> -->
        <!-- 允许输入数字，调起带符号的纯数字键盘 -->
        <van-field v-model="card.balance" type="number" label="余额" :rules="[{ required: true, message: '请输入余额' }]" />

        <!-- 输入密码 -->
        <!-- <van-field v-model="password" type="password" label="密码" /> -->
        <div style="margin: 16px;">
          <van-button round block type="info" native-type="submit">
            添加银行卡
          </van-button>
          <van-button round block style="margin-top:10px"   type="primary" native-type="submit" to="/querycard">
            查看我的账户
          </van-button>
        </div>
      </van-form>
      
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      show: false,
      show1: false,
      card: {},
      user2:{}
    };
  },
  methods: {
    onClickLeft() {
      this.$router.push("/Shouye");
    },
    onSubmit(value) {
    //   console.log(this.card, "card");
    this.user2 = JSON.parse(sessionStorage.getItem("user"))
    if (this.user2==null){
            this.$router.push("/login")
        }
        this.card.user_name = this.user2.name;
        this.$http.post("user/addcard", this.card).then(res => {
        if (res.data.code == 200) {
          this.$toast.success('添加成功');
          this.card = {};
        } else {
          this.$toast({message:'添加失败',icon:'cross'});
        }
      }).catch(res=>{
        this.$toast({message:'添加失败',icon:'cross'});
      });
    }
  }
};
</script>
