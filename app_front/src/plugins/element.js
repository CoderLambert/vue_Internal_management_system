import Vue from 'vue'
import { Button, Form, FormItem, Input, Message, Select,
  Option,
  OptionGroup,
  Container,
  Header,
  Aside,
  Main,
  Dropdown,
  DropdownMenu,
  DropdownItem,
  Menu,
  Submenu,
  MenuItem,
  MenuItemGroup,
  Breadcrumb,
  BreadcrumbItem,
  Card,
  Upload,
  Table,
  TableColumn,
  Loading,
  MessageBox,
  Row,
  Col,
  Pagination,
  Backtop,
  Tag,
  Tooltip,
  // Notification,
  CascaderPanel,
  // Drawer,
  Dialog,
  Link
} from 'element-ui'

Vue.use(Aside)

Vue.use(Backtop)
Vue.use(Button)
Vue.use(Breadcrumb)
Vue.use(BreadcrumbItem)

Vue.use(Card)
Vue.use(CascaderPanel)

Vue.use(Col)
Vue.use(Container)

// Vue.use(Drawer)
Vue.use(Dropdown)
Vue.use(DropdownMenu)
Vue.use(DropdownItem)
Vue.use(Dialog)

Vue.use(Form)
Vue.use(FormItem)

Vue.use(Header)

Vue.use(Input)

Vue.use(Link)

Vue.use(Main)
Vue.use(Menu)
Vue.use(MenuItem)
Vue.use(MenuItemGroup)

// Vue.use(Notification)

Vue.use(Option)
Vue.use(OptionGroup)

Vue.use(Pagination)

Vue.use(Row)

Vue.use(Select)
Vue.use(Submenu)

Vue.use(Table)
Vue.use(TableColumn)
Vue.use(Tag)
Vue.use(Tooltip)

Vue.use(Upload)
// Message 全局组件需要挂载
Vue.prototype.$message = Message
Vue.use(Loading.directive)

Vue.prototype.$loading = Loading.service
Vue.prototype.$msgbox = MessageBox
Vue.prototype.$alert = MessageBox.alert
Vue.prototype.$confirm = MessageBox.confirm
Vue.prototype.$prompt = MessageBox.prompt
// Vue.prototype.$notify = Notification
