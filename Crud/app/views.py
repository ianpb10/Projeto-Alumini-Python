from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import EgressosForm
from app.models import Egressos
from django.core.paginator import Paginator

def home(request):
    data = {}
    # data['db'] = Egressos.objects.all()
    all = Egressos.objects.all()
    paginator = Paginator(all, 1)
    pages =request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'home.html', data)

def form(request):
    data = {}
    data['form'] = EgressosForm()
    return render(request, 'form.html', data)

def create(request):
    form = EgressosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    data = {'form': form}
    return render(request, 'form.html', data)  
  
def view(request, pk):
    data = {}
    data['db'] = Egressos.objects.get(cpf=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    db = Egressos.objects.get(cpf=pk)
    form = EgressosForm(instance=db)
    return render(request, 'form.html', {'form': form, 'db': db})


def update(request, pk):
    data = {}
    data['db'] = Egressos.objects.get(cpf=pk)
    form = EgressosForm(request.POST or None, instance=data['db']) 
    if form.is_valid():
        form.save()
    return redirect('home')

def delete(request, pk):
    db = Egressos.objects.get(cpf=pk)
    db.delete()
    return redirect('home')




