from django import forms
from .models import Post, Tag
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "author", "body", "tags", "slug", "status"]

    def clean_slug(self):
        new_slug = self.cleaned_data["slug"].lower()
        if new_slug == "create":
            raise ValidationError("Slug may not be 'create'")
        return new_slug
