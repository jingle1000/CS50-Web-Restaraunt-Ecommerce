from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Profile
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
    context = {
        "address":usrprfl.address,
        "city": usrprfl.city,
        "state": usrprfl.state,
        "zipcode": usrprfl.zipcode
    }
    return render(request, 'users/profile.html', context)
