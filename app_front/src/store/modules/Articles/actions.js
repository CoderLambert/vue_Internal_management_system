import { getArticalInfo } from '@/api/api.js'

const actions = {
    // 获取所有笔记本信息
    async  getAllArticles ( context ) {
        context.commit('setArticles', [])
        let res = await getArticalInfo( { params: context.state.quuery_params } )

        if (res.status === 400) {
            this.$message.error('提交发生错误')
        } else {
            context.commit('setArticles', res.data.results)
            context.commit('setTotalCount', res.data.count)
        }
    },

    reset (context, value ) {
        context.commit('QuueryParamsreset', value)
        context.dispatch('getAllArticles')
    }

}

export default actions