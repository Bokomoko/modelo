from django import forms
from .models import Aluno
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'nickname', 'email', 'campo_de_estudo',
                  'discordid', 'telefone', 'data_nascimento']
        # fields = '__all__'
        labels = {
            'nome': 'Nome',
            'nickname': 'Nickname',
            'email': 'Email',
            'campo_de_estudo': 'Campo de Estudo',
            'discordid': 'Discord ID',
            'telefone': 'Telefone',
            'data_nascimento': 'Data de Nascimento',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'campo_de_estudo': forms.TextInput(attrs={'class': 'form-control'}),
            'discordid': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control'}),
        }
