import datetime

from blog.models import Tag
from django.db import models
from django.utils import timezone


class Topic(models.Model):
    STATUS_CHOICES = (
        ("ACTIVE", "active"),
        ("CLOSED", "closed"),
    )
    title = models.CharField(max_length=250, db_index=True)
    author = models.CharField(max_length=100, db_index=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name="topics")
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="active")

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)


class Message(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, db_index=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.text

    def was_published_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)
