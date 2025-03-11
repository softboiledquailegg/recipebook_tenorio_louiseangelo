from django.urls import path, include
from . import views
from .views import recipelistView, recipedetailView

app_name = "ledger"

urlpatterns = [
    path('recipes/', recipelistView.as_view(), name='recipe_list'),
    path('recipe/<int:recipe_id>/', recipedetailView.as_view(), name='recipe_detail'),
    path('register/', views.register, name='register'),
] 