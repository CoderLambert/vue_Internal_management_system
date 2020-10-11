<template>
    <el-dialog
      title="编辑文章分类名称"
      :visible.sync="editTypeDialogVisible"
      :before-close="handleClose"
      width="50%"
      center>
        <el-form
            :model="editTypeForm"
            status-icon
            ref="editTypeFormRef"
            :rules="this.editTypeFormRules"
            v-if='editTypeDialogVisible'
            label-width="140px"
        >
            <el-form-item
              prop="name"
              label="分类名称"
            >
              <el-input 
                  :value="editTypeForm.name"
                  @input="changeEditTypeName"
              >
              </el-input>
            </el-form-item>

            <el-form-item
              prop="parent"
              label="父分类名称"
            >

            <el-select clearable filterable @change="changeEditTypeParent" :value="editTypeForm.parent" placeholder="无父分类">
              <el-option
                v-for="item in Types"
                :key="item.id"
                :label="item.name"
                :value="item.id">
              </el-option>
            </el-select>

            </el-form-item>

            <el-form-item>
            <el-button type="success" style="float:right" @click="submitAddForm('editTypeFormRef')">提交</el-button>
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
        editTypeFormRules: {
          name: [
            { required: true, message: '请输入笔记本名称', trigger: 'blur' }
          ],
          parent: [ ]
        }
    }
  },
  methods: {
    changeEditTypeName (TypeName) {
      this.$store.commit('ArticlesType/setEditTypeName', TypeName)
    },
    changeEditTypeParent (ParentType) {
      this.$store.commit('ArticlesType/setEditTypeParent', ParentType)
    },
    handleClose () {
        this.$store.commit('ArticlesType/closeEditTypeDialog')
    },
    submitAddForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.$store.dispatch('ArticlesType/editType', this.editTypeForm)
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
        editTypeForm: state => state.editTypeForm,
        editTypeDialogVisible: state => state.editTypeDialogVisible
      }
    )
  },

 watch: {
    editTypeDialogVisible ( newName, oldName ) {
      this.$store.dispatch('ArticlesType/getAllTypeInfo')
    },
    immediate: true
  } 
}
</script>

<style lang="less" scoped>
</style>