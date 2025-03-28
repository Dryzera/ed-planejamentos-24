from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def contact(request):
    return render(request, template_name='general/contacts.html', context={'site_title': 'Contatos - '})

def error_codes(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Você não está autenticado. Você verá os demais códigos de erro quando fizer login.')
    return render(request, template_name='errors.html', context={'site_title': 'Códigos de Erros - '})

def know_us(request):
    return render(request, template_name='know_us.html')

@login_required(login_url='home:login')
def tutorials(request):
    return render(request, 'tutorials.html', context={'site_title': 'Tutoriais - '})