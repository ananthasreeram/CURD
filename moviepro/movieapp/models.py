from django.db import models

class MovieData(models.Model):
    movie_name=models.CharField(max_length=30)
    hero_name=models.CharField(max_length=30)
    heroine_name=models.CharField(max_length=30)
    director_name=models.CharField(max_length=30)
    rating=models.IntegerField()
    release_date=models.DateField(max_length=100)
    budget=models.IntegerField()
