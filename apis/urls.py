from django.urls import path
from apis.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'apis'

urlpatterns = [
    # email verification urls
    path('send-mail/', SendMail.as_view(), name='send-mail'),
    path('check-code/', VerifyCode.as_view(), name='check-code'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
