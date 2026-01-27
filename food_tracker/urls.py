from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_list, name='food_list'),    # URL pattern for the food list view will run in root app URL 
]