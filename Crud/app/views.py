from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    data = {}
    return render(request, 'home.html')

def form(request):
    return render(request, 'form.html')