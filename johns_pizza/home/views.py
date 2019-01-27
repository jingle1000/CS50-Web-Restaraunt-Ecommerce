from django.shortcuts import render
from django.http import HttpResponse


foods = [
    {
        "Category":"Pizza",
        "Name": "Classic",
        "Toppings": "Cheese",
        "Size": "Small",
        "Price": 17.45
    },
    {
        "Category":"Pizza",
        "Name": "Classic",
        "Toppings": "Cheese",
        "Size": "Medium",
        "Price": 17.45
    },
    {
        "Category":"Pizza",
        "Name": "Sicilian",
        "Toppings": "Cheese",
        "Size": "Large",
        "Price": 17.45
    },
    {
        "Category":"Pasta",
        "Name": "Baked Ziti w/Mozzarella",
        "Toppings": "N/A",
        "Size": "Regular",
        "Price": 17.45
    },
    {
        "Category":"Pasta",
        "Name": "Baked Ziti w/Meatballs",
        "Toppings": "",
        "Size": "Regular",
        "Price": 17.45
    },
]

def index(request):
    food_data = {}
    for food in foods:
        category = food["Category"]
        food_attrs = {"name":[food['Name']], "toppings":[food['Toppings']], "size":[food['Size']], "price":[food['Price']]}
        try:
            if food['Name'] not in list(food_data[category][0]["name"]):
                food_data[category][0]["name"].append(food['Name'])
            if food['Toppings'] not in list(food_data[category][0]["toppings"]):
                food_data[category][0]["toppings"].append(food['Toppings'])
            if food['Size'] not in list(food_data[category][0]["size"]):
                food_data[category][0]["size"].append(food['Size'])
            food_data[category][0]["price"].append(food['Price'])
        except KeyError:
            food_data[category] = []
            food_data[category].append(food_attrs)
    context = {
        "foods": food_data
    }
    return render(request, 'home/index.html', context=context)

def about(request):
    return render(request, 'home/about.html')
