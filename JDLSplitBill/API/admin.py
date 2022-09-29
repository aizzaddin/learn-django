from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = [
        "domain",
        "email",
        "first_name"
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("domain", )}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("domain", "first_name")}),)


admin.site.register(User, CustomUserAdmin)
