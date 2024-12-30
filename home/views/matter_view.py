from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from home.forms import AddMatterForm
from home.models import Matter

class MatterAdd(View):
    template_name = 'matter/add.html'
    form_template = AddMatterForm

    def get(self, request, *args, **kwargs):
        form = self.form_template()
        return render(request, self.template_name, context={'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_template(request.POST)
        print(form.errors)

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
            messages.success('Aula adicionada!')
            return redirect('home:home')
            
        messages.error(request, 'Algo deu errado [cod. 01].')
        return render(request, self.template_name, context={'form': form})
