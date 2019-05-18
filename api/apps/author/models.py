from django.db import models


class Author(models.Model):
    author = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.author
