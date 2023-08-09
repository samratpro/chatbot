from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import *
from pptx import Presentation
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
import openai

# Create your views here.

def home(request):
    template = 'home.html'
    
    context = {}
        
    return render(request, template, context) # Return for Templates


def dashboard(request):
    template = 'dashboard.html'
    chat_all = Chat.objects.all()
    context = {'chat_all':chat_all}
    return render(request, template, context) # Return for Templates



@login_required(login_url='login')
def new_chat(request):
    chat_all = Chat.objects.all()
    context = {'chat_all':chat_all}
    if request.method == 'POST':
        title = request.POST.get('title')
        chat = Chat.objects.create(title=title, user=request.user)
        return redirect('chat_detail', chat_id=chat.id)
    return render(request, 'new_chat.html', context)


@login_required(login_url='login')
def chat_detail(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    ChatData = ChatMessage.objects.filter(chat=chat)
    
    chat_all = Chat.objects.all()
    context = {'chat_all':chat_all, 'chat': chat, 'ChatData': ChatData}
    
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        sender = request.user
        replay = 'replay message'
        ChatMessage.objects.create(chat=chat, sender=sender, prompt=prompt, replay=replay)
        
        # Call OpenAI API to generate a response based on the user's message
        # Store the response in the database as a new message
        
        return redirect('chat_detail', chat_id=chat.id)

    return render(request, 'chat_detail.html', context)


@login_required(login_url='login/')  # login/  is custom login URL path
def delete_chat(request, chat_id):   # ```data_id``` should be pass in url as <data_id>
    data = Chat.objects.get(pk=chat_id)
    data.delete()
    return redirect('/dashboard')