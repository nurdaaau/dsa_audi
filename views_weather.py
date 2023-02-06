import random

from django.http import HttpRequest, HttpResponse


def show_weather(request: HttpRequest) -> HttpResponse:
    temperature = random.randint(-40, 40)
    feel = "OK"
    if temperature > 20:
        feel = "hot"
    if temperature < 0:
        feel = "cold"
    if temperature < -10:
        feel = "terribly cold"
    return HttpResponse(f"Today: {temperature} grad celsius, it is {feel}!")
