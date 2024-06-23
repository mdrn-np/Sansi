from django.urls import path, include

urlpatterns = [
    path("topics/", include("topics.urls")),
]
