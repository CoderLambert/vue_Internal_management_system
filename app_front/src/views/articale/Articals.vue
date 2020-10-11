<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ name: 'Home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>文章</el-breadcrumb-item>
      <el-breadcrumb-item>文章列表</el-breadcrumb-item>
    </el-breadcrumb>

    <el-card style="margin: 20px 0;width:100%">
        <div class="edit-header">
          <el-row :gutter="40">
            <el-col :span="7">            
              <el-input
                placeholder="搜索内容( 文章内容 )"
                @clear="getAllArticles"
                @keyup.enter.native="getAllArticles"
                :value="quuery_params.search"
                @input="setQuueryParamsSearch"
                class="search-content-bar"
                clearable
              >
              <el-button
                slot="append" 
                icon="el-icon-search" 
                @click="getAllArticles">
              </el-button>
              </el-input>
            </el-col>
            <el-col :span="4">
              <el-cascader
                placeholder="选择文章分类"
                :options="ArticaleTypesTree"
                :props="{ multiple: true, checkStrictly: true, label: 'name', value: 'id', emitPath: false }"
                ref="tree"
                clearable
                filterable
                @change="showCheckedTypes"
                @visible-change="changeSelectType"
                >
                <!-- @clearCheckedNodes="clearCheckedTypeNodes" -->

                <template slot-scope="{ node, data }">
                  <span>{{ data.name }}</span>
                  <span > ({{ data.articles }}) </span>
                </template>
              </el-cascader>
            </el-col>
<!-- v-model="value"  -->
            <el-col :span="4">
              <el-select  
                @change="changeSelectNote" 
                :value="quuery_params.note"
                clearable 
                placeholder="选择笔记本">
                <el-option
                  v-for="item in Notes"
                  :key="item.id"
                  :label="item.name"
                  :value="item.id">
                </el-option>
              </el-select>
            </el-col>

            <el-col :span="4">
              <el-select  
                @change="changeSelectUser" 
                :value="quuery_params.user" 
                clearable 
                placeholder="选择作者">
                <el-option
                  v-for="item in UserOptions"
                  :key="item.id"
                  :label="item.username"
                  :value="item.id">
                </el-option>
              </el-select>
            </el-col>

          </el-row>
            <section id='artical-ordering'>
              <ul>
                <li class="artical-ordering-title"> 排序</li>
                <li class="artical-ordering-direc" @click="changeOrderDirection()">{{ this.orderMessage}}</li>
                <li
                  v-for="(condition, index) in orderConditions"
                  v-bind:key="index"
                  :class="{'active': active_order == index}"
                  @click="orderingArtical(condition.name,index)"
                  >
                  {{ condition.title }}
                </li>
              </ul>
            </section>
        </div>

      <div class="article-list"> 
        <el-card class="article-box" 
            v-for="(article,key) in articles" 
            v-bind:key="key"
            shadow="hover"
        >       
        <div style="display:inline-block">
          <el-link class="article-meta-item-title" 
            @click="toArticalDetail(article.id)"
            :underline="false" 
          >
            {{article.title}} 
          </el-link>
          <a
            class="article-meta-item-title"
            style="margin-left:10px; color:skyblue;text-decoration-line: none;" 
            target = '_blank'
            v-bind:href="article.orginal_link" 
            v-if="!article.original"
          >
            (转)
          </a>
          <span 
            class="article-meta-item-title" 
            style="margin-left:10px; color:red; text-decoration-line:bottom" 
          v-else>
              (原)
          </span>
          <span
            class="article-meta-item-title"
            style="margin-left:10px; color:#dae7ec;" 
            v-if="!article.public"
          >
            (私)
          </span>
        </div>
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
                  {{article.add_time | UTCDateFormat}}
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

        </el-card>

      </div>
      
      <el-row :gutter="10" type="flex" justify="center">
        <el-col :xs="5" :sm="4" :md="16" :lg="8" :xl="6">
          <el-pagination
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page="quuery_params.pagenum"
            :page-sizes="[5, 10, 20, 50, 100, 200]"
            :page-size="quuery_params.pagesize"
            layout="total, sizes, prev, pager, next, jumper"
            :total="total_count">
          </el-pagination>
        </el-col>
      </el-row>

    </el-card>
    <ul class="menu animated fadeIn">
        <!-- <li>
            <a href="#">笔记本</a>
            <ul class="submenu">
              <li :class="{'active': active_note_item == ''}"
                @click="filterArticalsByNote('')"
              >
                全部笔记本
              </li>        
              <li v-for="note in Notes" 
                :key="note.id"
                :class="{'active': active_note_item == note.id}"
                @click="filterArticalsByNote(note.id)"
              >
                <a > {{note.name}} </a> 
              </li>
            </ul>
        </li>
        <li>
            <a href="#">用户</a>
            <ul class="submenu">
              <li :class="{'active': active_user == ''}"
                @click="filterAuthorArtical('')"
              >
                所有用户
              </li>        
              <li v-for="user in UserOptions" 
                :key="user.id"
                :class="{'active': active_user == user.id}"
                @click="filterAuthorArtical(user.id)"
              >
                {{user.username}}
              </li>
            </ul>
        </li> -->
        <li  @click="reset(quuery_params_init)">
            <a> 重置 </a>
        </li>

        <li  @click="addArticle">
            <a> 新文章</a>
        </li>
    </ul>

  </div>
</template>

<script>
import { mapState, mapActions, mapMutations } from 'vuex'

export default {
  name: 'Articals',
  data () {
    return {
        articals_list: null,
        notes_list: null,
        active_user: '',
        active_order: 3,
        active_note_item: '',
        current_types: [],
        quuery_params_init: {
                note: '',
                types: null,
                user: '',
                search: '',
                pagenum: 1,
                pagesize: 10,
                ordering: '-add_time'
              }
    }
  },

  watch: {},
  mounted () {
    this.initFunc()
  },
  beforeDestroy () {},
  
  methods: {
      initFunc () {
        this.getAllTypeInfo()
        this.getAllArticles()
        this.getAllNoteInfo()
        this.getAllUserOptionsInfo()
      },
      showCheckedTypes (val) {
        let newArr = [] 
        newArr = newArr.concat(...val)
        this.setQuueryParamsTypes(this._.union(newArr).join(','))
      },
      changeOrderDirection () {
        this.changeOrderingDirection()
        this.changeOrderingOrderMessage()
        this.changeOrdering()
        this.setQuueryParamsPageNum(1)
        this.getAllArticles()
      },
      toArticalDetail (artical_id) {
        this.$router.push( { name: 'ArticalDetail', params: { artical_id } } )
      },
      handleCurrentChange (val) {
        this.setQuueryParamsPageNum(val)
        this.getAllArticles(this.quuery_params)
      },
      handleSizeChange (val) {
        this.setQuueryParamsPageSize(val)
        this.getAllArticles(this.quuery_params)
      },

      filterArticalsByNote (NoteID) {
        this.active_note_item = NoteID
        this.setQuueryParamsNote(NoteID)
        this.setQuueryParamsPageNum(1)
        this.getAllArticles()
      },
      filterAuthorArtical (UserID) {
        this.active_user = UserID
        this.setQuueryParamsUser(UserID)
        this.setQuueryParamsPageNum(1)      
        this.getAllArticles()
      },
      orderingArtical (condition, index) {
        this.active_order = index
        this.setOrderCondition(condition)
        this.changeOrdering()
        this.setQuueryParamsPageNum(1)
        this.setQuueryParamsPageSize(10)
        this.getAllArticles()
      },
      changeSelectNote (value) {
        this.setQuueryParamsNote(value)
        this.getAllArticles()
      },
      changeSelectUser (value) {
        this.setQuueryParamsUser (value)
        this.getAllArticles()
      },

      changeSelectType (value) {
        console.log(value)
        if ( value === false ) {
          if ( this.current_types !== this.quuery_params.types ) {
            this.getAllArticles()
          }
        } else {
            this.current_types = this.quuery_params.types
            console.log(this.current_types)
        }
      },
      addArticle () {
        this.$router.push( { name: 'AddMarkdown' })
      },
    ...mapActions('ArticlesType', ['getAllTypeInfo']),
    ...mapActions('Articles', ['getAllArticles', 'reset']),
    ...mapMutations('Articles', [
              'changeOrderingDirection', 
              'changeOrderingOrderMessage', 
              'changeOrdering', 
              'setOrderCondition', 
              'setQuueryParamsTypes', 
              'setQuueryParamsPageNum', 
              'setQuueryParamsPageSize', 
              'setQuueryParamsUser', 
              'setQuueryParamsNote',
              'setQuueryParamsSearch'
              ]),
    ...mapActions('ArticlesNote', ['getAllNoteInfo']),
    ...mapActions('User', ['getAllUserInfo', 'getAllUserOptionsInfo'])
    },
  computed: {
    ...mapState(
      'ArticlesNote', {
        Notes: state => state.Notes
      }),

    ...mapState(
      'ArticlesType', {
        Types: state => state.Types,
        searhParams: state => state.searhParams
      }),

    ...mapState(
      'Articles', {
        articles: state => state.articles,
        orderConditions: state => state.orderConditions,
        quuery_params: state => state.quuery_params,
        orderingDirection: state => state.orderingDirection,
        orderMessage: state => state.orderMessage,
        ordering: state => state.ordering,
        total_count: state => state.total_count
      }),
    ...mapState(
      'User', {
        Users: state => state.Users,
        UserOptions: state => state.UserOptions
      }),
    ArticaleTypesTree () {
        let msg_list_dict = {}
        let ArticaleTypes = this._.cloneDeep(this.Types)
        ArticaleTypes.forEach( item => {
            msg_list_dict[item['id']] = item
        })
        let result = []
        ArticaleTypes.forEach ( (item) => {
            let pid = item['parent']

            if ( Boolean(pid) === true ) {
              if ( msg_list_dict[pid] ) {
                if ( !msg_list_dict[pid].hasOwnProperty('children')) {
                  msg_list_dict[pid]['children'] = []
                }
                msg_list_dict[pid]['children'].push(item)
              } else {
                result.push(item)
              }
            } else {
              result.push(item)
            }
            // }
        })
        return result
    }
  },
  components: {}
}
</script>

<style lang="less" scoped>
.article-list {
    width: 94%;
    margin: 20px auto;
    clear: both;
    .article-box {
        margin: 20px;
        .article-abstract {
            display:block;
            font-size: 1em;
            width:61em;
            height: 3em;
            // white-space:pre-wrap;
            word-break:keep-all;
            overflow:hidden;
            text-overflow:"点击详情查看更多";
        }
        .article-meta-item-title {
              margin: -7px 0 4px;
              display: inherit;
              font-size: 18px;
              font-weight: 700;
              line-height: 1.5;
          }          

        .article-meta {
          display: flex;
          justify-content: space-between;
          margin-top:1rem;
          .article-meta-item {
            i {
                margin-right:5px;
            }
          }
          .article-meta-item:not(:last-child){ 
            margin-right: 30px;
          }
        }  
        .article-meta-original {
          color:skyblue; 
          font-size: 18px; 
          font-weight: 700; 
          line-height: 1.5;
          vertical-align: text-bottom;
        }
    }
}
.filter-note-condition {
  list-style: none;
  margin: 0 20px;
  padding: 0;
  li {
    display: inline-block;
    line-height: 24px;
    height:24px;
    width: 120px;
    background: #eee;
    border: 1px solid #eee;
    border-radius: 2px;
    text-align: center;
    margin:4px;

  }

}
.menu {
  position: absolute;
  top: 27%;
  right: 20px;
}

ul,
ol {
    margin: 0;
    padding: 0;
    list-style: none;
}

a {
    text-decoration: none;
    color: #666;
}
/*一级导航*/
/*背景色*/
ul.menu,
ul.submenu {
    background-color: #7bbfea;
    font-size: 14px;
    li {
      border-bottom: 1px solid #fff;
      &:hover {
        background: skyblue;
      }
    }
}

/*一级导航浮动*/
ul.menu::after {
    content: '';
    display: block;
    clear: both;
}

ul.menu>li {
    /* float: left; */
    width: 80px;
    line-height: 3em;
    height: 3em;
    text-align: center;
    cursor: pointer;
    position: relative;
    box-sizing: border-box;
}
        /*二级导航项分割线*/
        ul.submenu {
            /*默认隐藏*/
            display: none;
            position: absolute;
            top: 0;
            right:100%;
            width: 120px;
            animation: 0.5s disappear ease-in forwards;
            /* transition: 100%; */
        }

        ul.submenu>li {
            border-bottom: 1px solid #fff;
            border-left: 1px solid #fff;
            border-right: 1px solid #fff;
        }

        /*内容区*/
        .content {
            min-height: 800px;
            background-color: #fff;
        }
        /*选中特效*/
        ul.menu > li:hover {
            background-color: #2a5caa;
            border-left: 1px solid #fff;
        }
        ul.menu > li:hover > a {
            color: #fff;
        }
        ul.menu > li:hover > ul.submenu {
          display: block;
          transition: all 1s linear;

          cursor: pointer;
        }
        /*动画帧*/
        @keyframes fade {
          from {
              opacity: 0;
          }
          to {
              opacity: 1;
          }
        }
        /*基础动画样式*/
        .animated {
            animation-duration: 1s;
            animation-fill-mode: both;
        }
        .fadeIn {
            animation-name: fade;
            animation-direction: normal;
        }
#artical-ordering {
  margin: 20px;
  .artical-ordering-title{
    color: #909399;
    background: #fff;
    margin: 0 20px 0 0;
    width: 60px;
    font-size: 20px;
  }

  ul {
    display: flex;
    margin: 10px;
    // justify-content: space-between;
    li {
      // background: ;
      width:100px;
      margin-right: 50px;
      text-align: center;
      line-height: 30px;
      height: 30px;
      user-select: none;
      cursor: pointer;
      background: #f4f4f4;
    }
    .artical-ordering-direc {
      background: #e5eaf4;
      border: 1px solid #eee;
    }
  }
}
.active {
  background: skyblue!important;
}
</style>
