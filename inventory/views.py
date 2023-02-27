from django.shortcuts import render
from django.views.generic import ListView

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase


def home(request):
    context = {"name": "User"}
    return render(request, "inventory/home.html", context)


# Ingredient views
class IngredientList(ListView):
    model = Ingredient


# MenuItem views
class MenuItemList(ListView):
    model = MenuItem

# RecipeRequirement views
class RecipeRequirementList(ListView):
    model = RecipeRequirement


# Purchase views
class PurchaseList(ListView):
    model = Purchase

