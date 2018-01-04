from django.db import models
from django.contrib.auth.models import User

from ingredient.models import Ingredient, Measurement


class ShoppingList(models.Model):
    name = models.CharField(max_length=300, db_column='Name')
    user = models.ForeignKey(User, db_column='UserId')
    ingredients = models.ManyToManyField(Ingredient, through='ShoppingItem')

    class Meta:
        db_table = 'ShoppingList'


class ShoppingItem(models.Model):
    ingredient = models.ForeignKey(Ingredient, db_column='IngredientId')
    measurement = models.ForeignKey(Measurement, db_column='MeasurementId')
    shopping_list = models.ForeignKey(ShoppingList, db_column='ShoppingListId')

    class Meta:
        db_table = 'ShoppingItem'




