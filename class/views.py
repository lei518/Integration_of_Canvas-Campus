from django.contrib.auth import authenticate, login as auth_login , logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
def home_view(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home_view')  # Redirect to the home view after successful login
        else:
            messages.error(request, "Invalid username or password.")  # Add an error message
            return render(request, 'login.html')  # Render the login page again with an error
    else:
        return render(request, 'login.html')
def professor_dashboard(request):
        # Code to render the professor dashboard
        return render(request, 'prof.html')


def logout_view(request):
    logout(request)
    return redirect('login')


