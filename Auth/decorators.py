from django.shortcuts import redirect, HttpResponse


def LoginRedirect(function):
    def wrapper(request, *args, **kw):
        user = request.user
        if user.is_authenticated:
            if user.type == "student":
                return redirect("student-home")
            else:
                return redirect("doctor-home")
        else:
            return function(request, *args, **kw)
    return wrapper
