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
    
class GalleryCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория галерии'
        verbose_name_plural = 'Категории галерии'
        
class GalleryImage(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='gallery/', verbose_name='Изображение')
    
    def __str__(self):
        return f"Фото {self.id} ({self.category.name})"
    
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
