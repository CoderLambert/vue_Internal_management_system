import axios from 'axios'
import SS from '@/assets/js/utils.js'
// import { Message } from 'element-ui'
// axios.defaults.baseURL = 'https://www.liulongbin.top:8888/api/private/v1/'

// axios.defaults.baseURL = 'http://127.0.0.1:9200/api/'
const baseURL = 'http://127.0.0.1:9200/api/'
const instance = axios.create({
  baseURL,
  timeout: 30000
})

// 发送请求不允许携带 cookie
instance.defaults.withCredentials = false

// 请求拦截
instance.interceptors.request.use(
  config => {
    if (sessionStorage.getItem('token')) {
      // 判断是否存在token，如果存在的话，则每个http header都加上token
      config.headers.Authorization = `JWT ${sessionStorage.getItem('token')}`
    }
    return config
  },
  err => {
    return Promise.reject(err)
  }
)

// http response 拦截器
instance.interceptors.response.use(undefined, error => {
  let res = error.response
  switch (res.status) {
    case 400:
      SS.clearAll()
      console.log('登录失败，请检查密码或用户名是否正确')
      break
    case 401:
      console.log('401')
      break
    case 403:
      console.log('您没有该操作权限')
      break
    case 500:
      console.log('服务器错误')
      break
    default:
      alert('未知错误' + res.status)
  }
  console.log(res)
  return Promise.reject(error.response) // 返回接口返回的错误信息
})

export default instance
