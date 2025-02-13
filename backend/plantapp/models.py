from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('Category',blank=True,null=True,on_delete=models.PROTECT)
    def __str__(self):
        return self.name

class Genus(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    name_latin = models.CharField(max_length=255,blank=True)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Species(models.Model):
    genus = models.ForeignKey(Genus,on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    name_latin = models.CharField(max_length=255,blank=True)
    description=models.TextField(blank=True)
    def __str__(self):
        return self.name


class Plant(models.Model):
    species= models.ForeignKey(Species,on_delete=models.PROTECT)
    sort = models.CharField(max_length=255,blank=True)
    sort_latin = models.CharField(max_length=255,blank=True)
    description=models.TextField(blank=True,verbose_name="Описание")
    technology=models.TextField(blank=True,verbose_name="Агротехника")
    usage=models.TextField(blank=True,verbose_name='Использование')
    img = ThumbnailerImageField(blank=True,null=True)
    def get_description(self):
        if self.description:
            return self.description
        else:
            return self.species.description
    def preview(self):
        if self.img:
            return self.img['preview'].url

    def detail(self):
        if self.img:
            return self.img['detail'].url


    def species_name(self):
        return self.species.name.replace(self.species.genus.name,'').strip()
    def __str__(self):
        return self.species.genus.name +" " +self.species.name


class Photo(models.Model):
    plant =models.ForeignKey(Plant,on_delete=models.PROTECT)
    img = ThumbnailerImageField(blank=True,null=True)
    def preview(self):
        if self.img:
            return self.img['preview'].url

    def detail(self):
        if self.img:
            return self.img['detail'].url




