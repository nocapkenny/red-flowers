from django.contrib import admin
from stockapp.models import Pot,Goods, GalleryCategory, GalleryImage, PriceFile

# Register your models here.


@admin.register(Pot)
class PotAdmin(admin.ModelAdmin):
    list_display = ['id','size']
@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['plant','pot','price','height']
    
@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['id','category','image']
    list_filter = ['category']
    
@admin.register(PriceFile)
class PriceFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'is_active', 'uploaded_at')
    list_filter = ('is_active',)
    search_fields = ('file',)
