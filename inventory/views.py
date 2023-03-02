from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Sum, F

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm


class HomeView(TemplateView):
    template_name = "inventory/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["menu_items"] = MenuItem.objects.all()
        context["purchases"] = Purchase.objects.all()
        return context

# Ingredient views
class IngredientList(ListView):
    model = Ingredient


class IngredientCreate(CreateView):
    model = Ingredient
    template_name = "inventory/ingredient_create_form.html"
    form_class = IngredientForm


class IngredientUpdate(UpdateView):
    model = Ingredient
    template_name = "inventory/ingredient_update.html"
    form_class = IngredientForm


class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete.html"


# MenuItem views
class MenuItemList(ListView):
    model = MenuItem


class MenuItemCreate(CreateView):
    model = MenuItem
    template_name = "inventory/menuitem_create_form.html"
    form_class = MenuItemForm


class MenuItemUpdate(UpdateView):
    model = MenuItem
    template_name = "inventory/menuitem_update.html"
    form_class = MenuItemForm


class MenuItemDelete(DeleteView):
    model = MenuItem
    template_name = "inventory/menuitem_delete.html"
    form_class = MenuItemForm


# RecipeRequirement views
class RecipeRequirementList(ListView):
    model = RecipeRequirement


class RecipeRequirementCreate(CreateView):
    model = RecipeRequirement
    template_name = "inventory/recipe_requirement_create_form.html"
    form_class = RecipeRequirementForm


class RecipeRequirementUpdate(UpdateView):
    model = RecipeRequirement
    template_name = "inventory/recipe_requirement_update_form.html"
    form_class = RecipeRequirementForm


class RecipeRequirementDelete(DeleteView):
    model = RecipeRequirement
    template_name = "inventory/recipe_requirement_delete_form.html"
    form_class = RecipeRequirementForm


# Purchase views
class PurchaseList(ListView):
    model = Purchase


class PurchaseCreate(CreateView):
    model = Purchase
    template_name = "inventory/purchase_create_form.html"
    form_class = PurchaseForm


class PurchaseUpdate(UpdateView):
    model = Purchase
    template_name = "inventory/purchase_update_form.html"
    form_class = PurchaseForm


class PurchaseDelete(DeleteView):
    model = Purchase
    template_name = "inventory/purchase_delete_form.html"
    form_class = PurchaseForm


# View for report page

class ReportView(TemplateView):
    template_name = "inventory/report_template.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["purchases"] = Purchase.objects.all()
        revenue = Purchase.objects.aggregate(revenue=Sum("menu_item__price"))["revenue"]
        total_cost = 0
        for purchase in Purchase.objects.all():
            for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
                total_cost += recipe_requirement.ingredient.unit_price * recipe_requirement.quantity

        context["revenue"] = revenue
        context["total_cost"] = total_cost
        context["profit"] = revenue - total_cost

        return context
