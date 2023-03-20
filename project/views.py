import flask


class SomeService:
    def some_method(self, params):
        return params

    def something(self):
        return "hello"


def render(template, render_context):
    pass


def render_view(name):
    def dec(view_func):
        def wraps():
            data = view_func
            return flask.render_template(name, data)
        wraps.inner = view_func
        return wraps
    return dec


class MockView():
    def index(self):
        s = SomeService()
        result = s.something()
        return result


class MyView(object):
    someservices_cls = SomeService

    def __init__(self, request):
        self.request = request

    def index(self):
        s = self.someservices_cls()
        result = s.some_method(**self.request.params)
        self.render_context = dict(result=result)
        return render("index.html", self.render_context)


class FlaskView(object):
    def __init__(self, request):
        self.request = request

    def index(self):
        s = SomeService()
        result = s.some_method(**self.request.params)
        self.request.json = result  # 将上下文添加到request.environ中，事后可通过测试用例查看
        return render("index.html", self.request.json)
