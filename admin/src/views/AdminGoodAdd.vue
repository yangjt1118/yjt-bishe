<template>
  <div>
    <h1>新增理财产品</h1>
    <el-form ref="form" :model="form" label-width="80px" :rules="rules">
      <el-form-item label="商品名称" prop="name">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="商品价格" prop="price">
        <el-input v-model="form.price"></el-input>
      </el-form-item>
      <el-form-item label="文章图片">
        <el-upload
          class="avatar-uploader"
          action="https://jsonplaceholder.typicode.com/posts/"
          :show-file-list="false"
          :on-success="handleAvatarSuccess"
          :before-upload="beforeAvatarUpload"
        >
          <img v-if="imageUrl" :src="imageUrl" class="avatar" />
          <i v-else class="el-icon-plus avatar-uploader-icon"></i>
        </el-upload>
      </el-form-item>
      <el-form-item label="商品描述" prop="description">
        <el-input
          type="textarea"
          :autosize="{ minRows: 3, maxRows: 8 }"
          v-model="form.description"
        ></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="smbmit('form')">立即创建</el-button>
        <el-button @click="reset">取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<style>
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border-color: #409eff;
}
.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>

<script>
export default {
  data() {
    return {
      tag1: { tag_id: "" },
      na: [],
      form: {},
      value: "",
      imageUrl: "",
      uploadForm: new FormData(),
      fileList: [],
      rules: {
        name: [
          {
            required: true,
            message: "请输入产品名称",
            trigger: "blur",
          },
        ],
        price: [
          {
            required: true,
            message: "请输入产品价格",
            trigger: "blur",
          },
        ],
        description: [
          {
            required: true,
            message: "请输入产品描述",
            trigger: "blur",
          },
        ],
      },
      admin2:{}
    };
  },
  mounted() {},
  methods: {
    handleAvatarSuccess(res, file) {
      this.imageUrl = URL.createObjectURL(file.raw);
    },
    beforeAvatarUpload(file) {
      
            var testmsg=file.name.substring(file.name.lastIndexOf('.')+1)
      const isJPG1 =testmsg === 'jpg';
      const isJPG2 =testmsg === 'png';
      // const isLt2M = file.size / 1024 / 1024 < 10;

      if (!isJPG1&&!isJPG2) {
        this.$message.error(
          "上传图片只能是 jpg/png 格式!"
        );
      } else {
        this.uploadForm.append("image", file);
        console.log(this.uploadForm);
      }
    },
    //上传到服务器
    smbmit(formName) {
      this.admin2 = JSON.parse(sessionStorage.getItem("admin"));
      this.form.admin_id = this.admin2.admin_id;
      this.$refs[formName].validate((valid) => {
        if (valid) {
          Object.keys(this.form).forEach((key) => {
            this.uploadForm.append(key, this.form[key]);
          });
          let data = this.uploadForm;
          this.$http
            .post("admin/addgood", this.uploadForm)
            .then((res) => {
              // console.log(res.data.code,"返回数据");
              if (res.data.code == 200) {
                this.$message({
                  message: res.data.msg,
                  type: "success",
                });
              } else if (res.data.code == 400) {
                this.$message({
                  message: "发布商品失败",
                  type: "error",
                });
              }
            })
          console.log(data, 888);
          this.form = {};
          this.uploadForm = new FormData();
        } else {
          console.log("error submit!!");
          return false;
        }
      });

      // this.$refs.upload.submit();
    },
    reset() {
      this.form = {};
    },
  },
};
</script>
