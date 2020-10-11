<template>
    <el-dialog
      title="新增文章分类名称"
      :visible.sync="addTypeDialogVisible"
      :before-close="handleClose"
      width="50%"
      center>
        <el-form
            :model="addTypeForm"
            status-icon
            ref="addTypeFormRef"
            :rules="this.addTypeFormRules"
            v-if='addTypeDialogVisible'
            label-width="140px"
        >
            <el-form-item
              prop="name"
              label="分类名称"
            >
              <el-input 
                  :value="addTypeForm.name"
                  @input="changeAddTypeName"
              >
              </el-input>
            </el-form-item>

            <el-form-item
              prop="parent"
              label="父分类名称"
            >

            <el-select clearable filterable @change="changeAddTypeParent" :value='addTypeForm.parent' placeholder="无父分类">
              <el-option
                v-for="item in Types"
                :key="item.id"
                :label="item.name"
                :value="item.id">
              </el-option>
            </el-select>

            </el-form-item>

            <el-form-item>
            <el-button type="success" style="float:right" @click="submitAddForm('addTypeFormRef')">提交</el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: 'AddArticaleTypeDialog',
  data () {
    return {
        addTypeFormRules: {
          name: [
            { required: true, message: '请输入笔记本名称', trigger: 'blur' }
          ],
          parent: [ ]
        }
    }
  },
  methods: {
    changeAddTypeName (TypeName) {
      this.$store.commit('ArticlesType/setAddTypeName', TypeName)
    },
    changeAddTypeParent (ParentType) {
      this.$store.commit('ArticlesType/setAddTypeParent', ParentType)
    },
    // changeaddTypeFormParent (ev) {
    //   console.log(ev)
    // },
    handleClose () {
        this.$store.commit('ArticlesType/closeAddTypeDialog')
    },
    submitAddForm (formName) {
      this.$refs[formName].validate((valid) => {
        console.log(valid)
        if (valid) {
          this.$store.dispatch('ArticlesType/addType', this.addTypeForm)
        } else {
          console.log('error ')
          return false
        }
      })
    }
  },
  computed: {
    ...mapState(
      'ArticlesType', {
        Types: state => state.Types,
        addTypeForm: state => state.addTypeForm,
        addTypeDialogVisible: state => state.addTypeDialogVisible
      }
  )
  },
 watch: {
    addTypeDialogVisible ( newName, oldName ) {
      console.log(`newName ${newName}  oldname ${oldName}`)
      this.$store.dispatch('ArticlesType/getAllTypeInfo')
    },
    immediate: true
  } 
}
</script>

<style lang="less" scoped>
</style>