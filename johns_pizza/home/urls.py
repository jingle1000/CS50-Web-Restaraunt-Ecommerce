from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('food/<category>/<name>/<size>/<topping>', views.FoodInfo, name='check-food-price'),
    path('create-user-order/<category>/<name>/<size>/<topping>', views.createOrder, name="create-user-order")
]