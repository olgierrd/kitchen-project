from django.urls import path

from kitchen.views import (
    index,
    CookListView,
    DishListView,
    IngredientListView,
    CookDetailView,
    DishDetailView,
    IngredientDetailView,
    DishCreateView,
    IngredientCreateView,
    CookCreateView,
    CookXPUpdateView,
    DishUpdateView,
    DishDeleteView,
    CookDeleteView,
    IngredientUpdateView,
    IngredientDeleteView, DishTypeCreateView
)

urlpatterns = [
    # <-----------Home------------------>
    path("", index, name="index"),
    # <-----------Cook Views-------------->
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/<int:pk>/update/", CookXPUpdateView.as_view(), name="cook-xp-update"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
    # <-----------Dish Views-------------->
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishtypes/create/", DishTypeCreateView.as_view(), name="type-create"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    # <-----------Ingredient Views-------------->
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path("ingredients/<int:pk>/", IngredientDetailView.as_view(), name="ingredient-detail"),
    path("ingredients/<int:pk>/update/", IngredientUpdateView.as_view(), name="ingredient-update"),
    path("ingredients/create/", IngredientCreateView.as_view(), name="ingredient-create"),
    path("ingredients/<int:pk>/delete/", IngredientDeleteView.as_view(), name="ingredient-delete"),
]


app_name = "kitchen"
