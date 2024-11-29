from django.db import models

# Create your models here.
class Product(models.Model):
    pname = models.CharField(max_length=255)
    pdescription = models.TextField(max_length=2083)
    price = models.IntegerField()
    