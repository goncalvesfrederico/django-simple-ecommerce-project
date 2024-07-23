from typing import Any
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpRequest, HttpResponse
from user_profile.models import Profile
from user_profile.forms import UserForm, ProfileForm

class PerfilBase(View):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._template_name = "user_profile/create.html"
        self._context = {}

    def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:
        super().setup(request, *args, **kwargs)

        if request.user.is_authenticated:
            self._context.update(
                {
                    "userform": UserForm(data=request.POST or None, user=request.user, instance=request.user),
                    "profileform": ProfileForm(data=request.POST or None),
                }
            )
        else:
            self._context.update(
                {
                    "userform": UserForm(data=request.POST or None),
                    "profileform": ProfileForm(data=request.POST or None),
                }
            )
        self.render = render(request, self._template_name, self._context)

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return self.render


class Create(PerfilBase):
    def post(self, *args, **kwargs):
        return self.render


class Update(View):
    ...


class Login(View):
    ...


class Logout(View):
    ...
