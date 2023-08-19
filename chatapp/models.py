from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_credit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


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
    key = models.CharField(max_length=500)

    def __str__(self):
        return self.title
    

class StripKey(models.Model):
    title = models.CharField(max_length=200)
    public_key = models.CharField(max_length=500, null=True, blank=True)
    secrect_key = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title
    

class ApiCost(models.Model):
    title = models.CharField(max_length=500, default="API Cost Per 1k Words")
    cost_amount = models.FloatField(default=0.5)
    
    def __str__(self):
        return self.title