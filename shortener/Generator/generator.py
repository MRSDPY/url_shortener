import random
import string
from django.conf import settings


def get_code_bloc(size=settings.MIN_SIZE):
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(size))


def unique_generator(instance, size=settings.MIN_SIZE):
    code_bloc = get_code_bloc(size)
    url = instance.__class__
    data = url.objects.filter(shorted_url=code_bloc).exists()
    if data:
        return unique_generator(url, size)
    return code_bloc
