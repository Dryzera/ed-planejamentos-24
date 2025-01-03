from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='home:login')
def index(request):
    return render(request, template_name='index.html', context={'site_title': 'Home - '})

@login_required(login_url='home:login')
def error_codes(request):
    return render(request, template_name='errors.html', context={'site_title': 'Códigos de Erros - '})
