import pprint
import requests
import json


# 发送GET请求
def get():
    # GET参数以字典的形式通过params传值参数指定
    response = requests.get("http://127.0.0.1:5000/get", params={"foo": "bar"})
    # 使用相应对象的json方法看获取转换为Python字典的JSON数据
    pprint.pprint(response.json())


# 发送POST请求
def post():
    response = requests.post("http://127.0.0.1:5000/post", {"foo": "bar"})
    pprint.pprint(response.json())


# 发送JSON格式的POST请求
def post_json():
    # 指定json.dumps生成的字符串后，可直接发送数据而不进行URL编码
    response = requests.post("http://127.0.0.1:5000/post", json.dumps({"foo": "bar"}), headers={"Content-Type": "application/json"})
    pprint.pprint(response.json())


# 使用其他HTTP方法
def other_methods():
    response_put = requests.put("http://127.0.0.1:5000/put", {"foo": "bar"})
    response_delete = requests.delete("http://127.0.0.1:5000/delete")
    response_head = requests.head("http://127.0.0.1:5000/head")
    response_options = requests.options("http://127.0.0.1:5000/options")
    pprint.pprint(response_put.json())
    pprint.pprint(response_delete.json())
    pprint.pprint(response_head)
    pprint.pprint(response_options)


print("发送GET请求：")
get()
print("发送POST请求：")
post()
print("发送JSON格式的POST请求：")
post_json()
print("使用其他HTTP方法：")
other_methods()
