from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    available = models.IntegerField(default=0)
    image = models.CharField(max_length=1000, blank=True, default="")

    def __str__(self):
        return f"{self.name}, available: {self.available}"

