from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa


# Create your views here.

def home(request):
    if request.method == 'GET': 
        pessoas = Pessoa.objects.all()   
        return render(request, 'authenticacao/home.html', {'pessoas': pessoas})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        pessoa = Pessoa(nome = nome, email = email, senha = senha)
        pessoa.save()
        return render(request, 'authenticacao/home.html', {'nome': nome, 'email': email, 'senha': senha})

def listar(request):
    pessoas = Pessoa.objects.filter(nome__startswith='Francisco')| Pessoa.objects.filter(email='bl@gmail.com')
    # pessoas.delete()
    return render (request, 'authenticacao/listar.html', {'pessoas': pessoas})
