from django.urls import path
from user_profile.views import Create, Update, Login, Logout

app_name = "user_profile"

urlpatterns = [
    path('', Create.as_view(), name="create"),
    path('update/', Update.as_view(), name="udpate"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
]
