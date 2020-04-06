from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('results/', views.results, name='recipe-results'),
    path('ingredients_<id>/', views.ingredients, name='recipe-ingredients')

]


