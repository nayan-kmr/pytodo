from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['firstName'] and request.POST['firstName'] and request.POST['firstName'] and request.POST['firstName']:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.get(username=request.POST['username'])
                    return render(request, 'accounts/signup.html', {'error':'Username already exists.'})
                except User.DoesNotExist:
                    user = User.objects.create_user(
                    username=request.POST['username'],
                    first_name=request.POST['firstName'],
                    last_name=request.POST['lastName'],
                    email=request.POST['email'],
                    password=request.POST['password1'])
                    auth.login(request, user)
                    return redirect('/tasks/')
            else:
                return render(request, 'accounts/signup.html', {'error':'Passwords need to match.'})
        else:
            return render(request, 'accounts/signup.html', {'error':'All fields are required.'})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        #if username matches that in the database, log the user in, or else show an error
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('/tasks/')
        else:
            return render(request, 'accounts/login.html', {'error':'Username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
