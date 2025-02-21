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

class Vacancy(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название вакансии')
    salary = models.CharField(max_length=100, verbose_name='Зарплата')
    schedule = models.CharField(max_length=100, verbose_name='График')
    education = models.CharField(max_length=100, verbose_name='Образование')
    experience = models.CharField(max_length=100, verbose_name='Опыт')
    contacts_phone = models.CharField(max_length=100, verbose_name='Контактный телефон')
    contacts_email = models.EmailField(max_length=100, verbose_name='Контактная почта')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
    