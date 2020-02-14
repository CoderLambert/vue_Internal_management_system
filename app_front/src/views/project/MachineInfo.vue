<template>

  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ name: 'Home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>项目</el-breadcrumb-item>
      <el-breadcrumb-item>项目信息</el-breadcrumb-item>
    </el-breadcrumb>

    <el-card class="box-card-box">

    <el-row :gutter="10" type="flex" justify="start" class="search-box">
      <el-col :xs="5" :sm="4" :md="12" :lg="8" :xl="6">
        <el-input placeholder="搜索内容( BMC IP、主机 IP、所属项目名、备注 )"
          @clear="MachinesInfo"
          @keyup.enter.native="MachinesInfo"
          v-model="queryInfo.search"
          clearable
          >
          <el-button slot="append" icon="el-icon-search" @click="MachinesInfo"></el-button>
        </el-input>
      </el-col>

      <el-col :xs="5" :sm="4" :md="11" :lg="7" :xl="6" :offset=1>
        <el-button type="primary"  @click="showCenterDialogVisible">添加新的机器信息</el-button>
      </el-col>
    </el-row>

      <el-table
        :data="MachineInfoList"
        style="width: 100%"
        :highlight-current-row="true"
        border
        stripe
        :default-sort="{ prop: 'create_time', order: 'descending' }"
      >
        <el-table-column label="" type="expand">
          <template slot-scope="props">
            <el-form label-position="left" inline class="demo-table-expand">
              <el-form-item label="">
                <pre class="image-description">{{ props.row.description }}</pre>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>

        <el-table-column
          prop="project"
          label="所属项目"
          width="140"
          sortable
        >
        </el-table-column>

        <el-table-column
          prop="username"
          label="所属人员"
          width="120"
          sortable
        >
        </el-table-column>
      <el-table-column label="用户名/密码"
       width="230"
      >
        <template slot-scope="scope">

          <el-tooltip content="单击复制用户名" placement="bottom" effect="light">

          <span  v-if="scope.row.web_username"

            v-clipboard:copy="scope.row.web_username"
            v-clipboard:success="onCopy"
            v-clipboard:error="onError"
            class="svn-copy"

          >
          {{ scope.row.web_username }}
          </span>
          </el-tooltip>
            /
        <el-tooltip content="单击复制密码" placement="bottom" effect="light">
          <span  v-if="scope.row.web_password"
            v-clipboard:copy="scope.row.web_password"
            v-clipboard:success="onCopy"
            v-clipboard:error="onError"
            class="svn-copy"
          >
          {{ scope.row.web_password }}
          </span>
          </el-tooltip>

        </template>
      </el-table-column>

        <el-table-column
          label="BMC IP"
        >
        <template slot-scope="scope">
         <el-row>
            <el-col :span="12" :offset="2">
              {{ scope.row.BMC_ip }}
            </el-col>
            <el-col :span="10">
              <el-tooltip content="点击使用 HTTP 协议打开链接" placement="bottom" effect="light">
                <el-tag size="medium" @click="open_link(`http://${scope.row.BMC_ip}`)" > HTTP </el-tag>
              </el-tooltip>
              <el-tooltip content="点击使用 HTTPS 协议打开链接" placement="bottom" effect="light">
                <el-tag size="medium"  @click="open_link(`https://${scope.row.BMC_ip}`)"> HTTPS </el-tag>
              </el-tooltip>

            </el-col>
          </el-row>

        </template>

        </el-table-column>
        <el-table-column
          prop="Host_ip"
          label="主机 IP"

        >
        </el-table-column>
      </el-table>
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
          <el-input type="text" v-model="machineForm.BMC_ip" ></el-input>
        </el-form-item>

        <el-form-item
          prop="Host_ip"
          :error="ErroMessage.Host_ip"
          label="主机 IP"
        >
          <el-input type="text" v-model="machineForm.Host_ip" ></el-input>
        </el-form-item>
        <el-form-item
          prop="web_username"
          :error="ErroMessage.web_username"
          label="BMC 默认用户名">
            <el-input v-model.number="machineForm.web_username"></el-input>
        </el-form-item>

        <el-form-item
         prop="web_password"
         :error="ErroMessage.web_password"
         label="BMC 默认用户密码">
          <el-input v-model.number="machineForm.web_password"></el-input>
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
         prop="description"
         :error="ErroMessage.description"
         label="机器备注">
          <el-input v-model.number="machineForm.description"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm('machineFormRef')">提交</el-button>
          <el-button @click="resetForm">重置</el-button>
        </el-form-item>
      </el-form>
</el-dialog>

    <el-row :gutter="10" type="flex" justify="center">
      <el-col :xs="5" :sm="4" :md="16" :lg="8" :xl="6">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="queryInfo.pagenum"
          :page-sizes="[5,10, 20, 50, 100, 200]"
          :page-size="queryInfo.pagesize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total_page">
        </el-pagination>
      </el-col>
    </el-row>
    </el-card>
    </div>
</template>
<script>

export default {
  name: 'MachineInfo',
  data () {
    return {
      centerDialogVisible: false,
      user_options: [],
      projectOptions: [],
      MachineInfoList: [],
      total_page: null,
      queryInfo: {
        search: '',
        pagenum: 1,
        pagesize: 20
      },

      machineForm: {
        BMC_ip: '',
        Host_ip: '',
        web_username: '',
        web_password: '',
        user: '',
        project: '',
        description: ''
      },
      ErroMessage: {
        BMC_ip: '',
        Host_ip: '',
        web_username: '',
        web_password: '',
        user: '',
        project: '',
        description: ''
      },
      addMachineRules: {
        BMC_ip: [
          { required: true, message: '请输入该机器的BMC IP 信息', trigger: 'blur' }
        ],
        Host_ip: [
          // { required: true, message: '项目成员不能为空', trigger: 'change' }
        ],
        web_username: [
          // { required: true, message: '请输入该机器的用户名', trigger: 'blur' }
          // { validator: checkEmail, trigger: 'blur' }
        ],
        web_password: [
          // { required: true, message: '请选择你所属的部门', trigger: 'blur' }
        ],
        user: [
          { required: true, message: '请选择机器的所有人', trigger: 'change' }
        ],
        project: [
          { required: true, message: '请选择机器的所属项目', trigger: 'change' }
        ],
        description: [
          // { required: true, message: '请选择机器的所属项目', trigger: 'blur' }

        ]
      }
    }
  },
  components: { },
  created () {},
  mounted () {
    this.MachinesInfo()
  },
  beforeDestroy () {
  },

  methods: {
    MachinesInfo () {
      this.$http.get('machines/', { params: this.queryInfo })
        .then(
          res => {
            this.MachineInfoList = res.data.results
            console.log(res)
            this.total_page = Number(res.data.count)
          })
        .catch(err => {
          this.$message.error(err.data)
        })
    },

    handleCurrentChange (val) {
      this.queryInfo.pagenum = val
      this.MachinesInfo()
    },
    handleSizeChange (val) {
      this.queryInfo.pagesize = val
      this.MachinesInfo()
    },

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
            console.log(res)
            // this.total_page = Number(res.data.count)
          })
        .catch(err => {
          this.$message.error(err.data)
        })

      this.$http.get('users/?type=options')
        .then(
          res => {
            this.user_options = res.data
            console.log(res)
            // this.total_page = Number(res.data.count)
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
        description: ''
      }

      this.$refs[formName].validate((valid) => {
        if (valid) {
          // alert('submit!')
          console.log(this.machineForm)

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
        description: ''
      }
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
