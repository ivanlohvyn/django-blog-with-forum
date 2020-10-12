import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from blog.models import Tag


class Topic(models.Model):
    STATUS_CHOICES = (
        ("ACTIVE", "active"),
        ("CLOSED", "closed"),
    )
    title = models.CharField(max_length=250, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    pub_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.text

    def was_published_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "message"], name="unique_like_per_user"
            )
        ]
