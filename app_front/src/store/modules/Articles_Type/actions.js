import { getArticalTypeInfo, addArticleType, delArticleType, editArticleType } from '@/api/api.js'
import { Message } from 'element-ui'

const actions = {
    // 添加文章分类
    async addType (context, payload) {
        let res = await addArticleType ( payload )

        if (res.status === 400) {
            Message.error('提交发生错误')
        } else {
            Message.success('添加成功')
            context.dispatch('getAllTypeInfo')
            context.commit('setAddTypeName', '')
            context.commit('closeAddTypeDialog')
        }
    },
    // 删除文章分类
    async delType (context, TypeID) {
        let res = await delArticleType ( TypeID )
        if (res.status === 204) {
            Message.success('删除成功!')
            context.dispatch('getAllTypeInfo')
        } 
    },
    // 编辑文章分类
    async editType (context, payload) {
        let res = await editArticleType ( payload.id, { name: payload.name, parent: payload.parent } )
        if (res.status === 200) {
            Message.success('更新成功!')
            context.dispatch('getAllTypeInfo')
            context.commit('closeEditTypeDialog')
        } else {
            Message.error('更新失败!')
        }
    },
    // 获取所有文章分类信息
    async getAllTypeInfo ( context, searchInfo ) {
        context.commit('setTypes', [])
        let res = await getArticalTypeInfo( { params: searchInfo } )
        if (res.status === 200) {
            context.commit('setTypes', res.data)
        } else {
            Message.error('获取文章失败!')
        }
    }
}

export default actions