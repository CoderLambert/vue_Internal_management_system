import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import '@/assets/css/global.css'
import '@/assets/fonts/iconfont.css'
import instance from '@/axios'
Vue.config.productionTip = false

Vue.prototype.$http = instance

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
