from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_user, name='login'),
    path('home/', views.home, name='home'),
    path('add_event/', views.add_event, name='add_event'),
    path('register_for_event/', views.register_for_event, name='register_for_event'),
    path('register/<int:event_id>/', views.register, name='register'),
]