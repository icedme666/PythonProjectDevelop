import shelve  # 存储数据

from datetime import datetime
from flask import Flask, request, render_template, redirect, escape, Markup
application = Flask(__name__)

DATA_FILE = 'guestbook.dat'


def save_data(name, comment, create_at):
    """保存提交的数据"""
    # 通过shelve模块打开数据库文件
    database = shelve.open(DATA_FILE)
    if 'greeting_list' not in database:
        greeting_list = []
    else:
        greeting_list = database['greeting_list']
    # 将提交的数据添加到表头
    greeting_list.insert(0,{
        'name': name,
        'comment': comment,
        'create_at': create_at,
    })
    # 更新数据库
    database['greeting_list'] = greeting_list
    # 关闭数据库
    database.close()


def load_data():
    """返回已提交的数据"""
    # 通过shelve模块打开数据库文件
    database = shelve.open(DATA_FILE)
    # 返回greeting_list，若没有数据则返回空表
    greeting_list = database.get('greeting_list',[])
    database.close()
    return greeting_list


@application.route('/')
def index():
    """首页  使用模版显示页面"""
    # 读取已提交的数据
    greeting_list = load_data()
    return render_template('index.html', greeting_list = greeting_list)


@application.route('/post', methods=['POST'])
def post():
    """用于提交评论的URL"""
    # 获取已提交的数据
    name = request.form.get('name')
    comment = request.form.get('comment')
    create_at = datetime.now()
    # 保存数据
    save_data(name, comment, create_at)
    # 保存重定向后到首页
    return redirect('/')


@application.template_filter('nl2br')
def nl2br_filter(s):
    """将换行符置换为br的模版过滤器"""
    return escape(s).replace('\n', Markup('<br>'))


@application.template_filter('datetime_fmt')
def datetime_fmt_filter(dt):
    return dt.strftime('%Y/%m/%d %H:%M:%S')


from flask import jsonify
from bpmappers import Mapper, RawField, ListDelegateField


class GreetingMapper(Mapper):
    name = RawField()
    comment = RawField()


class GreetingListMapper(Mapper):
    greeting_list = ListDelegateField(GreetingMapper)


@application.route("/api/")
def api_index():
    """ 留言 """
    #读取提交的数据
    greeting_list = load_data()
    result_dict = GreetingListMapper({"greeting_list": greeting_list}).as_dict()
    # 以JSON格式返回响应
    return jsonify(**result_dict)


def main():
    application.run('127.0.0.1', 8000, debug=True)
