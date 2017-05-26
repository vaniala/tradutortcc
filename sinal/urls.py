from django.conf.urls import url
from sinal.views import index, exibir

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^sinais/(?P<sinal_id>\d+)$', exibir, name='exibir'),


]