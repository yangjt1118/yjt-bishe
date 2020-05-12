<template>
  <div style="height:100%;background-color:#f8f8f8;">
    <div>
      <van-nav-bar
        style=" background-color: white; color: white; font-size: 18px;;"
        title="我的账户"
        left-text="返回"
        left-arrow
        @click-left="onClickLeft"
        boder
        :fixed=true
      >
      </van-nav-bar>
    </div>

<div style="margin-top:46px" v-if="cardshow==true">
    <van-cell v-for="(item,index) in list" :key="index" style="margin-top:10px" >
      <div>银行卡卡号：<span class="explain">{{item.card_id}}</span></div>
      
      <div>
          <div>余额：<span class="explain">{{item.balance}}</span></div>
          <div class="time">开卡时间：<span class="explain">{{item.create_time.toString()}}</span></div>
      </div>
      <div><van-button size="small" type="primary">{{item.status}}</van-button></div>
  </van-cell>
</div>
<div class="noshow" v-else>
  <!-- <img src="https://img.yzcdn.cn/vant/empty-image-error.png" alt=""> -->
  <span>你还没有银行卡哦</span>
  </div>
  <van-button type="info" block round style="margin-top:10px" to="/addcard">新增银行卡</van-button>

  </div>
</template>
<script>
export default {
  data() {
    return {
      user: {},
      list:[],
      cardshow:false
    };
  },
  created() {
    this.fench();
  },
  methods: {
    async fench() {
      this.user2 = JSON.parse(sessionStorage.getItem("user"));
      // console.log("user2",this.user2)
      if (this.user2 == null) {
        this.$router.push("/login");
      }
      this.user.name = this.user2.name;
      // console.log(this.user);
      try {
        const res = await this.$http.post("user/querycard", this.user)
        console.log(res)
          if (res.data.code == 200) {
            if(res.data.data.length==0){
              this.cardshow=false
            }else{
              this.cardshow=true
              this.list = res.data.data;
              console.log
            }
          }
      }catch(err){
        console.log(err)
      }

    },
 onClickLeft() {
        this.$router.push("/Shouye")
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
.explain {
  font-size: 16px;
}
.time {
      font-size: 12px;
  color: #999999;
}
.noshow {
  margin-top: 46px;
  width: 100%;
  height: 30%;
  text-align: center;
  line-height: 190px;
  color: #999999;
}
.noshow img {
  width: 130px;
  height: 130px;
}
</style>
