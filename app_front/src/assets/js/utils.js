// 设置sessiStorage
var SS = {
  setUserInfo (res) {
    sessionStorage.setItem('token', res.token)
    sessionStorage.setItem('userid', res.user_id)
    sessionStorage.setItem('username', res.username)
  },

  clearUserInfo (res) {
    sessionStorage.removeItem('token')
    sessionStorage.removeItem('userid')
    sessionStorage.removeItem('username')
  },

  clearAll () {
    sessionStorage.clear()
  }
}

export default SS
