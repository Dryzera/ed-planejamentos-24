from django.db import models
from django.contrib.auth.models import User
from apis.utils import unique_slugify
from home.utils.variables import WEEK_DAY_CHOICES, STATUS_STUDENTS_CHOICE

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Matter(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Professor')
    school = models.ForeignKey(School, on_delete=models.SET_DEFAULT, blank=False, null=False, verbose_name='Escola', default='Escola Sem Nome')
    matter = models.CharField(max_length=30, help_text='Nome da aula', verbose_name='Matéria')
    day_week = models.CharField(choices=WEEK_DAY_CHOICES, max_length=20, blank=False, null=False)
    hour = models.TimeField(help_text='Horario de início da aula', verbose_name='Inicio Aula')
    duration = models.IntegerField(default=50, help_text='Duração da aula (em minutos)', verbose_name='Duração da aula')

    def __str__(self):
        return f'{self.school} | {self.teacher} | {self.matter}'
    
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schools = models.ManyToManyField(School, blank=False)
    date_payment = models.DateField(blank=False, null=True)
    date_expiration = models.DateField(blank=False, null=True)

    def __str__(self):
        return f'{self.user}'
    
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

class Activities(models.Model):
    user_upload = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=64, blank=False, null=False)
    description = models.TextField(blank=True, max_length=300)
    keywords = models.CharField(max_length=256, blank=True)
    url_image = models.FileField(upload_to='activities/%Y/%m', blank=False, null=False)
    status_student = models.CharField(choices=STATUS_STUDENTS_CHOICE, blank=False, null=False, max_length=20)
    licence = models.BooleanField(default=False, null=False, blank=False, help_text='Você confirma que a imagem enviada esta livre de direitos autorais e/ou autoriza o uso dela?')
    slug = models.SlugField(max_length=64, blank=True, null=False, unique=False)
    upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify.generate_slug(8, self.title)

        if self.licence == False:
            raise ValueError('Você precisa concordar com a licença para enviar a imagem.')
        return super().save(*args, **kwargs)
    