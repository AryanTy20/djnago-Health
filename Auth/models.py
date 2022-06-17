import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

    def _create_user(self, name, email, password, age, gender, address, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            name=name,
            age=age,
            gender=gender,
            address=address,
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name=None, email=None, password=None, age=None, gender=None, address=None, **extra_fields):
        return self._create_user(name, email, password, age, gender, address, False, False, **extra_fields)

    def create_superuser(self, name, email, password, **extra_fields):
        user = self._create_user(
            name, email, password, is_staff=True, is_superuser=True, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    genderchoices = [
        (None, "Select Gender"),
        ("Male", "male"),
        ("Female", "female"),
    ]

    # profilepic = models.ImageField(_("profile pic"))
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=254, null=True, unique=True, blank=True)
    email = models.EmailField(_("email"), max_length=50)
    age = models.CharField(max_length=2, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    gender = models.CharField(
        max_length=6, choices=genderchoices, default=None, blank=True, null=True)
    address = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Types(models.TextChoices):
        STUDENT = "student", "STUDENT"
        DOCTOR = "doctor", "DOCTOR"
        ADMIN = "admin", "ADMIN"

    default_type = Types.ADMIN
    type = models.CharField(
        max_length=10, choices=Types.choices, default=default_type, blank=True, null=True)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = [
        "email", "age", "phone", "gender", "address"
    ]

    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = self.default_type
        return super().save(*args, **kwargs)


# Additionals

# class studentAdditional():
#     departmentchoice = [
#         (None, "select Department"),
#         ("Mtech-civil", "mtech"),
#         ("MCA", "mca"),
#         ("Mtech-cs", "mtechcs"),
#     ]

#     regNo = models.CharField(_("Registration Number"),
#                              unique=True, max_length=20)
#     name = models.OneToOneField(
#         User, on_delete=models.CASCADE)
#     department = models.CharField(
#         max_length=50, choices=departmentchoice, default=None, blank=False)

#     def __str__(self):
#         return self.name + " | " + self.department


# class doctorAdditional():
#     name = models.OneToOneField(
#         User, on_delete=models.CASCADE)
#     specialization = models.CharField(max_length=40)
#     yearofex = models.CharField(max_length=2)

#     def __str__(self):
#         return self.name + " | " + self.specialization


# managers
class studentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type="student")


class doctorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type="doctor")


class Student(User):
    default_type = User.Types.STUDENT
    objects = studentManager()
    departmentchoice = [
        (None, "select Department"),
        ("Mtech-civil", "mtech"),
        ("MCA", "mca"),
        ("Mtech-cs", "mtechcs"),
    ]

    regNo = models.CharField(_("Registration Number"),
                             unique=True, max_length=20)
    department = models.CharField(
        max_length=50, choices=departmentchoice, default=None, blank=False)

    def __str__(self):
        return self.name + " | " + self.department

    class Meta:
        proxy: True

    # def showAdditional(self):
    #     return self.studentadditional


class Doctor(User):
    default_type = User.Types.DOCTOR
    objects = doctorManager()
    specialization = models.CharField(max_length=40)
    yearofex = models.CharField(_("exprience in year"), max_length=2)

    class Meta:
        proxy: True

    def __str__(self):
        return self.name + " | " + self.specialization


# class user_type(models.Model):
#     is_doctor = models.BooleanField(default=False)
#     is_patient = models.BooleanField(default=False)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         if self.is_patient == True:
#             return User.get_name(self.user) + " - is_patient"
#         else:
#             return User.get_name(self.user) + " - is_doctor"


# class Student(models.Model):

#     departmentchoice = [
#         (None, "select Department"),
#         ("Mtech-civil", "mtech"),
#         ("MCA", "mca"),
#         ("Mtech-cs", "mtechcs"),
#     ]

#     regNo = models.CharField(_("Registration Number"),
#                              unique=True, max_length=20)
#     name = models.OneToOneField(
#         User, on_delete=models.CASCADE)
#     department = models.CharField(
#         max_length=50, choices=departmentchoice, default=None, blank=False)

#     def __str__(self):
#         return self.name + " | " + self.department


# class Doctor(models.Model):

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.OneToOneField(
#         User, on_delete=models.CASCADE)
#     specialization = models.CharField(max_length=40)
#     yearofex = models.CharField(max_length=2)

#     def __str__(self):
#         return self.name + " | " + self.specialization
