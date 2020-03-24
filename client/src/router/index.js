import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import Ping from '../components/Ping.vue'
import test from '../components/test.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/', redirect: '/home' },
  { path: '/home', component: Home },
  { path: '/ping', component: Ping },
  { path: '/test', component: test}
]

const router = new VueRouter({
  routes
})

export default router
