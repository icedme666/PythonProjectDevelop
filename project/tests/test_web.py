import os
import sys
import unittest
from mock import patch
from webtest import TestApp


p = os.path.dirname(os.path.dirname((os.path.abspath('__file__'))))
if p not in sys.path:
    sys.path.append(p)


from project.db import _setup_db, _teardown_db
from project.app import myapp, myapp2


def _makeOne():
    return TestApp(myapp2)


def _callAUT(url, params={}, method="GET", remote_user=None):
    extra_environ = {"REMOTE_USER": remote_user}
    if method == "GET":
        return _makeOne().get(url, params=params, extra_environ=extra_environ)
    elif method == "POST":
        return _makeOne().post(url, params=params, extra_environ=extra_environ)

# 使用方法
def test_it():
    import project.app
    app = TestApp(project.app)
    res = app.get("/")
    assert "Hello" in res


# 与外部服务有关的测试
def setUpModule():
    _setup_db()


def tearDownModule():
    _teardown_db()


def _init_data():
    # 生成shuju
    pass


def _init_search_result():
    # 创建mock的外部服务结果
    pass


class TestWithMock(unittest.TestCase):

    def _getTarget(self):
        app = TestApp(myapp)
        return app

    @patch("othersite.search")
    def test_it(mock_search):
        """ 测试 """
        # 前提条件
        mock_search.return_value = _init_search_result()
        _init_data()
        # 准备测试对象
        app = self._getTarget()
        # 执行测试对象
        res = app.get("/?search_word=abcd")
        # 确认结果
        assert "20" in res
        mock_account.deposit.assert_called_with(q="abcd")


    # Cookie的相关测试：WebTest支持Cookie所以能正常执行基于Cookie会话及认证的相关测试
    def test_cookie(self):
        app = TestApp(myapp)
        res = app.get("/")
        assert res.body == "response 0"

        res = app.get("/")
        assert res.body == "response 1"

    # 与认证相关的测试
    def test_with_login(self):
        result = _callAUT("/", remote_user="dummy")
        assert result.body == "OK"

    def test_without_login(self):
        result = _callAUT("/")
        assert result.location == "/login"
