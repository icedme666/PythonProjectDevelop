from webob.dec import wsgify


def myapp(request):
    c = int(request.cookie.get("count", "0"))
    request.response.set_cookie("count", str(c+1))
    return "response %d" % c


def myapp2(request):
    if not request.remote_user:
        return HTTPFound(location="/login")
    return "OK"
