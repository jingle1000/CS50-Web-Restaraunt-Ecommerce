from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('food/<category>/<name>/<size>/<topping>', views.FoodInfo, name='food')
]