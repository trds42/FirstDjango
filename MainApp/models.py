from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    info = models.TextField(max_length=2000, default="-")

    def __repr__(self):
        return f"Item: {self.name} {self.brand} count: {self.count}"

