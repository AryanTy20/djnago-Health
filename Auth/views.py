from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, HttpResponse
from .forms import studentRegForm, doctorRegForm
from .decorators import LoginRedirect
# Create your views here.


@LoginRedirect
def Login(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        user = authenticate(username=name, password=password)
        if user:
            login(request, user)
            if user.type == "student":
                return redirect("student-home")
            else:
                return redirect("doctor-home")
        else:
            return HttpResponse("<h1>Wrong credential</h1>")

    else:
        return render(request, "auth/login.html")


def Register(request):
    return render(request, "auth/register.html", {"studentReg": studentRegForm, "doctorReg": doctorRegForm})
