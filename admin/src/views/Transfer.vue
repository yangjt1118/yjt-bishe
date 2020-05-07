<template>
  <el-card style="margin:20px;width:500px">
    <el-form
      :label-position="labelPosition"
      :model="transfer"
      label-width="80px"
      ref="transfer"
    >
      <el-form-item label="卡号" prop="ucard">
        <el-select v-model="transfer.scard" placeholder="请选择你的卡号">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            :disabled="item.disabled"
          >
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="金额" prop="mount">
        <el-input v-model="transfer.mount"></el-input>
      </el-form-item>
      <el-form-item label="对方卡号" prop="dcard">
        <el-input v-model="transfer.dcard"></el-input>
      </el-form-item>
      <el-form-item label="对方姓名" prop="dname">
        <el-input v-model="transfer.dname"></el-input>
      </el-form-item>
      <el-form-item label="支付密码" prop="paypassword">
        <el-input v-model="transfer.paypassword"></el-input>
      </el-form-item>
       <el-button @click="register" type="primary">转账</el-button>
        <el-button>取消</el-button>
    </el-form>
  </el-card>
</template>

<script>
export default {
  data() {
    return {
      labelPosition: "left",
      transfer: {},
      options: [],
      arr1: [],
      na: [],
      value: "",
      mes: { name: "" }
    };
  },
  mounted() {
    this.fench();
  },
  methods: {
    fench() {
      this.user2 = JSON.parse(sessionStorage.getItem("user"));
      if (this.user2==null){
            this.$router.push("/login")
        }
      this.mes.name = this.user2.name;
      this.$http.post("user/querycard", this.mes).then(res => {
        if (res.data.code == 200) {
          this.arr1 = res.data.data;
          // console.log("arr1", this.arr1);
          this.na = this.arr1.map(function(v) {
            return v.card_id;
          });
          // console.log(
          //   this.arr1.map(function(v) {
          //     return v.card_id;
          //   }),
          //   77777
          // );
          for (let index in this.na) {
            this.options.push({
              value: this.na[index],
              lable: this.na[index]
            });
          }
        }
      });
    },
    register() {
      let ww = JSON.parse(sessionStorage.getItem("user"));
      // console.log(ww.name);
      this.transfer.name = ww.name;
      // console.log(this.transfer);
      this.$http.post("user/transfer", this.transfer).then(res => {
        if (res.data.code == 200) {
          this.$message({
            message: "转账成功",
            type: "success"
          });
          this.transfer={}
        } else {
          this.$message({
            message: "转账失败",
            type: "success"
          });
          this.transfer={}
        }
      });
    }
  }
};
</script>
