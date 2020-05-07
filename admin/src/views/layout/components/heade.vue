<template>
<div class="">
    <!-- <div class="el-icon-s-home icon" @click="leftrightflag" ></div> -->
   <!-- <span class="color">后管系统</span> -->
   <div class="sys" @click="butsystem" v-bind:class="[isactive==true?'colour1':'colour2']">系统管理</div>
   <div v-if="isunderline" class="underline1"></div>
   <div class="user" @click="butuser" v-bind:class="[inactive==true?'colour1':'colour2']">用户管理</div>
   <div v-if="inunderline" class="underline2"></div>
<!-- <el-button type="primary"  class="system" @click="butsystem" v-bind:class="{ active: isActive }">系统管理</el-button> -->
<!-- <el-button type="primary" class="user" @click="butuser"  v-bind:class="{ active: isActive1 }">用户管理</el-button> -->
<div>
  <img class="imgmargin" src="@/assets/touxiang.png">
    <el-col :span="5">
    <!-- <span class="demonstration">click 激活</span> -->
    <el-dropdown trigger="click" class="aaa" @command="handleCommand">
         
      <span class="el-dropdown-link">
         <!-- <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar> -->
        梁俊<i class="el-icon-arrow-down el-icon--right"></i>
      </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item command="more">更多</el-dropdown-item>
        <el-dropdown-item command="a">个人信息</el-dropdown-item>
        <el-dropdown-item command="b">修改密码</el-dropdown-item>
        <!-- <el-dropdown-item command="c">退出登录</el-dropdown-item> -->
      </el-dropdown-menu>
    </el-dropdown>
  </el-col>
  <img class="exit" @click="exit()" src="@/assets/exit.png">
          <el-dialog title="密码修改" class="dialog-width" :visible.sync="dialogTableVisible" center :append-to-body='true' :lock-scroll="false" >
          <Password @passworddialog="passworddialog"></Password>
          </el-dialog>
</div>
</div>
</template>
<script>
import Password from "../../but/passwordbut"
export default {
    data() {
    return {
      flag:'',
      leftrighrflag:'right',
      isunderline:true,
      inunderline:false,
      dialogTableVisible:false,
      // ispassclose:''
      isactive:true,
      inactive:false
    }
  },
  components:{
    Password
  },
  methods: {
    butsystem(){
       this.flag=true;
       this.isactive=true
       this.inactive=false
       console.log('1')
       this.isunderline=true;
       this.inunderline=false;
      this.$emit('changehead',this.flag)
    },
    butuser(){
       this.flag=false
       this.isactive=false
       this.inactive=true
       this.isunderline=false;
       this.inunderline=true;
         console.log('2')
      this.$emit('changehead',this.flag)
    },
    // leftrightflag(){
    //     if(this.leftrighrflag=='left'){
    //         this.leftrighrflag='right'
    //         this.$emit('changehead',this.leftrighrflag)
    //     }else{
    //         this.leftrighrflag='left'
    //         this.$emit('changehead',this.leftrighrflag)
    //     }
    // },
    handleCommand(command){
        if(command=='c'){
        this.$router.push({path:'/'});
        sessionStorage.setItem('token','')
        }else if(command=='b'){
          this.dialogTableVisible=true
        }else if(command=='more'){
          console.log('走的更多')
        }
    },
    exit(){
      this.$router.push({path:'/'});
      // sessionStorage.setItem('token','')
    },
    passworddialog(data){
      console.log('data',data)
      if(data=='close'){
        this.dialogTableVisible=false;
      }
    }
  },
    
}
</script>
<style scoped>
.color{
    position: absolute;
    color: azure;
    font-size: 28px;
    padding-left: 40px;
    padding-top: 25px
}
.backgroud{
    background: #FFFFFF;
    height:50px;
    box-shadow:0px 2px 12px 0px rgba(188,188,188,0.5);
}

.user{
  /* margin: 14px 500px 14px 650px; */
  position: absolute;
  top: 14px;
  left: 1000px;
   width:64px;
height:22px;
font-size:16px;
font-family:PingFangSC-Regular,PingFang SC;
background: #FFFFFF;
/* color:rgba(153,153,153,1); */
line-height:22px;
}
/* .icon{
    padding-top: 40px;
    padding-left: 15px;
    position: absolute;
    z-index: 100;
} */
/* .active{
   border-bottom:1px solid #DCDFE6
} */
.aaa{
    position: absolute;
    top: 14px;
    right: 60px;
}
.imgmargin{
    position: absolute;
    top: 8px;
    right: 120px;
}
.exit{
  position: absolute;
  top: 16px;
  right: 20px;
}
.sys{
  margin: 14px 500px 14px 500px;
  width:64px;
  height:22px;
  font-size:16px;
  font-family:PingFangSC-Semibold,PingFang SC;
  background: #FFFFFF;
/* color:rgba(67,128,255,1); */
line-height:22px;
}
.underline1{
  position: absolute;
  left: 630px;
  width:200px;
height:4px;
background:rgba(67,128,255,1);
}
.underline2{
  position: absolute;
  left: 930px;
  width:200px;
height:4px;
background:rgba(67,128,255,1);
}
.colour1{
  color:rgba(67,128,255,1);
  font-weight:600;
}
.colour2{
  color:rgba(153,153,153,1);
  font-weight:400;
}
</style>