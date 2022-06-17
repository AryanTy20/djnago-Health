from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import logout, login, authenticate
from Auth.forms import studentRegForm
from Auth.models import Student
from django.views.decorators.http import require_POST
from .decorators import loginRequired


@loginRequired
def Home(request):
    user = Student.objects.get(name=request.user)
    print(user)
    return render(request, "student/home.html")


@require_POST
def Register(request):
    if request.method == 'POST':
        form = studentRegForm(request.POST)
        if form.is_valid:
            form.save()
            name = request.POST.get("name")
            password = request.POST.get("password1")
            user = authenticate(username=name, password=password)
            login(request, user)
            return redirect("student-home")
        else:
            return HttpResponse("<h1>something went wrong</h1>")
    else:
        return


def Logout(request):
    logout(request)
    return redirect("login")
