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

class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu Nome',
                }
            ),
            label='Nome:'
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite sobrenome',
                }
            ),
            label='Sobrenome:',
            required=False,
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu email',
                }
            ),
            label='E-Mail:'
    )

    user = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Crie seu usúario',
                }
            ),
            label='Usuário:'
    )


    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Crie sua senha'
            }
        ),
        label='Senha:'
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Digite novamente sua senha'
            }
        ),
        label='Confirme a Senha:'
    )
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'user', 'password')

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data
        validation_error_messages = {}

        first_name = cleaned.get('first_name')
        usuario_data = cleaned.get('user')
        email_data = cleaned.get('email')
        password_data = cleaned.get('password')
        password2_data = cleaned.get('password2')

        usuario_db = User.objects.filter(username=usuario_data).exists()
        email_db = User.objects.filter(email=email_data).exists()

        error_msg_user_exists = 'Este usuário já existe.'
        error_msg_email_exists = 'Este e-mail já existe.'
        error_msg_password_match = 'A senha não confere.'
        error_msg_password_short = 'Sua senha precisa ter pelo menos 6 caracteres.'
        error_msg_required_field = 'Este campo é obrigatório.'
        error_msg_missing_characters = 'Este campo precisa de pelo menos 3 caracteres.'

        if self.usuario:
            if User.objects.filter(username=usuario_data).exists():
                validation_error_messages['username']  = error_msg_user_exists
            if User.objects.filter(email=email_data).exists():
                validation_error_messages['email'] = error_msg_email_exists

            if password_data:
                if password_data != password2_data:
                    validation_error_messages['password'] = error_msg_password_match
                    validation_error_messages['password2'] = error_msg_password_match

            if len(password_data) < 6:
                validation_error_messages['password'] = error_msg_password_short

        else:
            if usuario_db:
                validation_error_messages['user']  = error_msg_user_exists

            if email_db:
                validation_error_messages['email'] = error_msg_email_exists

            if not password_data:
                validation_error_messages['password'] = error_msg_required_field

            if not password2_data:
                validation_error_messages['password2'] = error_msg_required_field

            if password_data:
                if password_data != password2_data:
                    validation_error_messages['password'] = error_msg_password_match
                    validation_error_messages['password2'] = error_msg_password_match

            if len(password_data) < 6:
                validation_error_messages['password'] = error_msg_password_short

            if len(first_name) < 3:
                validation_error_messages['first_name'] = error_msg_missing_characters


        if validation_error_messages:
            raise(forms.ValidationError(
                validation_error_messages 
            ))

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