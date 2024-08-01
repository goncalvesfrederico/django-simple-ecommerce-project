from django.shortcuts import render, redirect
from django.views.generic import View

class CartDetail(View):
    template_name = "cart/cartdetail.html"

    def get(self, *args, **kwargs):
        user = self.request.user
        cart = self.request.session.get("cart")

        if not user.is_authenticated:
            return redirect("user_profile:login")
        
        context = {
            "user": user,
            "cart": cart,
        }
        return render(self.request, self.template_name, context)


class Buy(View):
    ...


class SaveOrder(View):
    ...