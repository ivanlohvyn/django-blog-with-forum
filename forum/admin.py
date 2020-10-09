from django.contrib import admin

from .models import Message, Topic

admin.site.register(Topic)
admin.site.register(Message)
