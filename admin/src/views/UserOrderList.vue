<template>
  <div>
  <el-table
    :data="tableData"
    stripe 
    style="margin:0px">
    <el-table-column
      prop="id"
      label="购买编号"
      >
    </el-table-column>
    <el-table-column
      prop="name"
      label="商品名称"
      >
    </el-table-column>
    <el-table-column
      prop="price"
      label="价格">
    </el-table-column>
    <el-table-column
      prop="scard"
      label="支付卡号">
    </el-table-column>
    <el-table-column
      prop="user_name"
      label="购买用户">
    </el-table-column>
    <el-table-column
      prop="create_time"
      label="购买时间">
    </el-table-column>
  </el-table>

  </div>
</template>

<script>
  export default {
    data() {
      return {
        tableData:[],
        user2:{}
      }
    },
    mounted() {
        this.fench()
    },
    methods: {
        fench(){
          this.user2 = JSON.parse(sessionStorage.getItem("user"));
        console.log("user2",this.user2.name)
        if (this.user2==null){
            this.$router.push("/login")
        }
            this.$http.post("user/orderhistory",this.user2)
            .then(res=>{
                if(res.data.code==200){
                    this.tableData=res.data.data
                }
            })
        }
    },
  }
</script>