from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Topping(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    category = models.CharField(max_length=80)
    def __str__(self):
        return f"{self.category}"

class Size(models.Model):
    size = models.CharField(max_length=80)
    def __str__(self):
        return f"{self.size}"

class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True)
    toppings = models.ForeignKey(Topping, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.category}, {self.name}, {self.size}, {self.toppings}, {self.price}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    foods = models.ForeignKey(Food, on_delete=models.CASCADE)

    @property
    def price(self):
        return self.foods.price
    def __str__(self):
        return f"Order for {self.user} Total: {self.price} "
    
    
    






