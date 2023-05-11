from django.shortcuts import render

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

def privacy_policy(request):
    return render(request, 'privacy-policy.html')

def register(request):
    return render(request, 'register.html')

def error_404(request, exception):
    return render(request, '404-error.html')
