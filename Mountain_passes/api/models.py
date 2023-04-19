from django.db import models
from .rez import STATUS


class Tourist(models.Model):
    name = models.CharField(max_length=15)
    fam = models.CharField(max_length=15) # фамилия
    otc = models.CharField(max_length=15) # отчество
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name},{self.fam}, {self.email}'


class Pass(models.Model):
    beauty_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    other_titles = models.CharField(max_length=100)
    connect = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    add_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=8, choices=STATUS, default='new')
    tourist = models.ForeignKey('Tourist', on_delete=models.CASCADE)
    coordinates = models.ForeignKey('Coordinates', on_delete=models.CASCADE)
    levels = models.ForeignKey('Level', blank=True, on_delete=models.PROTECT)


class Coordinates(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.FloatField()


class Level(models.Model):
    winter_level = models.CharField(max_length=6, blank=True)
    spring_level = models.CharField(max_length=6, blank=True)
    summer_level = models.CharField(max_length=6, blank=True)
    autumn_level = models.CharField(max_length=6, blank=True)


class Images(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30)
    data = models.BinaryField()
    passes = models.ForeignKey('Pass', related_name='images', on_delete=models.CASCADE)
