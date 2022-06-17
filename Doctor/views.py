from django.shortcuts import redirect, render, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth import logout, login, authenticate
from Auth.forms import doctorRegForm
from Auth.models import Doctor
from .decorators import loginRequired
# Create your views here.


@loginRequired
def Home(request):
    return render(request, "doctor/home.html")


@require_POST
def Register(request):
    if request.method == 'POST':
        form = doctorRegForm(request.POST)
        if form.is_valid:
            form.save()
            user = authenticate(username=request.POST.get(
                "name"), password=request.POST.get("password1"))
            login(request, user)
            return redirect("doctor-home")
        else:
            return HttpResponse("<h1>something went wrong</h1>")
    else:
        return


def Logout(request):
    logout(request)
    return redirect("login")
