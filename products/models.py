from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.FloatField()
    summary = models.TextField(default="This is a great product.")