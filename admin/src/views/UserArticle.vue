<template>
  <div>
    <div>
      <el-row type="flex" class="row-bg" justify="center">
        <el-col :span="2">
          <div class="grid-content bg-purple"></div>
        </el-col>
        <el-col :span="14" style="background:white;padding:20px">
          <h2>{{article.title}}</h2>
          
          <div class="tagtime">
            <div>阅读量{{article.pageview}}</div>
            <span>{{article.tags.toString()}}</span>
          <span>{{article.create_time}}</span>
          </div>
          <div v-html="article.content"></div>
        </el-col>
        <el-col :span="2">
          <div class="grid-content bg-purple"></div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>
<script>
export default {
  data(){
    return {
      article:{},
      post:{id:""}
    }
  },
  mounted() {
    this.fench()
  },
  methods:{
    fench(){
    //   console.log(this.$route.params.pk_refinfo,333333333)
    //   // this.article=this.$route.params.pk_refinfo
      
      this.post.id=this.$route.params.pk_refinfo.id.toString()
    //   console.log(this.post.id.toString(),555)
      this.$http.post("admin/articlebyid",this.post)
      .then(res=>{
        if(res.data.code==200){
          this.article=res.data.data
        }
      })
    }
  }
}
</script>
<style>
  .tagtime {
    font-size: 12px;
  color: rgb(153, 153, 153);
  margin-right: 18px;
  margin-bottom: 20px;
  }
  .tagtime span {
    margin-right: 20px;
  }
</style>