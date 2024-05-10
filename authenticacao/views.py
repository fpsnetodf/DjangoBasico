from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa, Cargo


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
    # dados = Pessoa.objects.filter(senha = "Paulo1234")[0]
    # adm = Cargo.objects.filter(id=1)[0]
    # dados = Pessoa.objects.filter(nome__startswith="Bruno")[0]
    # dados.cargo_id = adm
    # dados.save() 
    pessoas = Pessoa.objects.filter(cargo__pk = 2).filter(senha = "rcs1234") | Pessoa.objects.filter(nome__icontains = "alanna")
    # pessoas = Pessoa.objects.filter(nome__startswith='Francisco')| Pessoa.objects.filter(email='bl@gmail.com')
    # pessoas.delete()
    return render (request, 'authenticacao/listar.html', {'pessoas': pessoas})
