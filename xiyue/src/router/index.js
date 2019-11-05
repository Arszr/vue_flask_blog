/*
 * @Description: In User Settings Edit
 * @Author: your name
 * @Date: 2019-09-27 11:35:59
 * @LastEditTime: 2019-10-03 15:31:01
 * @LastEditors: Please set LastEditors
 */
import Vue from 'vue'
import Router from 'vue-router'
import Home from '../pages/Home.vue'
import AboutMe from '../pages/AboutMe.vue'
Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
      meta: {
        auth:true
      } //首页
    },
    {
      path: '/Home',
      redirect: {
        name: 'Home'
      },
      component: Home,
      meta: {
        auth:true
      } //首页
    },
    {
      path: '/AboutMe',
      name: 'AboutMe',
      component: AboutMe,
      meta: {
        auth:true
      } //关于我
    },
    {
      path: '/Login',
      name: 'Login',
			component: resolve => require(['../pages/Login.vue'], resolve),
			meta: {
				auth: true
			}
    }, //登录
    {
      path: '/Share',
      name: 'Share',
			component: resolve => require(['../pages/Share.vue'], resolve),
			meta: {
				auth: true
			}
			
    }, //文章列表
    {
      path: '/ShareDetail',
      name: 'ShareDetail',
			component: resolve => require(['../pages/ShareDetail.vue'], resolve),
			meta: {
				auth: true
			},
			
    }, //文章详情
    {
      path: '/flask',
      name: 'flask',
			component: resolve => require(['../pages/flaskToVue.vue'], resolve),
			meta: {
				auth: true
			},
			
		}, //文章详情
  ]
})
