
<template>
  <div class="hello background"  :style="{backgroundImage: 'url(' + login + ')' }">
     <div> 
     <div style=""> 
       <div style="width: 440px;height: 370px;position: relative;float: right;margin-top: 180px;margin-right: 150px;background:#FFFFFF"> 
         <div class="head">
            <div class="name">
           <div style="padding-top: 29px;padding-left: 75px;">内部后台管理平台</div>
           </div> 
         </div>
         <div class="body">
           <div class="empNo" >
             <img class="loginicon" style="padding-top:8px" src="@/assets/empNo.png" v-if="isempNo">
             <img class="loginicon" style="padding-top:8px" src="@/assets/empNo1.png" v-else>
             <input class="input" type="text" placeholder='请输入员工号' v-model="empNo">
           </div>
           <div class="empNo" style="margin-top:10px">
             <img class="loginicon" style="padding-top:6px" src="@/assets/username.png" v-if="isusername">
             <img class="loginicon" style="padding-top:6px" src="@/assets/username1.png" v-else>
             <input class="input" type="text" placeholder='请输入用户名' v-model="userName">
           </div>
           <div class="empNo" style="margin-top:10px">
             <img class="loginicon" style="padding-top:7px" src="@/assets/phone.png" v-if="isphone">
             <img class="loginicon" style="padding-top:7px" src="@/assets/phone1.png" v-else>
             <input class="input" type="text" placeholder='请输入联系方式' v-model="userPhone">
           </div>
           <div class="empNo" style="margin-top:10px">
             <img class="loginicon" src="@/assets/password.png" v-if="ispassword">
             <img class="loginicon" src="@/assets/password1.png" v-else>
             <input class="input" type="password" placeholder='请输入密码' v-model="password">
           </div>
           <div class="empNo" style="margin-top:30px;height:38px;" v-bind:class="[isactive==true?'colour1':'colour2']">
             <div style="float: left;margin: 9px 0px 0px 142px;color:#FFFFFF" @click="doLogin()">登录</div>
           </div>
         </div>
         <!-- <table> 
            <tr> 
                <td>员工号</td> <td> <el-input v-model="empNo" placeholder="请输入员工号" ></el-input> 
                </td> 
            </tr> 
            <tr> 
                <td>用户名</td> <td> <el-input v-model="userName" placeholder="请输入用户名" ></el-input> 
                </td> 
            </tr> 
            <tr> 
                <td>手机号</td> <td> <el-input v-model="userPhone" placeholder="请输入手机号" ></el-input> 
                </td> 
            </tr>
            <tr> 
                <td>密码</td> 
                <td> 
                  <el-input type="password" v-model="password" placeholder="请输入密码" >
                  </el-input> 
                </td> 
            </tr>  -->
            <!-- <tr>  -->
              <!-- 占两行--> 
              <!-- <td colspan="2"> 
                <el-button style="width: 300px" type="primary" @click="doLogin()" :plain="true">登录
                </el-button> 
              </td> 
            </tr>
          </table>  -->
       </div> 
      </div> 
      </div> 
  </div>
</template>
<!--mockjs应用页面-->
<script>
import login from '@/assets/666.jpg'
export default {
    data(){
        return{
          login:login,
            empNo:'',
            password:'',
            userName:'',
            userPhone:'',
            ip:'',
            isempNo:true,
            isusername:true,
            isphone:true,
            ispassword:true,
            isactive:true,
        }
    },
watch:{
    empNo(){
      if(this.empNo!==''){
        this.isempNo=false
        this.isactive=false
      }else {
        if(this.empNo==''){
          this.isempNo=true
          if(this.userPhone==''&&this.userName==''&&this.password==''){
            this.isactive=true
          }
        }
      }
    },
    userName(){
      if(this.userName!==''){
        this.isusername=false
        this.isactive=false
      }else{
        if(this.userName==''){
          this.isusername=true
          if(this.userPhone==''&&this.empNo==''&&this.password==''){
            this.isactive=true
          }
        }
      }
    },
    userPhone(){
      if(this.userPhone!==''){
        this.isphone=false
      }else{
        if(this.userPhone==''){
          this.isphone=true
          if(this.userName==''&&this.empNo==''&&this.password==''){
            this.isactive=true
          }
        }
      }
    },
    password(){
      if(this.password!==''){
        this.ispassword=false
      }else{
        if(this.password==''){
          this.ispassword=true
          if(this.userName==''&&this.empNo==''&&this.userPhone==''){
            this.isactive=true
          }
        }
      }
    },
},
    // created:{
    //   doLogin()
    // },
    mounted(){
      

    },
    methods:{
        
        doLogin(){
          let data={
            "head":{
              "orgId":"1",
              "channelId":"1",
              "ip":"127.0.0.1"
            },
            // "body":{
            //   "empNo":"00000001",
            //   "userName":"",
            //   "userPhone":"",
            //   "password":"wangxihong4"
            // }
            "body":{
              "empNo":this.empNo,//员工号
              "userName":this.userName,//用户名
              "userPhone":this.userPhone,//手机号
              "password":this.password//密码
            }
          }
          console.log('登录参数',data)
           this.$http.post('./api/manage/login.do',data).then((res)=>{
             if(res.body.code=='0'){
               this.$message({
               message: '登陆成功',
               type: 'success'
            });
            sessionStorage.setItem('userInfor',JSON.stringify(res.body.data))
            sessionStorage.setItem('token',res.body.data.token)
            setInterval(() => {
 
          this.refresh()

          }, 1800000);

               this.$router.push({path:'/layout'});
             }else if(res.body.code=='20002') {
              
              this.$message.error(
               '账号不存在或密码错误',
            );
             }else if(res.body.code=='10011'){
               this.$message({
               message: '员工号、用户号、手机号不能同时为空',
               type: 'warning'
            });
             }
              console.log('res',res)
               },function (error) {
                  console.log('error',error);
               })
        },
        refresh(){
          let data={
            "head":{
              "userId":"00000001",
              "orgId":"1",
              "channelId":"1",
              "ip":"127.0.0.1"
            }
          }
          this.$axios({
              url:'./api/public/refresh/token.do',
              method: 'post',
              data: data,
              headers:{
                'Content-Type':'application/json',
                'token':sessionStorage.getItem('token')
              }
              })
              .then(respanse=>{
              console.log('查询模板',respanse);
                if(respanse.data.code=='0'){
                        this.$message({
                        message: '查询成功',
                        type: 'success'
                      });
                sessionStorage.setItem('token',respanse.body.data.token)
              }else if(respanse.data.code=='20002') {
                        this.$message.error(
                        '出现错误',
                      );
              }
              })
        },
    }
}
</script>
<style>
.background{
  width: 100%;
        height: 100%;
        /* background: url('~@/src\assets\login.png') center center no-repeat;
        background-size: 100px auto; */
}
.input {
    border: none;
    height: 31px;
    outline: medium;
    width: 174px;
    background: #EFF5FF;
    /* color: #EFF5FF; */
    color: #333333;
    font-size:14px;
font-family:PingFangSC-Regular,PingFang SC;
}
input::-webkit-input-placeholder{
  color: #9EBAE0;
}
.name{
      width: 350px;
    height: 80px;
    margin-left: 45px;
    border-bottom: 0.01rem dashed #DCDCDC;
    font-size:24px;
font-family:PingFangSC-Medium,PingFang SC;
font-weight:500;
color:rgba(70,117,162,1)
}
.el-card__header {
border-bottom: none
}
.xuxian{
  width:380px;
  height:1px;
  background: rgba(220, 220, 220, 1);
  
  margin-left: 31px;
}
.head{
  width: 100%;
  height: 80px;
}
.body{
  width: 90%;
    height: 250px;
    margin-left: 22px;
    margin-top: 20px;
}
.empNo{
  width: 320px;
    height: 34px;
    margin-left: 38px;
    background: rgba(239,245,255,1);
}
.loginicon{
  float: left;
    padding: 5px 10px 0px 16px;
}
.colour1{
  background: #CCCCCC;
}
.colour2{
  background: #4380FF;
}
</style>
