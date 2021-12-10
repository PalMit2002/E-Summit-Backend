from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)


class Notify(models.Model):
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
