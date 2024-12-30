from django.urls import path
from home.views import *

app_name = 'home'

urlpatterns = [
    # login urls
    path('logout/', logout_view, name='logout'),
    path('login/', Login.as_view(), name='login'),
    
    # matter
    path('matter/add/', MatterAdd.as_view(), name='matter_add'),
    path('matter/', MatterRead.as_view(), name='matter'),

    path('', index, name='home'),
]
