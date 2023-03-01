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
    template_name = ""
    form_class = IngredientCreateForm


# MenuItem views
class MenuItemList(ListView):
    model = MenuItem


class MenuItemCreate(CreateView):
    model = MenuItem
    template_name = ""
    form_class = MenuItemCreateForm


# RecipeRequirement views
class RecipeRequirementList(ListView):
    model = RecipeRequirement


class RecipeRequirementCreate(CreateView):
    model = RecipeRequirement
    template_name = ""
    form_class = RecipeRequirementCreateForm


# Purchase views
class PurchaseList(ListView):
    model = Purchase


class PurchaseCreate(CreateView):
    model = Purchase
    template_name = ""
    form_class = PurchaseCreateForm
