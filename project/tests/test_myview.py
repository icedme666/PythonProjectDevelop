import unittest
import sys
import os


p = os.path.dirname(os.path.dirname((os.path.abspath('__file__'))))
if p not in sys.path:
    sys.path.append(p)


class DummyRequest(object):
    def __init__(self, params):
        self.params = params


class DummySomeService(object):
    def some_method(self, **kwargs):
        return kwargs


class TestIt(unittest.TestCase):
    def test_it(self):
        from project.views import MyView
        request = DummyRequest(params={"a": 1})
        target = MyView(request)
        target.someservices_cls = DummySomeService
        result = target.index()
        self.assertEqual(target.render_context["result"], {"a": 1})
