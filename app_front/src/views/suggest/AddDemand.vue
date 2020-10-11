<template>
  <div>

  <div>
    <el-dialog
    title="新需求信息"
    :visible.sync="AddDemandDialogVisible"
    width="50%"
    center>
        <el-form
            :model="AddDemandForm"
            status-icon
            ref="AddDemandFormRef"
            :rules="this.AddDemandRules"
            v-if='AddDemandDialogVisible'
            label-width="140px"
            class="add-Demand-form"
        >
            <el-form-item
            prop="description"
            :error="ErroMessage.description"
            label="需求描述"
            >
            <el-input 
                type="textarea"
                :rows="5" 
                v-model="AddDemandForm.description" 
            >
            </el-input>
            </el-form-item>
            <el-form-item>
            <el-button type="success" style="float:right" @click="submitEditForm('AddDemandFormRef')">提交</el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
  </div>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'AddDemand',
  data () {
    return {
      AddDemandDialogVisible: false,
      AddDemandForm: {
        'description': ''
      },
      ErroMessage: {
        'description': ''
      },
      AddDemandRules: {
        description: [
          { required: true, message: '请输入需求描述', trigger: 'blur' }
        ]
      } 
    }
  },
  computed: {},
  watch: {},
  mounted () {
    this.monitoring()
  },
  beforeDestroy () {},
  components: {},
  methods: {
    monitoring () {
        this.$on('addDemandEvent', () => {
            this.AddDemandDialogVisible = true
        })
    },

    addDemand () {
      this.$http.post(`suggest/demand/`, this.AddDemandForm)
          .then(
          res => {
            this.$message.success('新需求已提交')
              // this.ProjectsInfo()
              this.AddDemandDialogVisible = false
              this.$emit('updateDemondInfo')
          })
          .catch(err => {
            switch (err.status) {
                case 400:
                for (let key in err.data) {
                    this.ErroMessage[key] = err.data[key][0]
                }
                break
                default:

                console.log('请求发生未知错误')
            }
          })
    },
    submitEditForm (formName) {
        this.ErroMessage = {
            description: ''
        }
        this.$refs[formName].validate((valid) => {
            if (valid) {
              this.addDemand()
            } else {
            console.log('error submit!!')
            return false
            }
        })
    }
  }
}

</script>

<style lang="less" scoped>
.markdown-edit-container {
  height:400px
}
.demand-submit {
  margin: 20px;
  float: right;
}

</style>
