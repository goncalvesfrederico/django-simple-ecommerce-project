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

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            msg = "This email already exists!"
            self.add_error(
                "email",
                ValidationError(msg, code="invalid")
            )
        return email


class UpdateUserForm(forms.ModelForm):
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
    password1 = forms.CharField(
        label="Password",
        strip=False,
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        strip=False,
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
            }
        ),
        help_text="Use the same password as before."
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get("password1")
        if password:
            user.set_password(password)
        if commit:
            user.save()

        return user

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 or password2:
            if password1 != password2:
                msg = "Passwords do NOT match!!!"
                self.add_error("password2", ValidationError(msg))

    # validation if email already exists from created user, if exists don't save and show the message
    def clean_email(self):
        email = self.cleaned_data.get("email")
        current_email = self.instance.email  # get the current_email if the user are logged. Using my view instance
        if current_email != email:
            if User.objects.filter(email=email).exists():
                msg = "This email already exists!"
                self.add_error(
                    "email",
                    ValidationError(msg, code="invalid")
                )
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    "password1",
                    ValidationError(errors)
                )
        return password1