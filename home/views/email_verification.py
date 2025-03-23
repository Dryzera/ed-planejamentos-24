from home.models import User
import json
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.core.cache import cache 
from django.views.generic import View
from home.utils import email_sender

class SendMail(View):
    def get(self, request):
        return JsonResponse({"error": "Method not Allowed"}, status=405)
    
    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        email = data.get("email", "").strip()

        if not email:
            return JsonResponse({"error": "Please send e-mail address"}, status=400)
        
        code_generated = email_sender.validate_register(email)

        cache.set(f'code_{email}', code_generated, timeout=300)

        return JsonResponse({"success": "Code sended"}, status=200)
    
class VerifyCode(View):
    def get(self, request):
        return JsonResponse({"error": "Method not Allowed"}, status=405)

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        email = data.get('email', '').strip()
        code = data.get('code', '').strip()

        correct_code = cache.get(f'code_{email}')

        if correct_code and str(correct_code) == code:
            cache.set(f'validated_{email}', True, timeout=1440)
            cache.delete(f'code_{email}')
            return JsonResponse({"valid": True})
        
        return JsonResponse({"valid": False})