from django.db import models


class Product(models.Model):
    name = models.CharField(name='name', max_length=100)
    price = models.DecimalField(name='price', max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
