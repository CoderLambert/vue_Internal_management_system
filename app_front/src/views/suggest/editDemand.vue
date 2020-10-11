<template>
  <div>
    <el-dialog
    title="编辑需求信息"
    :visible.sync="EditDemandDialogVisible"
    width="50%"
    center>
        <el-form
            :model="EditDemandForm"
            status-icon
            ref="EditDemandFormRef"
            :rules="this.editDemandRules"
            v-if='EditDemandDialogVisible'
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
                v-model="EditDemandForm.description" 
            >
            </el-input>
            </el-form-item>

            <el-form-item
            prop="current_state"
            :error="ErroMessage.current_state"
            label="当前状态"
            >
                <el-radio-group v-model="EditDemandForm.current_state" size="medium">
                    <el-radio-button
                    v-for="item in demand_states"
                    :key="item.id"
                    :label="item.id"
                    >
                    {{item.state}}
                    </el-radio-button>
                </el-radio-group>
            </el-form-item>
            <el-form-item>
            <el-button type="success" style="float:right" @click="submitEditForm('EditDemandFormRef')">提交</el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
  </div>
      <!-- @EditDemandEvent = "handleEditDemandEvent" -->

</template>

<script>
// @ is an alias to /src
export default {
  name: 'editDemandInfo',
  props: [],
  data () {
    return {
        EditDemandDialogVisible: false,
        EditDemandForm: {
            'id': '',
            'description': '',
            'current_state': ''
        },
        ErroMessage: {
            'description': '',
            'current_state': ''
        },
        demand_states: [
            { id: 0, state: '待实现' },
            { id: 1, state: '已实现' },
            { id: 2, state: '已拒绝' }
        ],        
      editDemandRules: {
        description: [
          { required: true, message: '请输入需求描述', trigger: 'blur' }
        ],
        current_state: [
          { required: true, message: '请更新需求状态', trigger: 'change' }
        ]
      }     
    }
  },
  computed: {},
  watch: {},
  mounted () {
    this.monitoring() // 注册监听事件
  },
  beforeDestroy () {},

  methods: {
// EditDemandEvent
    monitoring () {
        this.$on('EditDemandEvent', ( res ) => {
            console.log('方法1:触发监听事件监听成功')
            // console.log(res)
            this.EditDemandDialogVisible = true
            this.EditDemandForm.id = res.id
            this.EditDemandForm.description = res.description
            this.EditDemandForm.current_state = res.current_state
        })
    },
    submitEditForm (formName) {
        this.ErroMessage = {
            description: '',
            current_state: '',
            id: ''
        }
        this.$refs[formName].validate((valid) => {
            if (valid) {
            // alert('submit!')
            console.log(this.EditDemandForm)
            this.$http.put(`suggest/demand/${this.EditDemandForm.id}/`, this.EditDemandForm)
                .then(
                res => {
                    this.$message.success('已更新需求信息!')
                    // this.ProjectsInfo()
                    this.EditDemandDialogVisible = false
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
            } else {
            console.log('error submit!!')
            return false
            }
        })
    }

  },
  components: {}
}
</script>

<style lang="less" scoped>
</style>
