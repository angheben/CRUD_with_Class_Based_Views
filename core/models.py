from django.db import models


class Product(models.Model):
    name = models.CharField(name='name', max_length=100)
    price = models.DecimalField(name='price', max_digits=8, decimal_places=2)
    category = models.CharField(name='category', max_length=100, default='None')

    def __str__(self):
        return self.name
