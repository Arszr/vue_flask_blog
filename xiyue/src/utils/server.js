/*
 * @Description: In User Settings Edit
 * @Author: your name
 * @Date: 2019-10-04 17:51:57
 * @LastEditTime: 2019-10-08 20:25:15
 * @LastEditors: Please set LastEditors
 */
import Vue from 'vue'

import axios from 'axios'

let portUrl = "http://127.0.0.1:5000/";


//用户登录
export const UserLogin =  (email,password,callback) =>{
  let params= {
      _email:email,
      _password:password,
  };
  let url = portUrl + 'login/';
  axios
      .post(url,params)
      .then(num => {
          console.log(num.data)
          callback && callback(num.data);
  })
}
// 用户注册
export const getRegister = (username,password,email,callback) =>{
  let params= {
    _username:username,
    _email:email,
    _password:password,
  };
  let url = portUrl + 'regist/';
  axios
    .post(url,params)
    .then(num => {
      console.log(num.data)
          callback && callback(num.data)
  })
}
//查询文章列表
export const ShowArticleAll = (artId,cateId,articleName,level,callback) =>{
  if(level == 1){
      var url = portUrl + 'article/?art_id='+artId+'&cate_id='+cateId+'&article_name='+articleName;
  }else{
      var url = portUrl + 'article/?art_id='+artId+'&cate_id='+cateId+'&article_name='+articleName;
  }
  axios
    .get(url)
    .then(num => {
          callback && callback(num.data);
  })
}

//文章分类查询
export const ArtClassData = (callback) => {
  if(sessionStorage.getItem('classList')){
      var data = JSON.parse(sessionStorage.getItem('classList'));
      callback && callback(data)
  }else{
      let url = portUrl + 'article';
      axios.get(url).then(num => {
          // console.log(num);
          if(num.data.code==1001){
              sessionStorage.setItem('classList',JSON.stringify(num.data.data));
              callback && callback(num.data.data)
          }else{
              alert("查询失败")
          }
      })
  }
}
//初始化时间
export const initDate = (oldDate,full) => {
  var odate = new Date(oldDate);
  var year =  odate.getFullYear();
  var month = odate.getMonth()<9? '0' + (odate.getMonth()+1) : odate.getMonth()+1;
  var date = odate.getDate()<10? '0'+odate.getDate() : odate.getDate();
  if(full=='all'){
      var t = oldDate.split(" ")[0];
      // console.log(oldDate,t.split('-')[0],t.split('-')[1],t.split('-')[2]);
      return t.split('-')[0]+'年'+t.split('-')[1]+'月'+t.split('-')[2]+'日';
  }else if(full=='year'){
      return year
  }else if(full== 'month'){
      return odate.getMonth()+1
  }else if(full == 'date'){
      return date
  }else if(full== 'newDate'){
      return year+'年'+month+'月'+date+'日';
  }
}