import string
import random
from django.utils.text import slugify

def generate_slug(k, text='') -> str:
    if text:
        slug_field = slugify(text) + ''.join(random.choices(string.ascii_lowercase + string.digits, k=k))
        return slug_field[:64]
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=k))

if __name__ == '__main__':
    print(generate_slug(16, 'Teste de slug grande com acentuação')) 