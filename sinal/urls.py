from django.conf.urls import url
from sinal.views import index, exibir, RegistrarSinalView

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^sinais/(?P<sinal_id>\d+)$', exibir, name='exibir'),
url(r'^registrar/$', RegistrarSinalView.as_view(), name='registrar'),


]