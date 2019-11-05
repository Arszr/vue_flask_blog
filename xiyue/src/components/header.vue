<!--
 * @Description: In User Settings Edit
 * @Author: your name
 * @Date: 2019-09-30 13:20:29
 * @LastEditTime: 2019-10-08 15:05:00
 * @LastEditors: Please set LastEditors
 -->
<!-- 头部公用 -->
<template>
  <div class="">
		<nav class="head-back">
			<el-row class="container">
  			<el-col :span="24">
					<!-- pc端导航 -->
					<div class="header-nav">
							<el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal"  @select="handleSelect"  :router="true">
  							<el-menu-item index="/Home">首页</el-menu-item>
								<el-menu-item index="/Share">生活</el-menu-item>
								<el-menu-item index="/Home">学习</el-menu-item>
								<el-menu-item index="/AboutMe">关于我</el-menu-item>
  						
							<div class="pcsearchinput" :class="input?'hasSearched':''">
								<el-input id="search-input" placeholder="输入查找内容" icon="search" v-model="input" >
								</el-input>
								<i class="el-icon-search pcsearchicon"></i>
							</div>
						<div class="userInfo">
							<div v-show="!haslogin" class="nologin">
								<a href="javascript:void(0);" @click="logoinFun(1)">登录&nbsp;</a>|
								<a href="javascript:void(0);" @click="logoinFun(0)">&nbsp;注册</a>
							</div>
							<div v-show="haslogin" class="haslogin">
								<i class="fa fa-fw fa-user-circle userImg"></i>
								<ul class="haslogin-info">
									<li>
										<a href="#/UserInfo">个人中心</a>
									</li>
									<li>
										<a href="javascript:void(0);" @click="userlogout">退出登录</a>
									</li>
								</ul>
							</div>
						</div>
					</el-menu>
					</div>
					<!-- 移动端导航 -->
				<div class="mobileBox">
					<div class="hideMenu">
						<i @click="pMenu=!pMenu" class="el-icon-menu"></i>
						<el-collapse-transition>
							<el-menu :default-active="activeIndex" class="mlistmenu" v-show="!pMenu" theme="dark" @open="handleOpen" @close="handleClose" :unique-opened="true" :router="true">
								<el-menu-item index="/Home">首页</el-menu-item>
								<el-menu-item index="/Share">生活</el-menu-item>
								<el-menu-item index="/Home">学习</el-menu-item>
								<el-menu-item index="/AboutMe">关于我</el-menu-item>
								
								<el-menu-item v-show="!haslogin" index="" @click="logoinFun(1)">登录</el-menu-item>
								<el-menu-item v-show="!haslogin" index="" @click="logoinFun(0)">注册</el-menu-item>
								<el-submenu v-show="haslogin" index="3">
									<template slot="title"><i class="fa fa-wa fa-user-circle-o"></i> 我的</template>
									<el-menu-item index="/UserInfo">个人中心</el-menu-item>
									<el-menu-item index="" @click="userlogout">退出登录</el-menu-item>
								</el-submenu>
							</el-menu>
						</el-collapse-transition>
						<div class="searchBox">
							<el-input placeholder="输入查找内容" icon="search" v-model="input" @keyup.enter.native="searchEnterFun" :on-icon-click="searchEnterFun">
							</el-input>
								
						</div>
					</div>
				</div>
				</el-col>
			</el-row>

		</nav>
		<div class="headImgBox" :style="{backgroundImage:'url('+require('../../static/img/bg.jpg')+')'}">
			
			<div id="user-logo">
				<a href="/Aboutme">
          <img :src="require('../../static/img/tou.jpg')" alt="">
        </a>
			</div>
			
			<div class="information">
				<span id="text-tion">别放弃啊少年</span>
			</div>
		</div>
  </div>
</template>

<script>
import {
	ArtClassData,
	LoginOut,
	navMenList,
	changeTheme,
	AboutMeData
} from '../utils/server.js'
// import {
// 	Typeit
// } from '../utils/plug.js'
export default {
	data() { //选项 / 数据
		return {
			userInfo: '', //用户信息
			haslogin: false, //是否已登录
			activeIndex: '/', //当前选择的路由模块
			state: '', //icon点击状态
			pMenu: true, //手机端菜单打开
			// path:'',//当前打开页面的路径
			input: '', //input输入内容
		}
	},
	watch: {

	},
	methods: { //事件处理器
		handleOpen(key, keyPath) { //分组菜单打开
			// console.log(key, keyPath);
		},
		handleClose(key, keyPath) { //分组菜单关闭
			// console.log(key, keyPath);
		},
		searchChangeFun(e) { //input change 事件
			// console.log(e)
			if (this.input == '') {
				this.$store.state.keywords = 'keyword';
				this.$router.push({path:'/'});
			}
		},
		searchEnterFun: function(e) { //input 输入 enter
			 var keyCode = window.event? e.keyCode:e.which;
			// console.log('CLICK', this.input, keyCode)
            //  console.log('回车搜索',keyCode,e);
             if(this.input){
				 					this.$store.state.keywords = this.input;
                 	this.$router.push({path:'/Share?keywords='+this.input});
             }
		},
		handleSelect(key, keyPath) { //pc菜单选择
			//    console.log(key, keyPath);
		},
		logoinFun: function(msg) { //用户登录和注册跳转
			// console.log(msg);
			localStorage.setItem('logUrl', this.$route.fullPath);
			// console.log(666,this.$router.currentRoute.fullPath);
			if (msg == 0) {
				this.$router.push({
					path: '/Login?login=0'
				});
			} else {
				this.$router.push({
					path: '/Login?login=1'
				});
			}
		},
		// 用户退出登录
		userlogout: function() {
			var that = this;
			this.$confirm('是否确认退出?', '退出提示', {
				confirmButtonText: '确定',
				cancelButtonText: '取消',
				type: 'warning'
			}).then(() => {
				// console.log(that.$route.path);
				
				if (localStorage.getItem('userInfo')) {
					localStorage.removeItem('userInfo');
					localStorage.removeItem('accessToken')
					that.haslogin = false;
					//    that.$router.replace({path:that.$route.fullPath});
					window.location.reload();
					that.$message({
						type: 'success',
						message: '退出成功!'
					});
				}
				if (that.$route.path == '/UserInfo') {
					that.$router.push({
						path: '/'
					});
				}
			})
			

		},
		
		routeChange: function() {
			var that = this;
			that.pMenu = true
			this.activeIndex = this.$route.path == '/' ? '/Home' : this.$route.path;
			if (localStorage.getItem('userInfo')) { //存储用户信息
				that.haslogin = true;
				that.userInfo = JSON.parse(localStorage.getItem('userInfo'));
				// console.log(that.userInfo);
			} else {
				that.haslogin = false;
			}
			// ArtClassData(function(msg) { //文章分类
			// 	// console.log(msg);
			// 	that.classListObj = msg;
			// })
			// navMenList(function(msg) { //实验室项目列表获取
			// 	// console.log('实验室',msg);
			// 	that.projectList = msg;
			// });
			if ((this.$route.name == "Share" || this.$route.name == "Home") && this.$store.state.keywords) {
				this.input = this.$store.state.keywords;
			} else {
				this.input = '';
				this.$store.state.keywords = '';
			}
		}
	},
	components: { //定义组件

	},
	watch: {
		// 如果路由有变化，会再次执行该方法
		'$route': 'routeChange'
	},
	created() { //生命周期函数
		//判断当前页面是否被隐藏
		var that = this;
		var hiddenProperty = 'hidden' in document ? 'hidden' :
			'webkitHidden' in document ? 'webkitHidden' :
			'mozHidden' in document ? 'mozHidden' :
			null;
		var visibilityChangeEvent = hiddenProperty.replace(/hidden/i, 'visibilitychange');
		var onVisibilityChange = function() {
			if (document[hiddenProperty]) { //被隐藏
				document.title = '藏好啦(つд⊂)';
			} else {
				document.title = '被发现啦(*´∇｀*)'; //当前窗口打开
				if (that.$route.path != '/DetailShare') {
					if (localStorage.getItem('userInfo')) {
						that.haslogin = true;
					} else {
						that.haslogin = false;
					}
				}
			}
		}
		document.addEventListener(visibilityChangeEvent, onVisibilityChange);
		// console.log();
		this.routeChange();
		
		
	},
	
}
</script>


// 头部样式
<style>

/*头部导航栏盒子*/

.head-back {
	width: 100%;
	/* background: -webkit-linear-gradient(top,  #3ae8ff9f 0%,#ffffff00 100%); */
	background: #00a7e0;
	/*margin-bottom:30px;*/
	box-shadow: 0 2px 4px 0 rgba(0, 0, 0, .12), 0 0 6px 0 rgba(0, 0, 0, .04);
	position: fixed;
	left: 0;
	top: 0;
	right: 0;
	z-index: 100;
}

.header-nav li.is-active {
	/*background: #48456C;*/
	background: rgba(93, 209, 255, 0.555);
}

.el-menu--horizontal>.el-submenu.is-active .el-submenu__title {
	border-bottom: none!important;
}

.header-nav .el-menu {
	background: transparent;
	border-bottom: none!important;
}

.header-nav .el-menu-demo li.el-menu-item,
.header-nav .el-menu--horizontal .el-submenu .el-submenu__title {
	height: 38px;
	line-height: 38px;
	border-bottom: none!important;

}

.header-nav .el-submenu li.el-menu-item {
	height: 38px;
	line-height: 38px;
}

.header-nav li .fa-wa {
	vertical-align: baseline;
}

.header-nav ul li.el-menu-item,
.header-nav ul li.el-menu-item.is-active,
.header-nav ul li.el-menu-item:hover,
.header-nav .el-submenu div.el-submenu__title,
.header-nav .el-submenu__title i.el-submenu__icon-arrow {
	color: #fff;
}

.header-nav .el-menu--horizontal .el-submenu>.el-menu {
	top: 38px;
	border: none;
	padding: 0;
}



.header-nav>ul .el-submenu .el-menu .el-menu-item {
	min-width: 0;
}

.header-nav>ul .el-submenu .el-menu .el-menu-item:hover {
	background: rgb(248, 248, 248);
}

/*pc搜索框*/

.header-nav .pcsearchinput {
	padding: 0;
	max-width: 170px;
	/*min-width: 30px;*/
	position: absolute;
	top: 0;
	right: 170px;
	height: 100%;
	line-height: 38px;
	cursor: pointer;
}

.header-nav .pcsearchinput i.pcsearchicon {
	color: rgb(255, 255, 255);
	padding-left: 10px;
	position: absolute;
	top: 12px;
	right: 4px;
}

.header-nav .pcsearchinput .el-input {
	width: 100%;
}

.header-nav .el-input__inner {
	height: 30px;
	border: none;
	background: rgba(255, 255, 255, 0);
	/*border: 1px solid #333;*/
	/* border-radius: 20px; */
	/* padding-right: 4px; */
	padding: 0;
	padding-left: 4px;
	color: #ffffff;
	border-bottom: 1px solid #fff;
	
}
#search-input::placeholder{
  color:rgb(255, 255, 255);

}

.header-nav .userInfo {
	height: 100%;
	line-height: 38px;
	position: absolute;
	right: 30px;
	top: 0;
	color: #fff;
}

.header-nav .userInfo a {
	color: #fff;
	font-size: 13px;
	transition: all 0.2s ease-out;
}

.header-nav .userInfo a:hover {
	color: #48456C;
}

.header-nav .nologin {
	text-align: right;
}

.header-nav .haslogin {
	text-align: right;
	position: relative;
	min-width: 150px;
	cursor: pointer;
}

.header-nav .haslogin ul {
	padding: 0px 5px;
	position: absolute;
	right: 0;
	visibility: visible;
	opacity: 1;
	transition: all 0.3s ease-out;
}

.header-nav .haslogin ul li {
	float: left;
	padding: 0 5px;
}


.header-nav .haslogin ul li:hover {
	color: #bf8fff;
}

/*******移动端*******/

.mobileBox {
	position: relative;
	height: 38px;
	line-height: 38px;
	color: #fff;
}

.hideMenu {
	position: relative;
	width: 100%;
	height: 100%;
	line-height: 38px;
}

.hideMenu ul.mlistmenu {
	width: 100%;
	position: absolute;
	left: 0;
	top: 100%;
	box-sizing: border-box;
	z-index: 999;
	box-shadow: 0 2px 6px 0 rgba(0, 0, 0, .12), 0 0 8px 0 rgba(0, 0, 0, .04);
	background: #00a7e0;
	color: #fff;
	border-right: none;
}

.hideMenu .el-submenu .el-menu {
	background: #00a7e0;
}

.hideMenu .el-menu-item,
.hideMenu .el-submenu__title {
	color: #fff;
}

.hideMenu>i {
	position: absolute;
	left: 10px;
	top: 12px;
	width: 30px;
	height: 30px;
	font-size: 16px;
	color: #fff;
	cursor: pointer;
}

.hideMenu .el-menu-item,
.el-submenu__title {
	height: 40px;
	line-height: 40px;
}
.submenu__title:hover{
	background: rgb(58, 199, 241);
}
.mobileBox .searchBox {
	padding-left: 40px;
	width: 100%;
	box-sizing: border-box;
}

.mobileBox .searchBox .el-input__inner {
	display: block;
	border-radius: 2px;
	border: none;
	height: 25px;
}

.hideMenu ul.mlistmenu.pshow {
	display: block;
}

.hideMenu ul.mlistmenu .el-submenu__icon-arrow,
.mobileBox li.el-menu-item a {
	color: #fff;
}

.hideMenu>ul li.el-menu-item:hover,
.hideMenu>ul li.el-menu-item.is-active {
	background: #68a9ff;
}



/*头部背景图*/

.headImgBox {
	height: 300px;
	position: relative;
	width: 100%;
	background-size: cover;
	background-position: center 50%;
	background-repeat: no-repeat;
	margin-bottom: 90px;

}

#user-logo {

	width: 100px;
	margin: auto;
	position: absolute;
	top: 250px;
	left: 280px;
	padding: 0 0;
	font-size: 16px;
	opacity: 0.98;
	border-radius: 50%;
	background: rgba(255, 255, 255, 0.8);
	height: 100px;
	z-index: 3;
	box-shadow: 0px 0px 20px #fac8fa;
	animation: b 1s ease-out;
	-webkit-animation: b 1s ease-out;
}

@-webkit-keyframes b {
	0% {
		-webkit-transform: translateY(90px);
		transform: translateY(90px);
	}
	80% {
		-webkit-transform: translateY(5px);
		transform: translateY(5px)
	}
	90% {
		-webkit-transform: translateY(-5px);
		transform: translateY(-5px)
	}
	to {
		-webkit-transform: translateY(0);
		transform: translateY(0)
	}
}

@keyframes b {
	0% {
		-webkit-transform: translateY(90px);
		transform: translateY(90px);
	}
	80% {
		-webkit-transform: translateY(5px);
		transform: translateY(5px)
	}
	90% {
		-webkit-transform: translateY(-5px);
		transform: translateY(-5px)
	}
	to {
		-webkit-transform: translateY(0);
		transform: translateY(0)
	}
}

#user-logo img {
	width: 100px;
	height: 100px;
	border-radius: 100%;
	transition: all .4s ease-in-out;
	-webkit-transition: all .4s ease-in-out;
	object-fit: cover;
}

#user-logo img:hover {
	transform: rotate(45deg);
	-webkit-transform: rotate(45deg);
}
.information {
	width:auto;
	height: 40px;
	line-height: 40px;
	position: absolute;
	padding: 5px;
	top: 300px;
	left: 400px;
	font-size: 18px;
	transform: matrix(1, 0, 0, 1, 0, 0);
	-webkit-transform: matrix(1, 0, 0, 1, 0, 0);
}

</style>

