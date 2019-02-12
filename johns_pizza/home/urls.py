from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('<category>/<name>/<size>/<toppings>/', views.getPrice, name="price-api"),
    path('addtocart/<category>/<name>/<toppings>/<size>/<quantity>', views.addToCart, name="add-to-cart-api"),
    path('getorders/', views.getOrders, name='orders-api')
]