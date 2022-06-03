# import email
# from pyexpat import model
# from unicodedata import name
from django.db import models

# Create your models here.
class contactus(models.Model):
    name = models.CharField(max_length=120)
    email=models.CharField(max_length=122)
    phone= models.CharField(max_length=122)
    subject = models.CharField(max_length=144)
    desc= models.TextField()

    def __str__(self):
        return self.name





    
