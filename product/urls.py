from django.urls import path
from product.views import ProductListView, ProductDetailView, AddToCart, DeleteFromCart, CartListView

app_name = "product"

urlpatterns = [
    path('', ProductListView.as_view(), name="productlist"),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name="productdetail"),
    path('addtocart/', AddToCart.as_view(), name="addtocart"),
    path('deletefromcart/', DeleteFromCart.as_view(), name="deletefromcart"),
    path('cart/', CartListView.as_view(), name="cart"),
]