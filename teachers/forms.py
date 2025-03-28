from django import forms
from teachers.models import School, Matter
from home.models import UserProfile
from teachers.utils.variables import WEEK_DAY_CHOICES

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