'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-06 14:02:56
@LastEditTime: 2019-10-12 20:04:27
@LastEditors: Please set LastEditors
'''

import pymongo,re

def get_user():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.xiyueblog
    user = db.user
    return user
    
def get_article():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.xiyueblog
    article=db.article
    return article

# 用户表
class User(object):
    def __init__(self, username, email, password):
        self.username=username
        self.email = email
        self.password = password

    # 添加用户
    def save(self):
        user = {"username":self.username, "email": self.email, "password": self.password}
        coll = get_user()
        id = coll.insert_one(user)

    # 查询
    @staticmethod
    def query_users(email):
        users = get_user().find_one({"email":email})
        return users

    # 删除
    @staticmethod
    def delete(email):
        users = get_user().find({"email": email})
        print(users)
        coll = get_user()
        coll.remove({"email": email})
        return email

    # 更新
    @staticmethod
    def update(email,password):
        users = get_user().find({"email": email})
        print(users)
        coll = get_user()
        coll.find({"email": email})
        coll.update({"email":email},{"$set":{"password":password}})
        return email

# 文章表
class Article(object):
    def __init__(self, _id:int,title,author,create_time,image,description, content,)->None:
        self.title=title
        self.content=content
        self.author=author
        self.create_time=create_time
        self.image=image
        self._id=_id
        self.description=description

    # 添加文章
    def save(self):
        article = {
            '_id':self._id,
            "title":self.title, 
            "author": self.author, 
            "create_time": self.create_time,
            "description":self.description,
            "image":self.image,
            'content':self.content
        }
        coll = get_article()
        coll.insert_one(article)

    # 标题查询
    @staticmethod
    def query_article(title):
        # search_title = get_user().find_one({"title":re.compile(title)})

        search_title = get_article().find_one({"title":{"$regex": title}})
        return search_title
    
    @staticmethod
    def art_max_id():
        max_id=get_article().find({}).count()
        return max_id

    @staticmethod
    def query_all_article():
        all_data=get_article().find()
        return list(all_data)



# 评论点赞表
class Answer(object):
    def __init__(self,collect:int=0,comment:int=0,browse:int=0,like:int=0):
        self.collect=collect    #收藏
        self.comment=comment    #评论
        self.browse=browse      #查看
        self.like=like          #点赞

    # 添加评论
    def add_collect(self):
        answer={"collect",self.collect}
        coll = get_article()
        coll.insert_one(answer)

    def add_comment(self):
        pass
            