from django.urls import path
from home.views import *

app_name = 'home'

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', Login.as_view(), name='login'),
    path('', index, name='home'),
]
