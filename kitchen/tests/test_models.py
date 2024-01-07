from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import Ingredient, Dish, Cook, DishType


class ModelTests(TestCase):
    # <----- str tests ----->
    def test_ingredient_str(self) -> None:
        ingredient = Ingredient.objects.create(name="Test Ingredient")
        self.assertEqual(str(ingredient), "Test Ingredient")

    def test_dish_str(self) -> None:
        ingredient = Ingredient.objects.create(name="Test Ingredient")
        dish = Dish.objects.create(
            name="Test Dish",
            description="Test Description",
            price=10.00,
        )
        dish.ingredients.add(ingredient)
        self.assertEqual(str(dish), "Test Dish")

    def test_cook_str(self) -> None:
        cook = get_user_model().objects.create_user(
            username="testuser",
            password="testpass",
            first_name="Test",
            last_name="User",
            years_of_experience=5,
        )
        self.assertEqual(str(cook), "Test User (testuser)")

    def test_dish_type_str(self) -> None:
        dish_type = DishType.objects.create(name="Test Dish Type")
        self.assertEqual(str(dish_type), "Test Dish Type")

    def test_cook_password_is_hashed(self) -> None:
        password = "testpass"
        cook = get_user_model().objects.create_user(
            username="testuser",
            password=password,
            first_name="Test",
            last_name="User",
            years_of_experience=5,
        )
        self.assertTrue(cook.check_password("testpass"))
        self.assertNotEqual(cook.password, password)

