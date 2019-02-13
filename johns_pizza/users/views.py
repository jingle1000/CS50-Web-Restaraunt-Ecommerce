from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Profile
from home.models import Order
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {"form":form})

@login_required
def profile(request):
    current_user_id = request.user.id
    usrprfl = Profile.objects.filter(user__id=current_user_id)[0]
    usrorders = Order.objects.filter(user__id=current_user_id, status='cart')[0]
    orders = []
    for food_entity in usrorders.foods.all():
        food_info = {}
        print(food_entity)
        food_info["quantity"] = str(food_entity.quantity)
        food_info["name"] = f"{food_entity.food.name} {food_entity.food.category.category}'s of size {food_entity.food.size.size} topped with {food_entity.food.toppings.name}"
        orders.append(food_info)
    context = {
        "address":usrprfl.address,
        "city": usrprfl.city,
        "state": usrprfl.state,
        "zipcode": usrprfl.zipcode,
        "orders":orders
    }
    return render(request, 'users/profile.html', context)
