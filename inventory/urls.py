from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # Ingredient paths
    path('ingredient/list', views.IngredientList.as_view(), name='ingredient_list'),
    path('ingredient/create_form', views.IngredientCreate.as_view(), name='ingredient_create'),

    # Menu items paths
    path('menu_item/list', views.MenuItemList.as_view(), name='menu_item_list'),
    path('menu_item/create', views.MenuItemCreate.as_view(), name='menu_item_create'),

    # Recipes paths
    path('recipe_req/list', views.RecipeRequirementList.as_view(), name="reciperequirement_list"),
    path('recipe_req/create_form', views.RecipeRequirementCreate.as_view(), name="reciperequirement_create"),

    # Purchase paths
    path('purchase/list', views.PurchaseList.as_view(), name='purchase_list'),
    path('purchase/create_form', views.PurchaseCreate.as_view(), name='purchase_create'),

]
