<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ name: 'Home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>文章</el-breadcrumb-item>
      <el-breadcrumb-item>笔记本</el-breadcrumb-item>
    </el-breadcrumb>

    <el-card class="box-card-box">
      <el-row :gutter="10" type="flex" justify="start" class="search-box">
        <el-col :xs="5" :sm="4" :md="12" :lg="8" :xl="6">
          <el-input
            placeholder="搜索内容(笔记本名称)"
            v-model="searchInfo.search"
            @keyup.enter.native="getNotes"
            @clear="getNotes"
            clearable
          >
            <el-button @click="getNotes" slot="append" icon="el-icon-search"></el-button>
          </el-input>
        </el-col>
        <el-button type="primary" @click="showAddNoteDialog" size="small">添加新的笔记本</el-button>
      </el-row>
      <el-divider></el-divider>
      <el-table
        :data="Notes"
        style="width: 100%"
        :highlight-current-row="true"
        stripe
        row-key="id"
      >
        <el-table-column prop="id" label="" width="100" sortable> </el-table-column>

        <el-table-column prop="name" label="笔记本" sortable> </el-table-column>
        <el-table-column prop="articles" label="文章总数" sortable> </el-table-column>
        <el-table-column prop="add_time" label="添加时间" sortable>
            <template slot-scope="scope">{{ scope.row.add_time | UTCDateFormat('YYYY-MM-DD HH:mm:ss') }}</template>
        </el-table-column>

        <el-table-column prop="modified_time" label="修改时间" sortable>
            <template slot-scope="scope">{{ scope.row.modified_time | UTCDateFormat('YYYY-MM-DD HH:mm:ss') }}</template>
        </el-table-column>
  
        <el-table-column label="操作">
            <template slot-scope="scope">

              <el-button
                  type="success"
                  size="mini"
                  plain
                  @click="editNoteName(scope.row.id, scope.row.name)"
              >编辑</el-button>

              <el-button
                  type="danger"
                  size="mini"
                  plain
                  @click="removeNote(scope.row.id)"
              >删除</el-button>
            </template>
        </el-table-column>

      </el-table>
    </el-card>
    <EditArticaleNoteDialog></EditArticaleNoteDialog>
    <AddArticaleNoteDialog></AddArticaleNoteDialog>
  </div>
</template>

<script>
// import { mapState, mapMutations, mapActions } from "vuex";
import { mapState, mapMutations, mapActions } from 'vuex'
import EditArticaleNoteDialog from '@/components/Articles/Note/EditArticleNoteDialog.vue'
import AddArticaleNoteDialog from '@/components/Articles/Note/AddArticaleNoteDialog.vue'

export default {
  name: 'ArticaleNotes',
  data () {
    return {
        editNoteForm: {
          name: null,
          id: null
        },
        addNoteInfo: {
            name: null
        },
        searchInfo: {
          search: null
        }
    }
  },
  mounted () {
    this.initFunc()
  },
  methods: { 
    initFunc () {
        this.getNotes()
    },
    getNotes () {
        this.getAllNoteInfo(this.searchInfo)
    },
    editNoteName ( id, name ) {
        this.editNoteForm.name = name
        this.editNoteForm.id = id
        this.setEditNoteForm( this.editNoteForm )
        this.showEditNoteDialog()
    },
    removeNote (id) {
      this.$confirm('确认删除改笔记本吗？', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
      }).then( () => {
        this.delNote(id)
      }).catch( () => {

      })
    },
    ...mapMutations('ArticlesNote', ['showAddNoteDialog', 'setEditNoteForm', 'showEditNoteDialog']),
    ...mapActions('ArticlesNote', ['getAllNoteInfo', 'delNote'])
  },
  computed: { 
    ...mapState(
      'ArticlesNote', {
        Notes: state => state.Notes,
        searhParams: state => state.searhParams
      }
    )
  },
  watch: { },
  components: {
    AddArticaleNoteDialog,
    EditArticaleNoteDialog
  }
}
</script>

<style lang="less" scoped>
</style>