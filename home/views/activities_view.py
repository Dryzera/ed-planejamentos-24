from django.views.generic import ListView, DetailView
from home.models import Activities
from django.shortcuts import get_object_or_404, render
from django.db.models import Q


class ActivityRead(ListView):
    template_name = 'activities/activities.html'
    model = Activities
    context_object_name = 'activities'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_title'] = 'Atividades - '
        context['search'] = self.request.GET.get('q', '').lower()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('q', '')

        if search:
            terms = search.lower().split()
            query = Q()

            for term in terms:
                query |= Q(title__icontains=term) | Q(keywords__icontains=term)

            queryset = queryset.filter(query)
        else:
            queryset = queryset.all()

        return queryset

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
    
def load_activities(request):
    return render(request, 'activities/load_activities.html', {'activities': Activities.objects.all()})