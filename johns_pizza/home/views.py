from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Food, Order

def index(request):
    food_objects = Food.objects.all()
    foods = []
    for food in food_objects:
        item = {}
        item["Category"] = str(food.category)
        item["Name"] = str(food.name)
        item["Toppings"] = str(food.toppings)
        item["Size"] = str(food.size)
        item["Price"] = float(food.price)
        foods.append(item)
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

def getPrice(request, category, name, size, toppings):
    food = Food.objects.filter(category__category=category, name=name, size__size=size, toppings__name=toppings)[0]
    price = str(food.price)
    context = {
        "price":price
    }
    return JsonResponse(context)

def getOrders(request):
    current_user_id = request.user.id
    user_orders = Order.objects.filter(user__id=current_user_id)[0]
    price = user_orders.get_total
    user_order_foods = user_orders.foods.all()
    print(user_order_foods)
    order_list = []
    for foodEntity in user_order_foods:
        food = []
        food.append(foodEntity.quantity)
        food.append(foodEntity.food.name)
        food.append(foodEntity.food.category.category)
        food.append(foodEntity.food.size.size)
        food.append(foodEntity.food.toppings.name)
        order_list.append(food)
        print(f"  {foodEntity.quantity} {foodEntity.food.name} {foodEntity.food.category}")
    context = {
        'orders': order_list,
        'price': price
    }
    return JsonResponse(context)

def addToCart(request, category, style, toppings, size, quantity):
    pass
