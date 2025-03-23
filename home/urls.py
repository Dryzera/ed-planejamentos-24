from django.urls import path
from django.contrib.auth.decorators import login_required
from home.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'

urlpatterns = [
    # email verification urls
    path('send-mail/', SendMail.as_view(), name='send-mail'),
    path('check-code/', VerifyCode.as_view(), name='check-code'),
    
    # ia question urls
    path('ed/', IAView.as_view(), name='ia_question'),

    # activity urls
    path('activity/<slug:slug>/', login_required(ActivityView.as_view(), login_url='home:login'), name='activity_view'),
    path('activities/', login_required(ActivityRead.as_view(), login_url='home:login'), name='activities'),

    # planning urls
    path('planning/finish/', login_required(PlanningFinish.as_view(), login_url='home:login'), name='planning_finish'),
    path('planning/generate-planning/', login_required(PlanningGenerate.as_view(), login_url='home:login'), name='planning_generate'),
    path('planning/create/', login_required(PlanningCreate.as_view(), login_url='home:login'), name='planning_create'),
    path('planning/', planning, name='planning'),

    # login urls
    path('profile/<int:pk>/edit/', login_required(EditProfile.as_view(), login_url='home:login'), name='edit_profile'),
    path('profile/<int:pk>/', view_profile, name='view_profile'),
    path('logout/', logout_view, name='logout'),
    path('cadastro/', Register.as_view(), name='register'),
    path('logar/', Login.as_view(), name='login'),
    
    # matter urls
    path('matter/<int:pk>/', login_required(MatterDetail.as_view(), login_url='home:login'), name='matter_view'),
    path('matter/add/', login_required(MatterAdd.as_view(), login_url='home:login'), name='matter_add'),
    path('matter/', login_required(MatterRead.as_view(), login_url='home:login'), name='matter'),

    path('nos-conheca/', know_us, name='signin'),
    path('contacts/', contact, name='contact'),
    path('tutorials/', tutorials, name='tutorials'),
    path('error-codes/', error_codes, name='errors'),
    path('', index, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
