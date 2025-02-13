from stockapp.models import Goods
from rest_framework import serializers

class GoodsSerializer(serializers.ModelSerializer):
    genus_name  = serializers.CharField(read_only=True)
    species_name  = serializers.CharField(read_only=True)
    pot_size = serializers.CharField(read_only=True)

    class Meta:
        model = Goods
        fields = "__all__"

