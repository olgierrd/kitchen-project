from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import IngredientForm, DishForm, CookForm, CookXPForm
from kitchen.models import Cook, Dish, Ingredient


# Create your views here.

# home page
def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_visits = request.session.get("num_visits", 1)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_visits": num_visits,
    }
    return render(request, "kitchen/index.html", context=context)


# <-----------Cook Views-------------->
class CookListView(generic.ListView):
    model = Cook
    paginate_by = 5


class CookDetailView(generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dishes__ingredients")


class CookCreateView(generic.CreateView):
    model = Cook
    form_class = CookForm


class CookXPUpdateView(generic.UpdateView):
    model = Cook
    form_class = CookXPForm
    success_url = reverse_lazy("kitchen:cook-list")


class CookDeleteView(generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")


# <-----------Dish Views-------------->
class DishListView(generic.ListView):
    model = Dish
    paginate_by = 5


class DishDetailView(generic.DetailView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


class DishCreateView(generic.CreateView):
    model = Dish
    form_class = DishForm
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("dish_list")


class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


# <-----------Ingredient Views-------------->
class IngredientListView(generic.ListView):
    model = Ingredient
    template_name = "kitchen/ingredient_list.html"
    context_object_name = "ingredient_list"
    paginate_by = 5


class IngredientDetailView(generic.DetailView):
    model = Ingredient
    success_url = reverse_lazy("kitchen:ingredient-list")


class IngredientCreateView(generic.CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "kitchen/ingredient_form.html"
    success_url = reverse_lazy("ingredient_list")


class IngredientUpdateView(generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")


class IngredientDeleteView(generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("kitchen:ingredient-list")
