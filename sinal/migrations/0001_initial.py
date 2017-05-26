# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-26 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sinal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('configuracao_da_mao', models.CharField(max_length=5)),
                ('ponto_de_articulacao', models.CharField(max_length=5)),
                ('movimento', models.CharField(max_length=5)),
                ('orientacao_das_maos', models.CharField(max_length=5)),
                ('expressao_facil_corporal', models.CharField(max_length=5)),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
    ]
