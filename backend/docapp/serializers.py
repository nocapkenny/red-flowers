from rest_framework import serializers
from docapp.models import Offer,OfferItem,Counterparty
from docapp.serializers_base import ModelSerializerId
from stockapp.models import Goods
from docapp.models import Vacancy


class CounterpartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Counterparty
        fields = "__all__"

class CounterpartyInlineSerializer(ModelSerializerId):
    class Meta:
        model = Counterparty
        fields = "__all__"

class OfferSerializer(serializers.ModelSerializer):
    counterparty = CounterpartyInlineSerializer()
    class Meta:
        model = Offer
        fields = "__all__"

class GoodsInlineSerializer(ModelSerializerId):
    genus_name  = serializers.CharField(read_only=True)
    species_name  = serializers.CharField(read_only=True)

    class Meta:
        model = Goods
        fields = "__all__"
class OfferItemSerializer(serializers.ModelSerializer):
    goods =GoodsInlineSerializer()
    class Meta:
        model = OfferItem
        fields = "__all__"
        
class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = "__all__"

