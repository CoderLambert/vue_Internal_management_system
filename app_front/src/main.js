import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import '@/assets/css/global.css'
import * as utils from '@/assets/js/utils.js'

import instance from '@/axios'

import VueBus from 'vue-bus'

import _ from 'lodash'
import VueClipboard from 'vue-clipboard2'
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import animated from 'animate.css' // npm install animate.css --save安装，再引入
import store from '@/store'
import './filters'
// use
Vue.use(mavonEditor)
Vue.use(VueClipboard)
Vue.use(VueBus)
Vue.use(animated)

Vue.config.productionTip = false

Vue.prototype.$http = instance
Vue.prototype._ = _
Vue.prototype.$ServerAddr = '127.0.0.1:9200'
Vue.prototype.$utils = utils
// 注册一个全局自定义指令 `v-focus`
Vue.directive('focus', {
  inserted: function (el) {
    el.focus()
  }
})

// Vue.filter('UTCDateFormat', function ( dataStr, pattern = 'YYYY-MM-DD HH:mm:ss' ) {
//   return moment.parseZone(dataStr).local().format(pattern)
// })

// Vue.filter('ArticalDetailFormat', function ( artical_id ) {
//   return `/article/${artical_id}`
// })
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
