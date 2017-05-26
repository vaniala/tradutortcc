# -*- coding: utf-8 -*-
from django import forms
from sinal.models import Sinal


class SinalForm(forms.ModelForm):
    configuracao_da_mao = forms.CharField(required=True)
    ponto_de_articulacao = forms.CharField(required=True)
    movimento = forms.CharField(required=True)
    orientacao_das_maos = forms.CharField(required=True)
    expressao_facil_corporal = forms.CharField(required=True)
    nome = forms.CharField(required=False)

    class Meta:
        model = Sinal
        fields = ('configuracao_da_mao', 'ponto_de_articulacao','movimento', 'orientacao_das_maos', 'expressao_facil_corporal', 'nome')

    def is_valid(self):
        valid = True
        if not super(SinalForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')
            valid = False

        return valid

    def is_valid_name(self):
        valid = True
        sinal_exists = Sinal.objects.filter(nome=self.data['nome']).exists()

        if sinal_exists:
            self.adiciona_erro('Sinal já existente')
            valid = False

        return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)