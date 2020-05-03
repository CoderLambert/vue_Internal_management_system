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
        <el-input placeholder="搜索内容(项目名、项目成员、SVN 路径)"
          @clear="ProjectsInfo"
          @keyup.enter.native="ProjectsInfo"
          v-model="queryInfo.search"
          clearable
          >
          <el-button slot="append" icon="el-icon-search" @click="ProjectsInfo"></el-button>
        </el-input>
      </el-col>

      <el-col :xs="5" :sm="4" :md="2" :lg="2" :xl="4" :offset="1">
        <el-button type="primary"  @click="clearExpand">{{expandFunc}}</el-button>
      </el-col>

      <el-col :xs="5" :sm="4" :md="4" :lg="4" :xl="4" :offset="1">
        <el-button type="primary" @click="showCenterDialogVisible">添加新的项目</el-button>
      </el-col>
    </el-row>

      <el-table
        :data="PeojectInfoList"
        style="width: 100%"
        :highlight-current-row="true"
        border
        stripe
        row-key="id"
        :expand-row-keys='expands'
        :default-sort="{ prop: 'create_time', order: 'descending' }"
      >
        <el-table-column  type="expand">
          <template slot-scope="props">

            <el-form label-position="left"  inline class="demo-table-expand">
              <el-form-item label="备注">
                <span class="content">{{ props.row.build }}</span>
              </el-form-item>

            </el-form>

          </template>
        </el-table-column>

        <!-- 索隐列 -->
        <!-- <el-table-column type="index" label="#"></el-table-column> -->

        <el-table-column
          prop="name"
          label="项目"
          sortable
          width="200"
        >
        </el-table-column>

      <el-table-column label="成员" width="230">
        <template slot-scope="scope">
          <el-tag
            size="medium"
            v-for="(user, index) in scope.row.member"
            v-bind:key="index"
            >{{ user.username }}
          </el-tag>
        </template>
      </el-table-column>

        <el-table-column
          label="SVN 路径"
        >

        <template slot-scope="scope">
          <!-- <p></p> -->
          <el-tooltip content="单击鼠标左键复制 SVN 地址" placement="bottom" effect="light">
          <div v-if="scope.row.svn"
            v-clipboard:copy="scope.row.svn"
            v-clipboard:success="onCopy"
            v-clipboard:error="onError"
            class="svn-copy"
          >
            {{ scope.row.svn }}
          </div>
          </el-tooltip>
        </template>
        </el-table-column>
        <el-table-column label="操作" width="180">
          <template slot-scope="scope">
            <el-button
              type="primary"
              size="mini"
              icon="el-icon-edit"
              circle
              @click="editProjectInfo(scope.row)"
            ></el-button>

            <el-button
              type="danger"
              size="mini"
              icon="el-icon-delete"
              circle
              @click="removeProject(scope.row.id, scope.row.name)"
            ></el-button>
          </template>
        </el-table-column>
      </el-table>

<el-dialog
  title=" 新建项目"
  :visible.sync="centerDialogVisible"
  width="50%"
  center>
      <el-form
        :model="projectForm"
        status-icon
        ref="projectFormRef"
        :rules="this.addProjectRules"
        v-if='centerDialogVisible'
        label-width="140px"
        class="add-project-form"
      >
        <el-form-item
          prop="name"
          :error="ErroMessage.name"
          label="项目名"
        >
          <el-input type="text" v-model="projectForm.name" ></el-input>
        </el-form-item>

        <el-form-item
          prop="member"
          :error="ErroMessage.member"
          label="成员"
        >
          <el-select filterable  v-model="projectForm.member" multiple placeholder="请选择">
            <el-option
              v-for="item in user_options"
              :key="item.id"
              :label="item.username"
              :value="item.id">
            </el-option>
          </el-select>
          <!-- <el-input type="text" v-model="projectForm.member"></el-input> -->
        </el-form-item>
        <el-form-item
          prop="svn"
          :error="ErroMessage.svn"
          label="SVN 地址">
            <el-input v-model="projectForm.svn"></el-input>
        </el-form-item>
        <el-form-item
         prop="build"
         :error="ErroMessage.build"
         label="Build 脚本参数">
          <el-input v-model="projectForm.build"></el-input>
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click="submitForm('projectFormRef')">提交</el-button>
          <el-button @click="resetForm">重置</el-button>
        </el-form-item>
      </el-form>
</el-dialog>

<el-dialog
  title="编辑项目信息"
  :visible.sync="EditProjectDialogVisible"
  width="50%"
  center>
      <el-form
        :model="EditProjectForm"
        status-icon
        ref="EditProjectFormRef"
        :rules="this.editProjectRules"
        v-if='EditProjectDialogVisible'
        label-width="140px"
        class="add-project-form"
      >
        <el-form-item
          prop="name"
          :error="ErroMessage.name"
          label="项目名"
        >
          <el-input type="text" v-model="EditProjectForm.name" ></el-input>
        </el-form-item>

        <el-form-item
          prop="member"
          :error="ErroMessage.member"
          label="成员"
        >
          <el-select filterable  v-model="EditProjectForm.member" multiple placeholder="请选择">
            <el-option
              v-for="item in user_options"
              :key="item.id"
              :label="item.username"
              :value="item.id">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item
          prop="svn"
          :error="ErroMessage.svn"
          label="SVN 地址">
            <el-input  
              type="textarea"
              :rows="2" 
              v-model="EditProjectForm.svn">
            </el-input>
        </el-form-item>
        <el-form-item
         prop="build"
         :error="ErroMessage.build"
         label="Build 脚本参数">
          <el-input 
            type="textarea"
            :rows="2"
            v-model="EditProjectForm.build">
          </el-input>
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click="submitEditForm('EditProjectFormRef')">提交</el-button>
        </el-form-item>
      </el-form>
</el-dialog>

    <el-row :gutter="10" type="flex" justify="center">
      <el-col :xs="5" :sm="4" :md="16" :lg="8" :xl="6">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="queryInfo.pagenum"
          :page-sizes="[10, 20, 50, 100, 200]"
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
  name: 'PeojectInfo',
  data () {
    return {
      EditProjectDialogVisible: false,
      centerDialogVisible: false,
      direction: 'rtl',
      PeojectInfoList: [],
      total_page: null,
      queryInfo: {
        search: '',
        pagenum: 1,
        pagesize: 20
      },
      user_options: [],
      projectForm: {
        name: '',
        member: [],
        svn: '',
        build: ''
      },
      EditProjectForm: {
        name: '',
        member: [],
        svn: '',
        build: ''
      },
      addProjectRules: {
        name: [
          { required: true, message: '请输入项目名', trigger: 'blur' }

        ],
        member: [
          { required: true, message: '项目成员不能为空', trigger: 'change' }
        ],
        svn: [
          // { required: true, message: '请输入邮箱', trigger: 'blur' }
          // { validator: checkEmail, trigger: 'blur' }
        ],
        build: [
          // { required: true, message: '请选择你所属的部门', trigger: 'blur' }
        ]

      },
      editProjectRules: {
        name: [
          { required: true, message: '请输入项目名', trigger: 'blur' }

        ],
        member: [
          { required: true, message: '项目成员不能为空', trigger: 'change' }
        ],
        svn: [
          // { required: true, message: '请输入邮箱', trigger: 'blur' }
          // { validator: checkEmail, trigger: 'blur' }
        ],
        build: [
          // { required: true, message: '请选择你所属的部门', trigger: 'blur' }
        ]

      },

      ErroMessage: {
        name: '',
        member: '',
        svn: '',
        build: ''
      },
      expands: [],
      expandFunc: '展开所有'
    }
  },
  components: { },
  created () {},
  mounted () {
    this.ProjectsInfo()
  },
  beforeDestroy () {
  },

  methods: {
    clearExpand () {
      if (this.expands.length > 0) {
        this.expands = []
        this.expandFunc = '全部展开'
      } else {
        for (let i = 0; i < this.PeojectInfoList.length; i++) {
          this.expands.push(this.PeojectInfoList[i]['id'])
        }
        this.expandFunc = '全部收缩'
      }
    },

    UserOptionsInfo () {
      this.$http.get('users/?type=options')
        .then(
          res => {
            this.user_options = res.data
            console.log(res)
            // this.total_page = Number(res.data.count)
          })      
    },
    ProjectsInfo () {
      this.$http.get('projects/', { params: this.queryInfo })
        .then(
          res => {
            this.PeojectInfoList = res.data.results
            console.log(res)
            this.total_page = Number(res.data.count)
          })
        .catch(err => {
          this.$message.error(err.data)
        })
    },

    handleCurrentChange (val) {
      this.queryInfo.pagenum = val
      this.ProjectsInfo()
    },
    handleSizeChange (val) {
      this.queryInfo.pagesize = val
      this.ProjectsInfo()
    },
    // handleClose (done) {
    //   this.$confirm('确认关闭？')
    //     .then(_ => {
    //       done()
    //     })
    //     .catch(_ => {})
    // },
    onCopy (e) {
      this.$message.success(`已复制 ${e.text} 到粘贴板`)
    },
    onError: function (e) {
      this.$message.error('复制 SVN 地址失败！')
    },
    showCenterDialogVisible () {
      this.centerDialogVisible = true
      this.UserOptionsInfo()
    },
    submitForm (formName) {
      this.ErroMessage = {
        name: '',
        member: '',
        svn: '',
        build: ''
      }

      this.$refs[formName].validate((valid) => {
        if (valid) {
          // alert('submit!')
          console.log(this.projectForm)

          this.$http.post('projects/', this.projectForm)
            .then(
              res => {
                this.$message.success('创建新项目成功!')
                this.ProjectsInfo()
                this.centerDialogVisible = false
                this.projectForm = {
                  name: '',
                  member: [],
                  svn: '',
                  build: ''
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
                  console.log('请求发生未知错误')
              }
            })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    resetForm () {
      this.projectForm = {
        name: '',
        member: [],
        svn: '',
        build: ''
      }
    },

    editProjectInfo (project) {
      console.log(project)
      this.EditProjectDialogVisible = true
      // this.UserOptionsInfo()
      this.$http.get('users/?type=options')
        .then(
          res => {
            this.user_options = res.data
            let member_id = []
            for (let i = 0; i < project.member.length; i++) {
              member_id.push(project.member[i].id)
            }
            this.EditProjectForm = {
              id: Number(project.id),
              name: project.name,
              member: member_id,
              svn: project.svn,
              build: project.build
            }
          })    
    },

    submitEditForm (formName) {
      this.ErroMessage = {
        name: '',
        member: '',
        svn: '',
        build: ''
      }

      this.$refs[formName].validate((valid) => {
        if (valid) {
          // alert('submit!')
          console.log(this.EditProjectForm)
          this.$http.put(`projects/${this.EditProjectForm.id}/`, this.EditProjectForm)
            .then(
              res => {
                this.$message.success('已更新项目信息!')
                this.ProjectsInfo()
                this.EditProjectDialogVisible = false
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

    removeProject (ProjectID, ProjectName) {
      this.$confirm('此操作将删除该项目, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      })
        .then(() => {
          this.$http.delete(`projects/` + ProjectID + '/').then(() => {
            this.$message({
              message: `${ProjectName}  已删除`,
              type: 'success'
            })
            this.queryInfo.pagenum = 1
            this.ProjectsInfo()
          })
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
    margin-top: 20px
  }
  .el-tag{
    margin:  10px;
  }
  .add-project-form{
    margin:20px;
    .el-select{
      width: 100%
    }
  }
  .demo-table-expand {
    font-size: 0;

    .el-form-item {
      margin-right: 0;
      margin-bottom: 0;
      width: 100%;
      vertical-align: top;
      border-bottom:1px solid #dfdfdf;
      .content{
          font-size: 20px
        }
      .el-form-item__label {
        width: 90px ;
        color: #99a9bf;
        font-size: 44px
      }
    }
  }

</style>
