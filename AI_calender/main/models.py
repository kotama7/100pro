from django.db import models
from datetime import date

# Create your models here.
class Schedule(models.Model):
    start_date = models.DateField()
    description = models.CharField(max_length=100,blank=True)
    end_date = models.DateField()

    def __str__(self):
        return self.description

class Individual_data(models.Model):
    name = models.CharField(max_length=100,primary_key=True,unique=True)
    password = models.CharField(max_length=100)
    schedule = models.ForeignKey(Schedule,on_delete=models.CASCADE)

    def __str__(self):
        return self.schedule

    def __str__(self) -> str:
        return self.data