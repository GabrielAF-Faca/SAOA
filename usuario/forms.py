from django import forms
from django.db import models


class BuscaUsuarioForm(forms.Form):
    # 1 campo da tupla fica no banco de dados
    # 2 campo da tupla eh mostrado para o usuario
    TIPOS_USUARIOS = (
        (None, '-----'),
        ('ADMINISTRADOR', 'Administrador'),
        ('COORDENADOR', 'Coordenador do Evento'),
        ('MEMBRO', 'Membro'),
    )

    TIPOS_TITULACAO = (
        (None, '-----'),
        ('TECNICO', 'Técnico'),
        ('GRADUANDO', 'Graduando'),
        ('GRADUADO', 'Graduado'),
        ('ESPECIALISTA', 'Especialista'),
        ('MESTRE', 'Mestre'),
        ('DOUTOR', 'Doutor')
    )

    AREA = (
        (None, '-----'),
        ('HUMANAS', 'Ciências Humanas'),
        ('SAUDE', 'Ciências da Saúde'),
        ('SOCIAIS', 'Ciências Sociais'),
        ('TECNOLOGICAS', 'Ciências Tecnológicas'),
    )

    tipo = forms.ChoiceField(label='Tipo de usuário', choices=TIPOS_USUARIOS, required=False)
    titulacao = forms.ChoiceField(label='Titulação', choices=TIPOS_TITULACAO, required=False)
    area = forms.ChoiceField(label='Área de interesse', choices=AREA, required=False)
