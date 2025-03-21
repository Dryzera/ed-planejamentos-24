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
        user = request.user

        if user.is_authenticated:
            context = {}
            context['site_title'] = f'ED IA - '

            if not PromptIa.objects.filter(user=user).exists():
                PromptIa.objects.create(user=user, context=[])

            prompt_model = PromptIa.objects.get(user=user)

            context['prompt_model'] = prompt_model
            context['site_title'] = 'ED IA -'

            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, {'site_title': 'ED IA -'})
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            prompt_model_ia = PromptIa.objects.get(user=request.user)
            prompt_text = request.POST.get('prompt')
            inference_allowed = verify_inferences(request.user)

            if inference_allowed:
                question_ia(prompt_text, request.user)
                return redirect('home:ia_question')
            
            date_last_inteference = localtime(prompt_model_ia.updated_at)
            date_string = f'{date_last_inteference.day+1}/{date_last_inteference.month}/{date_last_inteference.year} - {date_last_inteference.hour}:{date_last_inteference.minute}'
            datetime_instance = datetime.strptime(date_string, '%d/%m/%Y - %H:%M')
            datetime_local = datetime.strftime(datetime_instance, '%d/%m/%Y - %H:%M')

            messages.error(request, f'Seu limite expirou. Aguarde até {datetime_local} para usar novamente ou assine um plano pago.')
            return redirect('home:ia_question')
        else:
            messages.info(request, 'Crie uma conta para usar nossos serviços!')
            return redirect('home:register')
