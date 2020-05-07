# yjt-bishe
大学毕设
### **服务器运行**

首先安装python3.8，选择安装路径，然后配置python环境，在环境变量的系统变量中的path中添加python路径 python下的Script路径。

![img](file:///C:\Users\杨建亭\AppData\Local\Temp\ksohtml23760\wps1.jpg)然后在终端输入python --version和pip --version

![img](file:///C:\Users\杨建亭\AppData\Local\Temp\ksohtml23760\wps2.jpg)出现上面图片即安装成功，然后使用pip命令安装运行所需的python插件

如果pip版本不是最新的版本，需要运行 Python -m pip install --upgrade pip 更新pip版本

pip install flask pip install Flask-SQLAlchemy pip install pymysql pip install flask-cors

在数据库新建一个数据库 数据库命和配置如下：

![img](file:///C:\Users\杨建亭\AppData\Local\Temp\ksohtml23760\wps3.jpg)修改建表文件(server\message_models.py)第十行的198298，这是我的密码，请修改为你的密码即可，

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:198298@127.0.0.1:3306/bsbank'

然后在终端输入D:/Work/python/python.exe xxx（message_models.py所在的路径）即可建表成功。（D:/Work/python/python.exe是你python3.8的路径下的python.exe可执行文件的路径）

 

然后在终端输入D:/Work/python/python.exe xxx（message_models.py所在的路径）即可运行后台。

### **前端运行**

终端进入bishe00文件夹的路径，输入npm install 安装依赖，安装完毕后输入npm run serve运行

![img](file:///C:\Users\杨建亭\AppData\Local\Temp\ksohtml23760\wps4.jpg) 

毕设02运行方法与毕设00相同
