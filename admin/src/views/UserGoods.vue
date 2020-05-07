<template>
    <div>
      <el-row :gutter="20">
        <el-col :span="6" v-for="(item,index) in items" :key="index">
            <el-card class="card1" shadow="hover">
      <img src="../assets/goods1.png" class="image">
      <div style="padding: 14px;">
        <span>{{item.name}}</span>
        <div class="bottom clearfix">
          <p>描述: {{item.description}}</p>
          <time class="time">上架时间：{{item.create_time}}</time>
          <el-button type="text" class="button" @click="buy(index)">购买</el-button>
        </div>
      </div>
    </el-card></el-col>
      </el-row>
      <el-dialog title="购买详情" :visible.sync="dialogFormVisible">
  <el-form :model="form">
    <el-form-item label="商品名称" :label-width="formLabelWidth">
      <el-input v-model="form.name" autocomplete="off"></el-input>
    </el-form-item>
    <el-form-item label="商品价格" :label-width="formLabelWidth">
      <el-input v-model="form.price" autocomplete="off"></el-input>
    </el-form-item>
    <el-form-item label="银行卡" :label-width="formLabelWidth">
      <el-select v-model="form.scard" placeholder="请选择你的支付卡号">
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
    <el-form-item label="支付密码" :label-width="formLabelWidth">
      <el-input v-model="form.paypassword" autocomplete="off" show-password></el-input>
    </el-form-item>
  </el-form>
  <div slot="footer" class="dialog-footer">
    <el-button @click="dialogFormVisible = false">取 消</el-button>
    <el-button type="primary" @click="buy1">购买</el-button>
  </div>
      </el-dialog>
    </div>
</template>
<style>
.card1 {
    margin-top:10px
}
  .time {
    font-size: 13px;
    color: #999;
  }
  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }
  .bottom p {
        font-size: 13px;
        color: #999;
           display: block;
   overflow: hidden;
   white-space: nowrap;

   text-overflow: ellipsis;
   width: 90%;
  }

  .button {
    margin-top: 5px;
    padding: 0;
    float: right;
  }

  .image {
    width: 80%;
    height:40%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }
</style>

<script>
export default {
  data() {
    return {
      currentDate: new Date(),
      items:{},
      user2:{},
      form: {},
      options:[],
      formLabelWidth: '120px',
      dialogFormVisible: false,
      mes:{}
    };
  },
  mounted() {
    this.fench()
  },
  methods: {
    fench(){
      this.user2 = JSON.parse(sessionStorage.getItem("user"))
      if (this.user2==null){
            this.$router.push("/login")
        }
      this.$http.get("admin/querygood")
      .then(res=>{
        if(res.data.code==200){
          // console.log(res.data.data)
          this.items=res.data.data
        }
      })
    },
    buy(index){
      this.dialogFormVisible=true
      this.items[index].user_name=this.user2.name
      this.mes.name = this.user2.name;
       this.$http.post("user/querycard", this.mes).then(res => {
        if (res.data.code == 200) {
          this.arr1 = res.data.data;
          // console.log("arr1", this.arr1);
          this.na = this.arr1.map(function(v) {
            return v.card_id;
          });
          for (let index in this.na) {
            this.options.push({
              value: this.na[index],
              lable: this.na[index]
            });
          }
        }
      });
      this.form=this.items[index]
      
    },
    buy1(){
      this.$http.post("user/buygood",this.form)
      .then(res=>{
        if(res.data.code==200){
          this.$message({
            message: res.data.msg,
            type: "success"
          });
        }else{
          this.$message({
            message: res.data.msg,
            type: "success"
          });
        }
      })
      this.dialogFormVisible=false
    }
  },
}
</script>