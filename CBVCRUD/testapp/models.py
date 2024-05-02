from django.db import models
from django.urls import reverse

class Books(models.Model):
    title=models.CharField(max_length=55)
    author=models.CharField(max_length=55)
    pages=models.IntegerField()
    price=models.FloatField()

    def get_absolute_url(self):
        return reverse('detail')