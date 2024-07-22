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
        # if self.request.session.get("cart"):
        #     del self.request.session["cart"]
        #     self.request.session.save()

        http_referer = self.request.META.get("HTTP_REFERER", reverse("product:productlist"))
        variation_id = self.request.GET.get("vid")

        if not variation_id:
            messages.error(self.request, "Product not found!")
            return redirect(http_referer)

        variation = get_object_or_404(Variation, id=variation_id)
        variation_stock = variation.stock
        product = variation.product
        product_id = product.pk
        product_name = product.name
        variation_name = variation.name or ""
        unit_price = variation.price
        unit_promotional_price = variation.promotion_price
        quantity = 1
        product_slug = product.slug
        product_image = product.image.name if product.image else ""

        if variation_stock < 1:
            messages.error(self.request, "Insufficient stock")
            return redirect(http_referer)

        # if cart does not exist in session, then create the cart.
        if not self.request.session.get("cart"):
            self.request.session["cart"] = {}
            self.request.session.save()

        cart = self.request.session["cart"]
        if variation_id in cart:
            cart_quantity = cart[variation_id]["quantity"]
            cart_quantity += 1

            if variation_stock < cart_quantity:
                messages.warning(self.request, f"Insufficient stock for {cart_quantity}x on {product_name} product. Added {variation_stock}x to your cart.")
                cart_quantity = variation_stock
            
            cart[variation_id]["quantity"] = cart_quantity
            cart[variation_id]["total_price"] = unit_price * cart_quantity
            cart[variation_id]["full_promotional_price"] = unit_promotional_price * cart_quantity
        else:
            cart[variation_id] = {
                "product_id": product_id,
                "product_name": product_name,
                "variation_name": variation_name,
                "variation_id": variation_id,
                "unit_price": unit_price,
                "unit_promotional_price": unit_promotional_price,
                "total_price": unit_price,
                "full_promotional_price": unit_promotional_price,
                "quantity": quantity,
                "product_slug": product_slug,
                "product_image": product_image,
            }

        # print(cart)
        self.request.session.save()

        messages.success(self.request, f"The {product_name} {variation_name} product has been added to your cart {cart[variation_id]["quantity"]}x.")
        return redirect(http_referer)


class DeleteFromCart(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get("HTTP_REFERER", reverse("product:productlist"))
        variation_id = self.request.GET.get("vid")

        if not variation_id:
            return redirect(http_referer)
        
        if not self.request.session.get("cart"):
            return redirect(http_referer)
        
        if variation_id not in self.request.session["cart"]:
            return redirect(http_referer)
        
        cart = self.request.session["cart"][variation_id]
        messages.success(self.request, f"Product {cart["product_name"]} {cart["variation_name"]} has been removed from your cart.")

        del self.request.session["cart"][variation_id]
        self.request.session.save()

        return redirect(http_referer)


class CartListView(View):
    def get(self, *args, **kwargs):
        context = self.request.session.get("cart")
        return render(
            self.request, 
            "product/cart.html", 
            {
                "cart": context,
            }
        )


class CheckoutView(View):
    ...