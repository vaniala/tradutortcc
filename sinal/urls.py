from django.conf.urls import url
from sinais.views import index, exibir, RegistrarSinalView

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^sinais', exibir, name='exibir'),
    # url(r'^sinais/(?P<sinal_id>\d+)$', 'sinais.views.exibir', name='exibir'),
    # url(r'^registrar/$', RegistrarSinalView.as_view(), name='registrar'),

]