from django.db import models
from django.contrib.auth import get_user_model
from emoji_picker.widgets import EmojiPickerTextInputAdmin

class Journal(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    feeling = models.CharField(widget=EmojiPickerTextInputAdmin)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
