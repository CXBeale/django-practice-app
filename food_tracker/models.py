from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class FoodEntry(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="food_entries"
    )
    food_name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()                       # Time of eating the food item
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.food_name} ({self.date} {self.time})"
