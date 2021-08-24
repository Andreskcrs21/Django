from django.http import request
from django.shortcuts import render

# Create your views here.
def matricula(request):
    return render(request, "AppMatricula/matricula.html")