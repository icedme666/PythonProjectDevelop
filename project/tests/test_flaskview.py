import unittest
import flask
import os
import sys
import mock


p = os.path.dirname(os.path.dirname((os.path.abspath('__file__'))))
if p not in sys.path:
    sys.path.append(p)


class DummySomeService(object):
    def some_method(self, **kwargs):
        return kwargs


class DummyRequest(object):
    def __init__(self, params):
        self.params = params
        self.json = {}


from project.views import FlaskView
from project import views
import project
@mock.patch("project.views.SomeService")
def test_it(MockSomeService):
    request = DummyRequest(params={})
    views.SomeService = DummySomeService

    app = flask.Flask(__name__)
    with app.test_request_context(json={"a": 1}):
        result = FlaskView(request)
        result.index()
        assert flask.request.json == {"a": 1}
