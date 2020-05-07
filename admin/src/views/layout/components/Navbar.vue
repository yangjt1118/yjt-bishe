<template>
  <div id="">
    <!-- <el-card class="box-card"> -->
      <!-- <div slot="header" class="clearfix" style="padding-bottom:10px"> -->
        <!-- <i class="el-icon-caret-right" @click="packUp" v-show="isCollapse"></i>
        <i class="el-icon-caret-left" @click="unfold" v-show="!isCollapse"></i> -->
        <!-- <el-breadcrumb separator="/" style="float:left;margin-left:20px;">
          <el-breadcrumb-item v-for="(item,index) in breadItemDate" :key="index">{{item}}</el-breadcrumb-item>
        </el-breadcrumb> -->
      <!-- </div> -->
      <!-- <div class="text item" style="padding:10px 10px 10px 25px">
        
        <el-tag
          :key="tag"
          v-for="tag in dynamicTags"
          size="mini"
          closable
          :disable-transitions="false"
          @close="handleClose(tag)"
          @click="handleClick(tag)"
          >
          {{tag}}
        </el-tag>
      </div> -->
    <!-- </el-card> -->
  </div>
</template>

<script>
/* eslint-disable */
export default {
  props:['isCollapse'],
  data() {
    return {
      collapse : '',
      breadItemDate:['首页','导航一','导航二','导航三'],
      dynamicTags: ['标签一', '标签二', '标签三'],
      // showindex:localStorage.getItem('index')
    }
  },
  components: {
    
  },
  created(){
    this.collapse = this.isCollapse
    
  },
  // watch(){
  //   showindex()
  //   console.log('2')
  //   this.showindex=localStorage.getItem('index')
  //   console.log('this.showindex',this.showindex)
  // },
  methods: {
    handleClose(tag) {
        this.dynamicTags.splice(this.dynamicTags.indexOf(tag), 1);
    },
    handleClick(tag){
      console.log(tag)
    },
    
    // packUp(){
    //   this.collapse = false
    //   this.$emit('changeSidebar',this.collapse)
    // },
    // unfold(){
    //   this.collapse = true
    //   this.$emit('changeSidebar',this.collapse)
    // }
  }
}
</script>
<style type="text/css">
  .el-icon-caret-left{
    float: left;
  }
  .el-icon-caret-right{
    float: left;
  }
  .el-tag + .el-tag {
    margin-left: 10px;
  }
  .button-new-tag {
    margin-left: 10px;
    height: 32px;
    line-height: 30px;
    padding-top: 0;
    padding-bottom: 0;
  }
  .input-new-tag {
    width: 90px;
    margin-left: 10px;
    vertical-align: bottom;
  }
  .el-header{
    padding :0;
  }
  .el-card__body{
    padding:0;
  }
</style>