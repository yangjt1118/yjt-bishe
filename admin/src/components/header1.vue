<template>
  <div>
    <el-row type="flex" class="row-bg">
      <el-col :span="6"><img src="../assets/logo.png" alt="" style="width:214.5px;height:54px;top:10px"></el-col>
  <el-col :span="6"><div class="grid-content bg-purple"></div></el-col>
  <el-col :span="10"><div class="grid-content bg-purple-light"></div></el-col>
  <el-col :span="2"><el-dropdown trigger="click" class="aaa" @command="handleCommand">
      <span class="el-dropdown-link">
         <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
        <i class="el-icon-arrow-down el-icon--right">杨建亭</i>
      </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item command="a">个人信息</el-dropdown-item>
        <el-dropdown-item command="b">修改密码</el-dropdown-item>
        <el-dropdown-item command="c">退出登录</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown></el-col>
</el-row>
    
  </div>
</template>
<style>

</style>