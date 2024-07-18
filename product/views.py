from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.views.generic import ListView, DetailView, View
from product.models import Product, Variation

class ProductListView(ListView):
    model = Product
    template_name = "product/list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product/product.html"
    context_object_name = 'product'


class AddToCart(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get("HTTP_REFERER", reverse("product:productlist"))
        variation_id = self.request.GET.get("vid")

        if not variation_id:
            messages.error(self.request, "Product not found!")
            return redirect(http_referer)

        variation = get_object_or_404(Variation, id=variation_id)

        # if cart does not exist in session, then create the cart.
        if not self.request.session.get("cart"):
            self.request.session["cart"] = {}
            self.request.session.save()

        cart = self.request.session["cart"]
        if variation_id in cart:
            #TODO: create a exists cart
            ...
        else:
            #TODO: variation does not exist in cart.
            ...

        return HttpResponse(f"{variation.product} - {variation.name}")


class RemoveFromCart(View):
    ...


class CartListView(View):
    ...


class Finish(View):
    ...