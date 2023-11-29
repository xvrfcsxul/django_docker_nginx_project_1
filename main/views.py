from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Event, UserProfile
from .forms import EventForm

def index(request):
    return render(request, 'index.html')

def registration(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()
        return redirect('index')
    return render(request, 'registration.html')

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Перенаправляем на страницу home после успешной авторизации
        else:
            # Обработка ошибки авторизации
            return render(request, 'login.html', {'error_message': 'Неверные почта или пароль'})
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

@login_required
def add_event(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            user_profile.events.add(event)
            return redirect('home')
    else:
        form = EventForm()

    return render(request, 'add_event.html', {'form': form})

@login_required
def register_for_event(request):
    events = Event.objects.all()
    user_events = request.user.registered_events.all()
    return render(request, 'register_for_event.html', {'events': events, 'user_events': user_events})

@login_required
def register(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    request.user.registered_events.add(event)
    return redirect('register_for_event')