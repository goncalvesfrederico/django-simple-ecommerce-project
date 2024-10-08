from django.urls import path
from user_profile.views import LoginView, CreateView, LogoutView, PerfilUpdateView

app_name = "user_profile"

urlpatterns = [
    path('', LoginView.as_view(), name="login"),
    path('create/', CreateView.as_view(), name="create"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('update_profile/', PerfilUpdateView.as_view(), name="update"),
]
