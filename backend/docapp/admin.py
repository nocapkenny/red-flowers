from django.contrib import admin
from docapp.models import OfferItem, Offer, Counterparty, Vacancy

# Register your models here.


class OfferItemInlineAdmin(admin.TabularInline):
    model = OfferItem


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    inlines = [OfferItemInlineAdmin]


@admin.register(Counterparty)
class CounterpartyAdmin(admin.ModelAdmin):
    pass


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'salary', 'schedule')
    list_filter = ('education', 'experience')
