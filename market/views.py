from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from market.models import Car, Order


def show_cars(request: HttpRequest) -> HttpResponse:
    context = {
        "cars": Car.objects.all()
    }
    return render(request, "cars.html", context)


def audi_purchase(request: HttpRequest, id_: int) -> HttpResponse:
    car = Car.objects.filter(id=id_).first()

    if request.method == "POST":
        Order.objects.create(
            car=car,
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
        )
        return HttpResponseRedirect("/audi")

    return render(request, "purchase_form.html", {"car": car})
