from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path
from market.views import show_cars, audi_purchase
from views_weather import show_weather
from views_name import name


def hello_world(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world),
    path('weather', show_weather),
    path('audi', show_cars),
    path('buy_car/<int:id_>', audi_purchase),
    path('name', name),
]
