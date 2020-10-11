import { getNoteInfo, addArticleNote, delArticleNote, editArticleNote } from '@/api/api.js'
import { Message } from 'element-ui'

const actions = {
    // 添加笔记本
    async addNote (context, payload) {
        let res = await addArticleNote ( payload )
        if (res.status === 201) {
            Message.success('添加成功')
            context.dispatch('getAllNoteInfo')
            context.commit('setAddNoteName', '')
            context.commit('closeAddNoteDialog')
        }
    },
    // 删除笔记本
    async delNote (context, ArticalID) {
        let res = await delArticleNote ( ArticalID )
        if (res.status === 204) {
            Message.success('删除成功!')
            context.dispatch('getAllNoteInfo')
        }        
            // .then ( (res) => {
            //     Message.success('删除成功!')
            //     context.dispatch('getAllNoteInfo')
            // } )
    },
    // 编辑笔记本
    async editNote (context, payload) {
        let res = await editArticleNote ( payload.id, { name: payload.name } )
        if (res.status === 200) {
            Message.success('更新成功!')
            context.dispatch('getAllNoteInfo')
            context.commit('closeEditNoteDialog')
        }  
    },
    // 获取所有笔记本信息
    async getAllNoteInfo ( context, searchInfo ) {
        context.commit('setNotes', [])
        let res = await getNoteInfo( { params: searchInfo } )

        if (res.status === 200) {
            context.commit('setNotes', res.data)
        } else {
            this.$message.error('获取所有笔记本信息发生错误')
        }
    }
}

export default actions