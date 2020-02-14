<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ name: 'Home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>镜像</el-breadcrumb-item>
      <el-breadcrumb-item>上传镜像</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card class="box-card-box">
      <el-form
        ref="uploadImageFormRef"
        :model="uploadImageForm"
        :rules="this.uploadImageRules"
        label-width="80px"
      >
        <el-form-item prop="project"  label="项目名">
          <el-select filterable v-model="uploadImageForm.project" placeholder="请选择所属项目">
            <el-option
              v-for="option in projectOptions"
              :key="option.id"
              :label="option.name"
              :value="option.id">
            </el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="文件描述">
          <el-input
            type="textarea"
            :autosize="{ minRows: 4, maxRows: 8 }"
            placeholder="请输入内容"
            v-model="uploadImageForm.project_description"
          >
          </el-input>
        </el-form-item>

        <el-form-item prop="romFile" label="">
          <el-upload
            class="upload-demo"
            ref="upload"
            action=""
            :on-preview="handlePreview"
            :on-remove="handleRemove"
            :limit="1"
            :file-list="fileList"
            :on-change="fileChange"
            :auto-upload="false">
            <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
            <el-button style="margin-left: 10px;" size="small" type="success" @click="onSubmit">上传到服务器</el-button>
            <div slot="tip" class="el-upload__tip">只能上传rom文件，且不超过 64MB</div>
          </el-upload>
        </el-form-item>

      </el-form>
    </el-card>

  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'ImageUpload',
  data () {
    return {
      fileList: [],
      projectOptions: '',
      project: '',
      project_description: '',
      param: '', // 表单要提交的参数
      uploadImageForm: {
        project: '',
        project_description: '',
        romFile: ''
      },
      // 第一步 定义 rules 对象
      // 第二步 form 表单绑定 rules对象
      // 第三步 form-item 通过 prop 绑定属性验证规则
      uploadImageRules: {
        romFile: [
          { required: true, message: '上传的文件不能为空', trigger: 'blur' }
        ],
        project: [
          { required: true, message: '请选择文件所属的项目', trigger: 'blur' }
        ]
        // project_description: [
        //   { required: true, message: '请选择你的用户角色', trigger: 'blur' }
        // ]
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
  computed: {
  },
  mounted () {
    this.projectOptionList()
  },
  beforeDestroy () {
  },

  methods: {

    ResetUploadImageForm () {
      this.$refs.uploadImageFormRef.resetFields()
    },
    onSubmit () {
      event.preventDefault() // 取消默认行为
      this.$refs.uploadImageFormRef.validate((valid) => {
        console.log('valid =>' + valid)
        if (valid) {
          // 创建 formData 对象
          let formData = new FormData()
          formData.append('roms', this.uploadImageForm.romFile)
          formData.append('project', this.uploadImageForm.project)
          formData.append('description', this.uploadImageForm.project_description)
          formData.append('userid', sessionStorage.getItem('userid'))
          this.$http.post(`images/`, formData, {
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
          }// 设置header信息
          ).then(res => {
            this.$message.success('上传成功')
            this.uploadImageForm = {
              project: '',
              project_description: '',
              romFile: ''
            }
          })
        }
      })
    },

    fileChange (file) {
      this.uploadImageForm.romFile = file.raw// 上传文件变化时将文件对象push进files数组
    },
    handleSuccess (response, file, fileList) {
      this.fileList = fileList
    },
    handleExceed (files, fileList) {
      this.$message.warning(`handleExceed ${files.length} 个文件`)
    },

    handleRemove (files, fileList) {
      this.$message.warning(`handleRemove ${files.length} 个文件`)
    },
    handlePreview (files, fileList) {
      this.$message.warning(`handlePreview ${files.length} 个文件`)
    },

    // 项目选项名列表
    projectOptionList () {
      this.$http.get(`project/name`).then(res => {
        console.log(res)
        this.projectOptions = res.data
        this.formData = null
      })
    }
  },
  components: {

  }
}
</script>

<style lang="less" scoped>

</style>
