from django.db import models

# Create your models here.

class KodeeTrybee(models.Model):
    Category = models.CharField(max_length=50)
    Image1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    Image2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    Duration = models.CharField(max_length=50)
    Fee = models.CharField(max_length=20)
    Discount = models.CharField(max_length=20)
    Content = models.TextField(blank=False)
    Level = models.CharField(max_length=20)
    Push_date = models.DateField(auto_now_add=False)
    
    
    def __str__(self):
        return self.Category
        
class Form(models.Model):
    lastName = models.CharField(max_length=50, null=True)
    firstName = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=20, null=True)
    phoneNumber = models.CharField(max_length=15, null=True)
    city = models.CharField(max_length=20, null=True)
    education = models.CharField(max_length=20, null=True)
    course = models.CharField(max_length=20, null=True)
    knowlegde = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.lastName