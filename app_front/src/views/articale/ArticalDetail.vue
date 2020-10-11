<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ name: 'Home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>文章</el-breadcrumb-item>
      <el-breadcrumb-item>文章详情</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card style="margin: 20px 0;width:100%">

      <article v-if="article"> 
            <section class="article-meta">
              <div class="article-meta-item">
                <el-link @click="filterAuthorArtical(article.user_info.id)">
                  <i class="el-icon-user"></i>
                  <span class="article-meta-item-content">
                    {{article.user_info.name}}
                  </span>
                </el-link>
              </div>

              <div>
                <span  class="article-meta-item">
                  <i class="el-icon-notebook-1"></i>
                    <span class="article-meta-item-content">                   
                      {{article.note.name}}
                    </span>
                </span>

                <span  class="article-meta-item">
                  <i class="el-icon-view el-icon--right"></i>
                    <span class="article-meta-item-content">                   
                      {{article.browse_num}}
                    </span>
                </span>

                <span  class="article-meta-item">
                  <i class="el-icon-date"></i>
                    <span class="article-meta-item-content">
                      {{article.add_time | UTCDateFormat }}
                    </span>
                </span>
              </div>
            </section>
              <section class="article-meta">
                <div>
                  <span  class="article-meta-item">
                    <i class="el-icon-collection-tag"></i>
                      <el-tag type="info" size="mini" v-for="(type,index) in article.types" v-bind:key="index" style="margin:0 10px">
                        {{type.name}}
                      </el-tag>
                  </span>
                </div>
              </section>

              <mavon-editor 
                :subfield="false"
                :boxShadow="false"
                 defaultOpen="preview"
                :toolbarsFlag="false"
                :previewBackground="previewBackground"
                :navigation="navEnable"
                :value="article.text_content" 
            />
          <footer>
            <h2 class="article-meta-item-title">
              <!-- {{article.title}}  -->
            <a class="article-meta-item-title" style="margin-left:10px; color:skyblue;text-decoration-line: none;" 
              target = '_blank' v-bind:href="article.orginal_link" 
              v-if="!article.original"
            >
              原文地址: {{article.orginal_link}}
            </a>
            </h2>
          </footer>
          </article>        
    </el-card>
        <ul class="user-operation-list"> 
          <!-- <li class="user-operation-delete" @click="changeNav">目录</li> -->
          <li class="user-operation-edit" @click="editArticalDialogVisible(article.id)">编辑</li>
          <li class="user-operation-delete" @click="delArticalDialogVisible = true">删除</li>
        </ul>
  
    <el-dialog
      title="删除文章"
      :visible.sync="delArticalDialogVisible"
      width="30%"
      >
      <span>请确认是否删除该文章？</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="delArticalDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="deleteArtical(article.id)">确 定</el-button>
      </span>
    </el-dialog>

  </div>
</template>

<script>
// @ is an alias to /src
import { getArticalInfo, delArtical } from '@/api/api.js'

export default {
  name: 'ArticalDetail',
  data () {
    return {
        navEnable: false,
        article: null,
        previewBackground: 'white',
        delArticalDialogVisible: false
    }
  },
  computed: {

  },
  watch: {},
  beforeMount () {
     getArticalInfo({
       id: this.$route.params.artical_id
    })
        .then ( (res) => {
          this.article = res.data
        })
  },
  beforeDestroy () {},

  methods: {
    editArticalDialogVisible (artical_id) {
      this.$router.push( { name: 'EditMarkdown', params: { artical_id } })
    },
    deleteArtical (ArticalID) {
      this.delArticalDialogVisible = false
      delArtical(ArticalID)
        .then ( (res) => {
          this.$message.success('已删除')
          this.$router.push( { name: 'Articles' })
        })
    }
  },
  components: {}
}
</script>

<style lang="less" scoped>
.article-derail {
  margin: 20px auto;
}

footer {
  height: 80px;
  line-height: 30px;
}
.article-meta {
  display: flex;
  justify-content: space-between;
  margin:1rem 0;
  .article-meta-item {
    i {
        margin-right:5px;
    }
  }
  .article-meta-item:not(:last-child){ 
    margin-right: 30px;
  }
}
ul {
  position: absolute;
  margin: 0;
  padding: 0;
  right: 25px;
  top: 40%;
  z-index: 9999;
  list-style: none;
  li {
    width: 60px;
    line-height: 3em;
    height: 3em;
    text-align: center;
    cursor: pointer;
    position: relative;
    box-sizing: border-box;
    border: 1px solid #dcdfe0;
    &:hover {
            background-color: skyblue;
        }
    &:hover > a {
            color: #fff;
        }
  }
  .user-operation-delete {
    color: red;
  }
  .user-operation-edit {
    color: grey
  }
}
</style>
