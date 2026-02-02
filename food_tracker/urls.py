from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_list, name='food_list'),    # URL pattern for the food list view will run in root app URL 
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]