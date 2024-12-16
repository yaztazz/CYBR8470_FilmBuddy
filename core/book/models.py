from django.db import models


from django.contrib.auth.models import User

class Emenitites(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Movie(models.Model):
    movie_name =models.CharField(max_length=100)
    movie_description = models.TextField()
    movie_image = models.CharField(max_length=500)
    price = models.IntegerField()
    emenities = models.ManyToManyField(Emenitites)
    title = models.CharField(max_length=255)
    image_url = models.URLField(default='http://127.0.0.1:8000/static/images/default.jpg')  # URL for the movie image
    
    def __str__(self):
        return self.movie_name
    

