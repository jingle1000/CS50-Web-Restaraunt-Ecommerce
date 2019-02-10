from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('<category>/<name>/<size>/<toppings>/', views.getPrice, name="price-api")
]