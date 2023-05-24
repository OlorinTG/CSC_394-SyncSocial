from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def group_meetup(request):
    return render(request, 'group-meetup.html')

def meeting_time_location_suggestion(request):
    return render(request, 'meeting-time-location-suggestion.html')

def notification(request):
    return render(request, 'notification.html')

def one_to_one_meetup(request):
    return render(request, 'one-to-one-meetup.html')

def polling(request):
    return render(request, 'polling.html')

def register(request):
    return render(request, 'register.html')

def error_404(request, exception):
    return render(request, '404-error.html')
def login(request):
    return render(request, 'login.html')
def calendar(request):
    return render(request, 'calendar.html')

def group(request):
    return render(request, 'group.html')

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'email', 'dates_free')  # Add other fields if you want


def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # or wherever you want to redirect the user after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})  # update the template name as per your project

def login_user(request):
    if request.method == 'POST':
        username = request.POST['login-email']
        password = request.POST['login-password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            ...
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})