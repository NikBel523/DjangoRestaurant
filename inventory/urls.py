from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # Ingredient paths
    path('ingredient/list', views.IngredientList.as_view(), name='ingredient_list'),

    # Menu items paths
    path('menu_item/list', views.MenuItemList.as_view(), name='menu_item_list'),

    # Recipes paths
    path('recipe_req/list', views.RecipeRequirementList.as_view(), name="reciperequirement_list"),

    # Purchase paths
    path('purchase/list', views.PurchaseList.as_view(), name='purchase_list'),

]
