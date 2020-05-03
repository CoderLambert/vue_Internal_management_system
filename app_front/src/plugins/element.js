import Vue from 'vue'
import {
    Button,
    Form,
    FormItem,
    Input,
    Message,
    Select,
    Option,
    OptionGroup,
    Container,
    Header,
    Aside,
    Main,
    Divider,
    Dropdown,
    DropdownMenu,
    DropdownItem,
    Menu,
    Submenu,
    MenuItem,
    MenuItemGroup,
    Badge,
    Breadcrumb,
    BreadcrumbItem,
    Card,
    Upload,
    Table,
    TabPane,
    TableColumn,
    Transfer,
    Loading,
    MessageBox,
    Row,
    Col,
    Pagination,
    Backtop,
    Tag,
    Tooltip,
    // Notification,
    // CascaderPanel,
    // Drawer,
    Dialog,
    Link,
    Carousel,
    CarouselItem,
    Radio,
    RadioGroup,
    RadioButton,
    InputNumber,
    Collapse,
    CollapseItem,
    Tabs,
    // InfiniteScroll,
    DatePicker,
    TimeSelect,
    TimePicker,
    Cascader,
    Tree,
    Progress,
    Checkbox,
    CheckboxButton,
    CheckboxGroup,
    Switch,
    Popconfirm  
} from 'element-ui'

Vue.use(Aside)

Vue.use(Badge)
Vue.use(Backtop)
Vue.use(Button)
Vue.use(Breadcrumb)
Vue.use(BreadcrumbItem)

Vue.use(Card)
// Vue.use(CascaderPanel)
Vue.use(Cascader)
Vue.use(Checkbox)
Vue.use(CheckboxButton)
Vue.use(CheckboxGroup)

Vue.use(Col)
Vue.use(Container)
Vue.use(Carousel)
Vue.use(CarouselItem)
Vue.use(Collapse)
Vue.use(CollapseItem)
    // Vue.use(Drawer)

Vue.use(DatePicker)
Vue.use(Divider)

Vue.use(TimeSelect)
Vue.use(TimePicker)
Vue.use(Dropdown)
Vue.use(DropdownMenu)
Vue.use(DropdownItem)
Vue.use(Dialog)

Vue.use(Form)
Vue.use(FormItem)

Vue.use(Header)

Vue.use(Input)
Vue.use(InputNumber)

Vue.use(Link)

Vue.use(Main)
Vue.use(Menu)
Vue.use(MenuItem)
Vue.use(MenuItemGroup)

// Vue.use(Notification)

Vue.use(Option)
Vue.use(OptionGroup)

Vue.use(Pagination)
Vue.use(Progress)
Vue.use(Popconfirm)

Vue.use(Row)
Vue.use(Radio)
Vue.use(RadioGroup)
Vue.use(RadioButton)

Vue.use(Select)
Vue.use(Submenu)
Vue.use(Switch)

Vue.use(Table)
Vue.use(Tabs)
Vue.use(TabPane)
Vue.use(TableColumn)
Vue.use(Tag)
Vue.use(Tooltip)
Vue.use(Tree)
Vue.use(Transfer)

Vue.use(Upload)
// Vue.use(InfiniteScroll)
// Message 全局组件需要挂载
Vue.prototype.$message = Message
Vue.use(Loading.directive)

Vue.prototype.$loading = Loading.service
Vue.prototype.$msgbox = MessageBox
Vue.prototype.$alert = MessageBox.alert
Vue.prototype.$confirm = MessageBox.confirm
Vue.prototype.$prompt = MessageBox.prompt