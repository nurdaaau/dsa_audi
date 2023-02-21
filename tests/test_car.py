from django.contrib.auth.models import User
from django.test import TestCase
from market.models import Car, Order, Purchase


class PurchaseTest(TestCase):
    def setUp(self):
        Car.objects.create(name="Audi A6")
        Car.objects.create(name="Audi A7")
        Car.objects.create(name="Audi A8")
        User.objects.create_user(username="bill", password="gates")
        response = self.client.get("/")
        self.client.post(response.url, {
            "username": "bill",
            "password": "gates",
        })

    def test_car_count(self):
        self.assertEqual(Car.objects.all().count(), 3)
        car = Car.objects.get(name="Audi A7")
        assert car.name == "Audi A7"

    def test_cars_left_function(self):
        car = Car.objects.get(name="Audi A6")
        # buy 3 cars
        Purchase.objects.create(car=car)
        Purchase.objects.create(car=car)
        Purchase.objects.create(car=car)
        # sell 1 car
        Order.objects.create(car=car)
        # we should have 2 cars left
        self.assertEqual(car.cars_left(), 2)

        car = Car.objects.get(name="Audi A8")
        self.assertEqual(car.cars_left(), 0)

    def test_cars_orders_by_client(self):
        # buy_car/<int:id_>
        car = Car.objects.get(name="Audi A8")
        # buy 3 cars
        Purchase.objects.create(car=car)
        Purchase.objects.create(car=car)
        Purchase.objects.create(car=car)
        # sell 1 car
        url = f"/buy_car/{car.id}"
        response = self.client.post(url, {
            "name": "Nurdaulet",
            "email": "nurda@mail.ru",
            "phone": "+77088294976",
        })
        self.assertEqual(response.status_code, 302)
        assert car.cars_left() == 2

    def test_purchase_order_default_is_one(self):
        car = Car.objects.get(name="Audi A7")
        purchase = Purchase.objects.create(car=car)
        self.assertEqual(purchase.count, 1)
