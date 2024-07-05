from django.contrib import admin
from . import forms

from .models import User


class UserAdmin(admin.ModelAdmin):
    form = forms.RegisterUserForm
    list_display = ('email', 'first_name', 'id')
    list_display_links = ('email', 'id', )


admin.site.register(User, UserAdmin)
