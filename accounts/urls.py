from django.urls import path
from .views import GetUserToken, RegisterUser, ReadUpdateUser
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("token/", GetUserToken.as_view(), name="get_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="get_refresh_token"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("user/", ReadUpdateUser.as_view(), name="user"),
]
