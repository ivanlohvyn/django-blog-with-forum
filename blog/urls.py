from django.urls import path

from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("post_list", views.post_list, name="post_list"),
    path("<str:slug>/", views.post_detail, name="post_detail"),
]
