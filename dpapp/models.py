from django.contrib.gis.db import models

class Users(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)





