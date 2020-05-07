<template>
  <div>
    <div>
      <el-row type="flex" class="row-bg" justify="center">
        <el-col :span="2">
          <div class="grid-content bg-purple"></div>
        </el-col>
        <el-col :span="14" style="background:white;padding:20px">
          <el-carousel height="250px">
            <el-carousel-item v-for="item in imgList" :key="item.id">
              <img :src="item.idView" alt="">
            </el-carousel-item>
          </el-carousel>
          <ul style="margin-top:20px">
            <li class="li" v-for="(item, index) in items" :key="index">
              <el-row :gutter="20">
                <el-col :span="4">
                  <img
                    :src="item.image"
                    alt
                    style="width:100px;height:66px"
                  />
                </el-col>
                <el-col :span="2"></el-col>
                <el-col :span="18" class="title">
                  <div class="title1" @click="queryarticle(index)">
                    {{ item.title }}
                  </div>
                  <div class="titleTag">
                    <span>阅读量 {{ item.pageview }}</span>
                  </div>
                  <div class="titleTag">
                    <span class="sellTag">{{ item.tags.toString() }}</span>
                    <span class="sellTime">{{
                      item.create_time.toString()
                    }}</span>
                  </div>
                </el-col>
              </el-row>
            </li>
          </ul>
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
  data() {
    return {
      items: [],
      imgList: [
          {id: 0, idView: require('../assets/bank1.png')},
          {id: 1, idView: require('../assets/bank2.png')},
          {id: 2, idView: require('../assets/bank3.png')},
          {id: 3, idView: require('../assets/bank4.png')},
        ],
      tag1: { tag_id: "" },
      image: "",
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
      this.$http.post("admin/queryarticle", this.tag1).then((res) => {
        if (res.data.code == 200) {
          console.log(res.data.data, 222222222);
          this.items = res.data.data;
          // let str1=this.items[2].image.slice(2)
          // let str2=str1.substr(0, str1.length - 1)
          // console.log(str2,222)
          for(let index in this.items){
            this.items[index].image=this.items[index].image.slice(2)
            this.items[index].image=this.items[index].image.substr(0, this.items[index].image.length - 1)
            this.items[index].image="data:image/png;base64,"+this.items[index].image
          }
          // console.log(this.items[2].image,222)
        }
      });
      this.$http.post("admin/queryarticleimage",this.tag1).then((res)=>{
        if (res.data.code == 200) {
          // console.log(res.data.data, 222222222);
          // this.items = res.data.data;
        }
      })
    },
    queryarticle(index) {
      // console.log(this.items[index], "article");
      this.$router.push({
        name: "UserArticle",
        params: { pk_refinfo: this.items[index], value: "test1" },
      });
    },
  },
};
</script>
<style>
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 150px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
.title1 {
  cursor: pointer;
}
.img {
  width: 130px;
  height: 100%;
  display: inline-block;
}
.title {
  padding: 0px;
  display: inline-block;
}
.li {
  height: 80px;
}
.titleTag {
  margin-top: 3px;
}
.title span {
  font-size: 12px;
  color: #999;
  margin-right: 18px;
}

ul {
  list-style: none;
  /* height: 100%; */
  margin: 0px;
  padding: 0px;
}
</style>
