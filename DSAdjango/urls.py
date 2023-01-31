from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.urls import path
from DSAdjango.views_audi import audi, audi_purchase
from DSAdjango.views_name import name
from DSAdjango.views_weather import show_weather


def hello_world(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        """
        <h3>Hello, Nurdaulet!</h3>
        <div style="font-size: 18px">
            <a href="/weather">What is the weather today?</a><br>
            <a href="/audi">Audi center</a><br>
            <a href="/name">What is your name?</a><br>
        </div>
        """
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world),
    path('weather', show_weather),
    path('audi', audi),
    path('buy_car/<int:id_>', audi_purchase),
    path('name', name),
]
