============
  留言板应用
============

工具版本
========

:Python: 3.11.0
:pip: 22.2.2
:conda: 4.5.12

安装与启动方法
=============

搭建conda虚拟环境
$ git clone 项目
$ cd guestbook
$ conda activate flask
$ pip install .
$ guestbook

开发流程
========

用于开发的安装
-------------
1. 检测
2. 按以下流程安装：
   pip install -e .
   pip freeze > requirements.txt
3. 提交代码
