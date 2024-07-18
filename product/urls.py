from django.urls import path
from product.views import ProductListView, ProductDetailView, AddToCart, RemoveFromCart, CartListView, Finish

app_name = "product"

urlpatterns = [
    path('', ProductListView.as_view(), name="productlist"),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name="productdetail"),
    path('addtocart/', AddToCart.as_view(), name="addtocart"),
    path('removefromcart/', RemoveFromCart.as_view(), name="removefromcart"),
    path('cart/', CartListView.as_view(), name="cart"),
    path('finish/', Finish.as_view(), name="finish"),
]
