import string
import random
import unicodedata

def _remove_special_caracteres(text):
    return ''.join(
        c for c in unicodedata.normalize('NFKD', text)
        if unicodedata.category(c) != 'Mn'
    ).lower().replace(' ', '-') + '-'

def generate_slug(k, text='') -> str:
    if text:
        return _remove_special_caracteres(text) + ''.join(random.choices(string.ascii_lowercase + string.digits, k=k))[:32]
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=k))

if __name__ == '__main__':
    print(generate_slug(16))