<template>
  <div class="about"><van-row style="height:10%;background-color: rgba(0, 128, 128, 0.158);z-index=1;position=absolute">
        <img src="../assets/logo.png" alt="" style="width:214.5px;height:54px;top:10px">
</van-row>
<!-- <van-sticky>
      <van-nav-bar >
      <template #left>
    <img src="../assets/logo.png" alt="" style="width:214.5px;height:54px;top:10px">
  </template>
    </van-nav-bar>
    </van-sticky> -->
    <div class="center"><router-view></router-view></div>

    <van-tabbar route style="">
      <van-tabbar-item replace to="/shouye" icon="home-o">
        首页
      </van-tabbar-item>
      <van-tabbar-item replace to="/good" icon="shop-o">
        理财
      </van-tabbar-item>
      <van-tabbar-item replace to="/person1" icon="user-o">
        我的
      </van-tabbar-item>
    </van-tabbar>
  </div>
</template>
<script>
// import Footer from '../components/footer'
export default {
  // components:{
  //   Footer
  // }
};
</script>
<style>
.about {
  height: 100%;
}
.center {
  /* background-color: #f8f8f8; */
  /* background-color: #a4b5d8; */
  /* height: 100%; */
}
.headerfont {
  color: ghostwhite;
  font-weight: 1000;
  font-size: 22px;
  text-align: center;
}
</style>
