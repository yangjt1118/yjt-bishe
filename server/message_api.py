from flask import jsonify, request, session ,Response
# from flask_wtf import FlaskForm
from token_util import generate_token, certify_token
# from message_models import app, db, Admin, Tag, User, Message, MessageToTag, CORS
from message_models import app, db, User, CORS, Admin, Transfer, Card, Tag, Article, ArticleToTag, Good, Order, Login
from  sqlalchemy import or_, extract, and_
import base64
import json
import datetime
"""
状态码 200 成功
状态码 400 失败
"""

CORS(app, supports_credentials=True)  # 设置跨域
@app.route('/set_cookie')
def hello_world():
    resp = Response("服务器返回信息")
    #设置cookie，
    resp.set_cookie('username','derek')
    return resp

# 管理员初始化 //
@app.route("/admin/init")
def init_admin():
    """
    账号：admin
    密码：default

    :return:
    """
    admin = Admin(name="admin", password="default")
    try:
        db.session.add(admin)
        db.session.commit()
        return jsonify(code=200, msg="初始化管理员成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="初始化管理员失败")


# 管理员登录 //
@app.route("/admin/login", methods=["POST"])
def login_admin():
    """
    传 账号 和 密码
    :return:
    """
    req_data = request.get_json()
    name = req_data.get("name")  # 获取账号
    password = req_data.get("password")  # 获取密码
    if not all([name, password]):
        return jsonify(code=400, msg="参数不完整")

    admin = Admin.query.filter(Admin.name == name).first()

    # 查找数据库管理员 # 验证密码
    if admin is None or password != admin.password:
        return jsonify(code=400, msg="登录失败，账号或密码错误")

    session["name"] = name
    session["admin_id"] = admin.id
    token = generate_token(name)
    data = {
        "admin_id":admin.id,
        "name": admin.name,
    }
    return jsonify(code=200,msg="登录成功",data=data)

# 管理员查看所有用户
@app.route("/admin/queryuser", methods=["GET"])
def admin_query_user():
    users = User.query.all()
    now_time = datetime.datetime.now()
    print((now_time + datetime.timedelta(days=-1)))  # 获取后一天
    # dat = datetime.date.today()
    # 先导入sql db对象
    payload1 = []
    payload2 = []
    week = [6,5,4,3,2,1,0]
    for i in week:
        usersi = User.query.filter(
            db.cast(User.create_time, db.DATE) == db.cast((now_time + datetime.timedelta(days=-i)), db.DATE)).all()
        payload1.append(len(usersi))
    print(payload1)
    for i in week:
        loginsi = Login.query.filter(
            db.cast(Login.create_time, db.DATE) == db.cast((now_time + datetime.timedelta(days=-i)), db.DATE)).all()
        payload2.append(len(loginsi))
    print(payload2)
    time = "2020-04-29"
    payload = []
    for user in users:
        # 获取cards
        card_ids = []
        cards = user.card,
        for card in cards:
            for c in card:
                card_ids.append(c.card_id)
        data = {
            "name":user.name,
            "gender":user.gender,
            "phone":user.phone,
            "address":user.address,
            "cards":card_ids,
            "create_time":user.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "status":user.status
        }
        payload.append(data)
    return jsonify(code=200,data=payload,data1=payload1,data2=payload2)


# 管理员增标签 //
@app.route("/admin/addtag", methods=["POST"])
def admin_add_tag():
    """
    tag_name
    :return:
    """
    req_data = request.get_json()
    name = req_data.get("name")
    admin_id = req_data.get("admin_id")
    if not all([name, admin_id]):
        return jsonify(code=400, msg="参数不完整")
    tag = Tag(name=name, admin_id=admin_id)
    try:
        db.session.add(tag)
        db.session.commit()
        return jsonify(code=200, msg="标签添加成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="标签添加失败")

# 查询标签
@app.route ("/admin/querytag", methods=["GET"])
def admin_query_tag():
    tags = Tag.query.all()
    # print(tags)
    payload = []
    for tag in tags:
        data={
            "tag_id":tag.id,
            "tag_name":tag.name
        }
        payload.append(data)
    return jsonify(code=200, data=payload)

# 管理员删标签 //
@app.route("/admin/tag", methods=["DELETE"])
def delete_tag():
    req_data = request.get_json()
    name = req_data.get("tag_name")  # 获取标签名
    admin_id = req_data.get("admin_id")  # 获取管理员的id

    # 参数不完整或者没登录
    if not all([name, admin_id]):
        return jsonify(code=400, msg="参数不完整或未登录")

    try:
        tag = Tag.query.filter(Tag.name == name).delete()
        db.session.commit()
        return jsonify(code=200, msg="删除标签成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="删除标签失败")

#管理员增新闻
@app.route("/admin/addarticle", methods=["POST"])
def admin_add_article():
    # req_data = request.get_json()
    admin_id = request.form.get("admin_id")
    tags = request.form.get("tags")
    title = request.form.get("title")
    content = request.form.get("content")
    data = request.files.get('image')
    badata = base64.b64encode(data.read())
    arr = tags.split(',')

    if not all([admin_id, tags, content,title]):
        return jsonify(code=400, msg="参数不完整")
    # for tag in tags:
    #     tag_names = Tag.query.filter(Tag.name==tag).all()
    # # print(tag_names)
    try:
        tags = Tag.query.filter(Tag.name.in_(arr)).all()
        print(tags)
        if len(tags) == 0:
            return jsonify(code=400)
        article = Article(content=content, admin_id=admin_id,title=title,pageview=0,image=badata)
        article.tags = tags
        db.session.add(article)
        db.session.commit()
        return jsonify(code=200, msg="发布资讯成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="发布资讯失败")

#查看文章
@app.route("/admin/queryarticle", methods=["POST"])
def admin_query_article():
    req_data = request.get_json()
    tag_id = req_data.get("tag_id")
    articless = ArticleToTag.query.filter(ArticleToTag.tag_id==tag_id).all()
    article_ids = []
    for article in articless:
        article_ids.append(article.article_id)
    articles = Article.query.filter(Article.id.in_(article_ids)).all()
    if len(tag_id) == 0:
        articles = Article.query.all()
    payload = []
    for article in articles:
        # 获取tags
        tag_names = []
        tags = article.tags,
        for tag in tags:
            for t in tag:
                print(t.name, "a")
                tag_names.append(t.name)
        # 生成器
        # tag_names = [t.name for t in tag for tag in tags]
        create_time = article.create_time.strftime("%Y-%m-%d %H:%M:%S"),
        admin_id = article.admin_id
        data = {"content": article.content,
                "title":article.title,
                "id": article.id,
                "tags": tag_names,
                "create_time": create_time,
                "admin_id": admin_id,
                "image":str(article.image),
                "pageview":article.pageview}
        payload.append(data)
    return jsonify(code=200, msg="查询成功", data=payload)
# 文章详情
@app.route("/admin/articlebyid", methods=["POST"])
def admin_article_byid():
    req_data = request.get_json()
    id = req_data.get("id")
    article = Article.query.get(id)
    # print(article)
    article1 = Article.query.filter(Article.id==id).update({"pageview":Article.pageview+1})
    # 获取tags
    tag_names = []
    tags = article.tags,
    for tag in tags:
        for t in tag:
            print(t.name, "a")
            tag_names.append(t.name)
    data = {
        "id":article.id,
        "title":article.title,
        "content":article.content,
        "tags": tag_names,
        "create_time":article.create_time.strftime("%Y-%m-%d %H:%M:%S"),
        "admin_id":article.admin_id,
        "image":str(article.image),
        "pageview":article.pageview
    }
    db.session.commit()
    return jsonify(code=200,data=data)
# 管理员删除单篇文章 //
@app.route("/admin/deletearticle", methods=["POST"])
def admin_delete_article():
    """
    上传留言对应的id
    作者的user_id判断作者
   :return:
    """
    req_data = request.get_json()
    id = req_data.get("id")
    # admin_id = req_data.get("admin_id")
    if not all([id]):
        return jsonify(code=400, msg="参数不完整")

    # 判断文章存在吗
    # msg = Article.query.get(id)
    # if msg is None:
    #     return jsonify(code=400, msg="留言不存在，无法删除操作")

    try:
        n = ArticleToTag.query.filter(ArticleToTag.article_id==id).delete(synchronize_session=False)
        m = Article.query.filter(Article.id==id) .delete(synchronize_session=False) # 删除多条数据
        db.session.commit()
        return jsonify(code=200, msg="删除成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="删除失败")

# 管理员批量删除文章 //
@app.route("/admin/batchdeletearticle", methods=["POST"])
def admin_batchdelete_article():
    """
    上传留言对应的id
    作者的user_id判断作者
   :return:
    """
    req_data = request.get_json()
    id = req_data.get("id")
    # admin_id = req_data.get("admin_id")

    if not all([id]):
        return jsonify(code=400, msg="参数不完整")

    # 判断文章存在吗
    # msg = Article.query.get(id)
    # if msg is None:
    #     return jsonify(code=400, msg="留言不存在，无法删除操作")

    try:
        n = ArticleToTag.query.filter(ArticleToTag.article_id.in_(id)).delete(synchronize_session=False)
        m = Article.query.filter(Article.id.in_(id)) .delete(synchronize_session=False) # 删除多条数据
        db.session.commit()
        return jsonify(code=200, msg="删除成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="删除失败")

# 管理员发布商品
@app.route("/admin/addgood", methods=["POST"])
def admin_add_good():
    req_data = request.get_json()
    admin_id = request.form.get("admin_id")
    name = request.form.get("name")
    description = request.form.get("description")
    price = request.form.get("price")
    data = request.files.get('image')
    badata = base64.b64encode(data.read())
    if not all([name, description, price, admin_id]):
        return jsonify(code=400, msg="参数不完整")
    good = Good(name=name, description=description, price = price, image = badata)
    try:
        db.session.add(good)
        db.session.commit()
        return jsonify(code=200, msg="商品添加成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="商品添加失败")

#商品列表
@app.route("/admin/querygood", methods=["GET"])
def admin_query_good():
    goods = Good.query.all()
    payload = []
    for good in goods:
        data = {"id": good.id, "name": good.name, "description": good.description,"price":str(good.price),
                "create_time": good.create_time.strftime("%Y-%m-%d %H:%M:%S"),"image":str(good.image),"order_count":good.order_count}
        payload.append(data)
    return jsonify(code=200, data=payload)
# 商品修改
@app.route("/admin/updategood", methods=["POST"])
def admin_update_good():
    req_data = request.get_json()
    admin_id = req_data.get("admin_id")
    id = req_data.get("id")
    name = req_data.get("name")
    description = req_data.get("description")
    price = req_data.get("price")
    good = Good.query.filter(Good.id==id).update({"name":name,"description":description,"price":price})
    try:
        db.session.commit()
        return jsonify(code=200,msg="修改商品信息成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400,msg="修改商品信息失败")
#商品删除
@app.route("/admin/deletegood", methods=["POST"])
def admin_delete_good():
    req_data = request.get_json()
    # admin_id = req_data.get("admin_id")
    id = req_data.get("id")
    if not all([id]):
        return jsonify(code=400,msg="参数不完整")
    goods = Good.query.filter(Good.id==id) .delete(synchronize_session=False) # 删除多条数据
    try:
        db.session.commit()
        return jsonify(code=200,msg="商品删除成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="商品删除失败")
#商品批量删除
@app.route("/admin/batchdeletegood", methods=["POST"])
def admin_batchdelete_good():
    req_data = request.get_json()
    # admin_id = req_data.get("admin_id")
    id = req_data.get("id")
    if not all([id]):
        return jsonify(code=400,msg="参数不完整")
    goods = Good.query.filter(Good.id.in_(id)) .delete(synchronize_session=False) # 删除多条数据
    try:
        db.session.commit()
        return jsonify(code=200,msg="商品删除成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="商品删除失败")
# 检查登录状态 //
@app.route("/admin/session", methods=["GET"])
def check_admin_session():
    name = session.get("name")
    admin_id = session.get("admin_id")

    if name is not None:
        # 操作逻辑 数据库什么的
        # 数据库里面 把你的头像 等级 金币数量 查询出来
        return jsonify(name=name, admin_id=admin_id)
    else:
        return jsonify(msg="出错了，没登录")


# 管理员退出登录 //
@app.route("/admin/logout")
def logout_admin():
    session.clear()
    return jsonify(msg="成功退出登录!")

# 用户注册 //
@app.route("/user/register", methods=["POST"])
def user_register():
    """
    账号
    密码
    用户名
    :return:
    """
    req_data = request.get_json()
    name = req_data.get("name")
    password = req_data.get("password")
    paypassword = req_data.get("paypassword")
    gender = req_data.get("gender")
    phone = req_data.get("phone")
    address = req_data.get("address")
    # image = request.form.get("image")
    # bafile = request.files['image'].read()
    # data = request.files.get('image')
    # badata = base64.b64encode(data.read())
    if len(password)< 6:
        print(len(password))
        return jsonify(code=400, msg="注册失败，请输入正确信息")
    if len(paypassword) < 6:
        print(222)
        return jsonify(code=400, msg="注册失败，请输入正确信息")
    user = User(name=name, password=password, paypassword=paypassword, gender=gender, phone=phone,address=address)
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify(code=200, msg="注册用户成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="注册失败，请检查信息是否可用")

# 用户登录 //
@app.route("/user/login", methods=["POST"])
def user_login():
    # resp = Response("服务器返回信息")
    # resp.set_cookie()
    req_data = request.get_json()
    # resp = Response("success")
    name = req_data.get("name")  # 获取账号
    # resp.set_cookie('username', 'name')
    password = req_data.get("password")  # 获取密码
    if not all([name, password]):
        return jsonify(code=400, msg="参数不完整")
    user = User.query.filter(User.name == name).first()
    if user is None or password != user.password:
        return jsonify(code=400, msg="账号或密码错误", data="账号或密码错误")
    if user.status == "冻结":
        return jsonify(code=400,msg="登录失败，账户已被冻结")
    #登录表
    login = Login()
    db.session.add(login)
    db.session.commit()
     # 验证账户密码
    session["name"] = user.name
    token = generate_token(name)
    data = {
            "name": user.name,
            'token': token,
            }
    return jsonify(code=200,  data=data)
# 用户上传修改头像
@app.route("/user/addimage",methods=["POST"])
def user_add_image():
    req_data = request.get_json()
    name = request.form.get("name")
    data = request.files.get('image')
    # print(data,1111)
    badata = base64.b64encode(data.read())
    # name = req_data.get("status")
    # image = req_data.get("content")
    # print(name,image)
    user = User.query.filter(User.name==name).update({"image":badata})
    db.session.commit()
    return jsonify(code=200, msg="上传头像成功")
# 加载用户头像
@app.route("/user/image",methods=["POST"])
def user_image():
    req_data = request.get_json()
    name = req_data.get("name")  # 获取账号
    user = User.query.filter(User.name == name).first()
    return user.image
def base64ToStr(s):
    '''
    将base64字符串转换为字符串
    :param s:
    :return:
    '''
    strDecode = base64.b64decode(bytes(s, encoding="utf8"))
    return str(strDecode, encoding='utf8')
# 加载文章图片
@app.route("/admin/queryarticleimage",methods=["POST"])
def query_article_image():

    s2 = 'cHl0aG9uOuWtl+espuS4sui9rOaNouaIkOWtl+iKgueahOS4ieenjeaWueW8jw=='

    print(base64ToStr(s2))
    req_data = request.get_json()
    tag_id = req_data.get("tag_id")
    articless = ArticleToTag.query.filter(ArticleToTag.tag_id == tag_id).all()
    article_ids = []
    for article in articless:
        article_ids.append(article.article_id)
    articles = Article.query.filter(Article.id.in_(article_ids)).all()
    if len(tag_id) == 0:
        articles = Article.query.all()
    payload = []
    print(articles)
    for article in articles:
        # data= {'image':str(article.image,'utf-8')}
        data = str(article.image)
        payload.append(data)
    print(len(payload))
    print(payload[2])
    payload1 = json.dumps(payload)
    return jsonify(code=200,data=payload)
#查询用户信息
@app.route("/user/query",methods=["POST"])
def user_query():
    req_data = request.get_json()
    name = req_data.get("name")
    user = User.query.get(name)
    data = {
        "name":user.name,
        "phone":user.phone,
        "address":user.address,
        "gender":user.gender,
        "create_time":user.create_time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(code=200,data=data)

#用户修改信息
@app.route("/user/update",methods=["POST"])
def user_update():
    req_data = request.get_json()
    name = req_data.get("name")
    gender = req_data.get("gender")
    phone = req_data.get("phone")
    address = req_data.get("address")
    if len(phone)!=11:
        return jsonify(code=400,msg="修改失败，请输入正确信息")
    user = User.query.filter(User.name==name).update({"gender":gender, "phone":phone, "address":address})
    try:
        db.session.commit()
        return jsonify(code=200, msg="修改信息成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="修改信息失败")
    # else:
    #     return jsonify(code=400, msg="修改信息失败")

#用户修改密码
@app.route("/user/updatepassword", methods=["POST"])
def user_updatepassword():
    req_data = request.get_json()
    name = req_data.get("name")
    password = req_data.get("password")
    user = User.query.get(name)
    password2 = req_data.get("password2")
    value= req_data.get("value")
    if value == "2":
        if user.paypassword != password:
            return jsonify(code=400,msg="原支付密码错误，请重新输入")
        user = User.query.filter(User.name == name).update({"paypassword": password2})
    if value == "1":
        if user.password != password:
            return jsonify(code=400,msg="原登录密码错误，请重新输入")
        user = User.query.filter(User.name == name).update({"password": password2})
    try:
        db.session.commit()
        return jsonify(code=200, msg="修改密码成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="修改密码失败")

# 管理员删除用户
@app.route("/admin/deleteuser", methods=["POST"])
def admin_delete_user():
    req_data = request.get_json()
    name = req_data.get("name")
    user = User.query.get(User.name)
    if user is None:
        return jsonify(code=400, msg="用户不存在，无法删除操作")
    try:
        u = User.query.filter(User.name == name).delete()
        db.session.commit()
        return jsonify(code=200,msg="删除用户成功")
    except Exception as e:
        print(e)
        db.session.rollback()
    return jsonify(code=200, msg="删除用户失败")


# 管理员修改用户状态
@app.route("/admin/updateuserstatus", methods=["POST"])
def admin_update_userstatus():
    req_data = request.get_json()
    name = req_data.get("name")
    status = req_data.get("status")
    user = User.query.filter(User.name == name).update({"status":status})
    try:
        db.session.commit()
        return jsonify(code=200,msg="修改状态成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=200, msg="修改状态失败")


# 用户退出登录 //
@app.route("/user/logout")
def user_logout():
    session.clear()
    return jsonify(code=200, msg="成功退出登录!")
#用户添加银行卡
@app.route("/user/addcard", methods=["POST"])
def user_addcard():
    req_data = request.get_json()
    user_name = req_data.get("user_name")
    card_id = req_data.get("card_id")
    balance = req_data.get("balance")
    if not all([user_name, card_id, balance]):
        return jsonify(code=400, msg="参数不完整")
    if len(card_id)<6:
        return jsonify(code=400,msg="添加失败，请输入正确的信息")
    card = Card(card_id=card_id, balance=balance, user_name=user_name)
    try:
        db.session.add(card)
        db.session.commit()
        return jsonify(code=200, msg="添加银行卡成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="添加银行卡失败")

#用户查看银行卡
@app.route("/user/querycard", methods=["POST"])
def user_querycard():
    req_data = request.get_json()
    name = req_data.get("name")
    cards = Card.query.filter(Card.user_name == name).all()
    payload = []
    for card in cards:
        card_id = card.card_id
        balance = card.balance
        create_time = card.create_time.strftime("%Y-%m-%d %H:%M:%S"),
        status = card.status
        data = {"card_id":card_id,"balance":str(balance),"create_time":create_time,"status":status}
        payload.append((data))
    return jsonify(code=200, msg="查询成功", data=payload)
# 用户转账
@app.route("/user/transfer", methods=["POST"])
def user_transfer():
    req_data=request.get_json()
    user_name = req_data.get("user_name")
    name = req_data.get("name")
    scard = req_data.get("scard")
    dname = req_data.get("dname")
    dcard = req_data.get("dcard")
    mount = req_data.get("mount")
    paypassword = req_data.get("paypassword")
    if not all([name, dcard, scard,dname, mount,paypassword]):
        print(name, dcard, scard,dname, mount,paypassword)
        return jsonify(code=400, msg="参数不完整")
    nn = User.query.all()
    namearr = []
    for n in nn:
        namearr.append(n.name)
    if dname not in namearr:
        return jsonify(msg="请输入正确的账号")
    if (name==dname):
        return jsonify(msg="请输入正确的账号")
    cc = Card.query.filter(Card.user_name == dname).all()
    cardarr = []
    for c in cc:
        cardarr.append(c.card_id)
    print(float(mount))
    if int(dcard) not in cardarr:
        return jsonify(msg="请输入正确卡号")
    if (scard==dcard):
        return jsonify(msg="请输入正确的卡号")
    p = User.query.filter(User.name == name).first()
    if (paypassword!=p.paypassword):
        return jsonify(msg="支付密码错误")
    s = Card.query.filter(Card.card_id == scard).first()
    if float(mount) > s.balance:
        return jsonify(msg="余额不足")
    try:
        m = Card.query.filter(Card.card_id == scard).update({"balance": Card.balance - float(mount)})
        n = Card.query.filter(Card.card_id == dcard).update({"balance": Card.balance + float(mount)})
        # u = session.query(User).join(Card).filter(Card.email_address == 'jack@google.com').one()
        # print(u)
        # s = Card.query.filter(Card.user_name == 2).all()
        # for ss in s:
        #     print(ss.balance,ss.card_id)
        transfer = Transfer(mount=mount, scard=scard, dname=dname,dcard=dcard,user_name=name)
        db.session.add(transfer)
        db.session.commit()
        return jsonify(code=200, msg="转账成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="转账失败")
# 用户购买商品
@app.route("/user/buygood", methods=["POST"])
def user_buy_good():
    req_data=request.get_json()
    user_name = req_data.get("user_name")
    name = req_data.get("name")
    scard = req_data.get("scard")
    price = req_data.get("price")
    paypassword = req_data.get("paypassword")
    if not all([name, scard, price, paypassword]):
        print(name, scard, price, paypassword)
        return jsonify(code=400, msg="参数不完整")
    # nnn = Good.query.get(name)
    # if nnn is None:
    #     return jsonify(code=400,msg="商品不存在")
    p = User.query.filter(User.name == user_name).first()
    if (paypassword!=p.paypassword):
        return jsonify(code=400, msg="支付密码错误")
    s = Card.query.filter(Card.card_id == scard).first()
    if float(price) > s.balance:
        return jsonify(code=400, msg="余额不足")
    good1 = Good.query.filter(Good.name == name).update({"order_count": Good.order_count + 1})
    try:
        m = Card.query.filter(Card.card_id == scard).update({"balance": Card.balance - float(price)})
        order = Order(name=name,user_name=user_name, price=price,scard=scard)
        # transfer = Transfer(price=mount, scard=scard, dname=dname,dcard=dcard,user_name=name)
        db.session.add(order)
        db.session.commit()
        return jsonify(code=200, msg="购买成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="购买失败")
#用户购买记录
@app.route("/user/orderhistory", methods=["POST"])
def user_order_history():
    req_data = request.get_json()
    name = req_data.get("name")
    orders = Order .query.filter(Order.user_name == name).all()
    print(orders)
    payload = []

    for order in orders:
        data = {"id":order.id, "name":order.name,"user_name":order.user_name,"create_time":order.create_time.strftime("%Y-%m-%d %H:%M:%S"),
                "scard":order.scard,"price":str(order.price)}
        payload.append(data)
    return jsonify(code=200,data=payload,msg="查询成功")
#转账日志
@app.route("/user/transferhistory", methods=["POST"])
def user_transferhistory():
    req_data = request.get_json()
    name = req_data.get("name")
    transfers = Transfer.query.filter(or_(Transfer.user_name == name, Transfer.dname==name)).all()
    stransfers = Transfer.query.filter(and_(extract('month', Transfer.create_time) == datetime.datetime.now().month),Transfer.user_name==name).all()
    dtransfers = Transfer.query.filter(and_(extract('month', Transfer.create_time) == datetime.datetime.now().month),Transfer.dname == name).all()
    print(stransfers)
    print(dtransfers)
    smount = 0
    dmount = 0
    payload1 = []
    for transfer in stransfers:
        smount += float(transfer.mount)
    print(smount)
    payload1.append(smount)
    for transfer in dtransfers:
        dmount += float(transfer.mount)
    print(dmount)
    payload1.append(dmount)
    print(payload1)
    # print(transfers)
    payload = []
    for transfer in transfers:
        id = transfer.id
        sname = transfer.user_name
        scard = transfer.scard
        dname = transfer.dname
        dcard = transfer.dcard
        create_time = transfer.create_time.strftime("%Y-%m-%d %H:%M:%S"),
        mount = transfer.mount
        data = {"id":id,"mount":str(mount),"sname":sname,"scard":scard,"dname":dname,"dcard":dcard,"create_time":create_time}
        payload.append((data))
    return jsonify(code=200, msg="查询成功", data=payload,data1=payload1)
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
