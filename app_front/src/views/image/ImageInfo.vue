<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ name: 'Home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>镜像</el-breadcrumb-item>
      <el-breadcrumb-item>文件信息</el-breadcrumb-item>
    </el-breadcrumb>

    <el-card class="box-card-box">
      <el-row :gutter="10" type="flex" justify="start" class="search-box">
        <el-col :xs="5" :sm="4" :md="12" :lg="8" :xl="6">
          <el-input
            placeholder="搜索内容(文件名、文件描述)"
            @clear="ImagesInfo"
            @keyup.enter.native="ImagesInfo"
            v-model="queryInfo.search"
            clearable
          >
            <el-button slot="append" icon="el-icon-search" @click="ImagesInfo"></el-button>

          </el-input>

        </el-col>
        <el-col :xs="5" :sm="4" :md="2" :lg="8" :xl="6">
          <el-button type="primary"  @click="clearExpand">{{expandFunc}}</el-button>
        </el-col>

      </el-row>

      <el-table
        :data="RomImageList"
        style="width: 100%"
        :highlight-current-row="true"
        border
        stripe
        row-key="id"
        :expand-row-keys='expands'
        :default-sort="{ prop: 'create_time', order: 'descending' }"
      >
        <el-table-column label type="expand">
          <template slot-scope="props">
            <el-form label-position="left" inline class="demo-table-expand">
              <el-form-item label>
                <pre class="image-description">{{ props.row.description }}</pre>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>
        <!-- 索隐列 -->
        <!-- <el-table-column type="index" label="#"></el-table-column> -->

        <el-table-column prop="project" label="所属项目" sortable width="200"></el-table-column>

        <el-table-column prop="name" label="文件名" sortable>
          <template slot-scope="scope">
            <span
              class="file-name"
              @click="downloadFun(scope.row.url,scope.row.name)"
            >{{ scope.row.name }}</span>
          </template>
        </el-table-column>

        <el-table-column prop="username" label="上传人" width="150" sortable></el-table-column>
        <el-table-column prop="create_time" label="上传时间" sortable width="200"></el-table-column>

        <el-table-column label="操作" width="180">
          <template slot-scope="scope">
            <el-button
              class="btns"
              size="mini"
              type="success"
              @click="downloadFun(scope.row.url)"
            >下载</el-button>
            <el-button
              type="primary"
              size="mini"
              icon="el-icon-edit"
              circle
              @click="editRomImageInfo(scope.row.id,scope.row.project_id, scope.row.description)"
            ></el-button>

            <el-button
              type="danger"
              size="mini"
              icon="el-icon-delete"
              circle
              @click="removeRomImage(scope.row.id, scope.row.name)"
            ></el-button>
          </template>
        </el-table-column>
      </el-table>

      <el-dialog title=" 更改文件信息" :visible.sync="editFormVisible" width="50%" center>
        <!-- :rules="this.editFormRules" -->

        <el-form
          :model="editForm"
          status-icon
          ref="editFormRef"
          v-if="editFormVisible"
          label-width="140px"
        >
          <el-form-item prop="project" label="文件所属项目">
            <el-select filterable v-model="editForm.project" placeholder="请选择">
              <el-option
                v-for="item in projectOptions"
                :key="item.id"
                :label="item.name"
                :value="item.id"
              ></el-option>
            </el-select>
          </el-form-item>
          <!-- :error="editFormRules.description" -->

          <el-form-item prop="description" label="文件备注">
            <el-input type="text" v-model="editForm.description"></el-input>
          </el-form-item>

          <el-form-item>
            <el-button type="primary" @click="submitEditForm('editFormRef')">提交</el-button>
            <el-button @click="editFormCancel">取消</el-button>
          </el-form-item>
        </el-form>
      </el-dialog>

      <el-row :gutter="10" type="flex" justify="center">
        <el-col :xs="5" :sm="4" :md="16" :lg="8" :xl="6">
          <el-pagination
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page="queryInfo.pagenum"
            :page-sizes="[5,10, 20, 50, 100, 200]"
            :page-size="queryInfo.pagesize"
            layout="total, sizes, prev, pager, next, jumper"
            :total="total_page"
          ></el-pagination>
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>
<script>
export default {
  name: 'ImageInfo',
  data () {
    return {
      isExpand: true,
      expands: [],
      expandFunc: '展开所有',
      projectOptions: [],
      editFormVisible: false,

      editForm: {
        id: '',
        project: '',
        description: ''
      },
      RomImageList: [],
      total_page: null,
      queryInfo: {
        search: '',
        pagenum: 1,
        pagesize: 20
      }
    }
  },
  components: {},
  created () {},
  mounted () {
    this.ImagesInfo()
  },
  beforeDestroy () {},
  // computed: {
  // 计算属性的 getter
  // expandRows: function () {
  //   // `this` 指向 vm 实例

  //   return this.message.split('').reverse().join('')
  // }
  // },
  methods: {

    clearExpand () {
      if (this.expands.length > 0) {
        this.expands = []
        this.expandFunc = '全部展开'
      } else {
        for (let i = 0; i < this.RomImageList.length; i++) {
          // console.log(key + '---' + obj[key])
          this.expands.push(this.RomImageList[i]['id'])
        }
        this.expandFunc = '全部收缩'
      }
    },

    ImagesInfo () {
      this.$http
        .get('images/', { params: this.queryInfo })
        .then(res => {
          this.RomImageList = res.data.results

          console.log(res)
          this.total_page = Number(res.data.count)
        })
        // .catch(err => {
        //   this.$message.error(err.data)
        // })
    },

    handleCurrentChange (val) {
      this.queryInfo.pagenum = val
      this.ImagesInfo()
    },
    handleSizeChange (val) {
      this.queryInfo.pagesize = val
      this.ImagesInfo()
    },
    downloadFun (fileUrl, fileName) {
      window.open(fileUrl, '_blank')
    },
    ProjectOptionsInfo () {
      this.$http
        .get(`project/name`)
        .then(res => {
          // console.log(res)
          this.projectOptions = res.data
        })
        .catch(err => {
          this.$message.error(err.data)
        })
    },
    editRomImageInfo (RomID, RomProject, RomDescription) {
      this.editForm = {
        id: Number(RomID),
        project: Number(RomProject),
        description: RomDescription
      }
      // console.log(this.editForm)
      this.ProjectOptionsInfo()
      this.editFormVisible = true
    },

    submitEditForm () {
      this.$http
        .patch(`images/` + this.editForm.id + '/', this.editForm)
        .then(() => {
          this.$message({
            message: `文件信息已更新！`,
            type: 'success'
          })
          this.ImagesInfo()
          this.editFormVisible = false
        })
        .catch(() => {
          this.$message({
            type: 'warning',
            message: '更新发生错误！'
          })
        })
    },
    editFormCancel () {
      this.editFormVisible = false
    },
    removeRomImage (fileID, fileName) {
      this.$confirm('此操作将删除该文件, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      })
        .then(() => {
          this.$http.delete(`images/` + fileID + '/').then(() => {
            this.$message({
              message: `${fileName}  已删除`,
              type: 'success'
            })
            this.queryInfo.pagenum = 1
            this.ImagesInfo()
          })
        })
        .catch(() => {
          this.$message({
            type: 'warning',
            message: '无法删除'
          })
        })
    }
  },

  computed: {}
}
</script>
<style lang="less" scoped>
.search-box {
  margin: 0 0 10px 0;
}
.file-name {
  color: skyblue;
  cursor: pointer;
}
.el-pagination {
  margin-top: 20px;
}
</style>
