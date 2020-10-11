<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ name: 'Home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>建议</el-breadcrumb-item>
      <el-breadcrumb-item>需求</el-breadcrumb-item>
    </el-breadcrumb>

    <el-card style="margin: 20px 0;width:100%">
      <el-col :xs="5" :sm="4" :md="12" :lg="8" :xl="6">

        <el-input placeholder="搜索内容(需求描述、上传人)"
          @clear="getDemandList"
          @keyup.enter.native="getDemandList"
          v-model="queryInfo.search"
          clearable
          >
          <el-button slot="append" icon="el-icon-search" @click="getDemandList"></el-button>
        </el-input>
      </el-col>
    <el-button 
      type="success" 
      class="demand-submit"
      size="mini"
      @click="addDemandInfo"
    >
      添加新的需求
    </el-button>

      <el-table
        :data="DemandData"
        style="width: 100%"
        >
        <el-table-column
          prop="description"
          label="需求描述"
        >
          <template  slot-scope="scope">
            <span
              :class='["demand-description"]'
            >
            <!-- [scope.row.current_state+1] -->
              {{ scope.row.description }}

            <!-- <mavon-editor                                    
              v-model="scope.row.description "                                     
              :subfield="false"                                    
              :boxShadow="false"                                    
              defaultOpen="preview"                                    
              :toolbarsFlag="false"                                   
            />   -->
            </span>
          </template>

        </el-table-column>
        <el-table-column
          prop="current_state"
          label="当前状态"
          sortable
          width="160">
          <template  slot-scope="scope">
            <span
              :class='["demand-status", DemandStatus[scope.row.current_state].class]'
            >
            <!-- [scope.row.current_state+1] -->
              {{ DemandStatus[scope.row.current_state].text }}
            </span>
          </template>

        </el-table-column>
        <el-table-column
          prop="owner"
          label="提交人员"
          sortable
          width="160">
        </el-table-column>
        
        <el-table-column
          prop="add_time"
          label="提交日期"
          sortable
          width="200">
          <template slot-scope="scope">
            <span
              class="file-name"
            >
              {{ scope.row.add_time | UTCDateFormat('YYYY-MM-DD HH:mm:ss')}}
            </span>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="180">
          <template slot-scope="scope">
            <el-button
              type="primary"
              size="mini"
              icon="el-icon-edit"
              circle
              @click="editDemandInfo(scope.row)"
            ></el-button>

            <el-button
              type="danger"
              size="mini"
              icon="el-icon-delete"
              circle
              @click="removeDemand(scope.row.id, scope.row.description)"
            ></el-button>
          </template>
        </el-table-column>

      </el-table>

    <el-row :gutter="10" type="flex" justify="center">
      <el-col :xs="5" :sm="4" :md="16" :lg="8" :xl="6">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="queryInfo.pagenum"
          :page-sizes="[10, 20, 50, 100, 200]"
          :page-size="queryInfo.pagesize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total_page">
        </el-pagination>
      </el-col>
    </el-row>

      <editDemandInfo @updateDemondInfo="getDemandList" ref="editDemandRef"></editDemandInfo>
      <AddDemand @updateDemondInfo="getDemandList"  ref="addDemandRef"></AddDemand>
    <div>
  </div>

  </el-card>

  </div>
</template>

<script>
// @ is an alias to /src
import AddDemand from '@/views/suggest/AddDemand.vue'

import editDemandInfo from '@/views/suggest/editDemand.vue'
export default {
  name: 'Demand',
  data () {
    return {
      demandInfo: {
        'description': ''
      },
      DemandData: [],
      DemandStatus: [
        { 'class': 'to-achieve', 'text': '待实现' },
        { 'class': 'Implemented', 'text': '已实现' },
        { 'class': 'Refused', 'text': '已拒绝' }
      ],

      total_page: null,

      queryInfo: {
        search: '',
        pagenum: 1,
        pagesize: 20
      }
    }
  },
  computed: {
  },
  watch: {},
  mounted () {
    this.getDemandList()
  },
  beforeDestroy () {},

  methods: {
    getDemandList () {
      this.$http.get('suggest/demand', { params: this.queryInfo })
        .then(
          res => {
            this.DemandData = res.data.results
            this.total_page = Number(res.data.count)
          })
        .catch(err => {
          this.$message.error(err.data)
        })
    },
    editDemandInfo (DemandInfo) {
      console.log('editDemandInfo ===> ')
      this.$refs.editDemandRef.$emit('EditDemandEvent', DemandInfo)
        // this.$emit('EditDemandInfo', DemandInfo)
    },
    addDemandInfo () {
      this.$refs.addDemandRef.$emit('addDemandEvent')
    },
    removeDemand (DemandID, DemandDescription) {
      this.$confirm('此操作将删除该项目, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      })
        .then(() => {
          this.$http.delete(`suggest/demand/` + DemandID + '/').then(() => {
            this.$message({
              message: `${DemandDescription}  已删除`,
              type: 'success'
            })
            this.queryInfo.pagenum = 1
            this.getDemandList()
          })
        })
    },
    addDemand () {
      this.$http.post('suggest/demand/', this.demandInfo)
        .then(
          res => {
            this.$message.success('新需求已提交')
          })
        .catch(err => {
          this.$message.error(err.data)
        })
    },
    handleCurrentChange (val) {
      this.queryInfo.pagenum = val
      this.getDemandList()
    },
    handleSizeChange (val) {
      this.queryInfo.pagesize = val
      this.getDemandList()
    }

  },
  components: {
    editDemandInfo,
    AddDemand
  }
}
</script>

<style lang="less" scoped>
.demand-description {
    font-weight: 400;
    color: #606266;
}
.demand-status {
  border: 1px solid;
  padding: 1px 2px 1px 2px;
  font-size: 12px;
  &.to-achieve {
    background-color: #ecf5ff;
  }
  &.Implemented {
    background-color: #FFE4B5;
  }
  &.Refused {
    background-color: #f56c6c;
  }
}

.demand-submit {
  // margin: 20px;
  float: right;
}
</style>
