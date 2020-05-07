<template>
  <div>
      <el-card style="margin:20px;">
          <el-select v-model="value" clearable  placeholder="请选择">
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
      </el-card>
    <el-card style="margin:20px">
      <el-table :data="card" stripe style="width: 100%">
        <el-table-column prop="id" label="流水号"></el-table-column>
        <el-table-column prop="mount" label="转账金额"></el-table-column>
        <el-table-column prop="sname" label="转账人"></el-table-column>
        <el-table-column prop="scard" label="转账卡号"></el-table-column>
        <el-table-column prop="dname" label="收账人"></el-table-column>
        <el-table-column prop="dcard" label="收账卡号"></el-table-column>
        <el-table-column prop="create_time" label="转账时间"></el-table-column>
    </el-table>
    </el-card>
  </div>
</template>
<script>
export default {
  data() {
    return {
      labelPosition:"right",
      card: [],
      user:{},
      user2:{},
      mes: { name: "" },
      options: [{
          value: '选项1',
        //   label: '黄金糕'
        }, {
          value: '选项2',
          label: '双皮奶'
        }, {
          value: '选项3',
          label: '蚵仔煎'
        }, {
          value: '选项4',
          label: '龙须面'
        }, {
          value: '选项5',
          label: '北京烤鸭'
        }],
        value: ''
    };
  },
  mounted() {
    this.fench();
  },
  methods: {
    fench() {
      // this.user2 = JSON.parse(sessionStorage.getItem("user"));
      //     for (let index in this.user2.card_id) {
      //       this.card.push({
      //         card_id: this.user2.card_id[index],
      //         balance: this.user2.card_balance[index],
      //         create_time: this.user2.ccreate_time[index],
      //         status: this.user2.status[index]
      //       });
      //     }
      this.user2 = JSON.parse(sessionStorage.getItem("user"));
      if (this.user2==null){
            this.$router.push("/login")
        }
      this.mes.name = this.user2.name;
        this.$http.post("user/transferhistory",this.mes).then(res=>{
        if (res.data.code == 200) {
          console.log(res.data.data,9999)
          this.card=res.data.data
        } 
      })
     
    },

  }
};
</script>