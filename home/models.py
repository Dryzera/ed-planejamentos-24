from django.db import models
from django.contrib.auth.models import User
from home.utils.variables import WEEK_DAY_CHOICES

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    logo_image = models.ImageField(blank=True, upload_to='images/logo_schools/')

    def __str__(self):
        return self.name

class Matter(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Professor')
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=False, verbose_name='Escola')
    matter = models.CharField(max_length=30, help_text='Nome da aula', verbose_name='Matéria')
    day_week = models.CharField(choices=WEEK_DAY_CHOICES, max_length=20, blank=False, null=False)
    hour = models.TimeField(help_text='Horario de início da aula', verbose_name='Inicio Aula')
    duration = models.IntegerField(default=50, help_text='Duração da aula (em minutos)', verbose_name='Duração da aula')

    def __str__(self):
        return f'{self.school} | {self.teacher} | {self.matter}'