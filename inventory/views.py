from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientCreateForm, MenuItemCreateForm, RecipeRequirementCreateForm, PurchaseCreateForm


def home(request):
    context = {"name": "User"}
    return render(request, "inventory/home.html", context)


# Ingredient views
class IngredientList(ListView):
    model = Ingredient


class IngredientCreate(CreateView):
    model = Ingredient
    template_name = "inventory/ingredient_create_form.html"
    form_class = IngredientCreateForm


class IngredientUpdate(UpdateView):
    model = Ingredient
    template_name = "inventory/ingredient_update.html"
    form_class = IngredientCreateForm


class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete.html"


# MenuItem views
class MenuItemList(ListView):
    model = MenuItem


class MenuItemCreate(CreateView):
    model = MenuItem
    template_name = "inventory/menuitem_create_form.html"
    form_class = MenuItemCreateForm


# RecipeRequirement views
class RecipeRequirementList(ListView):
    model = RecipeRequirement


class RecipeRequirementCreate(CreateView):
    model = RecipeRequirement
    template_name = "inventory/recipe_requirement_create_form.html"
    form_class = RecipeRequirementCreateForm


# Purchase views
class PurchaseList(ListView):
    model = Purchase


class PurchaseCreate(CreateView):
    model = Purchase
    template_name = "inventory/purchase_create_form.html"
    form_class = PurchaseCreateForm
