from django.contrib import admin
from .models import Pessoa, Cargo

# Register your models here.


admin.site.register(Pessoa)
admin.site.register(Cargo)