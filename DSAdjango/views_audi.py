from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

orders = []
cars = [
    {
        "id": 1,
        "model": "A6",
        "image": "https://thumb.tildacdn.com/tild3836-3936-4134-a433-353663656330/-/resize/520x/-/format/webp/2019.png"
    },
    {
        "id": 2,
        "model": "A7",
        "image": "https://thumb.tildacdn.com/tild3962-6335-4139-b962-386636356338/-/resize/520x/-/format/webp/2019.png"
    },
    {
        "id": 3,
        "model": "A8",
        "image": "https://thumb.tildacdn.com/tild3764-6131-4966-b237-393635633965/-/resize/520x/-/format/webp/2019.png"
    },
    {
        "id": 4,
        "model": "Q3",
        "image": "https://thumb.tildacdn.com/tild3032-6439-4663-b965-633332653537/-/resize/520x/-/format/webp/2019.png"
    },
]


def audi(request: HttpRequest) -> HttpResponse:
    global cars
    cars_cards = ""
    for car in cars:
        button = f"""<a href="/buy_car/{car["id"]}">BUY</a>"""
        for order in orders:
            if order["car"] == car:
                button = """<span style="background: red; color:white;">PURCHASED</span>"""
        cars_cards += f"""
        <div style="width: 200px; height: 200px; margin: 20px; background-color: #FAFAFA; text-align: center">
            <img width="170px" src="{car["image"]}" style="margin-top: 20px; margin-bottom: 50px;">
            Audi {car["model"]}<br>
            {button}
        </div>
        """
    if len(cars) == 0:
        cars_cards = "Sorry, no cars left today :("

    return HttpResponse(f"""
        Hello audi!<br><br>
        <div style="display: flex; flex-flow: row">
        {cars_cards}
        </div>
    """)


def audi_purchase(request: HttpRequest, id_: int) -> HttpResponse:
    global cars
    cars_with_id_match = [car for car in cars if car["id"] == id_]
    car = cars_with_id_match[0]
    if request.method == "POST":
        orders.append({
            "car": car,
            "name": request.POST.get("name"),
            "email": request.POST.get("email"),
            "phone": request.POST.get("phone"),
        })
        print(orders)
        return HttpResponseRedirect("/audi")

    return HttpResponse(f"""
    <h3>Great! You are going to purchase Audi {car["model"]}!</h3>
    <form method="post">
        <label for="name">Your name:</label>
        <input id="name" name="name" required><br>
        <label for="phone" required>Your phone number:</label>
        <input id="phone" name="phone"><br>
        <label for="email" required>Your email address:</label>
        <input id="email" name="email" type="email"><br>
        <button type="submit">submit</button>
        
    </form>    
    """)
