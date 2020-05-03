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
            placeholder="搜索内容(上传人、文件名、文件描述)"
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
    <el-tabs>
        <el-tab-pane  v-for="(projectList,key) in RomImageList"  v-bind:key = "key" :label="key">
          <el-table
            :data="projectList"
            :highlight-current-row="true"
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
            <el-table-column type="index" label="#"></el-table-column>
                  @click="downloadFun(scope.row.url,scope.row.name)"
            <el-table-column prop="name" label="镜像">
              <template slot-scope="scope">
                <span
                  class="file-name"
                  @click="downloadFun(scope.row.url,scope.row.name,scope.row.id)"

                >
                  {{ scope.row.name }}
                </span>
              </template>
            </el-table-column>

            <el-table-column prop="name" label="Release Note">
              <template slot-scope="scope">
                <span
                  class="file-name"
                  @click="downloadFun(scope.row.release_note,scope.row.release_note_name,scope.row.id)"
                >
                  {{ scope.row.release_note_name }}
                </span>
              </template>
            </el-table-column>

            <el-table-column prop="create_time" label="上传时间">
                <template slot-scope="scope">{{ scope.row.create_time | UTCDateFormat('YYYY-MM-DD HH:mm:ss') }}</template>
            </el-table-column>
            <el-table-column prop="username" label="上传人"></el-table-column>

            <el-table-column label="操作">
              <template slot-scope="scope">
                <!-- <el-button
                  class="btns"
                  size="mini"
                  type="success"
                  :loading="scope.row.id === current_button"
                  @click="downloadFun(scope.row.url,scope.row.name,scope.row.id)"
                >下载</el-button> -->
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

        </el-tab-pane>
    </el-tabs>

      <el-dialog title=" 更改文件信息" :visible.sync="editFormVisible" width="50%" center>

        <el-form
          :model="editForm"
          status-icon
          ref="editFormRef"
          v-if="editFormVisible"
          :rules="this.editFormRules"
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

          <el-form-item prop="description" label="文件备注">
            <el-input 
              type="textarea"
              :rows="2" 
              v-model="editForm.description">
            </el-input>
          </el-form-item>

          <el-form-item>
            <el-button type="primary" @click="submitEditForm('editFormRef')">提交</el-button>
            <el-button @click="editFormCancel">取消</el-button>
          </el-form-item>
        </el-form>
      </el-dialog>
    </el-card>
  </div>
</template>
<script>
import { saveAs } from 'file-saver'
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
        search: ''
      }
      // current_button: -1
    }
  },
  components: {},
  created () {},
  mounted () {
    this.ImagesInfo()
  },
  beforeDestroy () {},

  methods: {
    clearExpand () {
      if (this.expands.length > 0) {
        this.expands = []
        this.expandFunc = '全部展开'
      } else {
        for (let i = 0; i < this.RomImageList.length; i++) {
          this.expands.push(this.RomImageList[i]['id'])
        }
        this.expandFunc = '全部收缩'
      }
    },

    ImagesInfo () {
      this.$http
        .get('images/', { params: this.queryInfo })
        .then(res => {
          this.RomImageList = this._.groupBy(res.data, 'project') 
        })
    },

    downloadFun (fileUrl, fileName, fileID) {
      saveAs(fileUrl, fileName)
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
  }
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
