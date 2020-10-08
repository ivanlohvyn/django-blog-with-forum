from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse

from .forms import TopicForm
from .models import Message, Topic


def topic_list(request):
    latest_topic_list = Topic.objects.order_by("-created")[:10]
    return render(
        request,
        "forum/topic_list.html",
        context={"latest_topic_list": latest_topic_list},
    )


def topic_create(request):
    form = TopicForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            topic = form.save()
            return HttpResponseRedirect(
                reverse("forum:topic_detail", args=(topic.slug,))
            )
    else:
        form = TopicForm()
    return render(request, "forum/topic_create.html", {"form": form})


def topic_detail(request, slug):
    topic = get_object_or_404(Topic, slug__iexact=slug)
    message_list = topic.message_set.order_by("pub_date")
    return render(
        request,
        "forum/topic_detail.html",
        context={"topic": topic, "message_list": message_list},
    )
