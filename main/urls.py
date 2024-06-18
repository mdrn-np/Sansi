from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("todo/", include("todo.urls")),
    path("accounts/", include("accounts.urls")),
]
