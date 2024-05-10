from django.db import models

# Create your models here.

class Cargo(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    cargo = models.ForeignKey(Cargo,default=2 , on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome
    


