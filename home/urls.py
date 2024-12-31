from django.urls import path
from django.contrib.auth.decorators import login_required
from home.views import *

app_name = 'home'

urlpatterns = [
    # login urls
    path('logout/', logout_view, name='logout'),
    path('login/', Login.as_view(), name='login'),
    
    # matter
    path('matter/<int:pk>/', login_required(MatterDetail.as_view(), login_url='home:login'), name='matter_view'),
    path('matter/add/', login_required(MatterAdd.as_view(), login_url='home:login'), name='matter_add'),
    path('matter/', login_required(MatterRead.as_view(), login_url='home:login'), name='matter'),

    path('', index, name='home'),
]
