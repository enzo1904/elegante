from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def inicio(request):
    return render(request,'users/iniciosesion.html')

def registro(request):
    return render(request,'users/registro.html')

def barbero(request):
    return render(request,'users/barberos.html')
