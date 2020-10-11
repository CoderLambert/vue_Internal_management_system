<template>
  <div>
    <!-- <label class="mail-title">邮件通知</label> -->
          <!-- @change="changeMailEnable" -->

    <el-radio-group 
      v-model="mailEnable"
      @change="changeMailEnable"
      size="mini">
        <el-radio-button  :label="true" >开启</el-radio-button>
        <el-radio-button  :label="false" >关闭</el-radio-button>
    </el-radio-group>

    <div class="mail-info" v-show="mailEnable == true"
> 
        <span class="mail-target">邮箱地址:</span>
        <el-tag 
          type="info" 
          size="mini"
          v-for="(email,index) in targetMailAddr" 
          v-bind:key="index"
        >
          {{email}}
        </el-tag>
        <el-transfer 
            class="mail-user-list" 
            v-model="targetMailAddr" 
            filterable
            :data="targetEmailAddr"
            :titles="['用户列表', '收件人列表']"
            :button-texts="['移除', '添加']"
        >
        
          <section class="transfer-footer" slot="left-footer">
            <!-- <el-button type="primary" plain size="small" @click="addAdminGroup">
              管理员
            </el-button>
            <el-button type="primary" plain  size="small" @click="addBMCGroup">
              BMC 
            </el-button>
            <el-button type="primary" plain  size="small" @click="addBIOSGroup">
              BIOS 
            </el-button> -->

            <el-checkbox-group v-model="checkGroupList" size="mini">
              <el-checkbox-button label="1">管理员</el-checkbox-button>
              <el-checkbox-button label="2">BMC</el-checkbox-button>
              <el-checkbox-button label="3">BIOS</el-checkbox-button>
            </el-checkbox-group>
          </section>

          <!-- <section  slot="right-footer">
            <el-button type="warning" plain size="small" @click="addAdminGroup">
              管理员
            </el-button>
            <el-button type="warning" plain  size="small" @click="addBMCGroup">
              BMC 
            </el-button>
            <el-button type="warning" plain  size="small" @click="addBIOSGroup">
              BIOS 
            </el-button>
          </section> -->
        </el-transfer>

    </div>

    <!-- <el-dialog
      title=" 添加收件人地址"
      :visible.sync="addMailDialogVisible"
      width="1000px"
      center>

    </el-dialog> -->
  </div>
  
</template>
<script>
// getRoleInfo
// getDepartmentInfo
import { getUserEmail } from '@/api/api'

export default {
  name: 'ImageUploadMail',
//   props: ['ArticaleTypeList'],
  data () {
    return {
      mailEnable: true,
      targetMailAddr: [],
      EmialInfo: [],
      addMailDialogVisible: this.mailEnable,
      checkGroupList: [],
      RoleInfo: [],
      DepartmentInfo: []
    }
  },
  mounted () {
    this.mountedInit()
  },

  methods: {
    changeMailEnable (targetMailAddr) {
      this.addMailDialogVisible = targetMailAddr
      console.log(this.addMailDialogVisible)
    },
    mountedInit () {
      getUserEmail()
        .then ( (res) => {
          this.EmialInfo = res.data
          // console.log(this.EmialInfo)
        })
      // getDepartmentInfo()
      //   .then ( (res) => {
      //     this.DepartmentInfo = res.data
      //   } )
      // getRoleInfo()
      //   .then ( (res) => {
      //     this.RoleInfo = res.data
      //   })
    }
  },
  computed: {
    targetEmailAddr: function () {
      if (!this.mailEnable){
        return []
      } else {
        const data = []
        this.EmialInfo.forEach( element => {
          data.push({
            key: element.email,
            label: element.username + '\xa0\xa0\xa0' + '(' + element.email + ')'
          })
        })
        return data
      }
    }
  },
  watch: {}
  
}
</script>

<style lang="less" scope>
.mail-title {
    // font-weight: bold;
    margin-right : 20px ;
    // font-size: 32px;
}

// .mail-user-box {
//     // width:800px;
// }
.mail-user-list {
    // margin-top: 20px;
    .el-transfer-panel {
        width: 350px;
        // min-height: 400px;
    }
    .el-transfer-panel__filter {
            width: 250px;
    }
}
  .mail-info {
    // border: 1px solid #eee;
    margin-top: 5px;
    .mail-target {
      font-size: 18px;
      // font-weight: bold;
    }
    .el-tag {
      margin: 0 10px;
    }
  }
</style>
