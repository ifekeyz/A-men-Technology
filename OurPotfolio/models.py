from django.db import models
from datetime import datetime

class Project(models.Model):
    Name = models.CharField(max_length=20)
    Image1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    Image2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    Image3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    Category = models.CharField(max_length=50)
    Client = models.CharField(max_length=50)
    Project_date = models.DateField(auto_now_add=False)
    Url = models.CharField(max_length=50)

    Name1 = models.CharField(max_length=20)
    Image11 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    Image21 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    Image31 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    Category1 = models.CharField(max_length=50)
    Client1 = models.CharField(max_length=50)
    Project_date1 = models.DateField(auto_now_add=False)
    Url1 = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
# Create your models here.
