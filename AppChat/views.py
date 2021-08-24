from django.http import request
from django.shortcuts import render

# Create your views here.
def principal(request):
    return render(request, "principal/home.html")

def chat(request):
    return render(request, 'AppChat/chat.html')