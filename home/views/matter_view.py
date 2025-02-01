from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import View, ListView, DetailView
from home.forms import AddMatterForm
from home.models import Matter, UserProfile
from django.http import Http404
from django.db.models import Q

class MatterRead(ListView):
    template_name = 'matter/matter.html'
    model = Matter

    def get(self, request):
        user = request.user

        school = request.GET.get("school")
        day_week = request.GET.get("day_week")

        school = int(school) if school else None
        day_week = int(day_week) if day_week else None
        query = Q(teacher=user)

        if school is not None or day_week is not None:
            subquery = Q()
            if school is not None:
                subquery &= Q(school=school)
            if day_week is not None:
                subquery &= Q(day_week=day_week)
            query &= subquery

        matters = Matter.objects.filter(query).order_by('day_week', 'hour')

        schools_filter = UserProfile.objects.get(user=user).schools.all()
        return render(request, self.template_name, context={'matters': matters, 'schools': schools_filter, 'site_title': 'Aulas - '})

class MatterAdd(View):
    template_name = 'matter/add.html'
    form_template = AddMatterForm

    def get(self, request):
        form = self.form_template(user=self.request.user)
        return render(request, self.template_name, context={'form': form, 'site_title': 'Adicionar Aula - '})
    
    def post(self, request):
        form = self.form_template(request.POST)

        if form.is_valid():
            matter = Matter.objects.create(
                teacher=request.user,
                school=form.cleaned_data['school'],
                matter=form.cleaned_data['matter'],
                day_week=form.cleaned_data['day_week'],
                hour=form.cleaned_data['hour'],
                duration=form.cleaned_data['duration'],
            )
            matter.save()
            messages.success(request, 'Aula adicionada!')
            return redirect('home:matter')
            
        messages.error(request, 'Algo deu errado. [603]')
        return render(request, self.template_name, context={'form': form})


class MatterDetail(DetailView):
    template_name = 'matter/detail.html'
    model = Matter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.pk = self.kwargs['pk']
        object_matter = Matter.objects.get(pk=self.pk)
        context['matter'] = object_matter
        return context
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        object_matter = context['matter']
        if object_matter.teacher != self.request.user:
            raise Http404()
        
        form = AddMatterForm(user=request.user, instance=context['matter'])
        context['form'] = form
        context['site_title'] = f'Aula {object_matter.pk} - '

        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        apagar = request.POST.get('confirm_apagar') == 'on'
        pk = self.kwargs['pk']
        
        if apagar:
            self.model.objects.get(pk=pk).delete()
            messages.info(request, 'Aula apagada.')
            return redirect('home:matter')
        else:
            form = AddMatterForm(request.POST)

            if form.is_valid():
                matter = Matter.objects.get(pk=pk)
                matter.school=form.cleaned_data['school']
                matter.matter=form.cleaned_data['matter']
                matter.day_week=form.cleaned_data['day_week']
                matter.hour=form.cleaned_data['hour']
                matter.duration=form.cleaned_data['duration']
                matter.save()

                messages.success(request, 'Aula editada.')
                return redirect('home:matter_view', pk)
            messages.error(request, 'Algo deu errado. [602]')
            return redirect('home:matter_view', pk)
    