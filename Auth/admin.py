from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Doctor, Student

admin.site.site_header = "Medical Service"
admin.site.site_title = "Admin Panel"

# admin.site.index_template = 'admin/home.html'
admin.autodiscover()


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name',
         "age", "gender", "phone", "address", 'last_login', "type")}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('name', 'is_staff',
                    "is_active", "type", "date_joined")
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)

    # filter_horizontal = ('groups', 'user_permissions')
admin.site.register(User, UserAdmin)


class doctorAdmin(BaseUserAdmin):
    fieldsets = (
        ("Doctor Details", {'fields': ('name', 'email', "type",
         "age", "gender", "phone", "specialization", "yearofex", "address", 'last_login', )}),
        ('Permissions', {'fields': ('is_active',)})
        # ('Permissions', {'fields': (
        #     'is_active',
        #     'is_staff',
        #     'is_superuser',
        #     'groups',
        #     'user_permissions',
        # )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ("name", 'email', "type", "age", "gender", "phone", "address", "specialization", "yearofex", 'password1', 'password2')

            }
        ),
    )

    list_display = ('name', "specialization", "yearofex", "last_login")
    search_fields = ('email', "name", "specialization", "yearofex", "gender")
    ordering = ('email',)

    # filter_horizontal =()
admin.site.register(Doctor, doctorAdmin)


class studentAdmin(BaseUserAdmin):
    fieldsets = (
        ("Student Details", {'fields': ('name', 'email', "type",
         "age", "gender", "phone", "address", 'last_login', )}),
        ('Permissions', {'fields': ('is_active',)})
        # ('Permissions', {'fields': (
        #     'is_active',
        #     'is_staff',
        #     'is_superuser',
        #     'groups',
        #     'user_permissions',
        # )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ("name", 'email', "type", "age", "gender", "phone", "address", 'password1', 'password2')

            }
        ),
    )

    list_display = ('name', "department", "last_login")
    search_fields = ('email', "name", "department", "gender")
    ordering = ('email',)

    # filter_horizontal =()
admin.site.register(Student, studentAdmin)
