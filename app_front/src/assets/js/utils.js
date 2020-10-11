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

var sortByKey = function (arr, key) {
  let map = {}
  let dest = []
  for (let i = 0; i < arr.length; i++){
      let ai = arr[i]
      if ( !map[ai[key]] ) {
          dest.push({
              [key]: ai[key],
              data: [ai]
          })
          map[ai[key]] = ai
      } else {
          for (let j = 0; j < dest.length; j++){
              let dj = dest[j]
              if ( dj[key] === ai[key] ){
                  dj.data.push(ai)
                  break
              }
          }
      }
  }
  return dest
}

var treeShip = function ( dataList ) {
  var msg_list_dict = {}
  dataList.forEach( item => {
      msg_list_dict[item['id']] = item
  })

  var result = []
  dataList.forEach ( (item) => {
      var pid = item['parent']
      if (pid) {
          if (!msg_list_dict[pid].hasOwnProperty('children')) {
            msg_list_dict[pid]['children'] = []
          }
          msg_list_dict[pid]['children'].push(item)
      } else {
          result.push(item)
      }
  })
  return result
}

export { SS, sortByKey, treeShip }
