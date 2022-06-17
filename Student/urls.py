from django.urls import path

from django.urls import path
from .views import Home, Logout, Register


urlpatterns = [
    path("", Home, name="student-home"),
    path("register", Register, name="student-register"),
    path("logout", Logout, name="student-logout")
]
