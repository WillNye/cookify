from django.db import models
from django.contrib.auth.models import User

from ingredient.models import Ingredient, Measurement


class FoodType(models.Model):
    name = models.CharField(max_length=200, unique=True, db_column='Name')

    class Meta:
        db_table = 'FoodType'


class Recipe(models.Model):
    name = models.CharField(max_length=250, db_column='Name')
    user = models.ForeignKey(User, db_column='UserId')
    food_type = models.ForeignKey(FoodType, db_column='FoodType')
    recipe_image = models.FileField(db_column='RecipeImage')
    is_vegetarian = models.BooleanField(default=False, db_column='IsVegetarian')
    prep_time = models.TimeField(db_column='prepTime')
    cook_time = models.TimeField(db_column='cookTime')
    directions = models.TextField(db_column='Directions')
    ingredients = models.ManyToManyField(Ingredient, through='RecipeItem')
    subscribed_users = models.ManyToManyField(User, related_name='subscribed_users')

    class Meta:
        db_table = 'Recipe'


class RecipeItem(models.Model):
    ingredient = models.ForeignKey(Ingredient, db_column='IngredientId')
    measurement = models.ForeignKey(Measurement, db_column='MeasurementId')
    recipe = models.ForeignKey(Recipe, db_column='RecipeId')

    class Meta:
        db_table = 'RecipeItem'




