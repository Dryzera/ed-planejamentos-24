from django.urls import path
from django.contrib.auth.decorators import login_required
from teachers.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'teachers'

urlpatterns = [
    # activity urls
    path('atividade/<slug:slug>/', login_required(ActivityView.as_view(), login_url='home:login'), name='activity_view'),
    path('atividades/', login_required(ActivityRead.as_view(), login_url='home:login'), name='activities'),

    # planning urls
    path('planejamento/finalizado/', login_required(PlanningFinish.as_view(), login_url='home:login'), name='planning_finish'),
    path('planejamento/gerar/', login_required(PlanningGenerate.as_view(), login_url='home:login'), name='planning_generate'),
    path('planejamento/criar/', login_required(PlanningCreate.as_view(), login_url='home:login'), name='planning_create'),
    path('planejamento/', planning, name='planning'),
    
    # matter urls
    path('aula/<int:pk>/', login_required(MatterDetail.as_view(), login_url='home:login'), name='matter_view'),
    path('aula/adicionar/', login_required(MatterAdd.as_view(), login_url='home:login'), name='matter_add'),
    path('aulas/', login_required(MatterRead.as_view(), login_url='home:login'), name='matter'),

    path('', index, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
