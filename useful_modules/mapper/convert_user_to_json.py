import json


class User(object):
    def __init__(self, id, password, nickname, age):
        self.id = id
        self.password = password
        self.nickname = nickname
        self.age = age


def convert_user_to_json(user):
    """ 获取一个User对象并返回JSON """
    # 生成用于转换格式的字典对象
    user_dict = {
        "user_id": user.id,
        "user_nickname": user.nickname,
    }
    return json.dumps(user_dict)


user = User(1, "123456", "gxm", 6)
data = convert_user_to_json(user)
print(data)
