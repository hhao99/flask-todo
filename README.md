
Flask 应用开发和实践

目录

* [flask基本环境和核心功能](# 前言)
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

## 启动helloworld
首先需要引入两个环境变量
FLASK_APP=app.py
FLASK_ENV=development

第一个变量，是告诉flask命令flask应用的入口文件是什么，这里是app.py模块，后面我们会看到入口可以是一个模块，或者一个包。
默认情况下flask会寻找当前目录下的app.py或者run.py，但是不推荐这么做了。
FLASK_ENV和 FLASK_DEBUG是控制开发和生产模式的开关变量，在开发模式下，我们可以web界面看到调试的信息，可以利用系统内置的hot-reload模式不用重启应用看到代码更改之后的变化。
如果想要使用更稳定强大的hot-reload功能，推荐使用watchdog。
推荐使用python-dotenv，可以自动加载 .env文件中的环境变量

