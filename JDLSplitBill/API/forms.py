from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("domain", "first_name", "last_name",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields
