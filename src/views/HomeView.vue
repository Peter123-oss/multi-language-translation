<script lang="ts" setup>
import { ref } from 'vue'
import { ArrowDown } from '@element-plus/icons-vue'


const handleClick = () => {
  // eslint-disable-next-line no-alert
  alert('button click')
}

//下拉按钮显示被选项
const selectedLanguage = ref('')
const buttonStyle = ref({
  backgroundColor: '#FFFF',
  color: 'black',
  border: '0px',
  position: 'inherit',
  left: '70px',
  top: '50px'
})

const handleCommand = (command: string) => {
  selectedLanguage.value = command
}

const textarea=ref('')

</script>


<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <img src="./user/pictures/home_pic/logo.png" style="width: 237px;height: 50px;margin-top: 5px;;">
        <span>
          <el-button class="vip_service" plain:icon="vip" href="https://">
            <h2 style="font-weight: 400;">￥ 开通会员</h2>
          </el-button>
           
          <el-button class="login_button" >
            <img src="./user/pictures/home_pic/login.png" alt="">
            <h2>登录</h2>
          </el-button>
        </span>
      </el-header>
      <el-container>
        <el-aside>
          <div class="button" style="margin-top: 50px;">
            <img src="./user/pictures/home_pic/word.png">
            <el-button>按词翻译</el-button>
          </div>
          <div class="button">
            <img src="./user/pictures/home_pic/history.png">
            <el-button>历史记录查询</el-button>
          </div>
          <div class="button">
            <img src="./user/pictures/home_pic/sentence.png">
            <el-button>语句翻译</el-button>
          </div>
          <div class="button">
            <img src="./user/pictures/home_pic/picture.png">
            <el-button>图片识别</el-button>
          </div>
          <div class="button">
            <img src="./user/pictures/home_pic/voice.png">
            <el-button>语音识别</el-button>
          </div>
          <div class="button">
            <img src="./user/pictures/home_pic/document.png">
            <el-button>文档翻译</el-button>
          </div>
          <br>
          <div class="button" style="margin-left: 20px;">
            <el-button style="background-color: #FCCEA0;width: 130px;height: 40px;border-radius: 12px;"><h3 style="font-weight: 600;">￥ 会员中心</h3></el-button>
          </div>
        </el-aside>
        <el-main>
          <div class="trans_back">
            <el-dropdown @command="handleCommand">
              <el-button type="primary" :style="buttonStyle">
                {{ selectedLanguage || '下拉选择语言' }}<el-icon class="el-icon--right"><arrow-down /></el-icon>
              </el-button>
              <template #dropdown>
                <el-dropdown-menu>
                  <el-dropdown-item command="中文">中文</el-dropdown-item>
                  <el-dropdown-item command="英语">英语</el-dropdown-item>
                  <el-dropdown-item command="法语">法语</el-dropdown-item>
                  <el-dropdown-item command="俄语">俄语</el-dropdown-item>
                </el-dropdown-menu>
              </template>
            </el-dropdown>
            <el-input v-model="textarea" style="width: 310px;height: 350px;;position: inherit;top:100px;left:80px;border: none;" :autosize="{ minRows: 6, maxRows: 12 }" type="textarea"
              placeholder="输入要翻译的文本" />
                <button class="word_history"></button>
              <div class="separator"></div>
              <div class="result_block">
                这里输出结果
              </div>
          </div>
        </el-main>
      </el-container>
      <!-- <el-container>
        <el-aside >
          <div class="button1">
            <img src="./user/pictures/home_pic/word.png" style="width: 37px;height: 30px;">
            <el-button style="border: 0px;background-color: #F9FBFF;">按词翻译</el-button>
          </div>
          <div class="button2">
            <img src="./user/pictures/home_pic/history.png" style="width: 37px;height: 30px;">
            <el-button style="border: 0px;background-color: #F9FBFF;">历史记录查询</el-button>
          </div>
          <div class="button3">
            <img src="./user/pictures/home_pic/sentence.png" style="width: 37px;height: 30px;">
            <el-button style="border: 0px;background-color: #F9FBFF;">语句翻译</el-button>
          </div>
          <div class="button4">
            <img src="./user/pictures/home_pic/picture.png" style="width: 37px;height: 30px;">
            <el-button style="border: 0px;background-color: #F9FBFF;">图片识别</el-button>
          </div>
          <div class="button5">
            <img src="./user/pictures/home_pic/voice.png" style="width: 37px;height: 30px;">
            <el-button style="border: 0px;background-color: #F9FBFF;">语音识别</el-button>
          </div>
          <div class="button6">
            <img src="./user/pictures/home_pic/document.png" style="width: 37px;height: 30px;">
            <el-button style="border: 0px;background-color: #F9FBFF;">文档翻译</el-button>
          </div>
        </el-aside>
        <el-main>
          <div class="trans_back">

          </div>
        </el-main>
      </el-container> -->
    </el-container>
  </div>
</template>

<style scoped>
.word_history{
  background-image: url('./user/pictures/home_pic/history.png'); /* 设置背景图片 */
  background-size: cover; /* 背景图片覆盖整个按钮 */
  background-repeat: no-repeat; /* 防止背景图片重复 */
  background-position: center; /* 背景图片居中 */
  width: 40px;
  height: 40px;
  position: inherit;
  top:30px;
  right: 420px;
  border:none;
  cursor: pointer; /* 改变鼠标悬停时的光标 */
  /* 移除背景颜色，确保透明 */
  background-color: transparent; /* 明确设置背景为透明 */
  /* 如果需要按钮在鼠标悬停时改变透明度，可以添加以下代码 */
  opacity: 0.6; /* 初始透明度 */
}
.word_history:hover {
  opacity: 0.9; /* 鼠标悬停时完全不透明 */
}
.separator{
  background-color: #BBBBBB;
  width: 1px;
  height: 330px;
  position: inherit;
  top:100px;
  right: 375px;
}
.result_block{
  width: 290px;
  height: 350px;
  position: inherit;
  top:90px;
  right: 50px;

}
aside{
    .button {
    display: flex;
    /*启用flex布局 */
    align-items: center;
    /* 垂直居中对齐flex项 */
    height: 50px;
    margin-top: 15px;
    margin-left: 10px;
  }
  .button img {
    width: 37px;
    height: 30px;
  }

  .button .el-button {
    border: 0px;
    background-color: #F9FBFF;
    font-size: large;
  }

  .button2 {
    width: 120px;
  }

  .button1 {
    width: 130px;
  }

  .button:not(.button2) {
    width: 150px;
  }
}
/* .button6{
  height: 50px;
  width: 150px;
  margin-top: 20px;
  margin-left: 10px;
  display: flex;
  align-items: center;
}
.button5{
  height: 50px;
  width: 150px;
  margin-top: 20px;
  margin-left: 10px;
  display: flex;
  align-items: center;
}
.button4{
  height: 50px;
  width: 150px;
  margin-top: 20px;
  margin-left: 10px;
  display: flex;
  align-items: center;
}
.button3{
  height: 50px;
  width: 150px;
  margin-top: 20px;
  margin-left: 10px;
  display: flex;
  align-items: center;
}
.button2{
  height: 50px;
  width: 160px;
  margin-top: 20px;
  margin-left: 10px;
}
.button1{
  width: 150px;
  height: 50px;
  margin-top: 45px;
  margin-left: 10px;
  display: flex;
  align-items: center;
}  */
.login_button img{
  width: 55px;
  margin-top: 1.5px;
  cursor: pointer; /* 改变鼠标悬停时的光标 */
  /* 移除背景颜色，确保透明 */
  background-color: transparent; /* 明确设置背景为透明 */
  /* 如果需要按钮在鼠标悬停时改变透明度，可以添加以下代码 */
  opacity: 0.7; /* 初始透明度 */
}
.login_button img:hover{
  opacity: 1.0;
}
.login_button {
  position: absolute;
  width: 130px;
  height: 40px;
  top: 49%;
  /* 从顶部向下移动50% */
  left: 92%;
  /* 从左侧向右移动50% */
  transform: translate(-50%, -50%);
  border: 0ch;
  background-color: #F9FBFF;
  color: #101010;
}

.vip_service {
  position: absolute;
  top: 49%;
  /* 从顶部向下移动50% */
  left: 75%;
  /* 从左侧向右移动50% */
  transform: translate(-50%, -50%);
  border: 0ch;
  background-color: #F9FBFF;
  color: #fabf84;
  font-weight: bold;
}

.trans_back {
  background-color: #FFFF;
  width: 820px;
  height: 483px;
  position: absolute;
  /* 使用绝对定位 */
  top: 52%;
  /* 从顶部向下移动50% */
  left: 51.5%;
  border-radius: 20px;
  transform: translate(-50%, -50%);
}

.el-main {
  position: relative;
  background-color: #F4F9FF;
  height: 544px;
  border-radius: 40px;
  /* border: 3px solid; */
  overflow: hidden;
}

.el-aside {
  position: relative;
  width: 178px;
  background-color: #F9FBFF;
  /* border: 3px solid; */
  overflow: hidden;
  border-radius: 20px 0 0 20px;
}

.el-container {
  background-color: #F9FBFF;
  height: 607px;
  width: 1080px;
  border-radius:20px 20px 20px 20px;
}

.el-header {
  position: relative;
  height: 63px;
  background-color: #F9FBFF;
  /* border: 3px solid */
  border-radius: 20px 20px 0px 0px;
}

</style>