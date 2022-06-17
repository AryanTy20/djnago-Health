from dataclasses import field
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Student, Doctor


class studentRegForm(UserCreationForm):
    class Meta:
        model = Student
        fields = (
            "regNo", "name", "email", "age", "phone", "gender", "department", "password1", "password2", "address"
        )
        widgets = {
            "address": forms.Textarea(attrs={"rows": 3})
        }
        # exclude = ["password", "groups",
        #            "userpermissions", "is_superuser", "is_active", "is_staff"]


class doctorRegForm(UserCreationForm):
    class Meta:
        model = Doctor
        fields = (
            "name", "email", "age", "phone", "gender", "specialization", "yearofex", "password1", "password2", "address"
        )
        widgets = {
            "address": forms.Textarea(attrs={"rows": 3})
        }
