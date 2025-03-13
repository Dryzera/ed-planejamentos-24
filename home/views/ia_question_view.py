from django.contrib import messages
from home.planejamento.api_ia.main_ia import question_ia
from django.views.generic import View
from django.shortcuts import redirect, render
from home.models import PromptIa
from home.utils.verify_inferences import verify_inferences
from django.utils.timezone import localtime
from datetime import datetime

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
        prompt_model_ia = PromptIa.objects.get(user=request.user)
        prompt_text = request.POST.get('prompt')
        inference_allowed = verify_inferences(request.user)

        if inference_allowed:
            question_ia(prompt_text, request.user)
            return redirect('home:ia_question')
        
        datetime_local = datetime.strftime(localtime(prompt_model_ia.updated_at), '%d/%m/%Y - %H:%M')

        messages.error(request, f'Seu limite expirou. Aguarde até {datetime_local} para usar novamente ou assine um plano pago.')
        return redirect('home:ia_question')
    