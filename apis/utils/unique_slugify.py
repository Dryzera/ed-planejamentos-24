import string
import random
from django.utils.text import slugify

def generate_slug(k, text='', only_numbers=False) -> str:
    if text:
        slug_field = slugify(text) + '-' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=k))
        return slug_field[:64]
    elif only_numbers:
        return ''.join(random.choices(string.digits, k=k))
    
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=k))

if __name__ == '__main__':
    print(generate_slug(6, only_numbers=True)) 