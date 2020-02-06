import Vue from 'vue'
import { Button, Form, FormItem, Input, Message, Select,
  Option,
  OptionGroup } from 'element-ui'

Vue.use(Button)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Input)
Vue.use(Select)
Vue.use(Option)
Vue.use(OptionGroup)
// Message 全局组件需要挂载
Vue.prototype.$message = Message
