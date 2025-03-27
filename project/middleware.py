from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

class RestrictAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.restricted_paths = [
            "/planejamento/finalizado/",
            "/planejamento/gerar/",
            "/planejamento/criar/",
            '/planejamento/',
            '/aula/adicionar/',
            '/aulas/',
            '/aula/<int:pk>/',
            '/atividade/<slug:slug>/',
            '/atividades/',
        ]
        self._not_allowed_groups = ('Free',) 

    def __call__(self, request):
        if request.path in self.restricted_paths:
            if not request.user.is_authenticated:
                return redirect(reverse("home:login"))
            
            for group in self._not_allowed_groups:
                if request.user.groups.filter(name=group).exists():
                    messages.error(request, 'Você não possui acesso a essa página com o plano Free. [607]')
                    return redirect(reverse("home:home"))

        return self.get_response(request)