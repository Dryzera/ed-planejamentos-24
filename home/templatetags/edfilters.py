from django.template import Library

register = Library()

@register.filter
def add_min_right(number):
    number = str(number)
    numero = number.split(',')
    print(numero)
    return numero[0]