from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from user_profile.models import Profile
from product.models import Variation
from cart.models import Order, OrderItems
from utils.utils import qty_items, cart_total

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
            "page_title": "Cart Detail - "
        }
        return render(self.request, self.template_name, context)


class SaveOrder(View):
    template_name = "cart/saveorder.html"

    def get(self, *args, **kwargs):
        user = self.request.user
        cart = self.request.session.get("cart")

        if not user.is_authenticated:
            messages.error(self.request, "You must be logged in.")
            return redirect("user_profile:login")
        
        if not cart:
            messages.warning(self.request, "Your cart is empty! Please add the products to card!")
            return redirect("/")
        
        cart_items_ids = [i for i in cart]
        db_variations = list(Variation.objects.filter(id__in=cart_items_ids))
        
        for variation in db_variations:
            vid = str(variation.id)
            stock = variation.stock
            quantity_cart = cart[vid]["quantity"]
            unit_price = cart[vid]["unit_price"]
            unit_promotional_price = cart[vid]["unit_promotional_price"]
            error_messages = ""

            if stock < quantity_cart:
                cart[vid]["quantity"] = stock
                cart[vid]["total_price"] = stock * unit_price
                cart[vid]["full_promotional_price"] = stock * unit_promotional_price
                error_messages = "Insufficient stock for some items in your cart. Please check which items are affected"

            if error_messages:
                messages.error(self.request, error_messages)
                self.request.session.save()
                return redirect("product:cart")

        qty_total_cart = qty_items(cart)
        total_price_cart = cart_total(cart)
        save_order = Order(
            user=user,
            total=total_price_cart,
            total_qty=qty_total_cart,
            status="C",
        )
        save_order.save()

        OrderItems.objects.bulk_create(
            [
                OrderItems(
                    order=save_order,
                    product=v["product_name"],
                    product_id=v["product_id"],
                    variation=v["variation_name"],
                    variation_id=v["variation_id"],
                    price=v["total_price"],
                    promotional_price=v["full_promotional_price"],
                    quantity=v["quantity"],
                    image=v["product_image"],
                ) for v in cart.values()
            ]
        )

        del self.request.session["cart"]
        return redirect(
            reverse(
                "cart:buy",
                kwargs={"pk": save_order.pk},
            )
        )


class Buy(LoginRequiredMixin, DetailView):
    login_url = "user_profile:login"
    template_name = "cart/buy.html"
    model = Order
    pk_url_kwarg = "pk"
    context_object_name = "order"

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(user=self.request.user)
    

class Orders(LoginRequiredMixin, ListView):
    login_url = "user_profile:login"
    template_name = "cart/orders.html"
    model = Order
    context_object_name = "orders"
    paginate_by = 5
    ordering = ["-id"]

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(user=self.request.user)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Your orders - "
        return context


class OrderDetail(LoginRequiredMixin, DetailView):
    login_url = "user_profile:login"
    template_name = "cart/order-detail.html"
    model = Order
    context_object_name = "order"
    pk_url_kwarg = "pk"

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(user=self.request.user)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["page_title"] = f"{self.object} - "
        return context