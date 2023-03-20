from datetime import timedelta, date, datetime
import os
import sys
from testfixtures import Replacer, test_date


p = os.path.dirname(os.path.dirname((os.path.abspath('__file__'))))
if p not in sys.path:
    sys.path.append(p)


def is_last_of_month(d):
    return (d+timedelta(1)).day == 1


def test_is_last_of_month():
    d = date(2011, 11, 30)
    assert is_last_of_month(d), "%s" % d


def test_is_last_of_month_not():
    d = date(2011, 11, 29)
    assert not is_last_of_month(d), "%s" % d


def is_last_of_month_now():
    return is_last_of_month(datetime.now())


def test_is_last_of_month_now():
    with Replacer() as r:
        print("时间：")
        print(test_date(2011, 11, 30))
        r.replace("util.datetime", test_date(2011, 11, 30))  # 替换掉测试对象import的东西？
        assert is_last_of_month_now()

