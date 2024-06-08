import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import DietCalculator, Diet, Product, Ingredient
from .forms import DietCalculatorForm

logger = logging.getLogger(__name__)


def home(request):
    return render(request, 'authentication/index.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('register')
        
        if len(username) > 10:
            messages.error(request, "Username is too long!")
            return redirect('register')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!")
            return redirect('register')

        if not username.isalnum():
            messages.error(request, "Username must be alpha-numeric!")
            return redirect('register')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')  

    return render(request, 'authentication/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'authentication/index.html', {'fname': fname})
        else:
            messages.error(request, "Your Username or Password is wrong")
            return redirect('login')

    return render(request, 'authentication/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def about(request):
    return render(request, 'about.html')

def diet_calculator(request):
    if request.method == 'POST':
        form = DietCalculatorForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data['weight']
            age = form.cleaned_data['age']
            height = form.cleaned_data['height']
            sex = form.cleaned_data['sex']
            activity = form.cleaned_data['activity']
            goal = form.cleaned_data['goal']
            
            bmr = calculate_bmr(weight, age, height, sex)
            recommended_calories = calculate_calories(bmr, activity, goal)

            diet = form.save(commit=False)
            diet.bmr = bmr
            diet.recommended_calories = recommended_calories
            diet.save()
            logger.info(f"Diet created with ID: {diet.id}")

            return render(request, 'diets/diet_calculator_result.html', {
                'recommended_calories': recommended_calories,
                'diet_id': diet.id,
            })
        else:
            logger.error("Form is not valid: %s", form.errors)
    else:
        form = DietCalculatorForm()
    return render(request, 'diets/diet_calculator.html', {'form': form})

def diet_detail(request, diet_id):
    diet = get_object_or_404(Diet, pk=diet_id)
    return render(request, 'diets/diet_detail.html', {'diet': diet})

def calculate_bmr(weight, age, height, sex):
    weight = float(weight)
    age = int(age)
    height = float(height)

    if sex == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return round(bmr, 2)

def calculate_calories(bmr, activity, goal):
    activity_multiplier = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very_active': 1.9
    }
    calories = bmr * activity_multiplier[activity]

    if goal == 'lose':
        calories -= 500
    elif goal == 'gain':
        calories += 500 

    return round(calories, 1)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'diets/product_detail.html', {'product': product})

def ingredient_detail(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
    return render(request, 'diets/ingredient_detail.html', {'ingredient': ingredient})

def diet_list(request):
    diets = Diet.objects.all()
    return render(request, 'diets/diet_list.html', {'diets': diets})