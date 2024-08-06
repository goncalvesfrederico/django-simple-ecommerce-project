from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View
from user_profile.models import Profile

class CartDetail(View):
    template_name = "cart/cartdetail.html"

    def get(self, *args, **kwargs):
        user = self.request.user
        cart = self.request.session.get("cart")
        profile = Profile.objects.filter(user=user)
        cpf = profile.filter(cpf="")

        if not user.is_authenticated:
            return redirect("user_profile:login")
        
        if cpf:
            messages.error(self.request, "Your profile is not complete. Please update it.")
            return redirect("user_profile:update")
        
        if not cart:
            messages.warning(self.request, "Your cart is empty! Please add the products to card!")
            return redirect("/")
        
        context = {
            "user": user,
            "cart": cart,
        }
        return render(self.request, self.template_name, context)


class Buy(View):
    ...


class SaveOrder(View):
    ...