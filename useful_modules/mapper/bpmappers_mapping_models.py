import json
from bpmappers import Mapper, RawField, DelegateField, ListDelegateField
from mapping_model import User, Comment, get_user, get_comment


class UserMapper(Mapper):
    """ User模型与API的映射 """
    user_id = RawField("id")
    user_nickname = RawField("nickname")


class UserMapper2(UserMapper):
    """ User模型与API的映射2 """
    user_age = RawField("age")


class CommentMapper(Mapper):
    """ Comment模型与API的映射 """
    user = DelegateField(UserMapper)
    text = RawField()


def api_user_json(user_id):
    """ 以JSON格式返回用户数据的API """
    user = get_user(user_id)  # 获取User对象
    user_dict = UserMapper(user).as_dict()  # 映射到字典
    return json.dumps(user_dict, indent=2)  # 以JSON格式返回


def api_user_detail_json(user_id):
    """ 以JSON格式返回用户详细数据的API """
    user = get_user(user_id)  # 获取User对象
    user_dict = UserMapper2(user).as_dict()  # 映射到字典
    return json.dumps(user_dict, indent=2)  # 以JSON格式返回


def api_comment_json(comment_id):
    """ 以JSON格式返回留言数据的API """
    comment = get_comment(comment_id)  # 获取Comment对象
    comment_dict = CommentMapper(comment).as_dict()  # 映射到字典
    return json.dumps(comment_dict, indent=2)  # 以JSON格式返回


class SpamMapper(Mapper):
    spam = RawField("foo")


class ListSpamMapper(Mapper):
    spam_list = ListDelegateField(SpamMapper)


def main():
    # 获取用户数据的JSON并显示
    print("--- api_user_json ---")
    print(api_user_json(user_id=1))
    # 获取用户数据的详细JSON并显示
    print("--- api_user_detail_json ---")
    print(api_user_detail_json(user_id=1))
    # 获取留言数据的JSON并显示
    print("--- api_comment_json ---")
    print(api_comment_json(1))
    # 列表元素内元素的套娃式映射
    spam_list = ListSpamMapper({"spam_list": [{"foo": 123}, {"foo": 456}]}).as_dict()
    print(json.dumps(spam_list))


main()
