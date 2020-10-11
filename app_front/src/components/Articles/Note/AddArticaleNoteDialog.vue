<template>
    <el-dialog
      title="新增笔记本名称"
      :visible.sync="addNoteDialogVisible"
      :before-close="handleClose"
      width="50%"
      center>
        <el-form
            :model="addNoteForm"
            status-icon
            ref="addNoteFormRef"
            :rules="this.addNoteFormRules"
            v-if='addNoteDialogVisible'
            label-width="140px"
        >
            <el-form-item
            prop="name"
            label="笔记本名称"
            >
            <!-- addNoteForm.name -->
            <el-input 
                :value="addNoteForm.name"
                @input="changeAddNoteName"
                @keyup.enter.native="submitAddForm('addNoteFormRef')"
            >
            </el-input>
            </el-form-item>
            <el-form-item>
            <el-button type="success" style="float:right" @click="submitAddForm('addNoteFormRef')">提交</el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: 'AddArticaleNoteDialog',
  data () {
    return {
        addNoteFormRules: {
          name: [
            { required: true, message: '请输入笔记本名称', trigger: 'blur' }
          ]
        }
    }
  },
  methods: {
    changeAddNoteName (NoteName) {
      this.$store.commit('ArticlesNote/setAddNoteName', NoteName)
    },
    handleClose () {
        this.$store.commit('ArticlesNote/closeAddNoteDialog')
    },
    submitAddForm (formName) {
      this.$refs[formName].validate((valid) => {
        console.log(valid)
        if (valid) {
          this.$store.dispatch('ArticlesNote/addNote', this.addNoteForm)
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
        addNoteDialogVisible: state => state.addNoteDialogVisible,
        addNoteForm: state => state.addNoteForm
      }
    )
  },
 watch: {
    addNoteDialogVisible ( newName, oldName ) {
      this.$store.dispatch('ArticlesType/getAllTypeInfo')
    },
    immediate: true
  } 
}
</script>

<style lang="less" scoped>
</style>