<template>
  <div>
        <div id="chartLineBox1" style="width:800px;height:300px;display:inline-block"></div>
    <!-- <div id="chartLineBox2" style="width:500px;height:300px;display:inline-block"></div> -->
    <h1>用户列表</h1>
    <el-table
      :data="tableData"
      stripe
      style="margin:0px"
      :default-sort="{ prop: 'create_time', order: 'ascending' }"
    >
      <el-table-column prop="name" label="姓名"> </el-table-column>
      <el-table-column prop="gender" label="性别"> </el-table-column>
      <el-table-column prop="phone" label="电话"> </el-table-column>
      <el-table-column
        prop="address"
        label="地址"
        :show-overflow-tooltip="true"
      >
      </el-table-column>
      <el-table-column prop="cards" label="银行卡"> </el-table-column>
      <el-table-column prop="create_time" label="创建时间" sortable>
      </el-table-column>
      <el-table-column prop="status" label="状态"> </el-table-column>
      <el-table-column fixed="right" label="操作" width="150">
        <template slot-scope="scope">
          <el-button
            @click="updateuserstatus(scope.row)"
            type="warning"
            size="small"
            >修改状态</el-button
          >
        </template>
      </el-table-column>
    </el-table>
    <el-dialog
      title="修改用户状态"
      :visible.sync="centerDialogVisible"
      width="30%"
      center
    >
      <el-form ref="status" :model="form" label-width="80px">
        <el-form-item label="用户状态">
          <el-select v-model="form.status">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.label"
            ></el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="noaddtag">取 消</el-button>
        <el-button type="primary" @click="addtag">确 定</el-button>
      </span>
    </el-dialog>
    

  </div>
</template>

<script>
export default {
  data() {
    return {
      centerDialogVisible: false,
      tableData: [
        {
          cards: [],
        },
      ],
      user2: {},
      form: {},
      options: [
        {
          value: "正常",
          label: "正常",
        },
        {
          value: "冻结",
          label: "冻结",
        },
      ],
      chartsdatay1: [],
      chartsdatay2: [],

    };
  },
  mounted() {
    this.fench();
    // this.drawLine();
    // setTimeout(()=>{this.drawLine1()},0)

    // 指定图表的配置项和数据

    // var option = {

    // };
    // // 使用刚指定的配置项和数据显示图表。
    // this.chartLine.setOption(option);
  },
  methods: {
    fench() {
      this.user2 = JSON.parse(sessionStorage.getItem("admin"));
      // console.log("user2",this.user2.name)
      if (this.user2 == null) {
        this.$router.push("/login");
      }
      this.$http.get("admin/queryuser").then((res) => {
        if (res.data.code == 200) {
          this.tableData = res.data.data;
          this.chartsdatay1 = res.data.data1
          this.chartsdatay2 = res.data.data2
          this.drawLine1()
          for (let index in this.tableData) {
            this.tableData[index].cards = this.tableData[index].cards.join(
              "，"
            );
          }
        }
      });
    },
    drawLine() {
      // 基于准备好的dom，初始化echarts实例

    },
    drawLine1() {
     
            let day = new Date();
             // 基于准备好的dom，初始化echarts实例
 var s = day.getFullYear()+"-" + (day.getMonth()+1) + "-" + day.getDate();
 day.setTime(day.getTime()-24*60*60*1000);
 var s1 = day.getFullYear()+"-" + (day.getMonth()+1) + "-" + day.getDate();
 day.setTime(day.getTime()-24*60*60*1000);
 var s2 = day.getFullYear()+"-" + (day.getMonth()+1) + "-" + day.getDate();
 day.setTime(day.getTime()-24*60*60*1000);
 var s3 = day.getFullYear()+"-" + (day.getMonth()+1) + "-" + day.getDate();
 day.setTime(day.getTime()-24*60*60*1000);
 var s4 = day.getFullYear()+"-" + (day.getMonth()+1) + "-" + day.getDate();
 day.setTime(day.getTime()-24*60*60*1000);
 var s5 = day.getFullYear()+"-" + (day.getMonth()+1) + "-" + day.getDate();
 day.setTime(day.getTime()-24*60*60*1000);
 var s6 = day.getFullYear()+"-" + (day.getMonth()+1) + "-" + day.getDate();
let arr = []
arr.push(s6,s5,s4,s3,s2,s1,s)
          let myChart1 = this.$echarts.init(
            document.getElementById("chartLineBox1")
          );
          // 绘制图表
          myChart1.setOption({
            title: { text: "系统一周每日活跃" },
            tooltip: {
              //设置tip提示
              trigger: "axis",
            },

            legend: {
              //设置区分（哪条线属于什么）
              data: ["日注册人数",'日登录人数'],
            },
            color: ["#8AE09F", "#FA6F53"], //设置区分（每条线是什么颜色，和 legend 一一对应）
            xAxis: {
              //设置x轴
              type: "category",
              boundaryGap: false, //坐标轴两边不留白
              data: arr,
              name: "", //X轴 name
              nameTextStyle: {
                //坐标轴名称的文字样式
                color: "#FA6F53",
                fontSize: 16,
                padding: [0, 0, 0, 20],
              },
              axisLine: {
                //坐标轴轴线相关设置。
                lineStyle: {
                  color: "#FA6F53",
                },
              },
            },
            yAxis: {
              name: "",
              nameTextStyle: {
                color: "#FA6F53",
                fontSize: 16,
                padding: [0, 0, 10, 0],
              },
              axisLine: {
                lineStyle: {
                  color: "#FA6F53",
                },
              },
              type: "value",
            },
            series: [
              {
                name: "日注册人数",
                data: JSON.parse(JSON.stringify(this.chartsdatay1)),
                type: "line", // 类型为折线图
                lineStyle: {
                  // 线条样式 => 必须使用normal属性
                  normal: {
                    color: "#8AE09F",
                  },
                },
              },
              {
                name: "日登录人数",
                data: JSON.parse(JSON.stringify(this.chartsdatay2)),
                type: "line", // 类型为折线图
                lineStyle: {
                  // 线条样式 => 必须使用normal属性
                  normal: {
                    color: "#FA6F53",
                  },
                },
              },
            ],
          });
    },
    updateuserstatus(scope) {
      this.centerDialogVisible = true;
      this.form.name = scope.name;
      this.form.status = scope.status;
    },
    addtag() {
      this.centerDialogVisible = false;
      this.$http.post("admin/updateuserstatus", this.form).then((res) => {
        if (res.data.code == 200) {
          this.$message({
            message: res.data.msg,
            type: "success",
          });
          this.form = {};
          this.fench();
        }
      });
    },
    noaddtag() {
      this.centerDialogVisible = false;
      this.form = {};
    },
  },
};
</script>
