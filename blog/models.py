import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    STATUS_CHOICES = (
        ("PUBLISHED", "published"),
        ("UPDATED", "updated"),
    )
    title = models.CharField(max_length=250, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    body = models.TextField()
    tags = models.ManyToManyField("Tag", blank=True, related_name="posts")
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default="published"
    )

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

    def was_updated_recently(self):
        return self.updated >= timezone.now() - datetime.timedelta(days=1)


class Tag(models.Model):
    title = models.CharField(max_length=30, db_index=True)
    slug = models.SlugField(max_length=30, blank=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.title
