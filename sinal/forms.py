from django import forms
from django.db import models

# from django.contrib.auth.models import Sinal
from sinais.models import Sinal


class RegistrarSinalForm(forms.Form):
    configuracao_da_mao = forms.CharField(required=True)
    ponto_de_articulacao = forms.CharField(required=True)
    movimento = forms.CharField(required=True)
    orientacao_das_maos = forms.CharField(required=True)
    expressao_facil_corporal = forms.CharField(required=True)
    nome = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(RegistrarSinalForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')
            valid = False

        sinal_exists = Sinal.objects.filter(nome=self.data['nome']).exists()

        if sinal_exists:
            self.adiciona_erro('Sinal ja existente')
            valid = False

        return valid


def adiciona_erro(self, message):
    errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
    errors.append(message)