from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('ingredient/list', views.IngredientList.as_view(), name='ingredient_list'),
    path('menu_item/list', views.MenuItemList.as_view(), name='menu_item_list'),
    path('recipe_req/list', views.RecipeRequirementList.as_view(), name="recipe_req_list"),
    path('purchase/list', views.PurchaseList.as_view(), name='purchase_list'),

]
