
// 删除文章
export const delArtical = ArticalID => {
      return instance.delete(`/articles/${ArticalID}/`) 
  }

// 获取文章分类信息
export const getArticalType = () => { return instance.get('/article/type/') }

// 获取笔记本信息
export const getNoteInfo = () => { return instance.get(`/notes/`) }

// 添加笔记本
export const addArticleNote = (params) => { return instance.post(`/notes/`, params) }
// 删除笔记本
export const delArticleNote = (ArticalID) => { return instance.delete(`/notes/${ArticalID}/`) }