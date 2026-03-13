from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    units = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.quantity} {self.units} {self.name}"

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('appetizers', 'Appetizers'),
        ('main course', 'Main Course'),
        ('dessert', 'Dessert'),
        ('mostViewed', 'Most Viewed'),
        ('middleEast', 'Middle Eastern'),
        ('asia', 'Asian'),
        ('europe', 'European'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    methods = models.TextField()
    image = models.URLField(max_length=500, null=True, blank=True) 
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')
    isFav = models.BooleanField(default=False)
    def __str__(self):
        return self.name
