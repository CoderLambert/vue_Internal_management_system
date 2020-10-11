import Vue from 'vue'
import VueRouter from 'vue-router'

import Login from '../views/Login.vue'
import Register from '../views/Register.vue'

import Index from '../views/Index.vue'
// import Home from '../views/Home.vue'

import ImageUpload from '../views/image/Upload.vue'

import ImageInfo from '../views/image/ImageInfo.vue'

import ProjectInfo from '../views/project/ProjectInfo.vue'
import MachineInfo from '../views/project/MachineInfo.vue'

import Articles from '../views/articale/Articals.vue'
import ArticalDetail from '../views/articale/ArticalDetail.vue'
import AddMarkdown from '../views/articale/AddMarkdown.vue'
import EditMarkdown from '../views/articale/EditMarkdown.vue'

import ArticaleNotes from '../views/articale/Notes.vue'
import ArticaleTypes from '../views/articale/Types.vue'

import WebSite from '../views/navigation/WebSite.vue'
import WebSideType from '../views/navigation/WebSideType.vue'

import Demand from '../views/suggest/DemandList.vue'
import AddDemand from '../views/suggest/AddDemand.vue'

// import NotFound from '../views/404.vue'
Vue.use(VueRouter)

const routes = [

  { path: '/login', component: Login, name: 'login' },
  { path: '/register', component: Register, name: 'register' },

  { path: '/',
    component: Index,
    name: 'Index',
    redirect: '/home',
    children: [
      // { path: '/home', component: () => import('../views/Home.vue'), name: 'Home' },
      // { path: '/user/info', component: () => import('../views/image/Upload.vue'), name: 'UserInfo' },
      // { path: '/image/upload', component: () => import('../views/image/Upload.vue'), name: 'ImageUpload' },
      // { path: '/image/info', component: () => import('../views/image/ImageInfo.vue'), name: 'ImageInfo' },
      // { path: '/project/info', component: () => import('../views/project/ProjectInfo.vue'), name: 'ProjectInfo' },
      // { path: '/project/machine/info', component: () => import('../views/project/MachineInfo.vue'), name: 'MachineInfo' },
      // { path: '/article/add/markdown', component: () => import('../views/articale/AddMarkdown.vue'), name: 'AddMarkdown' },
      // { path: '/navigation/webside', component: () => import('../views/navigation/WebSite.vue'), name: 'WebSite' },
      // { path: '/navigation/webtype', component: () => import('../views/navigation/WebSideType.vue'), name: 'WebSiteType' },
      // { path: '/navigation/resource', component: () => import('../views/navigation/CloundResource.vue'), name: 'CloundResource' }
      // { path: '/navigation/resource', component: () => import('@/components/draggable.vue'), name: 'CloundResource' }

      // { path: '/home', component: Home, name: 'Home' },
      // { path: '/user/info', component: ImageUpload, name: 'UserInfo' },
      { path: '/image/upload', component: ImageUpload, name: 'ImageUpload', meta: { requiresAuth: true } },
      { path: '/image/info', component: ImageInfo, name: 'ImageInfo', meta: { requiresAuth: true } },
      { path: '/project/info', component: ProjectInfo, name: 'ProjectInfo', meta: { requiresAuth: true } },
      { path: '/project/machine/info', component: MachineInfo, name: 'MachineInfo', meta: { requiresAuth: true } },
      // meta: { keepAlive: true } 
      { path: '/articles/', component: Articles, name: 'Articles', meta: { requiresAuth: false } },
      { path: '/article/:artical_id', component: ArticalDetail, name: 'ArticalDetail', meta: { requiresAuth: false } },
      { path: '/article/add/markdown', component: AddMarkdown, name: 'AddMarkdown', meta: { requiresAuth: true } },
      { path: '/article/edit/markdown/:artical_id', component: EditMarkdown, name: 'EditMarkdown', meta: { requiresAuth: true } },
      { path: '/articles/notes', component: ArticaleNotes, name: 'ArticaleNotes', meta: { requiresAuth: true } },
      { path: '/articles/types', component: ArticaleTypes, name: 'ArticaleTypes', meta: { requiresAuth: true } },
      { path: '/navigation/webside', component: WebSite, name: 'WebSite', meta: { requiresAuth: false } },
      { path: '/navigation/webtype', component: WebSideType, name: 'WebSiteType', meta: { requiresAuth: false } },
      { path: '/suggest/demand', component: Demand, name: 'Demand', meta: { requiresAuth: false } },
      { path: '/suggest/demand/add', component: AddDemand, name: 'AddDemand', meta: { requiresAuth: false } },
      { path: '*', redirect: '/articles/' }
      
    ]

  }

]

const router = new VueRouter({
  // mode: 'history',
  routes
})

// 挂载路由导航
router.beforeEach((to, from, next) => {
// to 将要访问的路径
// from 代表从哪个路径跳转而来
// next是一个函数，代表放行
//  next()代表放行  next('/login') 强制跳转
// console.log('start')
// console.log(new Date())

  if (to.path === '/login' || to.path === '/register') {
    next()
  } else {
    if (to.matched.some(record => record.meta.requiresAuth)) {
      let token = window.sessionStorage.getItem('token')
      if (!token) {
        return next('/login')
      } else {
        next()
      }
    } else {
      next()
    }
  }
  // console.log('--ebd----')
  // console.log(new Date())
})

export default router
