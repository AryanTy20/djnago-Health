from django.shortcuts import redirect, HttpResponse


def loginRequired(function):
    def wrapper(request, *args, **kw):
        user = request.user
        print(user.type)
        if user.is_anonymous:
            return HttpResponse("<h1>You are not Authorize !!!</h1>")
        if not user.type == "student":
            return HttpResponse("<h1>You are not Authorize</h1>")
        else:
            return function(request, *args, **kw)
    return wrapper
