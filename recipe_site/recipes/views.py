from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import Recipe
from .forms import RecipeForm, UserRegisterForm, UserLoginForm


def home(request):
    recipes = Recipe.objects.all()[:5]  # Получаем 5 случайных рецептов
    return render(request, 'recipes/index.html', {'recipes': recipes})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'recipes/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Неверные учетные данные")
    else:
        form = UserLoginForm()

    return render(request, 'recipes/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def recipe_form(request, id=None):
    if id:
        recipe = Recipe.objects.get(id=id)
    else:
        recipe = None

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'recipes/recipe_form.html', {'form': form})


def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
