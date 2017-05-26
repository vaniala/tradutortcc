from django.shortcuts import render, get_object_or_404
from sinal.models import Sinal
from django.views.generic.base import View
from sinal.forms import SinalForm
from django.shortcuts import redirect
from django.http import HttpResponse


# def index(request):
#     return render(request, 'index.html', {'sinais': Sinal.objects.all()})


def exibir(request, sinal_id):
    sinal = Sinal.objects.get(id=sinal_id)
    return render(request, 'sinal.html', {"sinal": sinal})


def editar(request, sinal_id):
    sinal = get_object_or_404(Sinal, id=sinal_id)

    if request.method == 'POST':
        form = SinalForm(request.POST, instance=sinal)

        if form.is_valid():
            sinal = form.save(commit=False)
            sinal.save()
            return redirect('index')

    elif request.method == 'GET':
         form = SinalForm(instance=sinal)
         context = {'sinal': sinal,'form': form}
         return HttpResponse(render(request, 'editar.html', context))


class RegistrarSinalView(View):
    template_name = 'registrar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = SinalForm(request.POST)

        if form.is_valid() and form.is_valid_name():
            dados_form = form.data

            sinal = Sinal(configuracao_da_mao=dados_form['configuracao_da_mao'],
                          ponto_de_articulacao=dados_form['ponto_de_articulacao'],
                          movimento=dados_form['movimento'],
                          orientacao_das_maos=dados_form['orientacao_das_maos'],
                          expressao_facil_corporal=dados_form['expressao_facil_corporal'],
                          nome=dados_form['nome'])

            sinal.save()
            return redirect('index')

        return render(request, self.template_name, {'form': form})


def lista_sinais(request):
    sinais = Sinal.objects.all()
    var_get_search = request.GET.get('search_box')
    if var_get_search is not None:
        sinais = sinais.filter(nome__icontains=var_get_search)

    return render(request, 'todos_sinais.html', {'sinais': sinais})


def particionar(bitmask):
    i, l = 0, []
    while bitmask[i:i + 4]:
        l.append(bitmask[i:i + 4])
        i += 4
    return l


def index(request):
    sinais = Sinal.objects.all()
    string_search = request.GET.get('search_box2')
    if string_search is not None:
        dados = particionar(string_search)
        if len(dados) == 5:
            sinais = Sinal.objects.get(configuracao_da_mao=dados[0], ponto_de_articulacao=dados[1], movimento=dados[2],
                                       orientacao_das_maos=dados[3],
                                       expressao_facil_corporal=dados[4])
        else:
            sinais = None



    return render(request, 'index.html', {"sinal": sinais})