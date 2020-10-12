from django.urls import path

from account import views

app_name = "account"

urlpatterns = [
    path("sign/", views.sign, name="sign"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
