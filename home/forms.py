from django import forms
from django.contrib.auth.models import User

from . import models

class LoginForm(forms.ModelForm):
    user = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu usúario',
                }
            ),
            label='Usuário:'
    )


    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Digite sua senha'
            }
        ),
        label='Senha:'
    )
    
    class Meta:
        model = User
        fields = ('user', 'password',)