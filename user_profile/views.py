from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import FormView, View
from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from user_profile.forms import CreateUserForm, ProfileForm

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

    def post(self, request, *args: str, **kwargs) -> HttpResponse:
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
            return self.form_valid(create_form, profile_form)

    def form_valid(self, create_form, profile_form):
        context = self.get_context_data()
        context["create_form"] = create_form
        context["profile_form"] = profile_form
        print(context)
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

    def get(self, request):
        print(self.request)
        auth.logout(request)
        return redirect("user_profile:login")