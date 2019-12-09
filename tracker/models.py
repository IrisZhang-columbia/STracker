from django.db import models

# Create your models here.


class Sighting(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    unique_squirrel_id = models.CharField(primary_key=True, max_length=16)
    shift = models.CharField(choices=(('AM', 'AM'), ('PM', 'PM')), max_length=4)
    date = models.CharField(max_length=8)
    age = models.CharField(choices=(('?', '?'), ('Adult', 'Adult'), ('Juvenile', 'Juvenile')), max_length=12, blank=True)
    primary_fur_color = models.CharField(choices=(('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')), max_length=8, blank=True)
    location = models.CharField(choices=(('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')), max_length=12, blank=True)
    specific_location = models.TextField(blank=True)
    chasing = models.BooleanField()
    running = models.BooleanField()
    climbing = models.BooleanField()
    eating = models.BooleanField()
    foraging = models.BooleanField()
    other_activities = models.TextField(blank=True)
    kuks = models.BooleanField()
    quaas = models.BooleanField()
    moans = models.BooleanField()
    tail_flags = models.BooleanField()
    tail_twitches = models.BooleanField()
    approaches = models.BooleanField()
    indifferent = models.BooleanField()
    runs_from = models.BooleanField()
