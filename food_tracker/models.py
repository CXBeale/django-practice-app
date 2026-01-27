from django.db import models

# Create your models here.
class FoodEntry(models.Model):
    name = models.CharField(max_length=100)         # Name of the food item
    calories = models.PositiveIntegerField()        # Caloric content of the food item
    date = models.DateField()                       # Date of eating the food item

    def __str__(self):
        return f"{self.name} ({self.calories} kcal on {self.date})"