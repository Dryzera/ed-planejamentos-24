from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django_ratelimit.decorators import ratelimit
from django.http import HttpResponseForbidden

class RestrictAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.restricted_paths = [
            "/professores/planejamento/finalizado/",
            "/professores/planejamento/gerar/",
            "/professores/planejamento/criar/",
            '/professores/planejamento/',
            '/professores/aula/adicionar/',
            '/professores/aulas/',
            '/professores/aula/<int:pk>/',
            '/professores/atividade/<slug:slug>/',
            '/professores/atividades/',
        ]
        self._not_allowed_groups = ('Free',) 

    def __call__(self, request):
        if request.path in self.restricted_paths:
            if not request.user.is_authenticated:
                return redirect(reverse("home:login"))
            
            for group in self._not_allowed_groups:
                if request.user.groups.filter(name=group).exists():
                    messages.error(request, 'Você não possui acesso a essa página com o plano Free. [607]')
                    return redirect(reverse("teachers:home"))
        return self.get_response(request)
    

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST':
            ratelimited_response = ratelimit(key='ip', rate='10/m', method='POST', block=True)(self.get_response)(request)
            return ratelimited_response
        elif request.method == 'GET':
            ratelimited_response = ratelimit(key='ip', rate='15/m', method='GET', block=True)(self.get_response)(request)
            return ratelimited_response

        return self.get_response(request)