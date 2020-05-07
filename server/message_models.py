from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import *  # 导入模块
import pymysql

from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:198298@127.0.0.1:3306/bsbank'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:198298@127.0.0.1:3306/bsbank?charset=utf8mb4'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "jjjsks"


db = SQLAlchemy(app)  # 实例化的数据库


# 管理员表
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(32), nullable=False, unique=True)  # 账号
    password = db.Column(db.String(32), nullable=False)  # 密码
    articles = db.relationship("Article", backref = "admin")
    tags = db.relationship("Tag", backref="admin")  #

# 用户
class User(db.Model):
    __tablename__ = "user"
    # id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(32), nullable=False, unique=True, primary_key=True)  # 姓名
    image = db.Column(db.LargeBinary(length=2 ** 24))
    gender = db.Column(db.Enum("男","女"), nullable=False) # 性别
    phone = db.Column(db.String(11), nullable=False,unique=True)   # 电话号码
    address = db.Column(db.String(64), nullable=False) # 地址
    password = db.Column(db.String(16), nullable=False)  # 密码
    paypassword = db.Column(db.String(16), nullable=False)  # 支付密码
    create_time = db.Column(db.DateTime, default=datetime.now)  # 注册时间
    status = db.Column(db.Enum("正常", "冻结", "挂失"), server_default='正常', nullable=False) # 状态
    card = db.relationship("Card", backref="user")
    transfer = db.relationship("Transfer", backref = "user")
    # goods = db.relationship("Good", secondary="user_to_good", backref="users")  # 商品购买关系关联
    # status = db.Column(db.Enum("正常", "冻结", "挂失"), server_default='正常', nullable=False)  #
    # transfer = db.relationship("Transfer", backref="user")

# 银行卡
class Card(db.Model):
    __tablename__ = "card"
    # id = db.Column(db.Integer, primary_key=True)  # 主键
    card_id = db.Column(db.Integer, nullable=False,unique=True,primary_key=True)  # 银行卡卡号
    balance = db.Column(db.DECIMAL(11,2))  # 余额
    create_time = db.Column(db.DateTime, default=datetime.now)  # 注册时间
    user_name = db.Column(db.String(32), db.ForeignKey("user.name"))  # 所属用户
    status = db.Column(db.Enum("正常", "冻结", "挂失"), server_default='正常', nullable=False)  # 学生性别
#转账记录
class Transfer(db.Model):
    __tablename__ = "transfer"
    id = db.Column(db.Integer, primary_key=True)  # 主键 流水号
    mount = db.Column(db.DECIMAL(11,2), nullable=False,)
    # sname = db.Column(db.String(32), nullable=False)  # 转账人姓名
    scard = db.Column(db.Integer, nullable=False)  # 转账人银行卡
    dname = db.Column(db.String(32), nullable=False)  # 收账人姓名
    # dname = db.relationship("User", backref=db.backref("transfer"))
    # dname = db.Column(db.String(32),db.ForeignKey("user.name"))
    dcard = db.Column(db.Integer, nullable=False)  # 收账人银行卡
    create_time = db.Column(db.DateTime, default=datetime.now)  # 转账时间
    user_name = db.Column(db.String(32), db.ForeignKey("user.name"))  # 所属用户

# 文章标签
class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(10), nullable=False, unique=True)  # 标签名字
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))  # 所属管理员

# 文章
class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False) # 标题
    image = db.Column(db.LargeBinary(length = 2 ** 24))
    content = db.Column(db.Text, nullable=False) # 内容
    pageview = db.Column(db.Integer,nullable=False, default=0) # 浏览量
    create_time = db.Column(db.DateTime, default=datetime.now)
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))  # 所属用户
    tags = db.relationship("Tag", secondary="article_to_tag", backref="articles")  # 关系关联

# 中间表
class ArticleToTag(db.Model):
    __tablename__ = "article_to_tag"
    id = db.Column(db.Integer, primary_key=True)  # 主键
    article_id = db.Column(db.Integer, db.ForeignKey("article.id"))  # 所属留言条
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"))  # 所属标签

# 商品表
####### 商品用id买
class Good(db.Model):
    __tablename__ = "good"
    id = db.Column(db.INTEGER, primary_key=True) # 主键
    name = db.Column(db.String(32), nullable=False) # 商品名称
    description = db.Column(db.Text, nullable=False) # 商品简介
    image = db.Column(db.LargeBinary(length=2 ** 24))
    price = db.Column(db.DECIMAL(11,2), nullable=False) # 商品价格
    create_time = db.Column(db.DateTime, default=datetime.now)
    order_count = db.Column(db.Integer,nullable=False, default=0) # 销量

# 订单表
class Order(db.Model):
    __tablename__ = "order"
    ##################商品名称改成商品ID
    id = db.Column(db.INTEGER, primary_key=True) # 主键
    name = db.Column(db.String(32), nullable=False) # 已购买商品名称
    create_time = db.Column(db.DateTime, default=datetime.now) # 购买时间
    price = db.Column(db.DECIMAL(11,2), nullable=False) #支付的金额
    scard = db.Column(db.Integer, nullable=False) # 支付的卡号
    user_name = db.Column(db.String(10), db.ForeignKey("user.name"))
#登录表
class Login(db.Model):
    __tablename__ = "login"
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime,default=datetime.now)

# # 中间表
# class UserToGood(db.Model):
#     __tablename__ = "user_to_good"
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     user_id = db.Column(db.String(10), db.ForeignKey("user.name"))  # 所属留言条
#     good_id = db.Column(db.Integer, db.ForeignKey("good.id"))  # 所属标签

if __name__ == '__main__':
    db.create_all()
    # db.drop_all()