from django.db import models

class Sinal(object):
    def __init__(self, configuracao_da_mao='', ponto_de_articulacao='', movimento= '', orientacao_das_maos ='', expressao_facil_corporal='', nome=''):
        self.configuracao_da_mao = configuracao_da_mao
        self.ponto_de_articulacao = ponto_de_articulacao
        self.movimento = movimento
        self.orientacao_das_maos  = orientacao_das_maos
        self.expressao_facil_corporal = expressao_facil_corporal
        self.nome = nome