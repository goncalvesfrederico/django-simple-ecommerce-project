from django.urls import path
from user_profile.views import LoginView, CreateView

app_name = "user_profile"

urlpatterns = [
    path('', CreateView.as_view(), name="create"),
    # path('update/', Update.as_view(), name="udpate"),
    path('login/', LoginView.as_view(), name="login"),
    # path('logout/', Logout.as_view(), name="logout"),
]
