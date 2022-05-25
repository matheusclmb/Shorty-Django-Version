import string
from random import choice

from django.conf import settings

letters = string.ascii_lowercase + string.ascii_uppercase
punctuation = "_"
numbers = string.digits


SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 6)


def create_shortcode(size=SIZE):
    return "".join(choice(letters + punctuation + numbers) for _ in range(size))


def create_short_url(model_instance):
    random_code = create_shortcode()

    model_class = model_instance.__class__

    if model_class.objects.filter(shortcode=random_code).exists():
        return create_short_url(model_instance)

    return random_code
