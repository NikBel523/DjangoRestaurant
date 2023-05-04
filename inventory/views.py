from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Sum
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm


LOGIN_URL = "../login/"

def login_view(request):
    context = {
        "login_view": "active",
    }
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return HttpResponse("invalid credentials")

    return render(request, "registration/login.html", context)


class HomeView(TemplateView):
    template_name = "inventory/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["menu_items"] = MenuItem.objects.all()
        context["purchases"] = Purchase.objects.all()
        return context


# Ingredient views
class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient
    login_url = LOGIN_URL


class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = "inventory/ingredient_create_form.html"
    form_class = IngredientForm


class IngredientUpdate(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = "inventory/ingredient_update.html"
    form_class = IngredientForm


class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete.html"


# MenuItem views
class MenuItemList(LoginRequiredMixin, ListView):
    model = MenuItem
    login_url = LOGIN_URL


class MenuItemCreate(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = "inventory/menuitem_create_form.html"
    form_class = MenuItemForm


class MenuItemUpdate(LoginRequiredMixin, UpdateView):
    model = MenuItem
    template_name = "inventory/menuitem_update.html"
    form_class = MenuItemForm


class MenuItemDelete(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = "inventory/menuitem_delete.html"
    form_class = MenuItemForm


# RecipeRequirement views
class RecipeRequirementList(LoginRequiredMixin, ListView):
    model = RecipeRequirement
    login_url = LOGIN_URL


class RecipeRequirementCreate(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    template_name = "inventory/recipe_requirement_create_form.html"
    form_class = RecipeRequirementForm


class RecipeRequirementUpdate(LoginRequiredMixin, UpdateView):
    model = RecipeRequirement
    template_name = "inventory/recipe_requirement_update_form.html"
    form_class = RecipeRequirementForm


class RecipeRequirementDelete(LoginRequiredMixin, DeleteView):
    model = RecipeRequirement
    template_name = "inventory/recipe_requirement_delete_form.html"
    form_class = RecipeRequirementForm


# Purchase views
class PurchaseList(LoginRequiredMixin, ListView):
    model = Purchase
    login_url = LOGIN_URL


class PurchaseUpdate(LoginRequiredMixin, UpdateView):
    model = Purchase
    template_name = "inventory/purchase_update_form.html"
    form_class = PurchaseForm


class PurchaseDelete(LoginRequiredMixin, DeleteView):
    model = Purchase
    template_name = "inventory/purchase_delete_form.html"
    form_class = PurchaseForm


class NewPurchaseView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/purchase_create_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_items"] = [item for item in MenuItem.objects.all() if item.available()]
        return context

    def post(self, request):
        menu_item_id = request.POST["menu_item"]
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        requirements = menu_item.reciperequirement_set
        purchase = Purchase(menu_item=menu_item)
        for requirement in requirements.all():
            required_ingredient = requirement.ingredient
            required_ingredient.quantity -= requirement.quantity
            required_ingredient.save()

        purchase.save()
        return redirect("/inventory/purchase/list")


# View for report page

class ReportView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/report_template.html"
    login_url = './login/'

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
