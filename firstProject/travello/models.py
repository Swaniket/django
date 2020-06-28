from django.db import models

# Create your models here.

# To manage destinations 
# We will create the objects in the views.py
# models.Model is for converting the class into a model
class Destination(models.Model):
    # Creating variables to create db table
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    decs = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
