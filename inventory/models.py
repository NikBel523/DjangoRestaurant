from django.db import models

# Create your models here.


# Model for ingredients available in stock
class Ingredient(models.Model):
    UNIT_MEASURES = [
        ("KG", "Kilogram"),
        ("L", "Liter"),
        ("UN", "Unit"),
    ]
    name = models.CharField(max_length=30)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=2, choices=UNIT_MEASURES)
    unit_price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.name}"


# Model for each item of the menu
class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.name} for {self.price}$"


# Model for each recipe connected to is MenuItem and Ingredient
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.SET("NO INGREDIENT IN STORAGE"))
    quantity = models.FloatField(default=0)


# Model for monitoring of existing purchases of the MenuItems
class Purchases(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.SET("Menu item was deleted from menu"))
    time_stamp = models.DateTimeField(auto_now_add=True)
