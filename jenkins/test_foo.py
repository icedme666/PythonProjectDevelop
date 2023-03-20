import unittest
import foo
import os, sys

p = os.path.dirname(os.path.dirname((os.path.abspath('__file__'))))
if p not in sys.path:
    sys.path.append(p)


class SimpleTest(unittest.TestCase):
    """ 测试做除法的函数 """
    def test1(self):
        self.assertEqual(foo.divide(2, 2), 1)

    def test2(self):
        self.assertEqual(foo.divide(0, 1), 1)


unittest.main()