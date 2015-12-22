# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 15:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('nro_de_telefono', models.CharField(max_length=36, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('cuit', models.CharField(max_length=20, null=True)),
                ('cuil', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('es_notebook', models.BooleanField()),
                ('fabricante', models.CharField(max_length=20, null=True)),
                ('modelo', models.CharField(max_length=20, null=True)),
                ('procesador', models.CharField(max_length=30, null=True)),
                ('placa_madre', models.CharField(max_length=30, null=True)),
                ('memorias', models.CharField(max_length=30, null=True)),
                ('discos', models.CharField(max_length=30, null=True)),
                ('lectora', models.CharField(max_length=30, null=True)),
                ('gabinete', models.CharField(max_length=30, null=True)),
                ('placa_de_video', models.CharField(max_length=30, null=True)),
                ('dueño', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente')),
            ],
        ),
    ]
