from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('add/', views.add_food_entry, name='add_food_entry'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]