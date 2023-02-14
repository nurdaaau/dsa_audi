from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render

from market.models import BadUser, Car


def login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        bad_user = BadUser.objects.filter(username=username, password=password).first()
        if bad_user is None:
            return render(request, "login.html", context={"message": "Wrong username or password"})
        request.session["user_id"] = bad_user.id
        #return HttpResponseRedirect("/")
        context = {
            "cars": Car.objects.all()
        }
        return render(request, "cars.html", context)

    return render(request, "login.html")


def logout(request: HttpRequest) -> HttpResponse:
    request.session["user_id"] = None
    return HttpResponseRedirect("/")
    #return render(request, "login.html", context={"message": "Please log in"})
