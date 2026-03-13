from django.urls import path
from .views import (
    RecipeCreateView, RecipeUpdateView,
    RecipeListView, RecipeDetailView
)

urlpatterns = [
    path('', RecipeListView.as_view(), name='list-recipes'),                   # GET all the recipiec
    path('<int:id>/', RecipeDetailView.as_view(), name='recipe-detail'),      # GET one recipie by ID
    path('add/', RecipeCreateView.as_view(), name='add-recipe'),
]
