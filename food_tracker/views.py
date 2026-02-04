from django.shortcuts import render, redirect
from .models import FoodEntry
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm, FoodEntryForm


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

# User profile edit view
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'food_tracker/edit_profile.html', {'form': form})

# Food Entry list view
@login_required
def food_list(request):
    entries = FoodEntry.objects.filter(user=request.user).order_by('-date', '-time')
    return render(request, 'food_tracker/food_list.html', {'entries': entries})

# Add Food Entry view
@login_required
def add_food_entry(request):
    if request.method == 'POST':
        form = FoodEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user  # Link entry to the logged-in user
            entry.save()
            return redirect('food_list')
    else:
        form = FoodEntryForm()
    return render(request, 'food_tracker/add_food_entry.html', {'form': form})

