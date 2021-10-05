from django.urls import path
from .views import account
from .apps import AuthConfig

app_name = AuthConfig.name

urlpatterns = [
    path("register/", account.RegisterView.as_view(), name="register"),
    path("login/", account.LoginView.as_view(), name="login")
]
