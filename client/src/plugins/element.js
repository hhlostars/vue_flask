import Vue from 'vue'
import {
    Button, Container, Header, Main, Table, TableColumn, Dialog, Switch, Input, Form,
    FormItem, Message, MessageBox, Checkbox
} from 'element-ui'

Vue.use(Button)
Vue.use(Container)
Vue.use(Header)
Vue.use(Main)
Vue.use(Table)
Vue.use(TableColumn)
Vue.use(Dialog)
Vue.use(Switch)
Vue.use(Input)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Checkbox)

// 需要全局挂载
Vue.prototype.$message = Message
Vue.prototype.$confirm = MessageBox.confirm
