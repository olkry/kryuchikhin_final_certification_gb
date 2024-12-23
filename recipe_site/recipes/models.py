# models.py
from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.ManyToManyField('Ingredient', related_name='recipes')
    steps = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


