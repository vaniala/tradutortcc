from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def exibir(request):
    return render(request, 'sinal.html')