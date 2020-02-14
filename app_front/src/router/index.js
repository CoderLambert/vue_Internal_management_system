import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'

import Index from '../views/Index.vue'
import Home from '../views/Home.vue'

import ImageUpload from '../views/image/Upload.vue'

import UserInfo from '../views/user/UserInfo.vue'
import ImageInfo from '../views/image/ImageInfo.vue'
import ProjectInfo from '../views/project/ProjectInfo.vue'
import MachineInfo from '../views/project/MachineInfo.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/login', component: Login, name: 'login' },
  { path: '/register', component: Register, name: 'register' },

  { path: '/',
    component: Index,
    name: 'Index',
    redirect: '/home',
    children: [
      { path: '/home', component: Home, name: 'Home' },
      { path: '/user/info', component: UserInfo, name: 'UserInfo' },
      { path: '/image/upload', component: ImageUpload, name: 'ImageUpload' },
      { path: '/image/info', component: ImageInfo, name: 'ImageInfo' },
      { path: '/project/info', component: ProjectInfo, name: 'ProjectInfo' },
      { path: '/project/machine/info', component: MachineInfo, name: 'MachineInfo' }

    ]

  }

]

const router = new VueRouter({
  routes
})

// 挂载路由导航
router.beforeEach((to, from, next) => {
// to 将要访问的路径
// from 代表从哪个路径跳转而来
// next是一个函数，代表放行
//  next()代表放行  next('/login') 强制跳转

  if (to.path === '/login' || to.path === '/register') {
    next()
  } else {
    let token = window.sessionStorage.getItem('token')
    if (!token) {
      return next('/login')
    } else {
      next()
    }
  }
})

export default router
