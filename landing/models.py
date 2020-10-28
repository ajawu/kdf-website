from django.db import models
from django.utils import timezone


class Contact(models.Model):
    sender_email = models.EmailField()
    message_title = models.CharField(max_length=250)
    message_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
