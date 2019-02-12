from django.db import models
from django.utils import timezone
from model_utils import Choices
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

class OrderFood(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    @property
    def price(self):
        return self.food.price * self.quantity

    def __str__(self):
        return f"{self.food.category}: {self.food.name} - Price: {self.price}"
    


class Order(models.Model):
    STATUS = Choices(('cart', ('cart')), ('active', ('active')), ('completed', ('completed')))
    status = models.CharField(choices=STATUS, default=STATUS.cart, max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    foods = models.ManyToManyField(OrderFood)

    @property
    def get_total(self):
        total = 0
        for food in self.foods.all():
            total += food.price
        return total

    def __str__(self):
        return f"Order for: {self.user} - Total: {self.get_total} - Status: {self.status}"
    
    
def bootstrap():
    categorys = ["Pizza", "Pasta", "Sub"]
    sizes = ["Small", "Medium", "Large"]
    toppings = ["None", "Cheese", "One Topping", "Two Topping", "Three Topping"]
    for i in range(len(categorys)):
        c = Category(category=categorys[i])
        c.save()

    for i in range(len(sizes)):
        s = Size(size=sizes[i])
        s.save()
    
    for i in range(len(toppings)):
        t = Topping(name=toppings[i])
        t.save()
    






