from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from DiabeticRetinopathy.forms import RegisterForm
from DiabeticRetinopathy.models import *

# Register your models here.
class user_admin(UserAdmin):

    add_form = RegisterForm

    list_display = ('username', 'user_id', 'email', 'staff','admin')
    search_fields = ('username', 'user_id', 'email', 'staff','admin')
    list_filter = ('username', 'user_id', 'email')
    ordering = ('username',)
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('name','email')}),
        ('Permissions', {'fields': ('admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
         ),
    )

admin.site.register(User, user_admin)

admin.site.register(Report)