from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm
from django.db.models import Q
from django.views.decorators.csrf import requires_csrf_token
def index(request):
    return render(request, 'foods/index.html')

def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('food_store')  # Ensure 'food_store' is the correct name of the URL pattern
    else:
        form = RecipeForm()
    return render(request, 'foods/add_recipe.html', {'form': form})

def food_store(request):
    query = request.GET.get('q')
    if query:
        recipes = Recipe.objects.filter(Q(name__icontains=query) | Q(requirements__icontains=query) | Q(procedure__icontains=query))
    else:
        recipes = Recipe.objects.all()
    return render(request, 'foods/food_store.html', {'recipes': recipes})

def like_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.likes += 1
    recipe.save()
    return redirect('food_store')  # Ensure 'food_store' is the correct name of the URL pattern

def about(request):
    return render(request, 'foods/about.html')

def explore(request):
    return render(request, 'foods/explore.html')