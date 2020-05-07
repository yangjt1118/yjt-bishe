<template>
  <div >
    <div class="update" style="padding:20px">
          <el-form
            :label-position="labelPosition"
            :model="user"
            label-width="80px"
            ref="user"
            class="inputBox"
            :rules="rules"
          >
            <el-form-item label="性别" prop="gender">
              <el-radio-group v-model="user.gender">
                  <el-radio label="男"></el-radio>
                  <el-radio label="女"></el-radio>
             </el-radio-group>
            </el-form-item>
            <el-form-item label="电话" prop="phone">
              <el-input v-model.number="user.phone"></el-input>
            </el-form-item>
            <el-form-item label="地址" prop="address">
              <el-input  v-model="user.address"></el-input>
            </el-form-item>
            <el-button type="primary" @click="register('user')">修改</el-button>
            <el-button @click="reset(user)">重置</el-button>
          </el-form>
    </div>
  </div>
</template>
<script>
  //这里要俺需要引入，我不是一个对象
  import {isvalidPhone} from '../plugins/validate'
  //定义一个全局的变量，谁用谁知道
  var validPhone=(rule, value,callback)=>{
      if (!value){
          callback(new Error('请输入电话号码'))
      }else  if (!isvalidPhone(value)){
        callback(new Error('请输入正确的11位手机号码'))
      }else {
          callback()
      }
  }
import { mapMutations } from "vuex";
export default {
  data() {
    return {
      activeName: "first",
      labelPosition: "right",
      user: {},
      user2:{},
      rules:{
        gender:[
           { required: true, message: '请选择活动资源', trigger: 'change' }
        ],
        phone:[
          //  { required: true, message: '年龄不能为空'},
            // { type: 'number',message: '年龄必须为数字值'}
            { required:true, trigger: 'blur', validator: validPhone }//这里需要用到全局变量
        ],
        address:[
           { required: true, message: '请输入请输入账号名称活动名称', trigger: 'blur' },
        ],
      },
    };
  },
  mounted() {
      this.fench()
  },
  methods: {
    ...mapMutations(["changeLogin"]),
    fench(){
        this.user2 = JSON.parse(sessionStorage.getItem("user"));
        // console.log("user2",this.user2)
        if (this.user2==null){
            this.$router.push("/login")
        }
        this.user.name = this.user2.name;
        console.log(this.user)
        this.$http.post("user/query",this.user)
        .then(res=>{
            if(res.data.code==200){
                this.user=res.data.data
            }
        })
    },
    register(formName) {
      this.user.name = this.user2.name;
      this.$refs[formName].validate((valid) => {
          if (valid) {
            this.$http
        .post("user/update", this.user)
        .then(res => {
          if (res.data.code == 200) {
            this.$message({
              message: "修改成功",
              type: "success"
            });
            this.user={}
          } else {
            // console.log(res.data.data)
            this.$message({
              message: "修改失败,请稍后重试",
              type: "error"
            });
          }
        })
          } else {
            console.log('error submit!!');
            return false;
          }
        });
    },
    reset() {
      this.user={}
    }
  }
};
</script>

<style>
html,
body {
  padding: 0px;
  margin: 0px;
  height: 100%;
  /* width: 100%;
  background: url("../assets/timg.jpg") no-repeat center center;
  background-size:100% 100%; */
}
.update{
    margin: 20px;
    width: 400px;
     background:rgb(229, 233, 233);
	box-sizing:border-box;
	box-shadow:0 15px 25px rgba(0,0,0,.5);
	border-radius: 10px;/*登录窗口边角圆滑*/
}



</style>
