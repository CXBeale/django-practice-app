from django.shortcuts import render
from .models import FoodEntry

# Create your views here.
def food_list(request):
    print("Food list view called")
    entries = FoodEntry.objects.all().order_by('-date')      # Retrieve all food entries ordered by most recent first
    return render(request, 'food_tracker/food_list.html', {'entries': entries})