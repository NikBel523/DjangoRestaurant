from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    # Ingredient paths
    path('ingredient/list', views.IngredientList.as_view(), name='ingredient_list'),
    path('ingredient/create_form', views.IngredientCreate.as_view(), name='ingredient_create'),
    path('ingredient/update/<pk>', views.IngredientUpdate.as_view(), name='update_ingredient'),
    path('ingredient/delete/<pk>', views.IngredientDelete.as_view(), name='delete_ingredient'),

    # Menu items paths
    path('menu_item/list', views.MenuItemList.as_view(), name='menu_item_list'),
    path('menu_item/create', views.MenuItemCreate.as_view(), name='menu_item_create'),
    path('menu_item/update/<pk>', views.MenuItemUpdate.as_view(), name='menu_item_update'),
    path('menu_item/delete/<pk>', views.MenuItemDelete.as_view(), name='menu_item_delete'),

    # Recipes paths
    path('recipe_req/list', views.RecipeRequirementList.as_view(), name='reciperequirement_list'),
    path('recipe_req/create_form', views.RecipeRequirementCreate.as_view(), name='reciperequirement_create'),
    path('recipe_req/update/<pk>', views.RecipeRequirementUpdate.as_view(), name='reciperequirement_update'),
    path('recipe_req/delete/<pk>', views.RecipeRequirementDelete.as_view(), name='reciperequirement_delete'),

    # Purchase paths
    path('purchase/list', views.PurchaseList.as_view(), name='purchase_list'),
    path('purchase/create_form', views.NewPurchaseView.as_view(), name='purchase_create'),
    path('purchase/update/<pk>', views.PurchaseUpdate.as_view(), name='purchase_update'),
    path('purchase/delete/<pk>', views.PurchaseDelete.as_view(), name='purchase_delete'),

    # Utility paths
    path('report', views.ReportView.as_view(), name='report'),

]
