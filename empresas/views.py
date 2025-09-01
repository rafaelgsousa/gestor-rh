from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Empresa

# Create your views here.

def home(request):
    return HttpResponse('olá')

class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']
