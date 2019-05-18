from django.db import models
from api.apps.author.models import Author
from api.apps.category.models import Category


class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=500)
    image_url = models.URLField(max_length=500)
    author = models.ManyToManyField(Author)
    isbin = models.CharField(max_length=20) # primary_key=True
    year = models.PositiveSmallIntegerField()
    language = models.CharField(max_length=50)
    file_size = models.CharField(max_length=50)
    file_format = models.CharField(max_length=10)
    category = models.ManyToManyField(Category)
    description = models.TextField()
    download_link = models.URLField(max_length=500)

    def __str__(self):
        return self.title

