from django.contrib import admin
from stockapp.models import Pot,Goods

# Register your models here.


@admin.register(Pot)
class PotAdmin(admin.ModelAdmin):
    list_display = ['id','size']
@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['plant','pot','price','height']
