import copy
from typing import Any
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import FormView, View
from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from user_profile.forms import CreateUserForm, ProfileForm, UpdateUserForm
from user_profile.models import Profile

class CreateView(FormView):
    template_name = "user_profile/create.html"
    form_class = CreateUserForm
    success_url = reverse_lazy("user_profile:login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "create_form": context.pop("form"),
                "profile_form": ProfileForm(),
            }
        )
        return context

    def post(self, request, *args, **kwargs) -> HttpResponse:
        create_form = CreateUserForm(self.request.POST)
        profile_form = ProfileForm(self.request.POST)

        if create_form.is_valid() and profile_form.is_valid():
            user = create_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(self.request, "Your account has been created.")
            return self.form_valid(create_form, profile_form)
        else:
            return self.form_invalid(create_form, profile_form)

    def form_valid(self, create_form, profile_form):
        return super().form_valid(create_form)
    
    def form_invalid(self, create_form, profile_form):
        context = self.get_context_data()
        context["create_form"] = create_form
        context["profile_form"] = profile_form
        return self.render_to_response(context)


class LoginView(FormView):
    template_name = "user_profile/login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy("product:productlist")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["login_form"] = context.pop("form")
        return context

    def form_valid(self, form):
        user = form.get_user()
        auth.login(self.request, user=user)
        messages.success(self.request, "You are sucessfully logged in!")
        return super().form_valid(form)
    

class LogoutView(LoginRequiredMixin, View):
    login_url = "user_profile:login"

    def get(self, *args, **kwargs):
        cart_saved = copy.deepcopy(self.request.session.get("cart"))
        auth.logout(self.request)
        self.request.session["cart"] = cart_saved
        self.request.session.save()
        return redirect("user_profile:login")
    

class PerfilUpdateView(LoginRequiredMixin, FormView):
    template_name = "user_profile/update_profile.html"
    form_class = UpdateUserForm
    success_url = reverse_lazy("cart:cartdetail")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not hasattr(self.request.user, "profile"):
            Profile.objects.create(user=self.request.user, born=None)

        context.update(
            {
                "update_user_form": UpdateUserForm(instance=self.request.user),
                "update_profile_form": ProfileForm(instance=self.request.user.profile),
            }
        )
        return context
    
    def post(self, request, *args: str, **kwargs) -> HttpResponse:
        update_user_form = UpdateUserForm(self.request.POST, instance=self.request.user)
        update_profile_form = ProfileForm(self.request.POST, instance=self.request.user.profile)

        if update_user_form.is_valid() and update_profile_form.is_valid():
            user = update_user_form.save()
            profile = update_profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(self.request, "Your account has been updated.")
            return self.form_valid(update_user_form)
        else:
            messages.error(self.request, "Verify the form!")
            return self.form_invalid(update_user_form)
    
    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data()
        context["update_user_form"] = form
        context["update_profile_form"] = ProfileForm(instance=self.request.user.profile)
        return self.render_to_response(context)