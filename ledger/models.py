from django.db import models
from django.urls import reverse

# Create your models here.
    
class Ingredient(models.Model):
    name = models.CharField(max_length = 255)

    def _str_(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length = 255)
    def _str_(self):
        return self.name

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length = 255)
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE)

    def _str_(self):
        return f"{self.quantity} of {self.ingredient.name} in {self.recipe}"