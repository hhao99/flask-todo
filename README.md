
Flask 应用开发和实践

目录

* flask基本环境和核心功能
* flask 基本route和blueprint
* form 和 template
* 数据库集成
* 安全相关
* rest api  
* 异步访问
* 前端集成
* 测试
* 部署和容器化


# 前言  
## flask 基于python的微内核web框架
python是通用的开发语言，在web应用开发方面，既有大而全的djaong，也有小而精的flask，还有其他各种特性的特定目的的web应用框架。
微内核框架，适合大而全的框架比较而言的。
微，不代表这功能少，什么都需要自己开发，而是将开发和架构的选择权交付给用户，只关注于核心的web请求和路由的功能，其他的功能通过可扩展的方式，同样可以完成django等大型框架实现的功能。
  
在这里，微内核可以快速起步，可以更灵活的选择所需要的相关技术框架，可以为应用的使用场景进行定制开发，扩展相关的功能。
  
在Nodejs上面，同样有express和koa的框架存在，需要使用哪一个框架，还是看具体的需求。
  
## 相关的资源
  
[fullstack] (https://www.fullstackpython.com/)
这里有起步python全面的资源，常用的web框架和相关的资源已经在这里
  
## 经典的起步教程
[flask mega ] (https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
[explore-flask] (http://exploreflask.com/)
  
我的flask 快速开始脚手架
[flask boilplate](http://github.com/hhao99/f3)
  
## 环境的准备
  
现在已经是python3的时代，不需要讨论2还是3，但是虚拟环境方面，还是要看大家的喜好。
  
python3 中已经内嵌了venv，同时也可以考虑conda。
  
我推荐miniconda, 尽量选择X64的发行版，相关镜像设置可以参考
[tsinghua mirrors](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)
[ustc mirros] (https://mirrors.tuna.tsinghua.edu.cn/anaconda/) ## 现在usts源中的anaconda的帮助不见了

## 工程目录选择
在我的开苏开始脚手架中，大家可以看到下面的目录结构

/-
|- config.py
|- requirements.txt
|- .gitignore
|- LICENSE
|- todo/-
      - __init__.py

对于简单的web应用，flask使用一个py文件就可以了，但是在实践当中，还是遵循合理的工程布局，将相关的功能和代码放在python模块和包中，这样可维护性和可扩展性会更好。



# 起步，flask的hello world
## Hello World 
首先，还是从hello world开始起步。
大家可以参考flask官方的教程的最小flask应用部分
[Flask official link](https://flask.palletsprojects.com/en/1.1.x/)

[flask quick start - minimal app](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application)

## flask的hello world 程序
app.py # the flask app start file

1. from flask import Flask
2. app = Flask(__name__)
3. @app.route('/')
4. def hello_world():
5.	return 'Hello, World!'

* 引入flask的包
* 实例化flask程序,这是一个符合wsgi标准的web程序
* 使用装饰符告诉flask web应用的路由
* 实际路由定义的函数
* 这里只是简单的返回 ’hello world!'

## 启动 Helloworld
首先需要引入两个环境变量
FLASK_APP=app.py
FLASK_ENV=development

第一个变量，是告诉flask命令flask应用的入口文件是什么，这里是app.py模块，后面我们会看到入口可以是一个模块，或者一个包。
默认情况下flask会寻找当前目录下的app.py或者run.py，但是不推荐这么做了。
FLASK_ENV和 FLASK_DEBUG是控制开发和生产模式的开关变量，在开发模式下，我们可以web界面看到调试的信息，可以利用系统内置的hot-reload模式不用重启应用看到代码更改之后的变化。
如果想要使用更稳定强大的hot-reload功能，推荐使用watchdog。
推荐使用python-dotenv，可以自动加载 .env文件中的环境变量

# 路由和模板初步

在 Hello World中，我们定义了一个web请求的入口，app.route是flask的装饰器，可以帮助我们在flask应用上下文中注册相关的view 控制器，用于处理用户提交url请求后相关的处理。
```
@app.route('/')
def index():
      return "Hello World!"
```
这是这个应用的主入口，用户在浏览器中输入http://localhost:5000/， flask就会解析这个请求，根据应用的配置信息和这个定义，将接下来的处理逻辑交给在这里定义的函数。

在现实应用中，http请求和处理远比这个示例复杂。

## http 请求基本信息
对于 http://localhost:5000/, 用户在浏览器中输入这个url，接下来会发生什么呢？

| Browser| Flask| app code|
|------|------|------|
| 发出get| ->| -|
| -| flask截获请求，判断请求方法，查找路由表，构造request和response对象，调用对应的处理函数| ->|
|-|<-|处理函数分析request对象，执行业务逻辑，返回response对象-|
|<-|flask对response对象进一步处理，返回请求结果到客户端|-|
|浏览器解析返回结果，显示相关的内容|-|-|


现在我们定义一个新的请求路径

```
@app.route('/home’)
def home():
      return "HOME"
```

我们可以使用http://localhost:5000/home 来访问这个新定义的功能了。

## 在route中定义变量
在route中，我们不仅可以定义路径，同时还可以定义我们需要处理的变量和变量的类型

```
@app.route('/hello/<username>')
def home(username):
      # greeting to the username
      return "Hello " + username
```

```
@app.route('/post/<int:post_id>')
def show_post(post_id):
      return f'Post Id: {post_id}'
```

```
@app.route('/home/<path:subpath>')
def show_subpath(subpath):
      return f'Subpath is {subpath}'
```

## url 绑定
在实际的应用中，我们需要在应用的不同位置引用需要访问的url地址，使用绝对路径可以解决问题，但是如果你的应用发生变化，所有相关的路径都需要修改。
url_for（）函数可以帮助我们解决这个问题，flask可以帮助我们反推出我们相关url处理函数中定义的url路径，这样我们可以在应用中可以清晰的指定这个请求需要处理的函数是什么。

具体url_for()的应用，我们在模板中会有相关的示例。

## http 方法
http 请求方法主要是GET，POST，PUT，UPDATE，DELETE，HEAD，其中最常用的是GET和POST,对于表单的处理，一般是使用post方式，所以需要在代码中明确处理的http方法

```
@app.route('/home',methods=['GET'])
def home():
      return "HOME"
```

```
@app.route('/new_user',methods=['GET','POST'])
def home():
      if request.method == 'POST':
            # processing the post 

```

## 静态文件
web应用中需要使用色的图片，样式，javascript等文件，可以利用web服务器来存取，但是如果只有flask，可以利用flask内置的静态url端点来服务这些请求

url_for（'static'，filename='style.css')

根据约定，需要应用相对路径下面创建static目录，将相关的文件放在这个目录下面。

## 使用模板

在动态web应用中，和html相关的样式，布局等和前端展示相关的内容，可以使用模板定义在不同的文件中，在请求中，将需要的内容更新后，将相关的内容展示交给相应的模板引擎进行渲染，然后返回给客户端。
Flask 缺省使用Jinja2模板引擎，你也可以配置自己的模板引擎。

```
@app.route('/home',methods=['GET'])
def home():
      title = 'Home'
      return render_template('index.html',title=title)
```

模板相关的文件放在应用相对的templates路径下面。

```
<!doctype html>
<head>
      <title> {{title}} </title>
</head>
<body>
      {%if name %}
      <h1>Hello {{name}}</h1>
      {%else %}
      <h1>Hello World</h1>
      {% endif %}
</body>
</html>
```
在模板中，flask 中相关的web请求的对象 request,response， session和g都是可见的，同时可以使用get_flashed_messages()或者后端推送的消息。

{{ title }} 可以在模板中直接输出python变量的内容， {% %} 可以执行模板的动态语言。


# Flask todo - 一个完整的todo应用功能

现在，我们需要开始一个完整的web应用程序。
循序渐进，我们首先从一个简单的todo应用开始。

## 应用逻辑
todo应用主要是追踪用户的代办事项。

第一步，可以显示用户的代办事项。
第二步，可以增删改相关的代办事项。
第三步，连接后台的数据库，持久化相关的用户状态到数据库。

## 第一步，简单的代办事项

首先我们采用修改现有的应用组织方式，删除现有app.py,采用包的方式，将todo相关的逻辑功能组织到一个目录里面。
···
Flask-todo/
      |- todo
            |- __init__.py
            |- templates
            |- static
      |- config.py
      |- .env
      |- LICENSE
      |- README.txt
      |- requirements.txt

···