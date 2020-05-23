from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import CustomUser
from .forms import CustomUserCreationForm,CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email","username","account_name","is_staff",]



admin.site.register(CustomUser,CustomUserAdmin)
