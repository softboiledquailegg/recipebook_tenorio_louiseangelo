from django.shortcuts import render
from .models import Recipe, RecipeIngredient

# Create your views here.

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }
    return render(request, 'recipelist.html', ctx)

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id = recipe_id)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    ctx = {
        'name': recipe.name,
        'ingredients': ingredients
    }
    return render(request, 'recipe.html', ctx)
