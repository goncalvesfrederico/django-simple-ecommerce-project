from typing import Any
from django import forms
from user_profile.models import Profile
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ["user"]


class UserForm(forms.ModelForm):
    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user = user

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password"]

    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
