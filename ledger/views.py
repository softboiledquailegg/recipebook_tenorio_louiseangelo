from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Recipe

# Create your views here.

class recipelistView(ListView):
    model = Recipe
    template_name = 'recipelist.html'

class recipedetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html'
    redirect_field_name = '/recipes/list'

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("ledger:recipe_list")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})
