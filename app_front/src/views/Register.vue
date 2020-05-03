<template>
  <div class="register-container-box">
    <div class="register-box">
      <div class="avatar-box">
        <img src="@/./assets/images/xingyue.jpg" alt="">
      </div>

      <el-form ref="registerFormRef"
        :model="registerForm"
        :rules="this.registerRules"
        :label-position="labelPosition"
        label-width="70px"
        class="register-box-form"
        >
        <el-form-item prop="username" :error="ErroMessage.username" label="用户名">
          <el-input type="text" v-model.trim="registerForm.username" prefix-icon="icon iconfont icon-user"></el-input>
        </el-form-item>
        <el-form-item prop="password" :error="ErroMessage.password" label="密码">
          <el-input type="password" v-model.trim="registerForm.password" prefix-icon="icon iconfont icon-3702mima"></el-input>
        </el-form-item>

        <el-form-item prop="email" :error="ErroMessage.email" label="邮箱">
          <el-input type="email" v-model.trim="registerForm.email" prefix-icon="el-icon-message" @keyup.enter.native="register"></el-input>
        </el-form-item>

        <el-form-item prop="department" :error="ErroMessage.department" label="部门">

          <el-select v-model="registerForm.department" multiple placeholder="请选择">
            <el-option
              v-for="item in department_options"
              :key="item.id"
              :label="item.name"
              :value="item.id">
            </el-option>
          </el-select>
        </el-form-item>

        <el-form-item prop="role" :error="ErroMessage.role" label="角色">
          <el-select v-model="registerForm.role" multiple placeholder="请选择">
            <el-option
              v-for="item in role_options"
              :key="item.id"
              :label="item.name"
              :value="item.id">
            </el-option>
          </el-select>
        </el-form-item>

        <el-form-item class="btns">
          <el-button type="success" class="register-btn" @click="UserRegister" >提交</el-button>
          <el-button type="info" class="register-btn" @click="ResetRegisterForm">重置</el-button>
        </el-form-item>

        <el-form-item class="register-tip">
          <p  @click="toLogin">返回登录界面</p>
        </el-form-item>

      </el-form>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import SS from '@/assets/js/utils.js'
import RegValid from '@/assets/js/regValidate.js'

export default {
  name: 'Register',
  data () {
    let checkUserName = (rule, value, callback) => {
      if (!RegValid.isUserName(value)) {
        return callback(new Error('用户名格式不正确!  (4到16位 [字母，数字，下划线，减号])'))
      } else {
        return callback()
      }
    }

    let checkEmail = (rule, value, callback) => {
      if (!RegValid.isEmail(value)) {
        return callback(new Error('邮箱格式不正确  (用户名@主机名.域名)'))
      } else {
        return callback()
      }
    }

    return {

      labelPosition: 'right',
      registerForm: {
        username: '',
        password: '',
        email: '',
        department: [],
        role: []
      },

      department_options: '',
      role_options: '',

      // 第一步 定义 rules 对象
      // 第二步 form 表单绑定 rules对象
      // 第三步 form-item 通过 prop 绑定属性验证规则
      registerRules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { validator: checkUserName, trigger: 'blur' }

        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' }
        ],
        email: [
          { required: true, message: '请输入邮箱', trigger: 'blur' },
          { validator: checkEmail, trigger: 'blur' }
        ],
        department: [
          { required: true, message: '请选择你所属的部门', trigger: 'blur' }
        ],
        role: [
          { required: true, message: '请选择你的用户角色', trigger: 'blur' }
        ]
      },
      ErroMessage: {
        username: '',
        password: '',
        email: '',
        department: '',
        role: ''
      }
    }
  },

  mounted () {
    console.log('sss')
    this.getRoleList()
    this.getDepartMentList()
  },
  methods: {
    // 重置表单
    ResetRegisterForm () {
      this.$refs.registerFormRef.resetFields()
    },

    createUser () {
      console.log('createUser')
      console.log(this)
      this.$refs.registerFormRef.validate((valid) => {
        console.log('valid =>' + valid)
        if (valid) {
          console.log('验证通过')
          this.$http.post('users/', this.registerForm)
            .then(
              res => {
                this.$message.success('注册成功!请登录')
                // setInterval(() => {
                this.$router.push({ name: 'login' })
                // }, 2000)
              })
            .catch(err => {
              switch (err.status) {
                case 400:
                  for (let key in err.data) {
                    this.ErroMessage[key] = err.data[key][0]
                  }
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
    // 登录
    UserRegister () {
      console.log(this.registerForm)

      this.ErroMessage = {
        username: '',
        password: '',
        email: '',
        department: '',
        role: ''
      }
      this.createUser()
    },
    toLogin () {
      this.$router.push({ name: 'login' })
    },

    getRoleList () {
      this.$http.get('roles/')
        .then(
          res => {
            this.role_options = res.data
          })
        .catch(err => {
          this.$message.error(err.data)
        })
    },
    getDepartMentList () {
      this.$http.get('departments/')
        .then(
          res => {
            this.department_options = res.data
          })
        .catch(err => {
          this.$message.error(err.data)
        })
    }
  }
}
</script>

<style lang="less" scoped>
.register-container-box {
  background-color: #2b4b6b;
  height: 100%;
  background: url('~@/assets/images/login_background.jpg') center center no-repeat;
  background-size:100% 100%;
}
.register-box{
  width: 450px;
  height: 550px;
  background-color:rgba(0,0,0,0);
  position: absolute;
  left: 50%;
  top:50%;
  transform: translate(-50%,-50%);

  .avatar-box {
    height: 130px;
    width: 130px;
    border: 1px solid #eee;
    border-radius: 50%;
    // 是图片和边框产生间距
    padding: 10px;
    //给边框加上阴影
    box-shadow: 0 0 10px #ddd;
    position: absolute;
    left: 50%;
    transform: translate(-50%,-50%);
    background-color: #fff;

    img {
      width: 100%;
      height: 100%;
      // 产生遮罩效果
      border-radius: 50%;
      background-color: #eee
    }
  }
  .register-box-form {
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
    .register-btn{
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
  .el-select{
    width: 100%;
  }

}
</style>
