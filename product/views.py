from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, View

class ProductListView(ListView):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return HttpResponse("ProductListView")


class ProductDetailView(DetailView):
    ...


class AddToCart(View):
    ...


class RemoveFromCart(View):
    ...


class CartListView(View):
    ...


class Finish(View):
    ...