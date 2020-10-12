from django.contrib import admin

from .models import Message, Topic, Like

admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Like)
