from django.shortcuts import render
from sinal.models import Sinal
from django.views.generic.base import View
from sinal.forms import RegistrarSinalForm
from django.shortcuts import redirect

def index(request):
    return render(request, 'index.html', {'sinais': Sinal.objects.all()})

def exibir(request, sinal_id):
    sinal = Sinal.objects.get(id=sinal_id)
    return render(request, 'sinal.html', {"sinal": sinal})

class RegistrarSinalView(View):
    template_name = 'registrar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegistrarSinalForm(request.POST)

        if form.is_valid():
            dados_form = form.data

            sinal = Sinal(configuracao_da_mao=dados_form['configuracao_da_mao'],
                          ponto_de_articulacao=dados_form['ponto_de_articulacao'],
                          movimento=dados_form['movimento'],
                          orientacao_das_maos=dados_form['orientacao_das_maos'],
                          expressao_facil_corporal=dados_form['expressao_facil_corporal'],
                          nome=dados_form['nome'])

            sinal.save()

            return redirect('index')


            # configuracao_da_mao = '1111', ponto_de_articulacao = '1111', movimento = '1111', orientacao_das_maos = '1111', expressao_facil_corporal = '1111', nome = 'odio'

        return render(request, self.template_name, {'form': form})