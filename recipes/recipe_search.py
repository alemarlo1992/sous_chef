import os 
import requests 
import json 
from django.http import HttpResponse
from django.template.loader import render_to_string

def search_recipe(recipe):

    url  = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"
    headers = {
            'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
            'x-rapidapi-key': ""
        }

    querystring = {"query":recipe}

    response = requests.request("GET", url, headers=headers, params=querystring)

    resp = response.json()

    return resp  

def get_ingredients(id):

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"+str(id)+"/ingredientWidget.json"

    headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': ""
    }

    response = requests.request("GET", url, headers=headers)
    resp = response.json()
    
    return resp

def recipe(id):

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"+str(324694)+"/analyzedInstructions"

    querystring = {"stepBreakdown":"false"}

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': ""
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    resp = response.json()
    
    return resp








    