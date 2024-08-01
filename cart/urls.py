from django.urls import path
from cart.views import Buy, SaveOrder, CartDetail

app_name = "cart"

urlpatterns = [
    path('buy/', Buy.as_view(), name="buy"),
    path('saveorder/', SaveOrder.as_view(), name="saveorder"),
    path('cartdetail/', CartDetail.as_view(), name="cartdetail"),
]
