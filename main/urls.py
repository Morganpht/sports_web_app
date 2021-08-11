from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.sign_in, name="sign-in"),
    path("register", views.register_request, name="register"),
]