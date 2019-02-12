from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Food)
admin.site.register(models.Topping)
admin.site.register(models.Category)
admin.site.register(models.Size)
admin.site.register(models.Order)
admin.site.register(models.OrderFood)
