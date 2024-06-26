# Generated by Django 5.0.5 on 2024-05-21 13:34

import django.contrib.auth.models
import usuario.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('tipo', models.CharField(choices=[('ADMINISTRADOR', 'Administrador'), ('COORDENADOR', 'Coordenador do Evento'), ('MEMBRO', 'Membro')], default='MEMBRO', help_text='* Campos obrigatórios', max_length=15, verbose_name='Tipo do usuário *')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome completo *')),
                ('titulacao', models.CharField(blank=True, choices=[('HUMANAS', 'Ciências Humanas'), ('SAUDE', 'Ciências da Saúde'), ('SOCIAIS', 'Ciências Sociais'), ('TECNOLOGICAS', 'Ciências Tecnológicas')], help_text='* Escolha área de interesse de trabalho', max_length=12, null=True, verbose_name='Área de pesquisa *')),
                ('instituicao', models.CharField(help_text='Registre a instituição/universidade/empresa', max_length=50, verbose_name='Instituição *')),
                ('email', models.EmailField(db_index=True, max_length=100, unique=True, verbose_name='Email')),
                ('celular', models.CharField(help_text='Use DDD', max_length=11, verbose_name='Número de celular com DDD *')),
                ('cpf', models.CharField(help_text='Apenas números', max_length=14, verbose_name='CPF *')),
                ('is_active', models.BooleanField(default=False, help_text='Se ativo, o usuário tem permissão para acessar o sistema', verbose_name='Ativo')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='Hash')),
            ],
            options={
                'verbose_name': 'usuário',
                'verbose_name_plural': 'usuários',
                'ordering': ['-tipo', 'nome'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
                ('administradores', usuario.models.AdministradorAtivoManager()),
                ('coordenadores', usuario.models.CoordenadorAtivoManager()),
                ('membros', usuario.models.MembroAtivoManager()),
            ],
        ),
    ]
