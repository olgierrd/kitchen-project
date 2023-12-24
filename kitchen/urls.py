from django.urls import path

from kitchen.views import index, CookListView, DishListView, IngredientListView, CookDetailView, DishDetailView, \
    IngredientDetailView

urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path("ingredients/<int:pk>/", IngredientDetailView.as_view(), name="ingredient-detail"),
]

app_name = "kitchen"
