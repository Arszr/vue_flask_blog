'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-09-28 21:20:50
@LastEditTime: 2019-10-12 19:57:55
@LastEditors: Please set LastEditors
'''
import json

from flask import Flask,request,render_template
from flask_cors import CORS
from flask_script import Manager
from model import Article,User,Answer



app = Flask(__name__)
manager = Manager(app)
CORS(app, supports_credentials=True)

# 查找数据库当前数量条数
global art_id_count
art_id_count=Article.art_max_id()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login/', methods=['GET','POST'])
@manager.command
def Login():
    if request.method == 'GET':
        return '1010'
    else:
        data = request.get_data()
        json_data=json.loads(data.decode('utf-8'))
      
        email = json_data.get("_email")
        password = json_data.get("_password")
        print(email,password)
        user=User.query_users(email)
        print(user.get('email'))
        if email == user.get('email') and password== user.get('password'):
            msg={
                'code':1010,
                'data':user.get('username'),
                'token':'111'

            }
            return json.dumps(msg)
        elif email != user.get('email') or password != user.get('password'):
            msg={
                'code':2008,
                
            }
            return json.dumps(msg)
        
@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        
        return '用post请求'
    else:
        data = request.get_data()
        json_data=json.loads(data.decode('utf-8'))
        username=json_data.get("_username")
        email = json_data.get("_email")
        password = json_data.get("_password")
        print(username,email,password)
        user=User.query_users(email)
        if user: 
            msg={'code':2002}
            return json.dumps(msg)
        else:
            user=User(username,email,password).save()
            msg={'code':1010}
            return json.dumps(msg)

@app.route('/search/',methods=['GET'])
def search():
    search_data = request.args.get('q')
    
@app.route('/article/',methods=['GET'])
def article():
    art_id=request.args.get('art_id')
    cate_id=request.args.get('cate_id')
    article_name=request.args.get('article_name')
    print(art_id,cate_id,article_name)
    global art_id_count 
    art_id_count += 1
    article=Article(art_id_count,'测试数据文章','作者','2019-12-10 10:10:10','/static/img/22.jpg','测试数据文章简介','内容').save()
    all_article=Article.query_all_article()
    all_article.reverse()
    result_data=all_article
    msg_data={
        'code':1001,
        'data': result_data, 
        'msg':'chenggong',
    }
    print(result_data)
    return json.dumps(msg_data)


    answer={                    'collect_count': 7,     #收藏
                                'comment_count': 80,    #评论
                                'browse_count': 865,    #查看
                                'like_count': 4,    #点赞
                                }


if __name__ == '__main__':
    app.run()
    # manager.run()
