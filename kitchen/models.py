from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.username})"


class Dish(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ingredients = models.ManyToManyField("Ingredient", related_name="dishes")
    dish_type = models.ManyToManyField(DishType, related_name="dishes")
    cooks = models.ManyToManyField(Cook, related_name="dishes")

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
