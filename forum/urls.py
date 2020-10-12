from django.urls import path

from forum import views

app_name = "forum"

urlpatterns = [
    path("topic_list", views.topic_list, name="topic_list"),
    path("topic_create/", views.topic_create, name="topic_create"),
    path("<str:slug>/", views.topic_detail, name="topic_detail"),
    path("<str:slug>/send_message/", views.send_message, name="send_message"),
    path("like_message", views.like_message, name="like_message"),
]
