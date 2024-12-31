from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='home:login')
def index(request):
    return render(request, template_name='index.html')