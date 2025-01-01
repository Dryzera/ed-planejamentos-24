from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from home.models import Matter, School
from home.planejamento import gerador

@login_required(login_url='home:login')
def planning(request):
    return render(request, 'planning/planning.html', context={'schools': School.objects.all()})

class PlanningCreate(View):
    template_name = 'planning/create.html'

    def post(self, request, *args, **kwargs):
        dia_semana = request.POST.get('dia_semana')
        school_pk = request.POST.get('school')
        data_planejamento = request.POST.get('data_planejamento')

        matters_available = Matter.objects.filter(teacher=request.user, school=school_pk, day_week=dia_semana).order_by('hour')
        if not matters_available:
            messages.error(request, 'Nenhuma aula para este dia da semana/escola foi encontrada.')
            return redirect('home:planning')
        
        planning = gerador.init_generate_document(matters_available, data_planejamento)
        print(planning)
        request.session['info_list'] = {
        'matters_available': list((i.school.name, i.matter) for i in matters_available),  # Certifique-se de que seja serializável
        'data_planejamento': data_planejamento,
        'planning': planning,
        'day_week': dia_semana
    }
        return redirect('home:planning_create')
    
    def get(self, request):
        info_list = self.request.session.get('info_list')
        print(info_list)
        if info_list['planning']:
            pass
        else:
            messages.error(request, 'Ocorreu um erro inesperado. O seu planejamento não foi gerado. Consulte os dados abaixo ou envie uma mensagem para os responsáveis.')

        return render(request, self.template_name)