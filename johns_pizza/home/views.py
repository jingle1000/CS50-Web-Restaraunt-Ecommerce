from django.shortcuts import render
from django.http import HttpResponse


pizza = [
    {
        "Type":"Regular",
        "Toppings": 0,
        "Small": 12.20,
        "Large": 17.45
    },
    {
        "Type":"Regular",
        "Toppings": 1,
        "Small": 13.20,
        "Large": 19.45
    },
    {
        "Type":"Regular",
        "Toppings": 2,
        "Small": 12.20,
        "Large": 17.45
    },
    {
        "Type":"Sicilian",
        "Toppings": 0,
        "Small": 12.20,
        "Large": 17.45
    },
    {
        "Type":"Sicilian",
        "Toppings": 1,
        "Small": 12.20,
        "Large": 17.45
    },
    {
        "Type":"Sicilian",
        "Toppings": 3,
        "Small": 12.20,
        "Large": 17.45
    },
]

def index(request):
    context = {
        'pizza':pizza
    }
    return render(request, 'home/index.html', context)

def about(request):
    return render(request, 'home/about.html')
