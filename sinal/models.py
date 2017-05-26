from django.db import models


# Create your models here.

class Sinal(models.Model):
    configuracao_da_mao = models.CharField(max_length=5, null=False)
    ponto_de_articulacao = models.CharField(max_length=5, null=False)
    movimento = models.CharField(max_length=5, null=False)
    orientacao_das_maos = models.CharField(max_length=5, null=False)
    expressao_facil_corporal = models.CharField(max_length=5, null=False)
    nome = models.CharField(max_length=255, null=False)

    def particionar(self, bitmask):
        i, l = 0, []
        while bitmask[i:i + 4]:
            l.append(bitmask[i:i + 4])
            i += 4
        # self.configuracao_da_mao = l[0]
        # self.ponto_de_articulacao = l[1]
        # self.movimento = l[2]
        # self.orientacao_das_maos = l[3]
        # self.expressao_facil_corporal = l[4]
        return l


# def get_bitmask_traduzido(request):
#         # return Sinal.objects.get(nome=)
#
#
# class Tradutor(models.Model):
#
#     # bitmask = models.ForeignKey(Perfil)


# configuracao_da_mao, ponto_de_articulacao, movimento, orientacao_das_maos, expressao_facil_corporal = bitmask.split()
