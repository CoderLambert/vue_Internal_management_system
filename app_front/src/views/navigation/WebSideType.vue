<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ name: 'Home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>导航</el-breadcrumb-item>
      <el-breadcrumb-item>网站分类</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card class="box-card-box">

      <div class="edit-header">
          <el-input
            placeholder="搜索内容(名称，优先级)"
            @clear="WebTypeInfo"
            @keyup.enter.native="WebTypeInfo"
            v-model="queryInfo.search"
            style="width:400px;margin-right:30px"
            clearable
          >
          <el-button slot="append" icon="el-icon-search" @click="WebTypeInfo"></el-button>
          </el-input>
          <div>
            
            <el-button @click="addNewWeType"  type="primary" size="small" icon="el-icon-circle-plus-outline" round>新增网站类型</el-button>
            <el-button @click="changeEditWebTypeState"  type="info" size="small" icon="el-icon-edit" round>{{EditState}}</el-button>
          </div>
     </div>

      <div  v-for="(webType, index) in webTypeList"
            v-bind:key="index">
        <div class="website-type">
           优先级: {{webType.order}}
        </div>
        <ul class='type-box'>
          <li class='type-box-item'
            v-for="(webtype, index) in webType.data"
            v-bind:key="index"
            >
            <div class="type-box-item-info">
              <span v-show="!editWebTypePage">
                  {{webtype.name}}
              </span>

              <el-dropdown v-show="editWebTypePage" @command="handleCommand" trigger="hover" :hide-on-click="true" size="small" >
                <span class="type-box-item-info">
                  {{ webtype.name }}
                </span>
                <el-dropdown-menu slot="dropdown">
                  <el-dropdown-item :command="{type:'edit',webTypeInfo:webtype}" style="color:#409eff"> 编辑 </el-dropdown-item>
                  <el-dropdown-item :command="{type:'delete',webTypeInfo:webtype}" style="color:#d93b2a">删除</el-dropdown-item>
                </el-dropdown-menu>
              </el-dropdown>

            </div>
          </li>
        </ul>
      </div>

<el-dialog
  title=" 新增站点分类"
  :visible.sync="addWebTypeDialogVisible"
  width="30%"
  center>
      <el-form
        :model="addWebTypeForm"
        status-icon
        ref="addWebTypeRef"
        :rules="this.WebInfoTypeFormRules"
        v-if='addWebTypeDialogVisible'
        label-width="140px"
        class="add-project-form"
      >
        <el-form-item
          prop="name"
          :error="addWebTypeFormErroMessage.name"
          label="网站分类名称"
        >
          <el-input type="text" v-model="addWebTypeForm.name" ></el-input>
        </el-form-item>

        <el-form-item
          prop="order"
          :error="addWebTypeFormErroMessage.order"
          label="网站优先级">
            <el-input-number v-model="addWebTypeForm.order" controls-position="right" @change="UpadateWebTypeAddOrder" :min="1" :max="100"></el-input-number>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitAddWebType('addWebTypeRef')">提交</el-button>
          <el-button @click="resetAddWebType">重置</el-button>
        </el-form-item>
      </el-form>
</el-dialog>
<el-dialog
  title="更改站点分类"
  :visible.sync="editWebTypeDialogVisible"
  width="30%"
  center>
      <el-form
        :model="editWebTypeForm"
        status-icon
        ref="editWebTypeRef"
        :rules="this.WebInfoTypeFormRules"
        v-if='editWebTypeDialogVisible'
        label-width="140px"
        class="add-project-form"
      >
        <el-form-item
          prop="name"
          :error="editWebTypeFormErroMessage.name"
          label="网站分类名称"
        >
          <el-input type="text" v-model="editWebTypeForm.name" ></el-input>
        </el-form-item>

        <el-form-item
          prop="order"
          :error="editWebTypeFormErroMessage.order"
          label="网站优先级">
            <el-input-number v-model="editWebTypeForm.order" controls-position="right" @change="UpadateWebTypeAddOrder" :min="1" :max="100"></el-input-number>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitEditWebType('editWebTypeRef')">提交</el-button>
          <el-button @click="resetAddWebType">重置</el-button>
        </el-form-item>
      </el-form>
</el-dialog>

    </el-card>
  </div>
</template>

<script>
// @ is an alias to /src
// import draggable from 'vuedraggable'
export default {
  name: 'WebSideType',
  data () {
    return {
      webTypeList: [],
      EditState: '编辑',
      addWebTypeDialogVisible: false,
      editWebTypeDialogVisible: false,
      
      addWebTypeForm: {
        name: '',
        order: 1
      },
      editWebTypeForm: {
        id: '',
        name: '',
        order: null
      },
      queryInfo: {
        search: ''
      },
      WebInfoTypeFormRules: {
        name: [
          { required: true, message: '请输入网站分类名称', trigger: 'blur' }
        ],
        order: [
          { required: true, message: '请输入网站排序', trigger: 'blur' }
        ]
      },
      addWebTypeFormErroMessage: {
        name: '',
        order: ''  
      },
      editWebTypeFormErroMessage: {
        name: '',
        order: '' 
      },
      editWebTypePage: false
    }
  },
  computed: {
  },
  mounted () {
    this.WebTypeInfo()
  },
  beforeDestroy () {
  },

  methods: {

    WebTypeInfo () {
      this.$http.get('web/type/', { params: this.queryInfo })
        .then(
          res => {
            let key = 'order'
            this.webTypeList = this.$utils.sortByKey(res.data, key)
            console.log(this.webTypeList)
          })
        .catch(err => {
          this.$message.error(err.data)
        })
    },
    changeEditWebTypeState () {
      if ( this.EditState === '编辑' ) {
        this.EditState = '取消编辑'
        this.editWebTypePage = true
      } else {
        this.EditState = '编辑'
        this.editWebTypePage = false
      }
    },
    UpadateWebTypeAddOrder (value) {
      console.log(value)
      this.addWebTypeForm.order = value
      console.log(this.addWebTypeForm)
    },
    UpadateWebTypeEditOrder (value) {
      console.log(value)
      this.editWebTypeForm.order = value
      console.log(this.editWebTypeForm)
    },

    addNewWeType () {
      console.log('addNewWebSite')
      // this.WebTypeInfo()
      this.addWebTypeDialogVisible = true
    },
    resetAddWebType () {
      this.addWebTypeForm = {
        name: '',
        order: 1
      }
    },
    submitAddWebType (formName) {
      this.addWebTypeFormErroMessage = {
        name: '',
        order: ''
      }

      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.$http.post('web/type/', this.addWebTypeForm)
            .then(
              res => {
                this.$message.success('创建新项目分类成功!')
                this.WebTypeInfo()
                this.addWebTypeDialogVisible = false
                this.addWebTypeFormErroMessage = {
                  name: '',
                  order: ''
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
    submitEditWebType (formName) {
      this.editWebTypeFormErroMessage = {
        name: '',
        order: ''
      }

      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.$http.put(`web/type/${this.editWebTypeForm.id}/`, this.editWebTypeForm)
            .then(
              res => {
                this.$message.success('创建新项目分类成功!')
                this.WebTypeInfo()
                this.editWebTypeDialogVisible = false
                this.editWebTypeFormErroMessage = {
                  name: '',
                  order: ''
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
    editWebTypeInfo (webTypeInfo) {
      console.log('editWebSiteInfo ==> ')
      console.log(webTypeInfo)
      this.editWebTypeForm = {
        id: webTypeInfo.id,
        name: webTypeInfo.name,
        order: webTypeInfo.order
      }
      this.editWebTypeDialogVisible = true
    },
    deleteWebTypeInfo (id) {
      this.$confirm('此操作将删除该站点类型, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      })
        .then(() => {
          this.$http.delete(`/web/type/${id}/`).then(() => {
            this.$message({
              message: `已删除`,
              type: 'success'
            })
            this.WebTypeInfo()
          })
        })
    },
    handleCommand (command){
      // this.$message.info(command.type)
      if ( command.type === 'edit') {
        this.editWebTypeInfo(command.webTypeInfo)
      } 
      if ( command.type === 'delete') {
        this.deleteWebTypeInfo(command.webTypeInfo.id)
      }
    }

  },
  components: {

  }
}
</script>

<style lang="less" scoped>
.edit-header {
  margin: 4px;
  display: flex;
  justify-content: space-between;
  margin-bottom: 15px;
}
.website-type {
  line-height: 30px;
  background: #b7d6ec;
  border-radius: 5px;
  padding: 5px;
  font-size: 18px;
  font-weight: 620;

}

.type-box {
  padding: 0 12px 9px;
  list-style: none;
  .type-box-item {
      display: inline-block;
      vertical-align: top;
      width: 33%;
      margin: 6px 0;
      padding: 0 6px;
      box-sizing: border-box;
      .type-box-item-info  {
        text-align: center;
        position: relative;
        display: block;
        // height: 34px;
        line-height: 60px;
        text-align: center;
        -webkit-text-decoration: none;
        text-decoration: none;
        font-size: 24px;
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
        width: 32%;
    }
    
  }
  @media only screen and (min-width: 540px) {
    .websie-item {
        width: 40%;
    }
  }
.el-dropdown {
  display: block;
  overflow: hidden;
  color: #EEEFF2;
  border: 1px solid skyblue
}
}

</style>
