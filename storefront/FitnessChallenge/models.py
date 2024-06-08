from django.db import models
from django import forms

# Create your models here.

SEX_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female')
]

ACTIVITY_CHOICES = [
    ('sedentary', 'Sedentary (little or no exercise)'),
    ('light', 'Lightly active (light exercise/sports 1-3 days/week)'),
    ('moderate', 'Moderately active (moderate exercise/sports 3-5 days/week)'),
    ('active', 'Active (hard exercise/sports 6-7 days a week)'),
    ('very_active', 'Very active (very hard exercise/sports & a physical job)'),
]

GOAL_CHOICES = [
    ('lose', 'Lose Weight'),
    ('maintain', 'Maintain Weight'),
    ('gain', 'Gain Weight'),
]

class DietCalculator(models.Model):
    weight = models.DecimalField(max_digits=5, decimal_places=2, help_text="Weight in kilograms")
    age = models.PositiveIntegerField(help_text="Age in years")
    height = models.DecimalField(max_digits=5, decimal_places=2, help_text="Height in centimeters")
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    activity = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    goal = models.CharField(max_length=10, choices=GOAL_CHOICES)
    bmr = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    recommended_calories = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Diet Calculator: {self.pk}"

class Diet(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='diets/')
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    diet = models.ForeignKey(Diet, related_name='products', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, related_name='ingredients', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class CaloriesCalculator(models.Model):
    kilometers_ran = models.DecimalField(max_digits = 3, decimal_places = 2, help_text = 'Kilometers ran')
    kilometers_walked = models.DecimalField(max_digits = 3, decimal_places = 2, help_text = 'Kilometers walked')
