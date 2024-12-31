from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from home.models import Matter, School

@login_required(login_url='home:login')
def planning(request):
    return render(request, 'planning/planning.html', context={'schools': School.objects.all()})

class PlanningCreate(View):
    template_name = 'planning/create.html'
    list_matters = []

    def post(self, request, *args, **kwargs):
        dia_semana = request.POST.get('dia_semana')
        school_pk = request.POST.get('school')

        matters_available = Matter.objects.filter(teacher=request.user, school=school_pk, day_week=dia_semana)
        if not matters_available:
            messages.error(request, 'Nenhuma aula para este dia da semana/escola foi encontrada.')
            return redirect('home:planning')       
        self.list_matters.append(matters_available)
        return redirect('home:planning_create')
    
    def get(self, request):
        qtd_matter = len(self.list_matters)
        print(self.list_matters)
        context = {
            'qtd_matter': qtd_matter,
            'list_matters': self.list_matters
        }
        return render(request, self.template_name, context=context)