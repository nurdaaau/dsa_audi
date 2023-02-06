from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from market.models import Car, Order

orders = []

cars = [
    {
        "id": 1,
        "available": 2,
        "model": "A6",
        "image": "https://thumb.tildacdn.com/tild3836-3936-4134-a433-353663656330/-/resize/520x/-/format/webp/2019.png",
    },
    {
        "id": 2,
        "available": 2,
        "model": "A7",
        "image": "https://thumb.tildacdn.com/tild3962-6335-4139-b962-386636356338/-/resize/520x/-/format/webp/2019.png",
    },
    {
        "id": 3,
        "available": 2,
        "model": "A8",
        "image": "https://thumb.tildacdn.com/tild3764-6131-4966-b237-393635633965/-/resize/520x/-/format/webp/2019.png",
    },
    {
        "id": 4,
        "available": 2,
        "model": "Q3",
        "image": "https://thumb.tildacdn.com/tild3032-6439-4663-b965-633332653537/-/resize/520x/-/format/webp/2019.png",
    },

]


def audi(request: HttpRequest) -> HttpResponse:
    global cars
    context = {
        "cars": cars,
        "name": "Timur"
    }
    return render(request, "cars.html", context)
