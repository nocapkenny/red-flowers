from rest_framework import serializers
from plantapp.models import Plant,Species,Genus,Category,Photo
from stockapp.models import Goods

class GoodsInlineSerializer(serializers.ModelSerializer):
    pot_size= serializers.CharField(read_only=True)
    class Meta:
        model = Goods
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
class GenusSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Genus
        fields = "__all__"
class SpeciesSerializer(serializers.ModelSerializer):
    genus = GenusSerializer()
    class Meta:
        model = Species
        fields = "__all__"

class PhotoSerializer(serializers.ModelSerializer):

    preview = serializers.CharField(read_only=True)
    detail= serializers.CharField(read_only=True)
    class Meta:
        model =Photo
        fields = "__all__"

class PlantSerializer(serializers.ModelSerializer):
    species = SpeciesSerializer()
    preview = serializers.CharField()
    detail= serializers.CharField()
    goods_set= GoodsInlineSerializer(read_only=True,many=True)
    min_price = serializers.SerializerMethodField()
    species_name = serializers.CharField()
    photo_set = PhotoSerializer(read_only=True,many=True)

    def get_min_price(self,obj):
        return obj.goods_set.all().order_by('price').first().price

    class Meta:
        model = Plant
        fields = "__all__"
