from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, View
from product.models import Product

class ProductListView(ListView):
    model = Product
    template_name = "product/list.html"
    context_object_name = "products"
    paginate_by = 10


class ProductDetailView(View):
    ...


class AddToCart(View):
    ...


class RemoveFromCart(View):
    ...


class CartListView(View):
    ...


class Finish(View):
    ...