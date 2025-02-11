from django.views.generic import ListView, DetailView
from home.models import Activities
from django.shortcuts import get_object_or_404


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

    def get_object(self):
        return get_object_or_404(Activities, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_title'] = 'Atividade - '
        context['activity'] = self.get_object()
        return context