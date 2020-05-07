<template>
  <div>
    <div id="myChart" :style="{ width: '1000px', height: '300px' }"></div>
    <!-- <div id="myChart1" :style="{ width: '500px', height: '300px' }"></div> -->
    <h1>银行资讯列表</h1>
    <el-row>
      <el-col :span="6">
        <el-select v-model="value" placeholder="输入查询的文章标签">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          ></el-option>
        </el-select>
        <el-button type="primary" @click="search">点击查询</el-button>
      </el-col>
      <el-col :span="6"></el-col>
      <el-col :span="6"></el-col>
      <el-col :span="6"><el-button type="danger" @click="batchdelete(tableChecked)">批量删除</el-button></el-col>
    </el-row>
    <el-table
      ref="multipleTable"
      :data="tableData"
      tooltip-effect="dark"
      style="width: 100%;margin-top:10px"
      @selection-change="handleSelectionChange"
    >
      <el-table-column type="selection" width="55"></el-table-column>
      <el-table-column prop="title" label="标题"></el-table-column>
      <el-table-column label="内容" show-overflow-tooltip>
        <template slot-scope="scope">
        <span style="margin-left: 10px" v-html="scope.row.content" show-overflow-tooltip></span>
      </template>
      </el-table-column>
      <el-table-column prop="tags" label="标签"></el-table-column>
      <el-table-column prop="create_time" label="发表时间" sortable></el-table-column>
      <el-table-column fixed="right" label="操作" width="150">
       <template slot-scope="scope">
           
            <el-button
              @click="deletebyid(scope.row)"
              type="danger"
              size="small"
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
        tableChecked:[],//被选中的记录数据-----对应“批量删除”传的参数值
        ids:[],//批量删除id
      multipleSelection: [],
      tag1: { tag_id: "" },
      depost:{id:""},
      depost1:{id:""},
      options: [],
      na: [],
      value:"",
      arr1:[],
      arr2:[]
    };
  },
  mounted() {
    this.fench();
    // this.drawLine1();
    this.$http.get("admin/querytag")
      .then(res=>{
          if(res.data.code==200){
              this.na=res.data.data
               for (let index in this.na) {
                this.options.push({
                value: this.na[index].tag_id,
                label: this.na[index].tag_name
                });
            }
          }
      })
 
 
 
 },
  methods: {
    fench() {
      this.$http.post("admin/queryarticle", this.tag1).then(res => {
        if (res.data.code == 200) {
          this.tableData = res.data.data;
          this.arr1=[]
          this.arr2=[]
          for (let index in this.tableData) {
            this.tableData[index].tags = this.tableData[index].tags.join("，");
             this.arr1.push(this.tableData[index].title)
             this.arr2.push(this.tableData[index].pageview)
          }
             this.drawlLine()
        }
      });
    },
    search(){
        this.tag1.tag_id=this.value.toString()
        this.$http.post("admin/queryarticle", this.tag1).then(res => {
        if (res.data.code == 200) {
          this.tableData = res.data.data;
        //   this.na = this.tableData.map(function(v) {
        //     return v.tags;
        //   });
        //   console.log(this.na,99999)
        //   for (let index in this.na) {
        //     this.options.push({
        //       value: this.na[index],
        //       lable: this.na[index]
        //     });
        //   }
          for (let index in this.tableData) {
            this.tableData[index].tags = this.tableData[index].tags.join("，");
          }
        }
      });
    },
    drawlLine(){
                            let myChart = this.$echarts.init(document.getElementById("myChart"));
      // 绘制图表
      myChart.setOption({
        title: { text: "银行资讯阅读量情况" },
        tooltip: {},
        xAxis: {
          data: this.arr1,
        },
        yAxis: {},
        series: [
          {
            name: "阅读量",
            type: "bar",
            barWidth:"40px",
            data: this.arr2,
          },
        ],
      });
    },
    drawLine1(){
        // 基于准备好的dom，初始化echarts实例
        let myChart1 = this.$echarts.init(document.getElementById('myChart1'))
        // 绘制图表
        myChart1.setOption({
            
 
            color:['#4472C5','#ED7C30','#80FF80','#FF8096','#800080'],//配置颜色
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)"
            },
            legend: {
                orient: 'vertical',
                x: 'left',
                data:['直接访问','邮件营销','联盟广告','视频广告','搜索引擎','游戏公告'],
                textStyle: {//------------此处更改表格中的字体颜色
                  fontSize: '12',
                  color:'teal'
                }
            },
            series: [
                {
                    name:'访问来源',
                    type:'pie',
                    radius: ['50%', '70%'],
                    avoidLabelOverlap: true,
                    label: {
                        normal: {
                            show: false,
                            position: 'center'
                        },
                        emphasis: {
                            show: true,
                            textStyle: {
                                fontSize: '30',
                                fontWeight: 'bold'
                            }
                        }
                    },
                    labelLine: {
                        normal: {
                            show: false
                        }
                    },
                    data:[
                        {value:335, name:'直接访问'},
                        {value:310, name:'邮件营销'},
                        {value:234, name:'联盟广告'},
                        {value:135, name:'视频广告'},
                        {value:1548, name:'搜索引擎'},
                    ]
                }
            ]
        });
    },
    batchdelete(){
      this.depost.id=this.multipleSelection
      this.$http.post("admin/batchdeletearticle",this.depost)
      .then(res=>{
        {
        if(res.data.code){
          this.$message({
            message: "删除成功",
            type: "success"
          });
        }
      }
       this.fench()
      })
     
    },

    deletebyid(scope) {
      this.depost1.id=scope.id
      this.$http.post("admin/deletearticle",this.depost1)
      .then(res=>{
        {
        if(res.data.code){
          this.$message({
            message: "删除成功",
            type: "success"
          });
        }
      }
      this.fench()
      })
      
    },
    handleSelectionChange(val) {
      for(let index in val){
        this.multipleSelection.push(val[index].id)
      }
      // console.log(this.multipleSelection)
//       function unique (arr) {
//   return Array.from(new Set(arr))
// }
      // console.log(unique(this.multipleSelection),22222222)
    },
    
  }
};
</script>