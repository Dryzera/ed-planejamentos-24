from home.planejamento.api_ia.main_ia import question_ia
from django.views.generic import View
from django.shortcuts import redirect, render
from home.models import PromptIa

class IAView(View):
    template_name = 'ed_ia/index.html'
    
    def get(self, request, *args, **kwargs):
        context = {}
        user = request.user
        context['site_title'] = f'ED IA - '

        if not PromptIa.objects.filter(user=user).exists():
            PromptIa.objects.create(user=user, context=[])

        prompt_model = PromptIa.objects.get(user=user)

        context['prompt_model'] = prompt_model

        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        prompt = request.POST.get('prompt')

        question_ia(prompt, request.user)
        
        return redirect('home:ia_question')
    