<template>
    <el-dialog
      title="修改笔记本名称"
      :visible.sync="editNoteDialogVisible"
      :before-close="handleClose"
      width="50%"
      center>
        <el-form
            :model="editNoteForm"
            status-icon
            ref="editNoteFormRef"
            :rules="this.editNoteFormRules"
            v-if='editNoteDialogVisible'
            label-width="140px"
        >
            <el-form-item
            prop="name"
            label="笔记本名称"
            >
            <el-input 
                :value="editNoteForm.name"
                @input="changeEditNoteName"
                @keyup.enter.native="submitEditForm('editNoteFormRef')"
            >
            </el-input>
            </el-form-item>
            <el-form-item>
            <el-button type="success" style="float:right" @click="submitEditForm('editNoteFormRef')">提交</el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: 'EditArticaleNoteDialog',
  data () {
    return {
        editNoteFormRules: {
          name: [
            { required: true, message: '请输入笔记本名称', trigger: 'blur' }
          ],
          id: [
            { required: true, message: '请给出笔记本ID', trigger: 'blur' }
          ]
        }
    }
  },
  methods: {
    changeEditNoteName (NoteName) {
      this.$store.commit('ArticlesNote/setEditNoteName', NoteName)
    },
    handleClose () {
        this.$store.commit('ArticlesNote/closeEditNoteDialog')
    },
    submitEditForm (formName) {
      this.$refs[formName].validate((valid) => {
        console.log(valid)
        if (valid) {
          this.$store.dispatch('ArticlesNote/editNote', this.editNoteForm)
        } else {
          console.log('error ')
          return false
        }
      })
    }
  },
  computed: {
    ...mapState(
      'ArticlesNote', {
        editNoteDialogVisible: state => state.editNoteDialogVisible,
        editNoteForm: state => state.editNoteForm
      }
  )
  }
}
</script>

<style lang="less" scoped>
</style>