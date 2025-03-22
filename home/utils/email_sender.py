from django.core.mail import send_mail
from project.settings import EMAIL_HOST_USER
from unique_slugify import generate_slug

def validate_register(email):
    code = generate_slug(6, only_numbers=True)

    subject = 'Confirmação de Email'
    msg = f'Para confirmar seu cadastro, envie este código para o site: {code}'

    send_mail(subject, msg, EMAIL_HOST_USER, email, fail_silently=False)

    return code