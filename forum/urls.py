from django.urls import path

from forum import views

app_name = "forum"

urlpatterns = [
    path("topic_list", views.topic_list, name="topic_list"),
    path("topic_create/", views.topic_create, name="topic_create"),
    path("<str:slug>/topic_detail/", views.topic_detail, name="topic_detail"),
]
