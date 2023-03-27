from django.conf import settings
import django
settings.configure()
django.setup()

from django.db import models
from bpmappers.djangomodel import ModelMapper


class Person(models.Model):
    """ 表示人的数据模型 """
    name = models.CharField("名字", max_length=20)
    age = models.IntegerField("年龄")

    class Meta:
        #指定app_label，防止应用名解析时出错
        app_label = ""


class PersonMapper(ModelMapper):
    """ 让Person模型映射到字典时需要用到的类 """
    class Meta:
        model = Person


def main():
    # 生成Person对象
    person = Person(id=123, name="gxm", age=6)
    # 映射到字典
    person_dict = PersonMapper(person).as_dict()
    print(person_dict)


main()
