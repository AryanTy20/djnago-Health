from unicodedata import name
from django.urls import path
from .views import Home, Register, Logout


urlpatterns = [
    path("", Home, name="doctor-home"),
    path("register", Register, name="doctor-register"),
    path("logout", Logout, name="doctor-logout")
]
