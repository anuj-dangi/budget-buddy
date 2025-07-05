from django.shortcuts import render
from django.http import HttpResponse
import pyrebase

# Firebase configuration
firebase_config = {
    
}

def index(request):
    return render(request, 'index.html')