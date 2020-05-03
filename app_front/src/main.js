import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import '@/assets/css/global.css'
import '@/assets/fonts/iconfont.css'
import instance from '@/axios'

import VueBus from 'vue-bus'
import moment from 'moment'
import marked from 'marked'

import _ from 'lodash'
import VueClipboard from 'vue-clipboard2'
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import animated from 'animate.css' // npm install animate.css --save安装，再引入
import store from '@/store'

// use
Vue.use(mavonEditor)
Vue.use(VueClipboard)
Vue.use(VueBus)
Vue.use(animated)

Vue.config.productionTip = false

Vue.prototype.$http = instance
Vue.prototype._ = _
Vue.prototype.$ServerAddr = '127.0.0.1:9200'

// 注册一个全局自定义指令 `v-focus`
Vue.directive('focus', {
  // 当被绑定的元素插入到 DOM 中时……
  inserted: function (el) {
    // 聚焦元素
    el.focus()
  }
})

Vue.filter('UTCDateFormat', function ( dataStr, pattern = 'YYYY-MM-DD HH:mm:ss' ) {
  var nowTime = new Date()
  var offset = nowTime.getTimezoneOffset() / 60
  return moment(dataStr).utcOffset(offset).format(pattern)
})

Vue.filter('Marked', function ( MD_Text ) {
  return marked(MD_Text)
})

Vue.filter('ArticalDetailFormat', function ( artical_id ) {
  return `/article/${artical_id}`
})
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
