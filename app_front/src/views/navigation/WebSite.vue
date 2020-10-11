<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ name: 'Home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>导航</el-breadcrumb-item>
      <el-breadcrumb-item>常用网站</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card class="box-card-box">

      <div class="edit-header">
          <el-input
            placeholder="搜索内容(网站名,地址,分类名,URL)"
            @clear="WebSiteInfo"
            @keyup.enter.native="WebSiteInfo"
            v-model="queryInfo.search"
            style="width:400px;margin-right:30px"
            clearable
          >
          <el-button slot="append" icon="el-icon-search" @click="WebSiteInfo"></el-button>
          </el-input>
          <div>
            <el-button @click="addNewWebSite"  type="primary" size="small" icon="el-icon-circle-plus-outline" round>新增站点</el-button>
            <el-button @click="changeEditWebSiteState"  type="info" size="small" icon="el-icon-edit" round>{{EditState}}</el-button>
          </div>
  
     </div>

      <div  v-for="(web, index) in webList"
            v-bind:key="index">
        <div class="website-type">
            {{web.type}}
        </div>
        <ul class='website-box'>
          <li class='websie-item'
            v-for="(website, index) in web.data"
            v-bind:key="index"
            >
            <el-tooltip :content="website.description"  placement="bottom" effect="light">
              <el-tag v-show="!editWebSitePage" disable-transitions @click="openlink(website.url)" 
                :closable='editWebSitePage' 
                class='website-item-link'
                @close="handleClose(website.id)">  
                {{ website.name }}
              </el-tag>
            </el-tooltip>

              <el-dropdown v-show="editWebSitePage" @command="handleCommand" trigger="hover" :hide-on-click="true" size="small" >
                <span class="website-item-link">
                  {{ website.name }}
                </span>
                <el-dropdown-menu slot="dropdown">
                  <el-dropdown-item :command="{type:'edit',webInfo:website}" style="color:#409eff"> 编辑 </el-dropdown-item>
                  <el-dropdown-item :command="{type:'delete',webInfo:website}" style="color:#d93b2a">删除</el-dropdown-item>
                </el-dropdown-menu>
              </el-dropdown>
          </li>
        </ul>
      </div>
    </el-card>

<el-dialog
  title=" 新增站点"
  :visible.sync="addWebDialogVisible"
  width="50%"
  center>
      <el-form
        :model="addWebForm"
        status-icon
        ref="addWebFormRef"
        :rules="this.WebInfoFormRules"
        v-if='addWebDialogVisible'
        label-width="140px"
        class="add-project-form"
      >
        <el-form-item
          prop="name"
          :error="addWebFormErroMessage.name"
          label="网站名"
        >
          <el-input type="text" v-model="addWebForm.name" ></el-input>
        </el-form-item>

        <el-form-item
          prop="url"
          :error="addWebFormErroMessage.url"
          label="网址">
            <el-input v-model.trim="addWebForm.url"></el-input>
        </el-form-item>

        <el-form-item
         prop="description"
         :error="addWebFormErroMessage.description"
         label="网站描述">
          <el-input 
            type="textarea"
            :rows="2" 
            v-model="addWebForm.description">
          </el-input>
        </el-form-item>
        <el-form-item
         prop="public"
         :error="addWebFormErroMessage.public"
         label="公开可见">

        <el-radio-group v-model="addWebForm.public"  size="mini">
          <el-radio-button :label='true'>所有人可见</el-radio-button>
          <el-radio-button :label='false'>仅自己可见</el-radio-button>
        </el-radio-group>

        </el-form-item>

        <el-form-item
          prop="type"
          :error="addWebFormErroMessage.type"
          label="所属分类"
        >
          <el-select filterable  v-model="addWebForm.type"  placeholder="请选择">
            <el-option
              v-for="item in webTypeList"
              :key="item.id"
              :label="item.name"
              :value="item.id">
            </el-option>
          </el-select>  
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitAddWebForm('addWebFormRef')">提交</el-button>
          <el-button @click="resetAddWebForm">重置</el-button>
        </el-form-item>
      </el-form>
</el-dialog>

<el-dialog
  title=" 编辑站点信息"
  :visible.sync="editWebDialogVisible"
  width="50%"
  center>
      <el-form
        :model="editWebForm"
        status-icon
        ref="editWebFormRef"
        :rules="this.WebInfoFormRules"
        v-if='editWebDialogVisible'
        label-width="140px"
        class="add-project-form"
      >
        <el-form-item
          prop="name"
          :error="editWebFormErroMessage.name"
          label="网站名"
        >
          <el-input type="text" v-model.trim="editWebForm.name" ></el-input>
        </el-form-item>

        <el-form-item
          prop="url"
          :error="editWebFormErroMessage.url"
          label="网址">
            <el-input v-model.trim="editWebForm.url"></el-input>
        </el-form-item>

        <el-form-item
         prop="description"
         :error="editWebFormErroMessage.description"
         label="网站描述">
          <el-input 
            type="textarea"
            :rows="2" 
            v-model="editWebForm.description">
            </el-input>
        </el-form-item>
        <el-form-item
         prop="public"
         :error="editWebFormErroMessage.public"
         label="公开可见">

        <el-radio-group v-model="editWebForm.public"  size="mini">
          <el-radio-button :label='true'>所有人可见</el-radio-button>
          <el-radio-button :label='false'>仅自己可见</el-radio-button>
        </el-radio-group>

        </el-form-item>

        <el-form-item
          prop="type"
          :error="editWebFormErroMessage.type"
          label="所属分类"
        >
          <el-select filterable  v-model="editWebForm.type"  placeholder="请选择">
            <el-option
              v-for="item in webTypeList"
              :key="item.id"
              :label="item.name"
              :value="item.id">
            </el-option>
          </el-select>  
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitEditWebForm('editWebFormRef')">提交</el-button>
          <el-button @click="resetEditWebForm">重置</el-button>
        </el-form-item>
      </el-form>
</el-dialog>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'WebSite',
  data () {
    return {
      webList: [],
      webTypeList: [],
      addWebDialogVisible: false,
      editWebDialogVisible: false,
      queryInfo: {
        search: ''
      },
      addWebForm: {
        name: '',
        url: '',
        description: '',
        public: false,
        type: ''
      },
      editWebForm: {
        name: '',
        url: '',
        description: '',
        public: false,
        type: ''
      },

      WebInfoFormRules: {
        name: [
          { required: true, message: '请输入网站名', trigger: 'blur' }
        ],
        url: [
          { required: true, message: '网址不能为空', trigger: 'blur' }
        ],
        type: [
          { required: true, message: '网站分类不能为空', trigger: 'change' }
        ],
        public: [
          { required: true, message: '请选择是否公开可见', trigger: 'change' }
        ]  
      },
      addWebFormErroMessage: {
        name: '',
        url: '',
        description: '',
        public: '',
        type: ''   
      },
      editWebFormErroMessage: {
        name: '',
        url: '',
        description: '',
        public: '',
        type: ''   
      },
      editWebSitePage: false,
      EditState: '编辑'
    }
  },
  computed: {
  },
  mounted () {
    this.WebSiteInfo()
  },
  beforeDestroy () {
  },

  methods: {
    buttonedit () {
      console.log('button click')
    },
    WebTypeInfo () {
      this.$http.get('web/type/')
        .then(
          res => {
            this.webTypeList = res.data
          })
        .catch(err => {
          this.$message.error(err.data)
        })
    },
    WebSiteInfo () {
      this.$http.get('web/site/', { params: this.queryInfo })
        .then(
          res => {
            let key = 'type'
            this.webList = this.$utils.sortByKey(res.data, key)
          })
        .catch(err => {
          this.$message.error(err.data)
        })
    },
    resetAddWebForm () {
      this.addWebForm = {
        name: '',
        url: '',
        description: '',
        public: '',
        type: ''    
      }
    },
    submitAddWebForm (formName) {
      this.addWebFormErroMessage = {
        name: '',
        url: '',
        description: '',
        public: '',
        type: ''   
      }
      this.$refs[formName].validate((valid) => {
        if (valid) {
          console.log(this[formName])
          this.$http.post(`web/site/`, this.addWebForm)
            .then(
              res => {
                this.$message.success('网站已添加!')
                this.WebSiteInfo()
                this.addWebDialogVisible = false
              })
            .catch(err => {
              switch (err.status) {
                case 400:
                  for (let key in err.data) {
                    this.addWebFormErroMessage[key] = err.data[key][0]
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
    openlink (url){
      window.open(url, '_blank')
    },
    addNewWebSite () {
      console.log('addNewWebSite')
      this.WebTypeInfo()
      this.addWebDialogVisible = true
    },

    changeEditWebSiteState () {
      if ( this.EditState === '编辑' ) {
        this.EditState = '取消编辑'
        this.editWebSitePage = true
      } else {
        this.EditState = '编辑'
        this.editWebSitePage = false
      }
    },
    resetEditWebForm () {
      this.editWebForm = {
        name: '',
        url: '',
        description: '',
        public: '',
        type: ''    
      }
    },
    editWebSiteInfo (webInfo) {
      this.editWebForm = {
        id: webInfo.id,
        name: webInfo.name,
        url: webInfo.url,
        description: webInfo.description,
        public: webInfo.public,
        type: webInfo.typeid   
      }
      this.WebTypeInfo()
      this.editWebDialogVisible = true
    },
    submitEditWebForm (formName) {
      this.editWebFormErroMessage = {
        name: '',
        url: '',
        description: '',
        public: '',
        type: ''   
      }
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // console.log(this[formName])
          this.$http.put(`web/site/${this.editWebForm.id}/`, this.editWebForm)
            .then(
              res => {
                this.$message.success('网站信息已更新!')
                this.WebSiteInfo()
                this.editWebDialogVisible = false
              })
            .catch(err => {
              switch (err.status) {
                case 400:
                  for (let key in err.data) {
                    this.editWebFormErroMessage[key] = err.data[key][0]
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
    deleteWebSite (id) {
      this.$confirm('此操作将删除该站点, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      })
        .then(() => {
          this.$http.delete(`/web/site/${id}/`).then(() => {
            this.$message({
              message: `已删除`,
              type: 'success'
            })
            this.WebSiteInfo()
          })
        })
    },
    handleClose (tagID) {
      this.deleteWebSite(tagID)
    },
    handleCommand (command){
      if ( command.type === 'edit') {
        this.editWebSiteInfo(command.webInfo)
      } 
      if ( command.type === 'delete') {
        this.deleteWebSite(command.webInfo.id)
      }
    }
  },
  components: {

  }
}
</script>

<style lang="less" scoped>
.edit-header {
  // margin: 4px;
  margin-bottom: 10px;
  display: flex;
  justify-content: space-between;
}

.website-type {
  line-height: 30px;
  background: #b7d6ec;
  border-radius: 5px;
  padding: 5px;
  font-size: 18px;
  font-weight: 620;
}

.website-box {
  padding: 0 12px 9px;
  list-style: none;
  .websie-item {
      display: inline-block;
      vertical-align: top;
      width: 25%;
      margin: 6px 0;
      padding: 0 6px;
      box-sizing: border-box;
      .website-item-link  {
        position: relative;
        display: block;
        height: 34px;
        line-height: 34px;
        text-align: center;
        -webkit-text-decoration: none;
        text-decoration: none;
        font-size: 18px;
        color: #3F4146;
        background-color: #f2f6f8;
        border-radius: 4px;
        border-color:  #EEEFF2;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        &:hover {
          background-color: skyblue;
          cursor: pointer;
        }
    }
  }
  @media only screen and (min-width: 768px) {
    .websie-item {
        width: 16.66666%;
    }
    
  }
  @media only screen and (min-width: 540px) {
    .websie-item {
        width: 20%;
    }
  }
}
.notClick {
    pointer-events: none;
    cursor: default;
}

.el-dropdown {
    display: block;
    overflow: hidden;
    color: #EEEFF2;
    border: 1px solid skyblue
}
.el-dropdown-item {
  width: 14rem;
}
</style>
