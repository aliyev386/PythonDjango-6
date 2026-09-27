import datetime

from django.http import HttpResponse


def current_weekday(request):
    day_name = datetime.datetime.now().strftime("%A")
    return HttpResponse(day_name)
