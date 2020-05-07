<template>
  <div style="height:100%;background-color:#f8f8f8;">
    <div>
      <van-nav-bar
        style=" background-color: white; color: white; font-size: 18px;;"
        title="转账记录"
        left-text="返回"
        left-arrow
        @click-left="onClickLeft"
        boder
        :fixed="true"
      >
      </van-nav-bar>
    </div>
    <div style="margin-top:60px;background-color:#fff;height:65px">
      <van-row>
        <van-col span="12"><span style="color:grey">本月收支金额汇总 </span></van-col>
        <van-col span="12" style="color:#39a9ed;word-spacing:5px">收 {{arr[1]}}</van-col>
      </van-row>
      <van-row>
        <van-col offset="12" span="12" style="color:red;word-spacing:5px">支 {{arr[0]}}</van-col>
      </van-row>
    </div>
    <div style="margin-top:15px" v-if="transfershow == true">
      <van-cell v-for="(item,index) in list" :key="index" style="margin-top:10px">
        <div class="time">
          转账时间：<span>{{ item.create_time.toString() }}</span>
        </div>
        <div class="balance">
          转账金额：<span style="color:#2724e4">{{ item.mount }}</span>
        </div>
        <div class="tname">
          <span>收账人：{{ item.dname }}</span>
          <span>收账账卡号：{{ item.dcard }}</span>
        </div>

        <div class="tname">
          <span>转账人：{{ item.sname }}</span>
          <span>转账卡号：{{ item.scard }}</span>
        </div>
      </van-cell>
    </div>
    <div class="noshow" v-else>
      <!-- <img src="https://img.yzcdn.cn/vant/empty-image-error.png" alt=""> -->
      <span>你还没有转账记录哦</span>
    </div>
    <van-button
      round
      block
      style="margin-top:10px"
      type="primary"
      native-type="submit"
      to="/transfer"
    >
      转账汇款
    </van-button>
  </div>
</template>
<script>
export default {
  data() {
    return {
      user: {},
      list: [],
      transfershow: false,
      arr:[]
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
      this.$http.post("user/transferhistory", this.user).then(res => {
        if (res.data.code == 200) {
          this.arr=res.data.data1
          if (res.data.data.length == 0) {
            this.transfershow = false;
          } else {
            this.transfershow = true;
          }
          this.list = res.data.data;
        }
      });
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
  background-color: aquamarine;
  color: white;
  font-size: 18px;
  line-height: 50px;
}
.time {
  font-size: 15px;
}
.time span {
  /* font-size: 18px; */
  color: #44bbeb;
}
.tname span {
  font-size: 13px;
  margin-right: 30px;
}
.balance {
  font-size: 16px;
}
</style>
