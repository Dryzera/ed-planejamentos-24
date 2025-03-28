from django.shortcuts import redirect, get_object_or_404, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from home.models import UserProfile
from teachers.models import Matter
from apis.planejamento import gerador
from teachers.utils.variables import WEEK_DAY_CHOICES
from teachers.utils.weekday import get_weekday
from teachers.utils.convert import convert_to_docx
from datetime import datetime
from django.http import FileResponse
import os
from django.conf import settings

@login_required(login_url='home:login')
def planning(request):
    schools = get_object_or_404(UserProfile, user=request.user).schools.all()
    return render(request, 'planning/planning.html', context={'schools': schools, 'site_title': 'Planejamentos - '})

class PlanningCreate(View):
    template_name = 'planning/create.html'

    def post(self, request, *args, **kwargs):
        school_pk = request.POST.get('school')
        data_planejamento = request.POST.get('data_planejamento')
        dia_semana = get_weekday(data_planejamento)

        matters_available = Matter.objects.filter(teacher=request.user, school=school_pk, day_week=dia_semana).order_by('hour')
        if not matters_available:
            messages.error(request, 'Nenhuma aula para este dia/escola foi encontrada. [603]')
            return redirect('teachers:planning')
        
        request.session['info_list'] = {
        'matters_available': list((i.pk) for i in matters_available),
        'data_planejamento': data_planejamento,
        'day_week': dia_semana,
        'school_pk': school_pk
        }
        return redirect('teachers:planning_create')
    
    def get(self, request):
        info_list = self.request.session.get('info_list')
        day_week = WEEK_DAY_CHOICES[int(info_list['day_week'])][1]

        matters_selected_ids = info_list['matters_available']
        matters_selected = []

        for matter_id in matters_selected_ids:
            matters_selected.append(Matter.objects.filter(pk=matter_id))

        date_formated = datetime.strptime(info_list['data_planejamento'], '%Y-%m-%d')

        context = {
            'matters_selected_list': matters_selected,
            'day_planning': date_formated,
            'day_week': day_week,
            'site_title': 'Gerar Planejamento - '
        }

        return render(request, self.template_name, context=context)
    
class PlanningGenerate(View):
    def post(self, request):
        info_list = self.request.session.get('info_list')
        list_matters = []
        term_for_ia = {}
        
        aditional_content = request.POST.get('aditional_content')
        base_sep_matter = True if request.POST.get('hourBased') == 'on' else False # aula sera separada por 1º etc...
        insert_name = True if request.POST.get('insertMyName') == 'on' else False
        insert_school = True if request.POST.get('insertSchoolName') == 'on' else False

        for key, value in request.POST.items():
            if key.startswith('term_for_ia-'):
                matter_id = key.split('-')[1]
                matter = Matter.objects.get(pk=matter_id)
                list_matters.append(matter)
                
                teacher = matter.teacher if insert_name else False
                school = matter.school if insert_school else False
                term_for_ia[matter_id] = value

        planning_generate = gerador.init_generate_document(list_matters, info_list['data_planejamento'], term_for_ia, aditional_content, base_sep_matter, school, teacher)
        request.session['info_list'] = {'response_planning': planning_generate}
         
        try:
            if planning_generate:
                convert_to_docx(planning_generate)
        except Exception as e:
            print(e)

        request.session.modified = True
        return redirect('teachers:planning_finish')

class PlanningFinish(View):
    template_name = 'planning/finish.html'

    def get(self, request):
        info_list = request.session.get('info_list')
        response_planning = info_list['response_planning']

        if not response_planning:
            messages.error(request, 'Ocorreu um erro inesperado ao gerar seu planejamento, tente novamente. [701]')
            return redirect('teachers:planning')
        else:
            messages.success(request, 'Seu planejamento foi gerado!')
            return render(request, self.template_name, context={'slug_file': response_planning, 'site_title': 'Download do Planejamento - '})

    def post(self, request):
        try:
            info_list = request.session.get('info_list')
            response_planning = info_list['response_planning']

            file_name = f'planejamento_{response_planning}.docx'
            file_path = os.path.join(settings.MEDIA_ROOT, "files_docx_generated", file_name)

            del request.session['info_list']
            if os.path.exists(file_path):
                return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)
            else:
                messages.error(request, 'Seu planejamento foi gerado, mas não foi encontrado no nosso banco de dados, tente novamente. [702]')
                return render(request, self.template_name)
        except TypeError:
            messages.error(request, 'Você já baixou o arquivo. Você não pode baixar duas vezes. [604]')
            return redirect('teachers:planning')