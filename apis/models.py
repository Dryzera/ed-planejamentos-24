from django.db import models
from django.contrib.auth.models import User

class PromptIa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    context = models.JSONField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    inference_counts = models.IntegerField(default=0, blank=False, null=False) 

    def __str__(self):
        return f'{self.user}'
    
    class Meta:
        verbose_name = 'Prompt Ia'
        verbose_name_plural = 'Prompts Ia'