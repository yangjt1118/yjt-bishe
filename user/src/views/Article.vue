<template>
  <div style="height:100%;background-color:#f8f8f8;">
    <div>
      <van-nav-bar
        style=" background-color: white; color: white; font-size: 18px;;"
        title="文章详情"
        left-text="返回"
        left-arrow
        @click-left="onClickLeft"
        boder
        :fixed="true"
      >
      </van-nav-bar>
    </div>
    <div style="margin-top:46px;padding:10px">
      <div style="text-align:center"><h2>{{ article.title }}</h2></div>

      <div class="tagtime">
        <div>阅读量：{{ article.pageview }}</div>
        <van-tag type="primary" plain style=";margin-top:10px"><span>{{ article.tags1}}</span></van-tag>
        
        <span style="margin-left:120px;margin-top:10px；">{{ article.create_time }}</span>
      </div>
      <img :src="article.image" style="" alt="" />
      <div v-html="article.content"></div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      post: { id: "" },
      article: {}
    };
  },
  mounted() {
    this.fench();
  },
  methods: {
    fench() {
      // console.log(this.$route.params.pk_refinfo,333333333)
      this.post.id = this.$route.params.pk_refinfo.id.toString();
      //   console.log(this.post.id.toString(),555)
      this.$http.post("admin/articlebyid", this.post).then(res => {
        if (res.data.code == 200) {
          this.article = res.data.data;
          this.article.tags1=this.article.tags.toString()
          this.article.image = this.article.image.slice(2);
          this.article.image = this.article.image.substr(
            0,
            this.article.image.length - 1
          );
          this.article.image = "data:image/png;base64," + this.article.image;
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
.tagtime {
  font-size: 12px;
  color: rgb(153, 153, 153);
  margin-right: 18px;
  margin-bottom: 10px;
}
.tagtime span {
  
}
</style>
