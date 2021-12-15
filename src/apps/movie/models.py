from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=150, blank=False, default='')
    year = models.CharField(max_length=4)
    cover = models.CharField(max_length=200, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.CharField(max_length=3, blank=False, default='')
    short_description = models.TextField(blank=True, default='')
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rating