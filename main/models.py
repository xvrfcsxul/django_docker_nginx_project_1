from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(blank=True, null=True)
    theme = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.title

User.add_to_class('registered_events', models.ManyToManyField(Event, blank=True))

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    events = models.ManyToManyField('Event', blank=True)

    def __str__(self):
        return self.user.username