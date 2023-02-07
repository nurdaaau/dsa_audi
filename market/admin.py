from django.contrib import admin

from market.models import Car, Order, Purchase, Payment

admin.site.register(Car)
admin.site.register(Order)
admin.site.register(Purchase)
admin.site.register(Payment)
