from typing import Any
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


class UserForm(forms.ModelForm):
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
    password = forms.CharField(
        required=False, 
        widget=forms.PasswordInput(),
        help_text=password_validation.password_validators_help_text_html()
    )
    password2 = forms.CharField(
        required=False, 
        widget=forms.PasswordInput(), 
        label="Confirm Password", 
        help_text="Use the same password as before."
    )
    
    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user = user

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "username", "password", "password2"]

    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        first_name_data = cleaned_data.get("first_name")
        last_name_data = cleaned_data.get("last_name")
        user_data = cleaned_data.get("username")
        password_data = cleaned_data.get("password")
        password2_data = cleaned_data.get("password2")
        email_data = cleaned_data.get("email")
        user_db = User.objects.filter(username=user_data).exists()
        email_db = User.objects.filter(email=email_data).exists()

        if self.user:
            if first_name_data == last_name_data:
                msg = "The First Name and Last Name could not be the same!!!"
                self.add_error("last_name", ValidationError(msg))
            
            if user_db:
                if user_data != user_db:
                    msg = "User already exists!"
                    self.add_error("username", ValidationError(msg))

            # validation the passwords
            if password_data or password2_data:
                if password_data != password2_data:
                    msg = "Passwords do NOT match!!!"
                    self.add_error("password2", ValidationError(msg))

            # validation if email already exists from created user ... consulting in database
            if email_db:
                msg = "This email already exists in database!"
                self.add_error("email", ValidationError(msg, code="invalid"))