from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect

from .models import Topic, Message


def topic_list(request):
    latest_topic_list = Topic.objects.order_by("-created")[:10]
    return render(
        request,
        "forum/topic_list.html",
        context={"latest_topic_list": latest_topic_list},
    )


def topic_detail(request, slug):
    topic = get_object_or_404(Topic, slug__iexact=slug)
    message_list = topic.message_set.order_by("pub_date")
    return render(
        request,
        "forum/topic_detail.html",
        context={"topic": topic, "message_list": message_list},
    )
