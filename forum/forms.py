from django import forms
from django.core.exceptions import ValidationError

from .models import Message, Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        user = forms.ModelMultipleChoiceField(queryset=None)
        fields = ["title", "tags", "slug", "status"]

    def clean_slug(self):
        new_slug = self.cleaned_data["slug"].lower()
        if new_slug == "create":
            raise ValidationError("Slug may not be 'create'")
        return new_slug

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']
