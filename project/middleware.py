from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

class RestrictAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.restricted_paths = [
            "/planning/finish/",
            "/planning/generate-planning/",
            "/planning/create/",
            '/planning/',
            '/contacts/',
            '/matter/add/',
            '/matter/',
            '/matter/<int:pk>/',
            '/activity/<slug:slug>/',
            '/activities/',
        ]
        self.required_group = 'Free' 

    def __call__(self, request):
        if request.path in self.restricted_paths:
            if not request.user.is_authenticated:
                return redirect(reverse("home:login"))
            
            if request.user.groups.filter(name=self.required_group).exists():
                messages.error(request, 'Você não possui acesso a essa página com o plano free. [607]')
                return redirect(reverse("home:home"))

        return self.get_response(request)