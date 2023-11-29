from django import forms
from .models import Event
from django.forms.widgets import DateTimeInput

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'theme', 'link']
        widgets = {
            'date': DateTimeInput(attrs={'type': 'datetime-local'}),
        }