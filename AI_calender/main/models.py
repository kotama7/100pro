from django.db import models
from datetime import date

# Create your models here.
class schedule(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)
    mode = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class Individual_data(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    data = models.ForeignKey(schedule,on_delete=models.CASCADE)
