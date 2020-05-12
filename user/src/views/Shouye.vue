<template>
  <div>
    <div class="gird">
      <van-grid :gutter="10" :column-num="3">
        <van-grid-item style="color: rgb(51, 70, 196)" icon="manager-o" text="我的账户" to="/querycard" />
        <van-grid-item style="color: rgb(255, 12, 202)" icon="credit-pay" text="新增银行卡" to="/addcard" />
        <van-grid-item style="color: rgb(35, 204, 16)" icon="refund-o" text="转账汇款" to="/transfer" />
        
        <!-- <van-grid-item icon="photo-o" text="文字" /> -->
      </van-grid>
    </div>

    <div class="gird">
      <van-grid :gutter="10" :column-num="3">
        <!-- <van-grid-item icon="photo-o" text="文字" /> -->
        <van-grid-item style="color: rgb(201, 224, 85)" icon="label-o" text="转账记录" to="/transferhistory" />
        <van-grid-item style="color: rgb(229, 186, 87)" icon="orders-o" text="购买记录" to="/orderhistory" />
        <van-grid-item style="color: rgb(219, 126, 247)" icon="photo-o" text="更多功能" @click="futuer" />
      </van-grid>
    </div>
    <van-swipe :autoplay="3000">
      <van-swipe-item v-for="(image, index) in images" :key="index">
        <img :src="image" />
      </van-swipe-item>
    </van-swipe>
    <van-list
      v-model="loading"
      :finished="finished"
      finished-text="没有更多了"
    >
      <van-cell v-for="(item,index) in list" :key="index" @click="queryarticle(index)">
        <van-row>
          <van-col span="7"><img :src="item.image" style="height:60px" alt=""></van-col>
          <van-col span="16" offset="1">
            <div style="font-weight:bold;overflow:hidden;height:25px">{{ item.title }}</div>
        <div class="tagtime">
          <!-- <span style="font-size:5px"><van-tag type="primary" plain>{{item.tags.toString()}}</van-tag></span>
      
      <span class="time">{{item.create_time.toString()}}</span> -->
          <van-row>
            <van-col span="9"
              ><van-tag type="primary" plain>{{
                item.tags1
              }}</van-tag></van-col
            >
            <van-col span="15">{{ item.create_time1 }}</van-col>
          </van-row>
        </div>
          </van-col>
        </van-row>
      </van-cell>
    </van-list>
  </div>
</template>
<script>
export default {
  data() {
    return {
      images: [
        require("../assets/bank1.png"),
        require("../assets/bank2.png"),
        require("../assets/bank3.png"),
        require("../assets/bank4.png")
      ],
      list: [],
      list1: [],
      loading: false,
      finished: true,
      tag1: { tag_id: "" }
    };
  },
  created() {
    this.fench();
  },
  methods: {
    fench() {
      this.$http.post("admin/queryarticle", this.tag1).then(res => {
        if (res.data.code == 200) {
          // console.log(res.data.data, 222222222);
          this.list = res.data.data;
          for (let index in this.list){
            this.list[index].create_time1=this.list[index].create_time.toString()
          this.list[index].tags1=this.list[index].tags.toString()
          this.list[index].image=this.list[index].image.slice(2)
            this.list[index].image=this.list[index].image.substr(0, this.list[index].image.length - 1)
            this.list[index].image="data:image/png;base64,"+this.list[index].image
          }
        }
      });
    },
    futuer(){
      this.$toast({message:'敬请期待更多功能',icon:'https://img.yzcdn.cn/vant/logo.png',});
    },
    // onLoad() {
    //   // 异步更新数据
    //   // setTimeout 仅做示例，真实场景中一般为 ajax 请求
    //   setTimeout(() => {
    //     for (let i = 0; i < 10; i++) {
    //       this.list.push(this.list.length + 1);
    //     }

    //     // 加载状态结束
    //     this.loading = false;

    //     // 数据全部加载完成
    //     if (this.list.length >= this.list.length) {
    //       this.finished = true;
    //     }
    //   }, 1000);
    // },
    queryarticle(index) {
      // console.log(this.items[index], "article");
      this.$router.push({
        name: "Article",
        params: { pk_refinfo: this.list[index], value: "test1" },
      });
    },
  }
};
</script>
<style>
img {
  margin-top: 10px;
  width: 100%;
  height: 180px;
}
.tagtime {
  margin-top: 20px;
  font-size: 12px;
  color: #999999;
  /* margin-right: 18px; */
}
.gird {
  margin-top: 5px;
}
</style>
