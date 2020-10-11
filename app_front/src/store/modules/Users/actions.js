import { getAllUsers, getUserOptions } from '@/api/api.js'

const actions = {
    async getAllUserInfo ( context, searchInfo ) {
        context.commit('setUsers', [])
        let res = await getAllUsers( { params: searchInfo } )
        if ( res.status === 200) {
            context.commit('setUsers', res.data)
        } else {
            this.$message.error('获取用户信息发生错误')
        }
    },
    async getAllUserOptionsInfo ( context, searchInfo ) {
        context.commit('setUserOption', [])
        let res = await getUserOptions( { params: searchInfo } )
        if ( res.status === 200) {
            context.commit('setUserOption', res.data)
        } else {
            this.$message.error('获取用户选项发生错误')
        }
    }
}

export default actions