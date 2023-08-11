from django.db import models
from django.contrib.auth.models import User




class Chat(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_cookie = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    prompt = models.TextField(null=True, blank=True)
    replay = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} - {self.chat}"


class OpenAIKey(models.Model):
    title = models.CharField(max_length=200)
    key = models.CharField(max_length=300)

    def __str__(self):
        return self.title
    

class StripKey(models.Model):
    title = models.CharField(max_length=200)
    key = models.CharField(max_length=300)

    def __str__(self):
        return self.title