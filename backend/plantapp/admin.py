from django.contrib import admin
from plantapp.models import Plant,Species,Genus,Category,Photo

class PhotoPlantInlineAdmin(admin.TabularInline):
    model =Photo
# Register your models here.
@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_filter = ["species__genus"]
    list_display = ['species','sort']
    inlines =[PhotoPlantInlineAdmin]

class SpeciesInlineAdmin(admin.TabularInline):
    model = Species

@admin.register(Genus)
class GenusAdmin(admin.ModelAdmin):
    inlines=[SpeciesInlineAdmin,]

@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ['genus','name','name_latin']
    list_filter = ['genus__category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
