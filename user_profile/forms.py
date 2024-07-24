from django import forms
from user_profile.models import Profile
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ["user"]


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text="Required.",
        error_messages={
            "min_length": "Please, add more than 2 letters.",
        },
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text="Required.",
        error_messages={
            "min_length": "Please, add more than 2 letters."
        }
    )
    email = forms.EmailField(
        required=True,
        help_text="Required",
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]

    def clean(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        if first_name == last_name:
            msg = "The First Name and Last Name could not be the same!!!"
            self.add_error("last_name", ValidationError(msg))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            msg = "This username already exists!"
            self.add_error(
                "username",
                ValidationError(msg, code="invalid")
            )
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            msg = "This email already exists!"
            self.add_error(
                "email",
                ValidationError(msg, code="invalid")
            )
        return email