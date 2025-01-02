from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from home.models import Matter, School
from home.planejamento import gerador
from home.utils.variables import WEEK_DAY_CHOICES
from datetime import datetime

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
        
        request.session['info_list'] = {
        'matters_available': list((i.pk) for i in matters_available),
        'data_planejamento': data_planejamento,
        'day_week': dia_semana,
        'school_pk': school_pk
    }
        return redirect('home:planning_create')
    
    def get(self, request):
        info_list = self.request.session.get('info_list')
        print(info_list)
        day_week = WEEK_DAY_CHOICES[int(info_list['day_week'])][1]

        matters_selected_ids = info_list['matters_available']
        matters_selected = []

        for matter_id in matters_selected_ids:
            matters_selected.append(Matter.objects.filter(pk=matter_id))

        date_formated = datetime.strptime(info_list['data_planejamento'], '%Y-%M-%d')

        context = {
            'matters_selected_list': matters_selected,
            'day_planning': date_formated,
            'day_week': day_week,
        }

        return render(request, self.template_name, context=context)
    
class PlanningGenerate(View):
    def post(self, request):
        info_list = self.request.session.get('info_list')
        term_for_ia = {}
        for key, value in request.POST.items():
            if key.startswith('term_for_ia-'):
                matter_id = key.split('-')[1]
                matters_available = Matter.objects.filter(pk=matter_id).order_by('hour')
                term_for_ia[matter_id] = value

        gerador.init_generate_document(matters_available, info_list['data_planejamento'], term_for_ia)