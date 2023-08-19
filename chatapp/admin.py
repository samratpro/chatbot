from django.contrib import admin
from .models import *


admin.site.register(Chat)
admin.site.register(ChatMessage)
admin.site.register(OpenAIKey)
admin.site.register(StripKey)
admin.site.register(UserProfile)
admin.site.register(ApiCost)

# Register your models here.
