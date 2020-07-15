from django import forms
from django.contrib import admin
from api.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'last_login', 'email', 'password']
        widgets = {'password': forms.PasswordInput}


class UserAdmin(admin.ModelAdmin):
    form = UserForm
