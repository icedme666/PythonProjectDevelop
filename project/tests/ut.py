import unittest


def setUpModule():
    """ 搭建测试环境 """


def tearDownModule():
    """ 测试环境清理 """


class TestIt(unittest.TestCase):
    def setUp(self):
        """ 搭建测试环境 """

    def test_it(self):
        """ 本方法是一个测试用例 """
        a = 1
        b = 2
        c = a + b
        self.assertEqual(c, 3)

    def tearDown(self):
        """ 搭建测试环境 """
