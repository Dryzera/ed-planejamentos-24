from django.core.mail import send_mail, get_connection
from project.settings import EMAIL_HOST_USER
from apis.utils.unique_slugify import generate_slug
from django.conf.global_settings import EMAIL_HOST_USER

def validate_register(email):
    connection = get_connection()
    
    code = generate_slug(6, only_numbers=True)

    subject = 'Confirmação de Email'
    msg = f'Para confirmar seu cadastro, envie este código para o site: {code}'

    send_mail(subject, msg, EMAIL_HOST_USER, [email], fail_silently=False)

    return code