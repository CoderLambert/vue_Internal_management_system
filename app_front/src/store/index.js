// 引入vue
import Vue from 'vue'
// 全局引入vueX
import Vuex from 'vuex'
import Articles from './modules/Articles'
import ArticlesNote from './modules/Articles_Note'
import ArticlesType from './modules/Articles_Type'
import User from './modules/Users'
import createLogger from 'vuex/dist/logger'

Vue.use(Vuex)
const debug = process.env.NODE_ENV !== 'production'

const store = new Vuex.Store({
  modules: {
    Articles,
    ArticlesNote,
    ArticlesType,
    User
  },
  plugins: debug ? [createLogger()] : []
})
export default store