from django.urls import path

from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("post_list", views.post_list, name="post_list"),
    path("post_create/", views.post_create, name="post_create"),
    path("<str:slug>/", views.post_detail, name="post_detail"),
    path("tag_list", views.tag_list, name="tag_list"),
    path("<str:slug>/tag_detail", views.tag_detail, name="tag_detail"),
    path("tag_create", views.tag_create, name="tag_create"),
]
