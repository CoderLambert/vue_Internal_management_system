<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ name: 'Home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>文章</el-breadcrumb-item>
      <el-breadcrumb-item>添加 Markdown</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card style="margin: 20px 0;width:100%">
      <h1 style="text-align:center;background:#eee;line-height:40px;border-radius:10px">添加文章</h1>
      <div class="box-card-box"> 
          <div class="article-content">
            <el-input 
              v-model="markdownForm.title" 
              required='true' 
              placeholder="添加标题"></el-input>
            <mavon-editor
              class="article-editor"
              ref=md
              toolbarsBackground="white"
              v-model="markdownForm.text_content"
              @imgAdd="handleEditorImgAdd"
            />
            <section class="article-meta">
              <el-row :gutter="20">
                <el-col :span="2">
                  <strong class="side-row-label">笔记本</strong>
                </el-col>
                <el-col :span="4">
                  <el-select 
                    v-model="markdownForm.note" 
                    placeholder="请选择所属笔记本" style="width:200px">
                    <el-option
                      v-for="item in Notes"
                      :key="item.id"
                      :label="item.name"
                      :value="item.id">
                    </el-option>
                  </el-select>
                </el-col>

                <el-col :span="6">
                  <el-button 
                    type="primary" 
                    @click="showAddNoteDialog"
                    icon="el-icon-circle-plus-outline"
                    plain>
                      添加笔记本
                  </el-button>
                </el-col>

              </el-row>
              <el-row>
                <el-col :span="2">
                  <strong class="side-row-label">是否公开</strong>
                </el-col>
                <el-col :span="3">
                  <el-radio-group v-model="markdownForm.public" size="mini" >
                    <el-radio-button :label='true'>是</el-radio-button>
                    <el-radio-button :label='false'>否</el-radio-button>
                  </el-radio-group>
                </el-col>
                <el-col :span="2">
                  <strong class="side-row-label">是否原创</strong>
                </el-col>
                <el-col :span="2">
                  <el-radio-group v-model="markdownForm.original" size="mini">
                    <el-radio-button :label='true'>是</el-radio-button>
                    <el-radio-button :label='false'>否</el-radio-button>
                  </el-radio-group>
                </el-col>
              </el-row>
              <el-row v-show="markdownForm.original == false">
                    <el-input v-model="markdownForm.orginal_link" placeholder="请补充原文地址"></el-input>
              </el-row>

                <el-button class="post-submit" 
                  type="success" 
                  size="medium"
                  @click="addArtical"
                  id="addArtical"
                >
                  发布
                </el-button>

              <el-row>
                <el-col :span="2">
                  <strong>文章分类</strong>
                </el-col>
                <el-col :span="2">
                  <el-button 
                    type="primary"
                    @click="showAddTypeDialog"
                    icon="el-icon-circle-plus-outline"
                    plain>
                      添加文章分类
                  </el-button>
                </el-col>
              </el-row>

              <el-row>
                  <el-checkbox-group v-model="markdownForm.types">
                    <ArticaleTypeTree   
                      :ArticaleTypeList = this.$utils.treeShip(Types)
                      style="display:flex"
                    >
                    </ArticaleTypeTree>
                  </el-checkbox-group>
              </el-row>

            </section>
      </div>
    </div>
    </el-card>
    
    <AddArticaleNoteDialog></AddArticaleNoteDialog>
    <AddArticaleTypeDialog></AddArticaleTypeDialog>
  </div>
</template>
<script>
// @ is an alias to /src
import ArticaleTypeTree from '@/components/Articles/Type/ArticaleTypeTree.vue'
import Validator from '@/assets/js/Validator.js'
import AddArticaleNoteDialog from '@/components/Articles/Note/AddArticaleNoteDialog.vue'
import AddArticaleTypeDialog from '@/components/Articles/Type/AddArticaleTypeDialog.vue'

import { mapState, mapMutations, mapActions } from 'vuex'

// import axios from 'axios'
export default {
  name: 'index',
  data () {
    return {
      choiced_type: '',
      articaleTypes: [],
      checkList: [],
      markdownForm: {
      //   // 笔记本名称
        note: '',
        // 标题
        title: '',
        // 内容
        text_content: '',

        original: true,
      //   // 转载地址
        orginal_link: '',
      //   // 是否对其他人可见
        public: true,
        types: []
      },
      filterText: ''
      
    }
  },
  computed: { 
    ...mapState(
      'ArticlesNote', {
        Notes: state => state.Notes
      }
    ),
    ...mapState(
      'ArticlesType', {
        Types: state => state.Types
      }
    )

    // ArticleTreeShip: treeShip(this.$store.state.ArticlesType.Types)
  },
  watch: {},
  mounted () {
    this.initFunc()
  },
  beforeDestroy () {},

  methods: {
    initFunc () {
      this.getAllTypeInfo()
      this.getAllNoteInfo()
      // this.$store.dispatch('ArticlesNote/getAllNoteInfo')
    },
    validataFunc (){
      const markDownValidator = new Validator()
      markDownValidator.add(this.markdownForm.note, [
        {
            strategy: 'isEmpty',
            errorMsg: '笔记本不能为空'
        }
      ])
      markDownValidator.add(this.markdownForm.title, [
        {
            strategy: 'isEmpty',
            errorMsg: '标题不能为空'
        }
      ])

      markDownValidator.add(this.markdownForm.text_content, [
        {
            strategy: 'isEmpty',
            errorMsg: '请输入文章内容'
        }
      ])
      markDownValidator.add(this.markdownForm.original, [
        {
            strategy: 'isEmpty',
            errorMsg: '请选择文章是否为原创'
        }
      ])
      markDownValidator.add(this.markdownForm.public, [
        {
            strategy: 'isEmpty',
            errorMsg: '请选择文章是否公开'
        }
      ])
      return markDownValidator.validation()
    },

    addArtical () {
      const errorMsg = this.validataFunc()
      if (errorMsg) {
        this.$message.error( errorMsg )
        return false
      }

      this.$http.post('articles/', this.markdownForm)
        .then(
          res => {
            this.$message.success('文章发布成功')
            this.$router.push( { name: 'Articles' })
          })
        .catch(err => {
          console.log(err)
          switch (err.status) {
            case 400:
              this.$message.error(err.request.responseText)
              break

            default:
              this.$message.error('发生错误,无法提交')
          }
        })
    },
    handleEditorImgAdd (pos, $file) {
      var _this = this
      // 第一步.将图片上传到服务器.
      var formdata = new FormData()
      formdata.append('image', $file)
      this.$http.post(`meta/image/`, formdata, {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
      }// 设置header信息
      ).then(res => {
        if ( res.status === 201 ) {
          this.$message.success('图片已上传')
          _this.$refs.md.$imglst2Url([[pos, window.location.origin + res.data.image]])
        } else {
          this.$message.error('图片上传失败')
        }
      })
    },

    ...mapMutations('ArticlesNote', ['showAddNoteDialog']),
    ...mapMutations('ArticlesType', ['showAddTypeDialog']),
    ...mapActions('ArticlesType', ['getAllTypeInfo']),
    ...mapActions('ArticlesNote', ['getAllNoteInfo'])
  },
  components: {
    ArticaleTypeTree,
    AddArticaleNoteDialog,
    AddArticaleTypeDialog
  }
}
</script>

<style lang="less" scoped>

  .article-editor {
    margin-top: 20px;
  }
  .el-row {
    margin-top: 20px;
  }

  #addArtical {
    width: 100px;
    position: absolute;
    bottom: 2em;
    right: 20px;
    z-index: 9999;
  }

</style>
