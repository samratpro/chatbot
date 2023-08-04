from django.db import models
from django.contrib.auth.models import User


class ChatCategory(models.Model):
    name = models.CharField(max_length=250)
    time = models.TimeField(null=True, blank=True)
    pdf_data = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Chat(models.Model):
    name = models.ForeignKey(ChatCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    pdf_data = models.TextField(blank=True, null=True)
    output = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)

