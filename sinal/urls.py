from django.conf.urls import url
from sinal.views import index, exibir, RegistrarSinalView, lista_sinais, editar

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^sinais/(?P<sinal_id>\d+)$', exibir, name='exibir'),
    url(r'^registrar/$', RegistrarSinalView.as_view(), name='registrar'),
    url(r'^editar/(?P<sinal_id>\d+)$', editar, name='editar'),
    # url(r'^delete/(?P<sinal_id>\d+)$', DeletarSinal.as_view(), name='server_delete'),
    url(r'^sinais/$', lista_sinais, name='lista_sinais')

]