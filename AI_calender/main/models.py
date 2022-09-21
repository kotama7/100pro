from django.db import models

# Create your models here.
class Individual_data(models.Model):
    name = models.CharField(max_length=100,primary_key=True,unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    start_date = models.DateTimeField()
    description = models.CharField(max_length=100,blank=True)
    end_date = models.DateTimeField()
    schedule_class = models.CharField(max_length=1) #labor=1,action=2,work=3
    user_data = models.ForeignKey(Individual_data,on_delete=models.CASCADE)

    def __str__(self):
        return self.description

