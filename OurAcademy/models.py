from django.db import models
from datetime import datetime

class Academy(models.Model):
    Name = models.CharField(max_length=20)
    Image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    Department = models.CharField(max_length=50)
    Duration = models.CharField(max_length=50)
    Academy_date = models.DateField(auto_now_add=False)
    Fee = models.CharField(max_length=50)
    Discount = models.CharField(max_length=10)

    Name2 = models.CharField(max_length=20)
    Image2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    Department2 = models.CharField(max_length=50)
    Duration2 = models.CharField(max_length=50)
    Academy_date2 = models.DateField(auto_now_add=False)
    Fee2 = models.CharField(max_length=50)
    Discount2 = models.CharField(max_length=10)

    def __str__(self):
        return self.Name
# Create your models here.