from django.contrib import admin

from market.models import Car, Order, Purchase

admin.site.register(Car)
admin.site.register(Order)
admin.site.register(Purchase)
