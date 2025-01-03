from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from home.forms import LoginForm
from django.contrib.auth import authenticate, login

@login_required(login_url='home:login')
def logout_view(request):
    logout(request)
    messages.info(request, 'Você saiu da sua conta.')
    return redirect('home:login')

class Login(View):
    template_name = 'autentication/login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')

        form = self.form_class()
        return render(request, self.template_name, context={'form': form, 'site_title': 'Login - '})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['user'],
                password=form.cleaned_data['password'],
            )

            if user is not None:
                login(request, user)
                messages.success(request, 'Logado com sucesso!')
                return redirect('home:home')
            
        messages.error(request, 'O login falhou.')
        return render(request, self.template_name, context={'form': form})
