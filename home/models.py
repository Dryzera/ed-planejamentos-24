from django.db import models
from django.contrib.auth.models import User
from teachers.models import School
    
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

