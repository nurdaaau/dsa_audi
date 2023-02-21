from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path
from market.views import show_cars, audi_purchase, payment
from market.views_auth import login_view, logout_view
from views_name import name
from views_weather import show_weather


def hello_world(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world),
    path('name', name),
    path('weather', show_weather),
    path('audi', show_cars),
    #path('', show_cars),
    path('buy_car/<int:id_>', audi_purchase),
    path('payment/<int:id_>', payment),
    path('login', login_view),
    path('logout', logout_view),
]
