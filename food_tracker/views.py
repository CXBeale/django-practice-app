from django.shortcuts import render, redirect
from .models import FoodEntry
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def food_list(request):
    print("Food list view called")
    entries = FoodEntry.objects.all().order_by('-date')      # Retrieve all food entries ordered by most recent first
    return render(request, 'food_tracker/food_list.html', {'entries': entries})

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# User profile view
@login_required
def profile(request):
    return render(request, 'food_tracker/profile.html')