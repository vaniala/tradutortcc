from django.shortcuts import render
from sinal.models import Sinal

def index(request):
    return render(request, 'index.html')

def exibir(request, sinal_id):

    sinal = Sinal()

    if sinal_id == '1':
        sinal = Sinal('0000', '0000', '0000', '0000', '0000', 'amor')


    return render(request, 'sinal.html', { "sinal" : sinal})