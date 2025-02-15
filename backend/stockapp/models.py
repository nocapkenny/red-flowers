from django.db import models
from plantapp.models import Plant
# Create your models here.

class Pot(models.Model):
    size = models.CharField(max_length=10)
    def __str__(self):
        return self.size

class Storage(models.Model):
    name = models.CharField(max_length=255)


class Goods(models.Model):
    plant = models.ForeignKey(Plant,on_delete=models.PROTECT)
    pot = models.ForeignKey(Pot,on_delete=models.PROTECT)
    height = models.CharField(max_length=10,blank=True)
    price = models.DecimalField(blank=True, null=True, max_digits=12, decimal_places=2)
    def genus_name(self):
        return self.plant.species.genus.name
    def species_name(self):
        return self.plant.species.name
    def pot_size(self):
        return self.pot.size
    def __str__(self):
        return self.plant.__str__()+". конт. " + self.pot_size()

class StorageItem(models.Model):
    storage = models.ForeignKey(Storage,on_delete=models.PROTECT)
    quantity = models.IntegerField()
    goods = models.ForeignKey(Goods,on_delete=models.PROTECT)
