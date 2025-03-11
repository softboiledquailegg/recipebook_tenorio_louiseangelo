from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

# Register your models here. 

class RecipeIngredientInline(admin.TabularInline):  
    model=RecipeIngredient
    extra=1  # Number of empty forms shown by default

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display=("name", "author", "created_on", "updated_on") 
    inlines=[RecipeIngredientInline] 

class RecipeIngredientInLine(admin.TabularInline):
    model=RecipeIngredient

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display=('name',)

@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display=('recipe', 'ingredient', 'quantity')