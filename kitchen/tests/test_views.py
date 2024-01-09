from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from kitchen.models import Ingredient, Dish

INGREDIENT_URL = reverse("kitchen:ingredient-list")
DISH_URL = reverse("kitchen:dish-list")
COOK_URL = reverse("kitchen:cook-list")


# <----- Ingredient Views ----->
class PublicIngredientTest(TestCase):
    def test_login_required(self) -> None:
        """
        Test that login is required to access ingredient list
        :return:
        """
        res = self.client.get(INGREDIENT_URL)
        self.assertNotEquals(res.status_code, 200)


class PrivateIngredientTest(TestCase):
    def setUp(self) -> None:
        self.client.force_login(get_user_model().objects.create_user(
            username="testuser",
            password="testpass",
            first_name="Test",
            last_name="User",
            years_of_experience=5,
        ))

    def test_retrieve_ingredients(self) -> None:
        """
        Test retrieving ingredients
        :return:
        """
        Ingredient.objects.create(name="Test Ingredient")
        Ingredient.objects.create(name="Test Ingredient 2")
        res = self.client.get(INGREDIENT_URL)
        self.assertEqual(res.status_code, 200)
        ingredients = Ingredient.objects.all()
        self.assertEqual(res.context["object_list"].count(), ingredients.count())
        self.assertTemplateUsed(res, "kitchen/ingredient_list.html")


# <----- Dish Views ----->
class PublicDishTest(TestCase):
    def test_login_required(self) -> None:
        """
        Test that login is required to access dish list
        :return:
        """
        res = self.client.get(DISH_URL)
        self.assertNotEquals(res.status_code, 200)


class PrivateDishTest(TestCase):
    def setUp(self) -> None:
        self.client.force_login(get_user_model().objects.create_user(
            username="testuser",
            password="testpass",
            first_name="Test",
            last_name="User",
            years_of_experience=5,
        ))

    def test_retrieve_dishes(self) -> None:
        """
        Test retrieving dishes
        :return:
        """
        dish = Dish.objects.create(
            name="Test Dish",
            description="Test Description",
            price=10.00,
        )
        dish.ingredients.add(Ingredient.objects.create(name="Test Ingredient"))
        res = self.client.get(DISH_URL)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "kitchen/dish_list.html")
        dishes = Dish.objects.all()
        self.assertEqual(res.context["object_list"].count(), dishes.count())
        self.assertTemplateUsed(res, "kitchen/dish_list.html")


# <----- Cook Views ----->
class PublicCookTest(TestCase):
    def test_login_required(self) -> None:
        """
        Test that login is required to access cook list
        :return:
        """
        res = self.client.get(COOK_URL)
        self.assertNotEquals(res.status_code, 200)


class PrivateCookTest(TestCase):
    def setUp(self) -> None:
        self.client.force_login(get_user_model().objects.create_user(
            username="testuser",
            password="testpass",
            first_name="Test",
            last_name="User",
            years_of_experience=5,
        ))

    def test_retrieve_cooks(self) -> None:
        """
        Test retrieving cooks
        :return:
        """
        res = self.client.get(COOK_URL)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "kitchen/cook_list.html")
        cooks = get_user_model().objects.all()
        self.assertEqual(res.context["object_list"].count(), cooks.count())
        self.assertTemplateUsed(res, "kitchen/cook_list.html")
