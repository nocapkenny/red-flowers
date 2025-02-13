from django.contrib import admin
from docapp.models import OfferItem,Offer,Counterparty

# Register your models here.

class OfferItemInlineAdmin(admin.TabularInline):
    model = OfferItem

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    inlines = [OfferItemInlineAdmin]

@admin.register(Counterparty)
class CounterpartyAdmin(admin.ModelAdmin):
    pass
