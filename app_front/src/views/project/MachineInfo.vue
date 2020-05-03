<template>

  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ name: 'Home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>项目</el-breadcrumb-item>
      <el-breadcrumb-item>项目信息</el-breadcrumb-item>
    </el-breadcrumb>

    <el-card class="box-card-box">

    <el-row :gutter="10" type="flex" justify="start" class="search-box">
      <el-col :xs="5" :sm="4" :md="12" :lg="12" :xl="11">
        <el-input placeholder="搜索内容( BMC IP、主机 IP、所属人员、所属项目名、备注 )"
          @clear="MachinesInfo"
          @keyup.enter.native="MachinesInfo"
          v-model="queryInfo.search"
          clearable
          >
          <el-button slot="append" icon="el-icon-search" @click="MachinesInfo"></el-button>
        </el-input>
      </el-col>
      <el-col :xs="5" :sm="4" :md="4" :lg="4" :xl="4" :offset=1>
        <el-button type="primary"  @click="showCenterDialogVisible">添加新的机器信息</el-button>
      </el-col>
    </el-row>
<el-dialog
  title=" 添加机器信息"
  :visible.sync="centerDialogVisible"
  width="50%"
  center>
      <el-form
        :model="machineForm"
        status-icon
        ref="machineFormRef"
        :rules="this.addMachineRules"
        v-if='centerDialogVisible'
        label-width="140px"
        class="add-project-form"
      >
        <el-form-item
          prop="BMC_ip"
          :error="ErroMessage.BMC_ip"
          label="BMI IP"
        >
          <el-input type="text" v-model.trim="machineForm.BMC_ip" ></el-input>
        </el-form-item>

        <el-form-item
          prop="Host_ip"
          :error="ErroMessage.Host_ip"
          label="主机 IP"
        >
          <el-input type="text" v-model.trim="machineForm.Host_ip" ></el-input>
        </el-form-item>
        <el-form-item
          prop="web_username"
          :error="ErroMessage.web_username"
          label="BMC 默认用户名">
            <el-input v-model="machineForm.web_username"></el-input>
        </el-form-item>

        <el-form-item
         prop="web_password"
         :error="ErroMessage.web_password"
         label="BMC 默认用户密码">
          <el-input v-model.trim="machineForm.web_password"></el-input>
        </el-form-item>

        <el-form-item
          prop="user"
          :error="ErroMessage.user"
          label="机器所有者"
        >
          <el-select filterable  v-model="machineForm.user"  placeholder="请选择">
            <el-option
              v-for="item in user_options"
              :key="item.id"
              :label="item.username"
              :value="item.id">
            </el-option>
          </el-select>
        </el-form-item>

        <el-form-item
          prop="project"
          :error="ErroMessage.project"
          label="机器所属项目"
        >
          <el-select filterable  v-model="machineForm.project"  placeholder="请选择">
            <el-option
              v-for="item in projectOptions"
              :key="item.id"
              :label="item.name"
              :value="item.id">
            </el-option>
          </el-select>
        </el-form-item>

        <el-form-item
          prop="current_state"
          :error="ErroMessage.current_state"
          label="当前机器状态"
        >
          <el-radio-group v-model="machineForm.current_state" size="medium">
            <el-radio-button
              v-for="item in machine_states"
              :key="item.id"
              :label="item.id"
              >
              {{item.state}}
            </el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item
          prop="start_time"
          v-show='machineForm.current_state!==1&& machineForm.current_state!==""'
          :error="ErroMessage.start_time"
          ref="addMachinePickerRef"
          label="使用开始时间"
        >
          <el-date-picker
            v-model="machineForm.start_time"
            type="datetime"
            placeholder="选择起始时间"   
            align="right"
            :picker-options="startPickerOptions"     
          >
          </el-date-picker>
        </el-form-item>
        <el-form-item
          prop="end_time"
          v-show='machineForm.current_state!==1 && machineForm.current_state!==""'
          :error="ErroMessage.end_time"
          label="使用结束时间"
        >
          <el-date-picker
            v-model="machineForm.end_time"
            type="datetime"
            placeholder="选择结束时间"
            align="right"
            :picker-options="addEndPickerOptions"  
            >
          </el-date-picker>
        </el-form-item>
        <el-form-item
         prop="description"
         :error="ErroMessage.description"
         label="机器备注" 
         :rows="4"
         >
          <el-input type="textarea" v-model="machineForm.description"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm('machineFormRef')">提交</el-button>
          <el-button @click="resetForm">重置</el-button>
        </el-form-item>
      </el-form>
</el-dialog>

<el-dialog
  title=" 修改机器信息"
  :visible.sync="EditMachineDialogVisible"
  width="50%"
  center>
      <el-form
        :model="EditMachineForm"
        status-icon
        ref="EditMachineFormRef"
        :rules="this.addMachineRules"
        v-if='EditMachineDialogVisible'
        label-width="140px"
        class="add-project-form"
      >
        <el-form-item
          prop="BMC_ip"
          :error="ErroMessage.BMC_ip"
          label="BMI IP"
        >
          <el-input type="text" v-model="EditMachineForm.BMC_ip" ></el-input>
        </el-form-item>

        <el-form-item
          prop="Host_ip"
          :error="ErroMessage.Host_ip"
          label="主机 IP"
        >
          <el-input type="text" v-model="EditMachineForm.Host_ip" ></el-input>
        </el-form-item>
        <el-form-item
          prop="web_username"
          :error="ErroMessage.web_username"
          label="BMC 默认用户名">
            <el-input v-model="EditMachineForm.web_username"></el-input>
        </el-form-item>

        <el-form-item
         prop="web_password"
         :error="ErroMessage.web_password"
         label="BMC 默认用户密码">
          <el-input v-model="EditMachineForm.web_password"></el-input>
        </el-form-item>

        <el-form-item
          prop="user"
          :error="ErroMessage.user"
          label="机器所有者"
        >
          <el-select filterable  v-model="EditMachineForm.user"  placeholder="请选择">
            <el-option
              v-for="item in user_options"
              :key="item.id"
              :label="item.username"
              :value="item.id">
            </el-option>
          </el-select>
        </el-form-item>

        <el-form-item
          prop="project"
          :error="ErroMessage.project"
          label="机器所属项目"
        >
          <el-select filterable  v-model="EditMachineForm.project"  placeholder="请选择">
            <el-option
              v-for="item in projectOptions"
              :key="item.id"
              :label="item.name"
              :value="item.id">
            </el-option>
          </el-select>
        </el-form-item>

        <el-form-item
          prop="current_state"
          :error="ErroMessage.current_state"
          label="当前机器状态"
        >
          <el-radio-group v-model="EditMachineForm.current_state" size="medium">
            <el-radio-button
              v-for="item in machine_states"
              :key="item.id"
              :label="item.id"
              >
              {{item.state}}
            </el-radio-button>
          </el-radio-group>
        </el-form-item>

        <el-form-item
          prop="start_time"
          v-show='EditMachineForm.current_state!==1'
          :error="ErroMessage.start_time"
          label="使用开始时间"
          ref="editMachinePickerRef"
        >
          <el-date-picker
            v-model="EditMachineForm.start_time"
            type="datetime"
            placeholder="选择起始时间"  
            align="right"
            :picker-options="startPickerOptions"          
          >
          </el-date-picker>
        </el-form-item>
        <el-form-item
          prop="end_time"
          v-show='EditMachineForm.current_state!==1'
          :error="ErroMessage.end_time"
          label="使用结束时间"
        >
          <el-date-picker
            v-model="EditMachineForm.end_time"
            type="datetime"
            placeholder="选择结束时间"
            align="right"
            :picker-options="endPickerOptions"  
            >
          </el-date-picker>
        </el-form-item>

        <el-form-item
         prop="description"
         :error="ErroMessage.description"
         label="机器备注">
          <el-input type="textarea"   :rows="4"
             v-model="EditMachineForm.description"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitEditForm('EditMachineFormRef')">提交</el-button>
        </el-form-item>
      </el-form>
</el-dialog>
<MachineItem 
  :MachineInfo = this.MachineInfoList 
  :MachineStates = this.machine_states
  @EditMachineInfo='handleEditMachineInfo'
>
</MachineItem>

    </el-card>
    </div>
</template>
<script>
import MachineItem from '@/components/MachineItem.vue'
export default {
  name: 'MachineInfo',
  components: { MachineItem },
  data () {
    return {
      time_range: '',
      expands: [],
      expandFunc: '展开所有',
      centerDialogVisible: false,
      EditMachineDialogVisible: false,
      user_options: [],
      projectOptions: [],
      MachineInfoList: [],
      queryInfo: {
        search: ''
      },
      machine_states: [
        { id: 1, state: '空闲' },
        { id: 2, state: '可查看' },
        { id: 3, state: '勿动' }
      ],
      machineForm: {
        BMC_ip: '',
        Host_ip: '',
        web_username: '',
        web_password: '',
        user: '',
        project: '',
        current_state: '',
        description: '',
        start_time: '',
        end_time: ''
      },
      EditMachineForm: {
        BMC_ip: '',
        Host_ip: '',
        web_username: '',
        web_password: '',
        user: '',
        project: '',
        current_state: '',
        description: '',
        start_time: '',
        end_time: ''
      },
      ErroMessage: {
        BMC_ip: '',
        Host_ip: '',
        web_username: '',
        web_password: '',
        user: '',
        project: '',
        current_state: '',
        description: '',
        start_time: '',
        end_time: ''
      },
      addMachineRules: {
        BMC_ip: [
          { required: true, message: '请输入该机器的BMC IP 信息', trigger: 'blur' }
        ],
        Host_ip: [],
        web_username: [],
        web_password: [],
        user: [
          { required: true, message: '请选择机器的所有人', trigger: 'change' }
        ],
        project: [
          { required: true, message: '请选择机器的所属项目', trigger: 'change' }
        ],
        description: [],
        current_state: [],
        time_range: []
      },
      startPickerOptions: {
          disabledDate: (time) => {
            let beginVal = new Date() - 3600 * 1000 * 24
            if ( beginVal) { 
                return time.getTime() < beginVal
            }
          },

          shortcuts: [
            {
              text: '10 分钟后',
              onClick (picker) {
                const date = new Date()
                date.setTime(date.getTime() + 600 * 1000 )
                picker.$emit('pick', date)
              }
            },
            {
              text: '20 分钟后',
              onClick (picker) {
                const date = new Date()
                date.setTime(date.getTime() + 600 * 1000 * 2 )
                picker.$emit('pick', date)
              }
            },
            {
              text: '30 分钟后',
              onClick (picker) {
                const date = new Date()
                date.setTime(date.getTime() + 600 * 1000 * 2 )
                picker.$emit('pick', date)
              }
            },
            {
              text: '1小时后',
              onClick (picker) {
                const date = new Date()
                date.setTime(date.getTime() + 600 * 1000 * 6 )
                picker.$emit('pick', date)
              }
            },
            {
              text: '2小时后',
              onClick (picker) {
                const date = new Date()
                date.setTime(date.getTime() + 600 * 1000 * 6 * 2 )
                picker.$emit('pick', date)
              }
            },
            {
              text: '6小时后',
              onClick (picker) {
                const date = new Date()
                date.setTime(date.getTime() + 600 * 1000 * 6 * 6)
                picker.$emit('pick', date)
              }
            }, 
            {
              text: '12小时后',
              onClick (picker) {
                const date = new Date()
                date.setTime(date.getTime() + 600 * 1000 * 6 * 12)
                picker.$emit('pick', date)
              }
            }
          ]
        },
      addEndPickerOptions: {
          shortcuts: [
            {
              text: '10 分钟',
              onClick: (picker) => {
                const date = new Date( this.$refs.addMachinePickerRef.fieldValue )
                date.setTime(date.getTime() + 600 * 1000 )
                picker.$emit('pick', date)
              }
            },
            {
              text: '20 分钟',
              onClick: (picker) => {
                const date = new Date( this.$refs.addMachinePickerRef.fieldValue )
                date.setTime(date.getTime() + 600 * 1000 * 2 )
                picker.$emit('pick', date)
              }
            },
            {
              text: '30 分钟',
              onClick: (picker) => {
                const date = new Date( this.$refs.addMachinePickerRef.fieldValue )
                date.setTime(date.getTime() + 600 * 1000 * 2 )
                picker.$emit('pick', date)
              }
            },
            {
              text: '1小时',
              onClick: (picker) => {
                const date = new Date( this.$refs.addMachinePickerRef.fieldValue )
                date.setTime(date.getTime() + 600 * 1000 * 6 )
                picker.$emit('pick', date)
              }
            },
            {
              text: '2小时',
              onClick: (picker) => {
                const date = new Date( this.$refs.addMachinePickerRef.fieldValue )
                date.setTime(date.getTime() + 600 * 1000 * 6 * 2 )
                picker.$emit('pick', date)
              }
            },
            {
              text: '6小时',
              onClick: (picker) => {
                const date = new Date( this.$refs.addMachinePickerRef.fieldValue )
                date.setTime(date.getTime() + 600 * 1000 * 6 * 6)
                picker.$emit('pick', date)
              }
            }, 
            {
              text: '12小时',
              onClick: (picker) => {
                const date = new Date( this.$refs.addMachinePickerRef.fieldValue )
                date.setTime(date.getTime() + 600 * 1000 * 6 * 12)
                picker.$emit('pick', date)
              }
            }
          ]
        },
      endPickerOptions: {
          shortcuts: [
            {
              text: '10 分钟',
              onClick: (picker) => {
                const date = new Date( this.$refs.editMachinePickerRef.fieldValue )
                date.setTime(date.getTime() + 600 * 1000 )
                picker.$emit('pick', date)
              }
            },
            {
              text: '20 分钟',
              onClick: (picker) => {
                const date = new Date( this.$refs.editMachinePickerRef.fieldValue )
                date.setTime(date.getTime() + 600 * 1000 * 2 )
                picker.$emit('pick', date)
              }
            },
            {
              text: '30 分钟',
              onClick: (picker) => {
                const date = new Date( this.$refs.editMachinePickerRef.fieldValue )
                date.setTime(date.getTime() + 600 * 1000 * 2 )
                picker.$emit('pick', date)
              }
            },
            {
              text: '1小时',
              onClick: (picker) => {
                const date = new Date( this.$refs.editMachinePickerRef.fieldValue )
                date.setTime(date.getTime() + 600 * 1000 * 6 )
                picker.$emit('pick', date)
              }
            },
            {
              text: '2小时',
              onClick: (picker) => {
                const date = new Date( this.$refs.editMachinePickerRef.fieldValue )
                date.setTime(date.getTime() + 600 * 1000 * 6 * 2 )
                picker.$emit('pick', date)
              }
            },
            {
              text: '6小时',
              onClick: (picker) => {
                const date = new Date( this.$refs.editMachinePickerRef.fieldValue )
                date.setTime(date.getTime() + 600 * 1000 * 6 * 6)
                picker.$emit('pick', date)
              }
            }, 
            {
              text: '12小时',
              onClick: (picker) => {
                const date = new Date( this.$refs.editMachinePickerRef.fieldValue )
                date.setTime(date.getTime() + 600 * 1000 * 6 * 12)
                picker.$emit('pick', date)
              }
            }
          ]
        }        
    }
  },
  created () {},
  mounted () {
    this.MachinesInfo()
  },
  beforeDestroy () {
  },

  methods: {
    handleEditMachineInfo (ev) {
      this.editMachineInfo(ev)
    },
    handleDeleteMachine (ev) {
      this.removeMachine (ev.id, ev.BMC_ip)
    },
    clearExpand () {
      if (this.expands.length > 0) {
        this.expands = []
        this.expandFunc = '全部展开'
      } else {
        for (let i = 0; i < this.MachineInfoList.length; i++) {
          this.expands.push(this.MachineInfoList[i]['id'])
        }
        console.log(this.expands)
        this.expandFunc = '全部收缩'
      }
    },

    MachinesInfo () {
      this.$http.get('machines/', { params: this.queryInfo })
        .then(
          res => {
            this.MachineInfoList = res.data
            // this.total_page = Number(res.data.count)
          })
        .catch(err => {
          this.$message.error(err.data)
        })
    },

    // handleCurrentChange (val) {
    //   this.queryInfo.pagenum = val
    //   this.MachinesInfo()
    // },
    // handleSizeChange (val) {
    //   this.queryInfo.pagesize = val
    //   this.MachinesInfo()
    // },

    onCopy (e) {
      this.$message.success(`已复制 ${e.text} 到粘贴板`)
    },
    onError: function (e) {
      this.$message.error('复制失败！')
    },

    open_link (URL) {
      console.log(URL)

      window.open(URL)
    },
    showCenterDialogVisible () {
      this.centerDialogVisible = true
      this.$http.get('users/?type=options')
        .then(
          res => {
            this.user_options = res.data
          })
        .catch(err => {
          this.$message.error(err.data)
        })

      this.$http.get('users/?type=options')
        .then(
          res => {
            this.user_options = res.data
          })
        .catch(err => {
          this.$message.error(err.data)
        })

      this.$http.get(`project/name`).then(res => {
        // console.log(res)
        this.projectOptions = res.data
        this.formData = null
      }).catch(err => {
        this.$message.error(err.data)
      })
    },
    submitForm (formName) {
      this.ErroMessage = {
        BMC_ip: '',
        Host_ip: '',
        web_username: '',
        web_password: '',
        user: '',
        project: '',
        current_state: '',
        description: ''
      }
      if (this.machineForm.current_state === 1){
        this.machineForm.start_time = new Date()
        this.machineForm.end_time = new Date() 
      }
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // alert('submit!')
          // console.log(this.machineForm)

          this.$http.post('machines/', this.machineForm)
            .then(
              res => {
                this.$message.success('添加机器信息成功!')
                this.MachinesInfo()
                this.centerDialogVisible = false
                this.machineForm = {
                  BMC_ip: '',
                  Host_ip: '',
                  web_username: '',
                  web_password: '',
                  user: '',
                  project: '',
                  current_state: '',
                  description: ''
                }
              })
            .catch(err => {
              switch (err.status) {
                case 400:
                  for (let key in err.data) {
                    this.ErroMessage[key] = err.data[key][0]
                  }
                  break
                default:

                  this.$message.error('请求发生未知错误')
              }
            })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    resetForm () {
        this.machineForm = {
          BMC_ip: '',
          Host_ip: '',
          web_username: '',
          web_password: '',
          user: '',
          project: '',
          current_state: '',
          description: ''
        }
    },                                                                                               
  editMachineInfo ( MachineInfo ) {
    console.log( MachineInfo )
    this.EditMachineDialogVisible = true
    this.UserOptionsInfo ()
    this.ProjectOptionsInfo()
    this.EditMachineForm = {
      id: Number(MachineInfo.id),
      BMC_ip: MachineInfo.BMC_ip,
      Host_ip: MachineInfo.Host_ip,
      web_username: MachineInfo.web_username,
      web_password: MachineInfo.web_password,
      user: MachineInfo.userid,
      project: MachineInfo.project_id,
      current_state: MachineInfo.current_state,
      description: MachineInfo.description
    }
  },
  
  removeMachine ( MachineID, MachineBMCIP ) {
    // console.log( MachineID )
    // console.log( MachineBMCIP )
      this.$confirm('此操作将删除该机器信息, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      })
        .then(() => {
          this.$http.delete(`machines/` + MachineID + '/').then(() => {
            this.$message({
              message: `${MachineBMCIP}  已删除`,
              type: 'success'
            })
            this.queryInfo.pagenum = 1
            this.MachinesInfo()
          })
        })
    },

    submitEditForm (formName) {
      this.ErroMessage = {
        BMC_ip: '',
        Host_ip: '',
        web_username: '',
        web_password: '',
        user: '',
        project: '',
        description: '',
        current_state: ''
      }

      this.$refs[formName].validate((valid) => {
        if (valid) {
          // console.log(this.EditProjectForm)
          this.$http.put(`machines/${this.EditMachineForm.id}/`, this.EditMachineForm)
            .then(
              res => {
                this.$message.success('已更新机器信息!')
                this.MachinesInfo()
                this.EditMachineDialogVisible = false
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
    },
    ProjectOptionsInfo () {
      this.$http
        .get(`project/name`)
        .then(res => {
          // console.log(res)
          this.projectOptions = res.data
        })
        .catch(err => {
          this.$message.error(err.data)
        })
    },
    UserOptionsInfo () {
      this.$http.get('users/?type=options')
        .then(
          res => {
            this.user_options = res.data
            console.log(res)
          })      
    }

  },

  computed: {
  }
}
</script>
<style lang="less" scoped>
  .search-box {
    margin:  0 0 10px 0;
  }
  .file-name{
    color: skyblue;
    cursor: pointer;
  }
  .el-pagination{
    margin: 20px
  }
  .el-tag{
    margin: 5px;
    &:hover{
      cursor: pointer;
    }
  }
  .el-row{
    display: flex;
    align-items: center;
  }
</style>
