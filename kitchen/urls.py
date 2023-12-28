from django.urls import path

from kitchen.views import index, CookListView, DishListView, IngredientListView, CookDetailView, DishDetailView, \
    IngredientDetailView, DishCreateView, IngredientCreateView, CookCreateView, CookXPUpdateView

urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/<int:pk>/update/", CookXPUpdateView.as_view(), name="cook-xp-update"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path("ingredients/<int:pk>/", IngredientDetailView.as_view(), name="ingredient-detail"),
    path("ingredients/create/", IngredientCreateView.as_view(), name="ingredient-create"),
]

app_name = "kitchen"
