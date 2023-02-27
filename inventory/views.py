from django.shortcuts import render
from django.views.generic import ListView

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
# Create your views here.


class IngredientList(ListView):
    model = Ingredient
    template_name = "inventory/ingredient_view.html"


class MenuItemList(ListView):
    model = MenuItem
    template_name = "inventory/menu_item.html"


class RecipeRequirementList(ListView):
    model = RecipeRequirement
    template_name = "inventory/recipe_requirements.html"


class PurchaseList(ListView):
    model = Purchase
    template_name = "inventory/purchase.html"