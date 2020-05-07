<template>
  <div>
    <van-row style="margin-top:0px">
      <van-col span="24" offset="" style="text-align:center">
        <van-uploader :after-read="afterRead" style="color:teal">
          <img class="tximg" :src="touxiang" alt="图片跑掉惹。。。" v-if="txshow==true" />
          <img class="tximg" src="../assets/mrtx1.jpg" alt="" v-else />

          <!-- <van-button icon="photo" plain hairline size="mini" >上传头像</van-button> -->
        </van-uploader>
      </van-col>
      <!-- <van-col span="8"></van-col> -->
    </van-row>
    <van-cell-group>
      <van-cell icon="user-o">{{ user.name }}</van-cell>
      <van-cell title="性别" icon="manager-o">{{ user.gender }}</van-cell>
      <van-cell title="电话" icon="phone-o">{{ user.phone }}</van-cell>
      <van-cell title="地址" icon="location-o">{{ user.address }}</van-cell>
      <van-cell title="修改个人信息" is-link to="/userupdate" />
      <van-cell title="修改密码" is-link to="/passwordupdate" />
    </van-cell-group>
    <!-- <van-row>
  <van-col></van-col>
</van-row> -->
    <van-button
      style="margin-top:10px"
      round
      block
      type="warning"
      to="/"
      @click="logout"
    >
      退出登录
    </van-button>
  </div>
</template>
<script>
export default {
  data() {
    return {
      user: {},
      user2: {},
      touxiang: "",
      arr: [],
      txshow:false
    };
  },
  mounted() {
    this.fench();
    this.fench1();
  },
  methods: {
    fench() {
      this.user2 = JSON.parse(sessionStorage.getItem("user"));
      // console.log("user2",this.user2)
      if (this.user2 == null) {
        this.$router.push("/login");
      }
      this.$http.post("user/query", this.user2).then(res => {
        if (res.data.code == 200) {
          this.user = res.data.data;
        }
      });
    },
    fench1() {
      this.$http.post("user/image", this.user2).then(res => {
        // console.log(res.data)
        if(res.data!=""){
          this.txshow=true
        }
        this.touxiang = "data:image/jpeg;base64," + res.data;
      });
    },
    logout() {
      sessionStorage.clear();
    },
    afterRead(file) {
      // 此时可以自行将文件上传至服务器

      // file.status=this.user2.name

      // file.content=file.content.substring(23)
      let arr = new FormData();
      // arr.append(JSON.stringify("photo"), JSON.stringify(file));
      console.log(file, 22222222222);
      arr.append("image", file.file);
      arr.append("name", this.user2.name);
      console.log(arr, 11);
      this.$http
        .post("user/addimage", arr)
        .then(res => {
          if (res.data.code == 200) {
            this.$toast.success("上传成功");
            this.card = {};
            this.fench1();
            this.txshow=true
          } else {
            this.$toast({ message: "上传失败", icon: "cross" });
          }
        })
        .catch(res => {
          this.$toast({ message: "上传失败", icon: "cross" });
        });
    }
  }
};
</script>
<style>
.tximg {
  border-radius: 50%;
  height: 100px;
  width: 100px;
}
</style>
