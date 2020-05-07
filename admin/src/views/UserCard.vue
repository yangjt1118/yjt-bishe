<template>
  <div>
    <el-card style="margin:20px;width:500px">
      <el-form
        :label-position="labelPosition"
        :model="card1"
        label-width="80px"
        ref="card1"
        :rules="rules"
      >
        <el-form-item label="卡号" prop="card_id">
          <el-input v-model="card1.card_id"></el-input>
        </el-form-item>
        <el-form-item label="余额" prop="balance">
          <el-input v-model="card1.balance"></el-input>
        </el-form-item>
        <el-button type="primary" @click="register('card1')">添加</el-button>
        <el-button @click="reset">重置</el-button>
      </el-form>
    </el-card>
    <el-card style="margin:20px">
      <el-table :data="card" stripe style="width: 100%">
        <el-table-column
          prop="card_id"
          label="卡号"
          width="180"
        ></el-table-column>
        <el-table-column
          prop="balance"
          label="余额"
          width="180"
        ></el-table-column>
        <el-table-column prop="create_time" label="添加时间"></el-table-column>
        <el-table-column prop="status" label="状态"></el-table-column>
      </el-table>
    </el-card>
  </div>
</template>
<script>
export default {
  data() {
    return {
      labelPosition: "right",
      card: [],
      card1: {
        user_id: ""
      },
      rules:{
        card_id:[
          { required: true, message: '请输入要添加的卡号', trigger: 'blur' },
          { min: 6, max: 16, message: '长度在 6 到 16 个字符', trigger: 'blur' }
        ],
        balance: [
            { required: true, message: '请输入卡金额', trigger: 'blur' },
          ],
      },
      user: {},
      user2: {},
      fench1:{
        name:""
      },
      ary: [],
      res: []
    };
  },
  mounted() {
    this.fench();
  },
  methods: {
    fench() {
      this.user2 = JSON.parse(sessionStorage.getItem("user"))
      if (this.user2==null){
            this.$router.push("/login")
        }
      console.log(this.user2.name)
      this.fench1.name=this.user2.name
      this.$http.post("user/querycard",this.fench1).then(res=>{
        if (res.data.code == 200) {
          console.log(res.data.data,9999)
          this.card=res.data.data
          console.log(this.card)
        } 
      })
      // this.user2 = JSON.parse(sessionStorage.getItem("user"));
      // // console.log(this.user2.ccreate_time);
      // for (let index in this.user2.ccreate_time) {
      //   this.user2.ccreate_time[index] = this.$moment(
      //     this.user2.ccreate_time[index]
      //   ).utcOffset(-480)._d;
      //   this.user2.ccreate_time[index] = this.$moment(
      //     this.$moment(this.time).format("YYYY-MM-DD HH:mm:ss")
      //   ).format("YYYY-MM-DD HH:mm:ss");
      // }
      // for (let index in this.user2.card_id) {
      //   this.card.push({
      //     card_id: this.user2.card_id[index],
      //     balance: this.user2.card_balance[index],
      //     create_time: this.user2.ccreate_time[index],
      //     status: this.user2.status[index]
      //   });
      // }
    },
    register(formName) {
      this.card1.user_name = this.user2.name;
      console.log(this.card1);
      this.$refs[formName].validate(valid => {
        if (valid) {
          this.$http.post("user/addcard", this.card1).then(res => {
        if (res.data.code == 200) {
          this.$message({
            message: "添加成功",
            type: "success"
          });
          this.card1 = {};
          this.fench();
        } else {
          this.$message({
            message: "添加失败",
            type: "error"
          });
        }
      });
        } else {
          console.log("error submit!!");
          return false;
        }
      });
      
    },
    reset() {
      this.card1 = {};
    }
  }
};
</script>
