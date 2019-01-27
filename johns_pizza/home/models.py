from django.db import models

# Create your models here.
class Food(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20)
    toppings = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.category} {self.name} {self.size} {self.num_toppings} {self.price}"


class Topping(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return f"{self.name}"





