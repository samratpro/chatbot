from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    template = 'home.html'
    
    context = {}
        
    return render(request, template, context) # Return for Templates


def dashboard(request):
    template = 'dashboard.html'
    
    context = {}
        
    return render(request, template, context) # Return for Templates