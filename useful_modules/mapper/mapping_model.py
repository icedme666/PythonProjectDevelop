import json


class User(object):
    def __init__(self, id, password, nickname, age):
        self.id = id
        self.password = password
        self.nickname = nickname
        self.age = age


class Comment(object):
    def __init__(self, id, user, text):
        self.id = id
        self.user = user
        self.text = text


def get_user(user_id):
    """ 返回用户对象的函数"""
    user = User(user_id, "123456", "gxm", 6)
    return user


def get_comment(comment_id):
    """ 返回留言对象的函数 """
    comment = Comment(id=comment_id, user=get_user(1), text="Hello World!")
    return comment


def mapping_user(user):
    """ User模型与API的映射 """
    return {"user_id": user.id, "user_nickname": user.nickname}


def mapping_user2(user):
    """ User模型与API的映射2 """
    return {"user_id": user.id, "user_nickname": user.nickname, "user_age": user.age}


def mapping_comment(comment):
    """ Comment模型与API的映射 """
    return {"user": mapping_user(comment.user), "text": comment.text}


def api_user_json(user_id):
    """ 以JSON格式返回用户数据的API """
    user = get_user(user_id)  # 获取User对象
    user_dict = mapping_user(user)  # 映射到字典
    return json.dumps(user_dict, indent=2)  # 以JSON格式返回


def api_user_detail_json(user_id):
    """ 以JSON格式返回用户详细数据的API """
    user = get_user(user_id)  # 获取User对象
    user_dict = mapping_user2(user)  # 映射到字典
    return json.dumps(user_dict, indent=2)  # 以JSON格式返回


def api_comment_json(comment_id):
    """ 以JSON格式返回留言数据的API """
    comment = get_comment(comment_id)  # 获取Comment对象
    comment_dict = mapping_comment(comment)  # 映射到字典
    return json.dumps(comment_dict, indent=2)  # 以JSON格式返回


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


main()
