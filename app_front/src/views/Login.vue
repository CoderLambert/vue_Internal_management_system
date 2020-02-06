<template>
  <div class="login-container-box">
    <div class="login-box">
      <div class="avatar-box">
        <img src="@/./assets/images/avar.jpg" alt="">
      </div>

      <el-form ref="loginFormRef" :model="loginForm" :rules="this.LoginRules" label-width="0px" class="login-box-form">
        <el-form-item prop="username">
          <el-input type="text" v-model="loginForm.username" prefix-icon="icon iconfont icon-user"></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input type="password" v-model="loginForm.password" prefix-icon="icon iconfont icon-3702mima" @keyup.enter.native="login"></el-input>
        </el-form-item>
        <el-form-item class="btns">
          <el-button type="success" class="login-btn" @click="login" >确认</el-button>
          <el-button type="info" class="login-btn" @click="resetLoginForm">重置</el-button>
        </el-form-item>
        <el-form-item class="register-tip">
          <p @click="toRegister">注册新用户</p>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import SS from '@/assets/js/utils.js'
export default {
  name: 'login',
  data () {
    return {
      loginForm: {
        username: '',
        password: ''
      },

      // 第一步 定义 rules 对象
      // 第二步 form 表单绑定 rules对象
      // 第三步 form-item 通过 prop 绑定属性验证规则
      LoginRules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' }

        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    // 重置表单
    resetLoginForm () {
      this.$refs.loginFormRef.resetFields()
    },
    // 登录
    login () {
      this.$refs.loginFormRef.validate(valid => {
        if (valid) {
          this.$http.post('login', this.loginForm)
            .then(
              res => {
                console.log(res)
                SS.setUserInfo(res.data)
                // this.$message.success('登录成功!')
                this.$router.push({ name: 'home' })
              })
            .catch(err => {
              switch (err.status) {
                case 400:
                  this.$message.error(err.data.non_field_errors[0])
                  break
                default:
                  this.$message.error('登录时发生未知错误')
              }
            })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },

    toRegister () {
      this.$router.push({ name: 'register' })
    }
  }
}
</script>

<style lang="less" scoped>
.login-container-box {
  background-color: #2b4b6b;
  height: 100%;
  background: url('~@/assets/images/login_background.jpg') center center no-repeat;
  background-size:100% 100%;
}
.login-box{
  width: 450px;
  height: 400px;
  background-color:rgba(0,0,0,0);
  position: absolute;
  left: 50%;
  top:50%;
  transform: translate(-50%,-50%);

  .avatar-box {
    height: 150px;
    width: 160px;
    border: 1px solid rgb(124, 167, 120);
    border-radius: 50%;
    // 是图片和边框产生间距
    padding: 10px;
    //给边框加上阴影
    box-shadow: 0 0 10px #ddd;
    position: absolute;
    left: 50%;
    transform: translate(-50%,-50%);
    background-color:rgb(144,193,88);

    img {
      width: 100%;
      height: 100%;
      // 产生遮罩效果
      border-radius: 50%;
      background-color: rgb(58, 160, 97)
    }
  }
  .login-box-form {
    position: absolute;
    bottom: 0;
    width: 100%;
    padding: 0 20px;
    box-sizing: border-box;

  }
  .btns {
    display:flex;
    // 横轴对齐方式
    justify-content: flex-end;
    .login-btn{
      background-color:rgb(119,173,71);
      border-color:rgb(119,173,71);
    }
  }
  .register-tip{
    color:#fff;
    padding: 0;
    margin: 0;
    display: flex;
    justify-content: flex-end;
    &:hover{
      cursor: pointer;
    }
  }
}
</style>
