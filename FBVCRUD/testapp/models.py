from django.db import models

class Employee(models.Model):
    no=models.IntegerField()
    name=models.CharField(max_length=55)
    sal=models.IntegerField()
    addr=models.CharField(max_length=55)
