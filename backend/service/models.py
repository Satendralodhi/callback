from django.db import models

# Create your models here.
class CALLBACK(models.Model):
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Mobile_Number=models.CharField(max_length=10)
    Email_Id=models.EmailField()
    Class=models.CharField(max_length=20)
    Goal=models.CharField(max_length=50)
    Preferred_Mode=models.CharField(max_length=20)
    State=models.CharField(max_length=20)
    Tearm_condition=models.BooleanField()
    Permission=models.BooleanField()
    

