<template>
  <van-tabbar v-model="active" inactive-color="#777777" active-color="#000000">
    <van-tabbar-item v-for="(item,index) in tabbars" :key="index" :to="(item.name)">
      <span>{{item.title}}</span>
      <img slot="icon" slot-scope="props" :src="props.active ? item.active : item.normal" />
    </van-tabbar-item>
  </van-tabbar>
</template>

<script>
export default {
  name: "tabbar",
  data() {
    return {
      active: 0,
      tabbars: [
        {
          name: "/",
          title: "发现",
          normal:
            "http://sucai.suoluomei.cn/sucai_zs/images/20190910093117-fx2.png",
          active:
            "http://sucai.suoluomei.cn/sucai_zs/images/20190910093117-fx.png"
        },
        {
          name: "article",
          title: "学习",
          normal:
            "http://sucai.suoluomei.cn/sucai_zs/images/20190910093117-xx.png",
          active:
            "http://sucai.suoluomei.cn/sucai_zs/images/20190910093117-xx2.png"
        },
        {
          name: "home",
          title: "我的",
          normal:
            "http://sucai.suoluomei.cn/sucai_zs/images/20190910093117-wd.png",
          active:
            "http://sucai.suoluomei.cn/sucai_zs/images/20190910093117-wd2.png"
        }
      ]
    };
  },
  methods: {},
  //通过路由跳转判断选中的样式
  created() {
      
    if (this.$route.name == "index") {
      this.active = 0;
    } else if (this.$route.name == "article") {
      this.active = 1;
    } else if (this.$route.name == "good") {
      this.active = 2;
    }
    console.log(this.active,21111111)
  }
};
</script>

<style>
</style>