from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True, db_column='Name')

    class Meta:
        db_table = 'Ingredient'


class Measurement(models.Model):
    description = models.CharField(max_length=100, unique=True, db_column='Description')

    class Meta:
        db_table = 'Measurement'

