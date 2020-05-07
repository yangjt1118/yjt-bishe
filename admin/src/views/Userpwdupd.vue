<template>
  <div>
    <div class="update" style="padding:20px">
      <el-form
        :label-position="labelPosition"
        :model="user"
        label-width="80px"
        ref="user"
        class="inputBox"
        :rules="rules"
      >
        <el-form-item label="下拉框" prop="value">
          <el-select v-model="user.value" placeholder="请选择修改类型">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="原密码" prop="password">
          <el-input v-model="user.password"></el-input>
        </el-form-item>
        <el-form-item label="新密码" prop="password2">
          <el-input v-model="user.password2"></el-input>
        </el-form-item>
        <el-button type="primary" @click="register('user')">修改</el-button>
        <el-button @click="reset('user')">重置</el-button>
      </el-form>
    </div>
  </div>
</template>
<script>

import { mapMutations } from "vuex";
export default {
  data() {
    return {
      labelPosition: "right",
      user: {},
      user2: {},
      options: [
        {
          value: "1",
          label: "修改登录密码"
        },
        {
          value: "2",
          label: "修改支付密码"
        }
      ],
      rules: {
        password:[
           { required: true, message: '请输入原密码', trigger: 'blur' },
           { min: 6, max: 16, message: '长度在 6 到 16 个字符', trigger: 'blur' }
        ],
        password2:[
           { required: true, message: '请输入要修改的密码', trigger: 'blur' },
           { min: 6, max: 16, message: '长度在 6 到 16 个字符', trigger: 'blur' }
        ],
        value: [
            { required: true, message: '请选择修改类型', trigger: 'change' }
          ],
      }
    };
  },
  mounted() {
    this.fench();
  },
  methods: {
    ...mapMutations(["changeLogin"]),
    fench() {
      this.user2 = JSON.parse(sessionStorage.getItem("user"));
      console.log("user2", this.user2);
      if (this.user2 == null) {
        this.$router.push("/login");
      }
      this.user.name = this.user2.name;
      console.log(this.user);
      this.$http.post("user/query", this.user).then(res => {
        if (res.data.code == 200) {
          this.user = res.data.data;
        }
      });
    },
    register(formName) {
      this.user.name = this.user2.name;
      this.$refs[formName].validate(valid => {
        if (valid) {
            console.log("this.user",this.user)
          this.$http.post("user/updatepassword", this.user).then(res => {
            if (res.data.code == 200) {
              this.$message({
                message: "修改成功",
                type: "success"
              });
              this.user = {};
            } else {
              console.log(res.data.msg);
              this.$message({
                message: res.data.msg,
                type: "error"
              });
              this.user = {};
            }
          });
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    reset() {
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
.update {
  margin: 20px;
  width: 400px;
  background: rgb(229, 233, 233);
  box-sizing: border-box;
  box-shadow: 0 15px 25px rgba(0, 0, 0, 0.5);
  border-radius: 10px; /*登录窗口边角圆滑*/
}
</style>
