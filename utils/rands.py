import string
from random import SystemRandom
from django.utils.text import slugify

def random_letters(k=5):
    return "".join(SystemRandom().choices(string.ascii_lowercase + string.digits, k=k))

def new_slugfy(text, k=5):
    return slugify(text) + "-" + random_letters(k)

if __name__ == "__main__":
    print(new_slugfy("testing the slugfy function", 3))