<template>
    <el-form ref="form" :model="sizeForm" label-width="80px" size="mini">
  <el-form-item label="用户id">
    <el-input v-model="sizeForm.userId" ></el-input>
  </el-form-item>
  <el-form-item label="用户名">
    <el-input v-model="sizeForm.userName" ></el-input>
  </el-form-item>
  <el-form-item label="旧密码">
    <el-input type="oldpassword" v-model="sizeForm.oldPassword" show-password></el-input>
  </el-form-item>
  <el-form-item label="新密码">
    <el-input type="newpassword" v-model="sizeForm.newPassword" show-password></el-input>
  </el-form-item>
  <el-form-item size="large">
    <el-button type="primary" @click="onSubmit">确定</el-button>
    <el-button @click="closepassword">取消</el-button>
  </el-form-item>
</el-form>

</template>

<script>
  export default {
    data() {
      return {
        sizeForm: {
          userId:JSON.parse(sessionStorage.getItem('userInfor')).empNo,
          userName:JSON.parse(sessionStorage.getItem('userInfor')).userName,
          oldPassword:'',
          newPassword:'',
        },
          ispassclose:''
      };
    },
    methods: {
      // onSubmit() {
      //   // var r=new XMLHttpRequest();
      //   // r.open('POST','./api/manage/update/password.do',true)
      //   // r.setRequestHeader("token",sessionStorage.getItem('token'))
      //   // r.send()
      //     let data={
      //           "head":{
      //           "userId":this.sizeForm.userId,
      //             "orgId":"1",
      //             "channelId":"1",
      //             "ip":"127.0.0.1"
      //           },
      //           "body":{
      //             "empNo":this.sizeForm.userId,
      //             "newPassword":this.sizeForm.newPassword,
      //             "oldPassword":this.sizeForm.oldPassword,
      //           }
      //         }
      //         // r.send(data)
      //         console.log('data',data)
      //     // let Headers={"Authorization": sessionStorage.getItem('token')}
      //   this.$http.post('./api/manage/update/password.do',data).then((res)=>{
      
      //       console.log('ressss',res)
      //        if(res.body.code=='0'){
      //          this.$message({
      //          message: '操作成功',
      //          type: 'success'
      //       });
      //       this.closepassword()
      //        }else if(res.body.code=='20002') {
              
      //         this.$message.error(
      //          '账号不存在或密码错误',
      //       );
      //        }
      //         console.log('res',res)
      //          },function (error) {
      //             console.log('error',error);
      //          })
      // },
      onSubmit(){
        let data={
                "head":{
                "userId":this.sizeForm.userId,
                  "orgId":"1",
                  "channelId":"1",
                  "ip":"127.0.0.1"
                },
                "body":{
                  "empNo":this.sizeForm.userId,
                  "newPassword":this.sizeForm.newPassword,
                  "oldPassword":this.sizeForm.oldPassword,
                }
              }
        this.$axios({
              url:'./api/manage/update/password.do',
              method: 'post',
              data: data,
              headers:{
                'Content-Type':'application/json',
                'token':sessionStorage.getItem('token')
              }
              
              })
              .then(respanse=>{
              console.log(respanse);
              console.log(respanse.data.code)
                if(respanse.data.code=='0'){
                        this.$message({
                        message: '操作成功',
                        type: 'success'
                      });
              }else if(respanse.data.code=='20002') {
                        this.$message.error(
                        '账号不存在或密码错误',
                      );
              }
              })
      },
      closepassword(){
        console.log('123')
        this.ispassclose='close'
        this.$emit('passworddialog',this.ispassclose)
      },
    }
  };
</script>
<style scoped>
/* .el-dialog{
  width: 50%!important
} */
</style>