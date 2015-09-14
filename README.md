# mysite
练习python和Django的项目
以下是学习笔记
第一部分

在命令行中，cd到你想要用来保存代码的目录，然后运行如下命令：
>>>django-admin startproject mysite（项目名称，可以改，以下红色字体均可根据实际情况更改）

在数据库中建相应的表
>>>python manage.py migrate

在mysite的目录下运行服务器
>>>python manage.py runserver

新建一个应用#项目和应用之间有什么不同？ 应用是一个Web应用程序，它完成具体的事项 —— 比如一个博客系统、一个存储公共档案的数据库或者一个简单的投票应用。 项目是一个特定网站中相关配置和应用的集合。一个项目可以包含多个应用。 一个应用可以运用到多个项目中。
>>>python manage.py startapp polls (应用名，可以改)

激活应用
在mysite/setting.py中的INSTALLED_APP中添加应用名"polls"如：
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
)
要想让Django知道polls
>>>python manage.py makemigratons polls

通过运行makemigrations，你告诉Django你已经对模型做了一些更改（在这个例子中，你新建了新的模型）并且愿意将这些更改存储为迁移文件。
迁移文件是Django 用于保存你的模型（同时也是你的数据库模式）的改动的方法—— 它们其实就是磁盘上的文件， sqlmigrate命令接收迁移文件的名字并返回它们的SQL语句：
>>>python manage.py sqlmigrate polls 0001

检查你的项目是否存在问题
>>>python manage.py check

再次运行migrate以在你的数据库中创建模型所对应的表
>>>python manage.py migrate

进入交互式shell
>>> python manage.py shell

第二部分

创建一个管理员账户
>>>python manage.py createsuperuser
之后就按照步骤写下用户名和密码

打开http://127.0.0.1:8000/admin/进入管理员界面

第三部分
