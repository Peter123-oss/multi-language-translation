<!-- HTML -->
<template>
    <div>

        <div class="login_back" style="background-color:#F4F9FF; position: relative; /* 设置相对定位 */">
            <div class="back_button"
                style="width: 50px;height: 30px; position: absolute; /* 设置绝对定位 */ top: 30px; /* 定位到顶部 */ left: 30px; /* 定位到左边 */">
                <el-button size="large":icon="Search">取消</el-button>
            </div>
            <div class="login_back2">
                <h1>账号密码登录</h1>
                <div class="login_block" style="margin-top: 50px;">
                    <el-form style="margin-left: 90px; width: 50%;">
                        <el-form-item>
                            <span style="height: 50px;">
                                <img src="./pictures/login_pic/login_face.png" style="width: 40px; ">

                                <el-input style="width:150px;height: 40px;margin-left: 10px;margin-bottom: 30px; "
                                    v-model="username" placeholder="请输入账号" /></span>
                        </el-form-item>

                        <el-form-item style="height: 50px;">
                            <span style="height: 50px;">
                                <img src="./pictures/login_pic/login_suo.png" style="width: 40px; ">
                                <el-input style="width:150px;height: 40px;margin-left: 10px;margin-bottom: 30px; "
                                    v-model="password" placeholder="请输入密码" show-password />
                            </span>
                            <br>
                            <el-button style="border: 0ch; margin-top: 4px;" plain:icon="forget"
                                href="https://">忘记密码？</el-button>

                            <el-button style="border: 0ch;width: 50px;;margin-left: 50px;color: #3291F8;"
                                plain:icon="register" href="https://">去注册</el-button>
                        </el-form-item>
                        <el-button
                            style="align-items: center; background-color:#A4ADB3; width: 180px;height: 50px;border-radius: 15px;border:0px;margin-left: 20px;margin-top: 60px;"
                            type="primary" @click="login">登录</el-button>
                    </el-form>
                </div><br>

                <h3>使用第三方登录</h3>
                <div class="third_login" style="margin-top: 20px;">
                    <button class="weixin_login"></button>
                    <button class="phone_login"></button>
                    <button class="qq_login"></button>


                </div>
            </div>
        </div>

    </div>

</template>

<!-- javascript -->
<script setup>

import { ref, onMounted } from 'vue'
import api from '../../utils/api'
const username = ref('');
const password = ref('');
// 箭头函数
// const  方法 = (形参)=>{
// 方法体
// }

// 耗时操作  异步
const login = async () => {

    // var url = "http://localhost:5000/user/login"
    const response = await fetch(api.user.login, {
        method: "POST",
        body: JSON.stringify({
            username: username.value,
            password: password.value
        })
    })
    const data = await response.json()
    console.log(data)
}



</script>

<!-- css -->
<style>
.weixin_login {
  background-image: url('./pictures/login_pic/weixin.png'); /* 设置背景图片 */
  background-size: cover; /* 背景图片覆盖整个按钮 */
  background-repeat: no-repeat; /* 防止背景图片重复 */
  background-position: center; /* 背景图片居中 */
  border: none; /* 移除边框 */
  width: 35px; /* 设置按钮宽度 */
  height:30px; /* 设置按钮高度 */
  cursor: pointer; /* 改变鼠标悬停时的光标 */
  margin-left: 90px;
  background-color: transparent; /* 明确设置背景为透明 */
  /* 如果需要按钮在鼠标悬停时改变透明度，可以添加以下代码 */
  opacity: 0.7; /* 初始透明度 */
}
.weixin_login:hover{
    opacity: 1.0;
}
.phone_login {
  background-image: url('./pictures/login_pic/phone.png'); /* 设置背景图片 */
  background-size: cover; /* 背景图片覆盖整个按钮 */
  background-repeat: no-repeat; /* 防止背景图片重复 */
  background-position: center; /* 背景图片居中 */
  border: none; /* 移除边框 */
  width: 35px; /* 设置按钮宽度 */
  height:35px; /* 设置按钮高度 */
  cursor: pointer; /* 改变鼠标悬停时的光标 */
  margin-left: 50px;
  background-color: transparent; /* 明确设置背景为透明 */
  /* 如果需要按钮在鼠标悬停时改变透明度，可以添加以下代码 */
  opacity: 0.7; /* 初始透明度 */
}
.phone_login:hover{
    opacity: 1.0;
}
.qq_login {
  background-image: url('./pictures/login_pic/qq.png'); /* 设置背景图片 */
  background-size: cover; /* 背景图片覆盖整个按钮 */
  background-repeat: no-repeat; /* 防止背景图片重复 */
  background-position: center; /* 背景图片居中 */
  border: none; /* 移除边框 */
  width: 35px; /* 设置按钮宽度 */
  height:35px; /* 设置按钮高度 */
  cursor: pointer; /* 改变鼠标悬停时的光标 */
  margin-left: 50px;
  background-color: transparent; /* 明确设置背景为透明 */
  /* 如果需要按钮在鼠标悬停时改变透明度，可以添加以下代码 */
  opacity: 0.7; /* 初始透明度 */
}
.qq_login:hover{
    opacity: 1.0;
}
h3 {
    text-align: center;
}

.login_back {
    color: F4F9FF;
    width: 1026px;
    height: 615px;
    margin-top: 10%;
    margin-bottom: 10%;
    margin-left: 90px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 50px;
}

.login_back2 {
    background-color: #FFFF;
    width: 400px;
    height: 500px;
    border-radius: 40px;
}

h1 {
    margin-top: 20px;
    color: #5D5D5D;
    text-align: center;
}
</style>