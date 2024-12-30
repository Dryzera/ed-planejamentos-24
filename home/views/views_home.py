from django.shortcuts import render
from django.contrib.auth.decorators import login_required # <- use in future

# Create your views here.
def index(request):
    return render(request, template_name='index.html')