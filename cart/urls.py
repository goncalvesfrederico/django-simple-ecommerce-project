from django.urls import path
from cart.views import Buy, Checkout, CartDetail

app_name = "cart"

urlpatterns = [
    path('', Buy.as_view(), name="buy"),
    path('checkout/', Checkout.as_view(), name="checkout"),
    path('cartdetail', CartDetail.as_view(), name="cartdetail"),
]
