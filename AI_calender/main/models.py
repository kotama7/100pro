from pickle import NONE
from django.db import models

# Create your models here.
class Individual_data(models.Model):
    name = models.CharField(max_length=100,primary_key=True,unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    start_date = models.DateField()
    description = models.CharField(max_length=100,blank=True)
    end_date = models.DateField()
    user_data = models.ForeignKey(Individual_data,on_delete=models.CASCADE)

    def __str__(self):
        return self.description

