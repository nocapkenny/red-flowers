from django.db import models

from stockapp.models import Goods
# Create your models here.

class Counterparty(models.Model):
    name = models.CharField(max_length=255)

class Offer(models.Model):
    counterparty = models.ForeignKey(Counterparty,on_delete=models.PROTECT)
    date = models.DateField(auto_now=True)

class OfferItem(models.Model):
    offer= models.ForeignKey(Offer,on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods,on_delete=models.PROTECT)
    count = models.IntegerField(default=1)
