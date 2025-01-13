from django.urls import path
from django.contrib.auth.decorators import login_required
from home.views import *

app_name = 'home'

urlpatterns = [
    # planning urls
    path('planning/finish/', login_required(PlanningFinish.as_view(), login_url='home:login'), name='planning_finish'),
    path('planning/generate-planning/', login_required(PlanningGenerate.as_view(), login_url='home:login'), name='planning_generate'),
    path('planning/create/', login_required(PlanningCreate.as_view(), login_url='home:login'), name='planning_create'),
    path('planning/', planning, name='planning'),

    # login urls
    path('logout/', logout_view, name='logout'),
    path('login/', Login.as_view(), name='login'),
    
    # matter urls
    path('matter/<int:pk>/', login_required(MatterDetail.as_view(), login_url='home:login'), name='matter_view'),
    path('matter/add/', login_required(MatterAdd.as_view(), login_url='home:login'), name='matter_add'),
    path('matter/', login_required(MatterRead.as_view(), login_url='home:login'), name='matter'),


    path('nos-conheca/', know_us, name='signin'),
    path('error-codes/', error_codes, name='errors'),
    path('', index, name='home'),
]
