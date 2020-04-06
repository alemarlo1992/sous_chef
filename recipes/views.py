from django.shortcuts import render
from django.template import loader, Context
from .models import Recipe 
from django.http import JsonResponse
from .recipe_search import *


def home(request):

    return render(request, 'recipes/home.html')

def results(request):

    recipe = request.POST['search_box']

    results = search_recipe(recipe)

    return render(request, 'recipes/results.html', results)

def ingredients(request, id):

    ingredients = get_ingredients(id) 


    return render(request, 'recipes/ingredients.html', ingredients)




