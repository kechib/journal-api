from django.db import models
from django.contrib.auth import get_user_model


class Journal(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    feeling = models.CharField(max_length=100)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

def __str__(self):
    # This must return a string
    return f"Your entry title '{self.title}' was created at '{self.created_at}'  with content {self.content} that was updated at '{self.updated_at}'. You are feeling {self.feeling}."
def as_dict(self):
    """Returns dictionary version of Journal models"""
    return {
        'id': self.id,
        'title': self.title,
        'content': self.content,
        'created_at': self.created_at,
        'updated_at': self.updated_at,
        'feeling': self.feeling
    }
