from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.   
    
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_on = models.DateTimeField(default = now, editable=False)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length = 255)
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE, default = 1, related_name='ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE,default = 1, related_name='recipe')

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} in {self.recipe}"