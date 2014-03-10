from django.db import models

# Create your models here.
class Balance(models.Model):
    wallet = models.CharField(max_length=50)
    acc = models.CharField(max_length=50)
    cur = models.CharField(max_length=3)
    amount = models.IntegerField()
    stamp = models.CharField(max_length=20)

