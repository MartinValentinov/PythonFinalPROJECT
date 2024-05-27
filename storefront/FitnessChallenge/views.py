from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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

        messages.success(request, 'You have successfully created an account! We have sent you a confirmation email, please confirm your account.')

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
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')

