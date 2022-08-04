from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse("Olá, no que poderiamos te ajudar?<br><br>OPCOES")