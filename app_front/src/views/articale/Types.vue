<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ name: 'Home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>文章</el-breadcrumb-item>
      <el-breadcrumb-item>文章标签</el-breadcrumb-item>
    </el-breadcrumb>
<!-- 
                @clear="getTypes"
            @keyup.enter.native="ImagesInfo"
             @click="ImagesInfo" -->
                         <!-- v-model="queryInfo.search" -->
            <!-- @keyup.enter.native="this.getAllTypeInfo(this.searchInfo)" -->
            <!-- v-model="searchInfo.search" -->

    <el-card class="box-card-box">
      <el-row :gutter="10" type="flex" justify="start" class="search-box">
        <!-- <el-col :xs="5" :sm="4" :md="12" :lg="8" :xl="6">
          <el-input
            placeholder="搜索内容(文章分类标签名称)"
            :value="searchInfo.search"
            @input="changeSearchParams"
            @clear="getTypes"
            clearable
          >
            <el-button @click="getTypes" slot="append" icon="el-icon-search"></el-button>
          </el-input>
        </el-col> -->
        <el-button type="primary" @click="AddFirstType" size="small">添加新的文章分类</el-button>

      </el-row>
      <el-divider></el-divider>
      <el-table
        v-if="refreshTable"
        :data="this.$utils.treeShip(Types)"
        style="width: 100%"
s        stripe
        resizable
        row-key="id"
        default-expand-all
        :row-style="rowStyle"
        :tree-props="{children: 'children', hasChildren: 'hasChildren'}">
      >
         <!-- :header-cell-style="{background:'#F3F4F7',color:'#555'}" -->

        <el-table-column
          label="分类"
          sortable
        >
          <template slot-scope="scope">
              <el-button  size="mini" type="primary" plain>
                {{ scope.row.name }} ({{ scope.row.articles}})
              </el-button>
          </template>
        </el-table-column>
        <el-table-column
          prop="id"
          label="ID"
          sortable
        >
        </el-table-column>
        <el-table-column
          label="父分类"
          sortable
        >
            <template slot-scope="scope">
                <el-button type="info" plain v-if="scope.row.parent" size="mini">{{ scope.row.parent_name }}</el-button>
            </template>
        </el-table-column>
        
        <!-- <el-table-column
          prop="parent"
          label="父分类 ID"
          sortable
        >
        </el-table-column>  -->

        <el-table-column prop="add_time" label="添加时间" sortable>
            <template slot-scope="scope">{{ scope.row.add_time | UTCDateFormat('YYYY-MM-DD HH:mm:ss') }}</template>
        </el-table-column>

        <!-- <el-table-column prop="modified_time" label="修改时间" sortable>
            <template slot-scope="scope">{{ scope.row.modified_time | UTCDateFormat('YYYY-MM-DD HH:mm:ss') }}</template>
        </el-table-column> -->

        <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button
                  type="success"
                  size="mini"
                  plain
                  @click="editTypeName(scope.row.id, scope.row.name, scope.row.parent)"
              >编辑</el-button>

              <el-button
                  type="primary"
                  size="mini"
                  plain
                  @click="addSubType(scope.row.id)"
              >添加</el-button>

              <el-button
                  type="danger"
                  size="mini"
                  plain
                  @click="removeType(scope.row.id)"
              >删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
    <EditArticleTypeDialog></EditArticleTypeDialog>
    <AddArticaleTypeDialog></AddArticaleTypeDialog>
  </div>
</template>

<script>
// mapMutations
import { mapState, mapActions, mapMutations } from 'vuex'
import EditArticleTypeDialog from '@/components/Articles/Type/EditArticleTypeDialog.vue'
import AddArticaleTypeDialog from '@/components/Articles/Type/AddArticaleTypeDialog.vue'

export default {
  name: 'ArticaleTypes',
  data () {
    return {
        editTypeForm: {
          name: null,
          id: null,
          parent: null
        },
        addTypeInfo: {
            name: null
        },
        // searchInfo: {
        //   search: null
        // },
        defaultProps: {
          children: 'children',
          label: 'name'
        },
        refreshTable: true
    }
  },
  mounted () {
    this.initFunc()
  },
  methods: { 
    initFunc () {
      // this.getTypes()
      this.getAllTypeInfo()
    },
    getTypes () {
      this.getAllTypeInfo()
    },
    editTypeName ( id, name, parent ) {
      console.log(id, name)
      this.editTypeForm.id = id
      this.editTypeForm.name = name
      this.editTypeForm.parent = parent
      this.setEditTypeForm( this.editTypeForm )
      this.showEditTypeDialog()
    },
    AddFirstType () {
      this.setAddTypeParent(null)
      this.showAddTypeDialog()
    },
    addSubType (id) {
      this.setAddTypeParent(id)
      this.showAddTypeDialog()
    },
    removeType (id) {
      this.$confirm('确认删除该文章分类吗？', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
      }).then( () => {
        this.delType(id)
      }).catch( () => {
      })
    },

    // changeSearchParams (value) {
    //   console.log(value)
    //   // this.refreshTable = !this.refreshTable
    //   this.searchInfo.search = value
    //   // this.refreshTable = !this.refreshTable
    // },
    rowStyle ( { row, rowIndex } ) {
      if (rowIndex === 0) {
        return { background: '#ebeef5' }
      } else {
        return {}
      }
    },
    ...mapMutations('ArticlesType', ['showAddTypeDialog', 'showEditTypeDialog', 'setEditTypeForm', 'setAddTypeName', 'setAddTypeParent']),
    ...mapActions('ArticlesType', ['getAllTypeInfo', 'delType', 'editType'])

  },
  computed: { 
    ...mapState(
      'ArticlesType', {
        Types: state => state.Types,
        searhParams: state => state.searhParams
      })
  },
  watch: {},
  components: {
    EditArticleTypeDialog,
    AddArticaleTypeDialog
  }
}
</script>

<style lang="less" scoped>

</style>