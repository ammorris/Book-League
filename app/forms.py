from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import CustomUser


User = get_user_model()


class UserSignupForm(UserCreationForm):
    username = forms.CharField(
        label="",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control",
            }
        ),
    )
    first_name = forms.CharField(
        label="",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "First name",
                "class": "form-control",
            }
        ),
    )
    last_name = forms.CharField(
        label="",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last name",
                "class": "form-control",
            }
        ),
    )
    email = forms.EmailField(
        label="",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control",
            }
        ),
    )
    password1 = forms.CharField(
        label="",
        max_length=30,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control",
            }
        ),
    )
    password2 = forms.CharField(
        label="",
        max_length=30,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Repeat password",
                "class": "form-control",
            }
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    readonly_fields = ("last_login", "groups", "date_joined", "user_permissions")
