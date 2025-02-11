from django.views.generic import ListView, DetailView
from home.models import Activities

class ActivityRead(ListView):
    template_name = 'activities/activities.html'
    model = Activities

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activities'] = Activities.objects.all()
        context['site_title'] = 'Atividades - '
        return context
    
class ActivityView(DetailView):
    template_name = 'activities/detail.html'
    model = Activities

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activities'] = Activities.objects.all()
        context['site_title'] = 'Atividades - '
        return context