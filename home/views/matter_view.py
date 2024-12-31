from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView, DetailView
from home.forms import AddMatterForm
from home.models import Matter
from django.http import Http404

class MatterRead(ListView):
    template_name = 'matter/matter.html'
    model = Matter

    def get(self, request):
        matters = Matter.objects.filter(teacher=request.user)
        return render(request, self.template_name, context={'matters': matters})

class MatterAdd(View):
    template_name = 'matter/add.html'
    form_template = AddMatterForm

    def get(self, request, *args, **kwargs):
        form = self.form_template()
        return render(request, self.template_name, context={'form': form})
    
    def post(self, request, *args, **kwargs):
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
            return redirect('home:home')
            
        messages.error(request, 'Algo deu errado [cod. 01].')
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
        
        form = AddMatterForm(instance=context['matter'])
        context['form'] = form

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
            messages.error(request, 'Existe algum erro no formulário.')
            return redirect('home:matter_view', pk)
    