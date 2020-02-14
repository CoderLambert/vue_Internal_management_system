import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import '@/assets/css/global.css'
import '@/assets/fonts/iconfont.css'
import instance from '@/axios'
import VueBus from 'vue-bus'
import VueClipboard from 'vue-clipboard2'

Vue.use(VueClipboard)
Vue.config.productionTip = false

Vue.prototype.$http = instance
Vue.use(VueBus)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
