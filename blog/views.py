from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect

from .models import Post, Tag


def index(request):
    return render(request, "blog/index.html")


def post_list(request):
    latest_post_list = Post.objects.order_by("-created")[:10]
    return render(
        request,
        "blog/post_list.html",
        context={"latest_post_list": latest_post_list},
    )


def post_detail(request, slug):
    post = get_object_or_404(Post, slug__iexact=slug)
    return render(request, "blog/post_detail.html", context={"post": post})
