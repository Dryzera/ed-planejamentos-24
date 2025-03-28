from django.urls import path
from django.contrib.auth.decorators import login_required
from home.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'

urlpatterns = [
    # ia question urls
    path('ed/', IAView.as_view(), name='ia_question'),

    # login urls
    path('perfil/<int:pk>/editar/', login_required(EditProfile.as_view(), login_url='home:login'), name='edit_profile'),
    path('perfil/<int:pk>/', view_profile, name='view_profile'),
    path('sair/', logout_view, name='logout'),
    path('cadastro/', Register.as_view(), name='register'),
    path('logar/', Login.as_view(), name='login'),

    path('nos-conheca/', know_us, name='signin'),
    path('contato/', contact, name='contact'),
    path('tutoriais/', tutorials, name='tutorials'),
    path('erros/', error_codes, name='errors'),
    path('', index, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
