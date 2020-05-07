<template>
  <div>
    <el-card class="box-card" style="margin:20px">
      <div class="text item">
        <div>姓名：{{ user.name }}</div>
        <el-divider></el-divider>
        <div>电话号码：{{user.phone}}</div>
        <el-divider></el-divider>
        <div>籍贯:{{user.address}}</div>
        <el-divider></el-divider>
        <div>创建时间:{{ user.create_time }}</div>
      </div>
    </el-card>
  </div>
</template>
<script>
export default {
  data() {
    return {
      user: {
        name: "",
        card_id: [],
        card_balance: [],
        create_time: ""
      },
      user2: {},
      time:""
    };
  },
  mounted() {
    this.fench();
  },
  methods: {
    fench(){
        this.user2 = JSON.parse(sessionStorage.getItem("user"));
        // console.log("user2",this.user2)
        if (this.user2==null){
            this.$router.push("/login")
        }
        this.user.name = this.user2.name;
        // console.log(this.user)
        this.$http.post("user/query",this.user)
        .then(res=>{
            if(res.data.code==200){
                this.user=res.data.data
            }
        })
    },
    created() {
      this.fench();
    }
  }
};
</script>
<style>
.text {
  font-size: 14px;
}

.item {
  padding: 18px 0;
}

.box-card {
  width: 480px;
}
</style>
