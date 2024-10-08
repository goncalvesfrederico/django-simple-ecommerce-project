from django.urls import path
from cart.views import Buy, SaveOrder, CartDetail, Orders, OrderDetail

app_name = "cart"

urlpatterns = [
    path('buy/<int:pk>', Buy.as_view(), name="buy"),
    path('saveorder/', SaveOrder.as_view(), name="saveorder"),
    path('cartdetail/', CartDetail.as_view(), name="cartdetail"),
    path('orders/', Orders.as_view(), name="orders"),
    path('order-detail/<int:pk>', OrderDetail.as_view(), name="orderdetail"),
]
