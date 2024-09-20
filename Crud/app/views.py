from django.shortcuts import render
from django.http import HttpResponse
from app.forms import EgressosForm

def home(request):
    data = {}
    return render(request, 'home.html')

def form(request):
    data = {}
    data['form'] = EgressosForm()
    return render(request, 'form.html', data)