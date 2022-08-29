from django.db import models
from datetime import date

# Create your models here.
class schedule(models.Model):
    date = models.DateField()
    description = models.CharField()
    details = models.CharField()
    mode = models.CharField()

    def __str__(self):
        return self.description

class Individual_data(models.Model):
    name = models.CharField()
    password = models.CharField()
    data = models.ForeignKey(schedule,on_delete=models.CASCADE)
