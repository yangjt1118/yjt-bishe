<template>
  <div>
    <div>
      <van-nav-bar
        style=" background-color: white; color: white; font-size: 18px;;"
        title="购买历史"
        left-text="返回"
        left-arrow
        @click-left="onClickLeft"
        boder
        :fixed="true"
      >
      </van-nav-bar>
    </div>
<div style="margin-top:46px" v-if="ordershow==true">
      <van-cell v-for="(item,index) in list" :key="index" style="margin-top:10px">
        <div >
        <span class="ttitle">购买商品名称：</span><span class="time">{{ item.name }}</span>
      </div >
      <div >
        <span class="ttitle">购买时间：</span><span class="time">{{ item.create_time.toString() }}</span>
      </div>
      <div >
        <span class="ttitle">购买金额：</span><span class="balance" style="color:#eb5e5e">{{ item.price }}</span>
      </div>
      <div class="tname">
        <span>收账人：{{ item.user_name }}</span>
        <span>收账账卡号：{{ item.scard }}</span>
      </div>
    </van-cell>
</div>
<div class="noshow" v-else>
  <!-- <img src="https://img.yzcdn.cn/vant/empty-image-error.png" alt=""> -->
  <span>你还没有购买记录哦</span>
  </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
        user:{},
        list:[],
        ordershow:false
    };
  },
  mounted() {
    this.fench();
  },
  methods: {
    fench() {
      this.user2 = JSON.parse(sessionStorage.getItem("user"));
      if (this.user2 == null) {
        this.$router.push("/login");
      }
      this.user.name = this.user2.name;
      this.$http.post("user/orderhistory", this.user).then(res => {
        if (res.data.code == 200) {
          if(res.data.data.length==0){
            this.ordershow=false
          }else{
            this.ordershow=true
            this.list = res.data.data;
          }
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
    .time{
        font-size: 15px;
        color: #44bbeb;
    }
    .balance {
    font-size: 16px;
}
.ttitle {
    font-size: 13px;
}
.tname{
    font-size: 13px;
    margin-right:30px
}
</style>