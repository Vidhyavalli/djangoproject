from django.db import models

# Create your models here.
class data(models.Model):
   name=models.CharField(max_length=20)
   age=models.IntegerField()
   city=models.CharField(max_length=20)
   address=models.CharField(max_length=50)