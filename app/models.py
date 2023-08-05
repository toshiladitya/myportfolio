from django.db import models

# Create your models here.
class Guest(models.Model):
    name=models.CharField( max_length=200)
    email=models.EmailField( max_length=254)
    subject=models.CharField( max_length=300)
    message=models.TextField()