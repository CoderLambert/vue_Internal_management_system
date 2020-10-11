import instance from '@/axios'

// 获取用户选项
export const getUserOptions = () => { return instance.get('users/?type=options') }
export const getAllUsers = () => { return instance.get('users/') }

// 获取用户邮箱信息
export const getUserEmail = () => { return instance.get(`/users/?type=email`) }

// 获取部门信息
export const getDepartmentInfo = () => { return instance.get(`/departments/`) }

// 获取用户角色信息
export const getRoleInfo = () => { return instance.get(`/roles/`) }

// =======================================================================
//
//                       文章
//
// =======================================================================

// 获取文章列表
export const getArticalInfo = params => {
    // 获取文章详情
    if ( 'id' in params ) {
        // return axios.get(`${host}/categorys/`+params.id+'/');
        return instance.get(`/articles/${params.id}/`) 
      } else {
        // 获取所有文章
        return instance.get(`/articles/`, params) 
      }    
    }
// 删除文章
export const delArtical = ArticalID => {
      return instance.delete(`/articles/${ArticalID}/`) 
  }

// =======================================================================
//
//                       笔记本 
//
// =======================================================================
// 获取笔记本信息
export const getNoteInfo = params => { return instance.get(`/notes/`, params) }
// 添加笔记本
export const addArticleNote = (params) => { return instance.post(`/notes/`, params) }
// 删除笔记本
export const delArticleNote = (ArticalID) => { return instance.delete(`/notes/${ArticalID}/`) }
// 编辑笔记本
export const editArticleNote = ( ArticalID, params ) => { return instance.put(`/notes/${ArticalID}/`, params) }
// =======================================================================
//
//                       分类 
//
// =======================================================================

// 获取文章分类信息
export const getArticalTypeInfo = params => { return instance.get('/article/types/', params) }
// 添加笔记本
export const addArticleType = (params) => { return instance.post(`/article/types/`, params) }
// 删除笔记本
export const delArticleType = (ArticalID) => { return instance.delete(`/article/types/${ArticalID}/`) }
// 编辑笔记本
export const editArticleType = ( ArticalID, params ) => { return instance.put(`/article/types/${ArticalID}/`, params) }