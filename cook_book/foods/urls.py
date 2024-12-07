from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('store/', views.food_store, name='food_store'),
    path('like/<int:recipe_id>/', views.like_recipe, name='like_recipe'),
    path('about/', views.about, name='about'),
    path('explore/', views.explore, name='explore'),
]