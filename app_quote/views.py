import random

from django.http import HttpResponse

QUOTES = [
    "The only way to do great work is to love what you do.",
    "Life is what happens when you're busy making other plans.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "It does not matter how slowly you go as long as you do not stop.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
]


def random_quote(request):
    quote = random.choice(QUOTES)
    return HttpResponse(quote)
