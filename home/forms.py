from django import forms
from django.contrib.auth.models import User
from home.models import Matter, School, UserProfile
from home.utils.variables import WEEK_DAY_CHOICES

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

class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu primeiro nome',
                }
            ),
            label='Nome:'
    )


    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu último nome'
            }
        ),
        label='Sobrenome:'
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu email'
            }
        ),
        label='Seu Email:'
    )
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class AddMatterForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

        if user:
            self.fields['school'].queryset = UserProfile.objects.get(user=self.user).schools.all()

    school = forms.ModelChoiceField(queryset=School.objects.all(), empty_label='(selecione)', label='Escola:')

    matter = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Digite aqui...'}
        ),
        help_text='Digite o nome da matéria',
        label='Matéria:'
    )

    day_week = forms.CharField(
        widget=forms.Select(
            choices=WEEK_DAY_CHOICES
        ),
        label='Dia da aula:',
    )

    hour = forms.TimeField(
        widget=forms.TimeInput(
            attrs={'type': 'time'}
        ),
        help_text='Coloque o horário em que a aula começa',
        label='Horário:'
    )

    duration = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'placeholder': 'Digite aqui...', 'class': 'duration'}
        ),
        help_text='Coloque a duração da aula em minutos',
        label='Duração:'
    )
    
    class Meta:
        model = Matter
        fields = ('school', 'matter', 'day_week', 'hour', 'duration')