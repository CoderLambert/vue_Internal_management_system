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
          <el-button class="upload-button" size="small" type="success" @click="onSubmit">上传到服务器</el-button>
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

        <el-row>
          <el-col :span="12">
          <el-form-item prop="romFile" label="">
            <div class="grid-content bg-purple">
              <el-upload
                class="upload-demo"
                ref="upload_image"
                action=""
                accept=".ima,.rom,.bin"
                :multiple="false"
                :show-file-list='true'
                :on-preview="handlePreview"
                :on-remove="handleRemove"
                :file-list="uploadFileList"
                :on-change="fileChange"
                :on-error="handleUploadError"
                :auto-upload="false">
                <el-button  size="mini" type="primary" plain>选择镜像文件</el-button>
                <div slot="tip" class="el-upload__tip">只能上传ima,rom,bin类型文件，且不超过 64MB</div>
              </el-upload>
            </div>
          </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item prop="releaseNoteFile" label="">

            <div class="grid-content bg-purple-light">
              <el-upload
                class="upload-demo"
                ref="upload_releaseNote"
                action=""
                accept=".txt,.log"
                :multiple="false"
                :show-file-list='true'
                :on-preview="handlePreview"
                :on-remove="handleReleaseNoteRemove"
                :file-list="uploadFileList"
                :on-change="releaseFileChange"
                :on-error="handleUploadError"
                :auto-upload="false">
                <el-button  size="mini" type="primary" plain>选择 Release Note 文件</el-button>
                <div slot="tip" class="el-upload__tip">请选择.txt、.log格式文本文件</div>
              </el-upload>
            </div>
            </el-form-item>
          </el-col>
        </el-row>

        <el-form-item label="邮件通知">
          <div style="display:inline">
            <ImageUploadMail  ref="ImageUploadMailRef"></ImageUploadMail>
          </div>
        </el-form-item>
      </el-form>
      <el-progress v-if="progressBarVisble" :text-inside="true" :stroke-width="16" status="success" :percentage="this.uploadProgress"></el-progress>

    </el-card>

  </div>
</template>

<script>
import axios from 'axios'
import ImageUploadMail from '@/components/ImageUploadMail.vue'
// @ is an alias to /src
export default {
  name: 'ImageUpload',
  data () {
    return {
      uploadFileList: [],
      projectOptions: '',
      project: '',
      project_description: '',
      param: '', // 表单要提交的参数
      uploadImageForm: {
        project: '',
        project_description: '',
        romFile: '',
        releaseNoteFile: ''
      },
      // 第一步 定义 rules 对象
      // 第二步 form 表单绑定 rules对象
      // 第三步 form-item 通过 prop 绑定属性验证规则
      uploadImageRules: {
        romFile: [
          { required: true, message: '请选择的上传镜像', trigger: 'blur' }
        ],
        releaseNoteFile: [
          { required: true, message: '请选择上传的 release Note 文件', trigger: 'blur' }
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
      },
      uploadProgress: 0,
      progressBarVisble: false,
      cancelUpload: null
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
  // 此功能仅当 :auto-upload="true" 时才会触发
  //  :before-upload="beforeUpload"

  // beforeUpload (file) {},
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
          formData.append('release_note', this.uploadImageForm.releaseNoteFile)

          formData.append('project', this.uploadImageForm.project)
          formData.append('description', this.uploadImageForm.project_description)
          formData.append('userid', sessionStorage.getItem('userid'))
          let CancelToken = axios.CancelToken
          this.cancelUpload = CancelToken.source()

          formData.append('target_mails', this.$refs.ImageUploadMailRef.targetMailAddr)
          console.log(this.$refs.ImageUploadMailRef)
          this.$http.post(`images/`, formData, {
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            cancelToken: this.cancelUpload.token,
            onUploadProgress: progressEvent => {
                let complete = ( progressEvent.loaded / progressEvent.total * 100 | 0 )
                this.uploadProgress = complete
                this.progressBarVisble = this.uploadProgress < 100
            }

          }// 设置header信息
          ).then(res => {
            this.$message.success( res.data[0].name + ' 已上传')
            this.uploadImageForm = {
              project: '',
              project_description: '',
              romFile: '',
              release_note: ''
            }
            // 隐藏已上传文件列表
            this.uploadFileList = []
            // 清空发送人邮件地址列表
            this.$refs.ImageUploadMailRef.targetMailAddr = []
          })
        }
      })
    },

    fileChange (file, fileList) {
      //  参考 https://blog.csdn.net/sunday_tutu/article/details/82018037
      var extType = file.name.substring( file.name.lastIndexOf('.')).toLowerCase()
      let supportExts = ['.rom', '.bin', '.ima']
      const isSupportType = supportExts.indexOf(extType) > -1
      const supportTypeInfo = supportExts.join(', ')

      const isLt64M = file.size / 1024 / 1024 < 64
      const isNullFile = file.size === 0
      if ( !isSupportType ) {
          this.$message({
              message: `上传文件只能是 ${supportTypeInfo} 格式!`,
              type: 'warning'
          })
      }

      if (!isLt64M) {
          this.$message({
              message: '上传文件大小不能超过 64MB',
              type: 'warning'
          })
      }
      if (isNullFile) {
          this.$message({
              message: '上传文件不能为空文件',
              type: 'warning'
          })
      }
      if ( isSupportType && ( isLt64M && !isNullFile ) ) {
        if ( fileList.length > 1 ){
          //  只保留第一个
          fileList = fileList.shift()
        }
        this.uploadImageForm.romFile = (file.raw)
      } else {
          this.$refs['upload_image'].clearFiles()
          this.uploadImageForm.romFile = ''
          this.uploadFileList = []
      }
    },

    releaseFileChange (file, fileList) {
      //  参考 https://blog.csdn.net/sunday_tutu/article/details/82018037
      var extType = file.name.substring( file.name.lastIndexOf('.')).toLowerCase()
      let supportExts = ['.txt', '.log']
      const isLt10M = file.size / 1024 / 1024 < 10
      const isNullFile = file.size === 0
      const isSupportType = supportExts.indexOf(extType) > -1
      const supportTypeInfo = supportExts.join('、')
      if ( !isSupportType ) {
          this.$message({
              message: `上传文件只能是 ${supportTypeInfo} 格式!`,
              type: 'warning'
          })
      }

      if (!isLt10M) {
          this.$message({
              message: '上传文件大小不能超过 10MB',
              type: 'warning'
          })
      }
      if (isNullFile) {
          this.$message({
              message: '上传文件不能为空文件',
              type: 'warning'
          })
      }
      if ( isSupportType && ( isLt10M && !isNullFile ) ) {
        if ( fileList.length > 1 ){
          //  只保留第一个
          fileList = fileList.shift()
        }
        this.uploadImageForm.releaseNoteFile = (file.raw)
      } else {
          this.$message({
              message: '上传文件不符合要求',
              type: 'warning'
          })
          this.$refs['upload_releaseNote'].clearFiles()
          this.uploadImageForm.releaseNoteFile = ''
          this.uploadFileList = []
      }
    },
    handleExceed (files, fileList) {
      this.$message.warning(`最多上传1个文件`)
    },
    handleUploadError (file, fileList) {
      this.$message.error(`上传文件失败`)
    },
    handleRemove (files, fileList) {
      this.$refs['upload_image'].clearFiles()
      this.uploadImageForm.romFile = ''
      this.$message.info(`取消上传文件`)
      if (this.cancelUpload) {
        // 判断cancelUpload是否存在
        this.cancelUpload.cancel('取消上传')
        // 在请求catch()的error中输出'取消上传'

        // 隐藏已上传文件列表
        this.progressBarVisble = false
      }
    },

    handleReleaseNoteRemove (files, fileList) {
      this.$refs['upload_releaseNote'].clearFiles()
      this.uploadImageForm.releaseNoteFile = ''
      this.$message.info(`取消上传文件`)
      if (this.cancelUpload) {
        // 判断cancelUpload是否存在
        this.cancelUpload.cancel('取消上传')
        // 在请求catch()的error中输出'取消上传'

        // 隐藏已上传文件列表
        this.progressBarVisble = false
      }
    },
    handlePreview (files, fileList) {
      this.$message.warning(`handlePreview ${files.length} 个文件`)
    },

    // 项目选项名列表
    projectOptionList () {
      this.$http.get(`project/name/`).then(res => {
        this.projectOptions = res.data
      })
    }
  },
  components: {
    ImageUploadMail
  }
}
</script>

<style lang="less" scoped>
.upload-button {
  // float: right;
  margin-left : 60px;
}

</style>
