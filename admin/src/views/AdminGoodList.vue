<template>
  <div>
    <div id="myChart" :style="{ width: '1000px', height: '300px' }"></div>
    <h1>理财产品列表</h1>
    <el-row>
      <el-col :span="6"> </el-col>
      <el-col :span="6"> </el-col>
      <el-col :span="6"> </el-col>
      <el-col :span="6"
        ><el-button type="danger" @click="batchdelete(tableChecked)"
          >批量删除</el-button
        ></el-col
      >
    </el-row>
    <el-table
      ref="multipleTable"
      :data="tableData"
      tooltip-effect="dark"
      style="width: 100%"
      @selection-change="handleSelectionChange"
    >
      <el-table-column type="selection" width="55"></el-table-column>
      <el-table-column prop="name" label="名称"></el-table-column>
      <el-table-column
        prop="description"
        label="描述"
        show-overflow-tooltip
      ></el-table-column>
      <el-table-column prop="price" label="价格" sortable></el-table-column>
      <el-table-column
        prop="create_time"
        label="上架时间"
        sortable
      ></el-table-column>
      <el-table-column fixed="right" label="操作" width="150">
        <template slot-scope="scope">
          <!-- <el-button @click="editArticle(scope.row)"  size="small"
              >编辑</el-button
            > -->
          <el-button @click="deletebyid(scope.row)" type="danger" size="small"
            >删除</el-button
          >
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tableData: [],
      multipleSelection: [],
      tableChecked: [], //被选中的记录数据-----对应“批量删除”传的参数值
      depost: { id: "" },
      depost1: { id: "" },
      arr1:[],
      arr2:[]
    };
  },
  mounted() {
    this.fench();
  },
  methods: {
    fench() {
      this.$http.get("admin/querygood").then((res) => {
        if (res.data.code == 200) {
          console.log(res.data.data.length);
          this.tableData = res.data.data;
          this.arr1=[]
          this.arr2=[]
          for (let index in this.tableData) {
            this.arr1.push(this.tableData[index].name);
            this.arr2.push(this.tableData[index].order_count);
          }
         this.drawLine()
        }
      });
    },
    drawLine(){
       let myChart = this.$echarts.init(document.getElementById("myChart"));
          // 绘制图表
          myChart.setOption({
            title: { text: "理财产品销售情况" },
            tooltip: {},
            xAxis: {
              data: this.arr1,
            },
            yAxis: {},
            series: [
              {
                name: "销量",
                type: "bar",
                barWidth : "40px",//柱图宽度
                data: this.arr2,
              },
            ],
          });
    },
    batchdelete() {
      this.depost.id = this.multipleSelection;
      this.$http.post("admin/batchdeletegood", this.depost).then((res) => {
        {
          if (res.data.code) {
            this.$message({
              message: "删除成功",
              type: "success",
            });
          }
        }
         this.fench();
      });
     
    },
    // editArticle(scope){
    //   console.log(scope.id)

    // },
    deletebyid(scope) {
      this.depost1.id = scope.id;
      this.$http.post("admin/deletegood", this.depost1).then((res) => {
        {
          if (res.data.code) {
            this.$message({
              message: "删除成功",
              type: "success",
            });
          }
        }
         this.fench();
      });
     
    },
    handleSelectionChange(val) {
      for (let index in val) {
        this.multipleSelection.push(val[index].id);
      }
    },
  },
};
</script>
