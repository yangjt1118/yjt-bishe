<template>
  <div>
   <h1>新增银行资讯</h1>
<el-form ref="form" :model="form" label-width="80px" :rules="rules">
      <el-form-item label="文章标题" prop="title">
        <el-input v-model="form.title" ></el-input>
      </el-form-item>
      <el-form-item label="文章标签" prop="tags">
        <el-select v-model="form.tags" multiple placeholder="请选择标签">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          ></el-option>
        </el-select>
        <span class="addtag" @click="toaddtag">没有合适的标签？点击新建</span>
      </el-form-item>
      <el-form-item label="文章图片">
               <el-upload
  class="avatar-uploader"
  action="https://jsonplaceholder.typicode.com/posts/"
  :show-file-list="false"
  :on-success="handleAvatarSuccess"
  :before-upload="beforeAvatarUpload">
  <img v-if="imageUrl" :src="imageUrl" class="avatar">
  <i v-else class="el-icon-plus avatar-uploader-icon"></i>
</el-upload>
      </el-form-item>
      <el-form-item label="文章内容" prop="content">
        <el-input type="textarea" :autosize="{ minRows: 3, maxRows: 8}" v-model="form.content"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="smbmit('form')">立即创建</el-button>
        <el-button @click="reset">取消</el-button>
      </el-form-item>
    </el-form>
    <el-dialog
  title="新增标签"
  :visible.sync="centerDialogVisible"
  width="30%"
  center>
  <el-form ref="tag" :model="tag" label-width="80px">
    <el-form-item label="文章标题" prop="title">
        <el-input v-model="tag.name" ></el-input>
      </el-form-item>
  </el-form>
  <span slot="footer" class="dialog-footer">
    <el-button @click="noaddtag">取 消</el-button>
    <el-button type="primary" @click="addtag">确 定</el-button>
  </span>
</el-dialog>
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
    border-color: #409EFF;
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
        centerDialogVisible: false,
        tag:{},
        tag1: { tag_id: "" },
      options: [],
      na: [],
      form: {},
      value: "",
      imageUrl: "",
      uploadForm: new FormData(),
      fileList: [],
            rules: {
        title: [
          {
            required: true,
            message: "请输入文章标题",
            trigger: "blur",
          },
        ],
        tags: [
          {
            required: true,
            message: "请选择文章标签",
            trigger: "blur",
          },
        ],
        content: [
          {
            required: true,
            message: "请输入文章内容",
            trigger: "blur",
          },
        ],
      },
      admin2:{}
      };
    },
     mounted() {
    this.fench();
  },
    methods: {
      toaddtag(){
        this.centerDialogVisible=true
      },
      addtag(){
        this.admin2 = JSON.parse(sessionStorage.getItem("admin"));
        this.tag.admin_id=this.admin2.admin_id
        console.log(this.tag)
        this.$http.post("/admin/addtag",this.tag)
        .then(res=>{
          if(res.data.code==200){
            this.$message({
            message: res.data.msg+"，刷新页面即可",
            type: "success"
          });
          }else{
            this.$message({
            message: res.data.msg,
            type: "error"
          });
          }
        })
        this.centerDialogVisible=false
        this.options=[]
        this.tag={}
        this.fench()
      },
      noaddtag(){
        this.centerDialogVisible=false
        this.tag={}
      },
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
      } else{
          this.uploadForm.append("image", file);
        console.log(this.uploadForm)
        }
        
      },
         //上传到服务器
     smbmit(formName) {
       this.form.admin_id = this.admin2.admin_id;
      // console.log(this.form);
      this.$refs[formName].validate((valid) => {
        if (valid) {
      this.form.content = this.form.content
        .replace(/\r\n/g, "<br/>")
        .replace(/\n/g, "<br/>")
        .replace(/\s/g, "&nbsp;&nbsp;&nbsp;&nbsp;");
      // let formdata1 = new FormData();
      // console.log(this.form.content, 77777);
      Object.keys(this.form).forEach(key => {
        this.uploadForm.append(key, this.form[key]);
      });
       let data = this.uploadForm;
       this.$http.post("admin/addarticle", this.uploadForm).then(res => {
        // console.log(res.data.code,"返回数据");
        if(res.data.code==200){
          this.$message({
            message: res.data.msg,
            type: "success"
          });
        }else if(res.data.code==400){
          this.$message({
          message:"发布资讯失败",
          type:"error"
        })
        }
      }).catch(err=>{
        this.$message({
          message:err.data.msg,
          type:"error"
        })
      })
        // this.$refs.upload.submit();
        console.log(data,888)
        this.form={}
        this.uploadForm=new FormData()
        }
        })
      },
      reset(){
        this.form={}
      },
          fench() {
            this.admin2 = JSON.parse(sessionStorage.getItem("admin"));
      this.$http.get("admin/querytag").then((res) => {
        if (res.data.code == 200) {
          this.na = res.data.data;
          // console.log(this.na,222222222)
          for (let index in this.na) {
            this.options.push({
              value: this.na[index].tag_name,
              label: this.na[index].tag_name,
            });
          }
          // console.log(this.options,66666666666)
        }
      });
    },
    }
  }
</script>
<style>
  .addtag {
    color: rgb(205, 226, 231);
    margin-left: 5px;
    cursor: pointer;
  }
  .addtag :hover{
    color: turquoise;
  }
</style>