from django.db import models


# Create your models here.
class feed(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    body = models.TextField()
