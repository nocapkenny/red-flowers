from stockapp.models import Goods, GalleryCategory, GalleryImage, PriceFile
from rest_framework import serializers
import os

class GoodsSerializer(serializers.ModelSerializer):
    genus_name  = serializers.CharField(read_only=True)
    species_name  = serializers.CharField(read_only=True)
    pot_size = serializers.CharField(read_only=True)
    class Meta:
        model = Goods
        fields = "__all__"
    
class PotSizeSerializer(serializers.Serializer):
    pot_size = serializers.CharField(read_only=True)
    
class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = "__all__"

class GalleryCategorySerializer(serializers.ModelSerializer):
    images = GalleryImageSerializer(many=True, read_only=True)
    first_image = serializers.SerializerMethodField()
    class Meta:
        model = GalleryCategory
        fields = "__all__"    

    def get_first_image(self, obj):
        first_image = obj.images.first()
        return first_image.image.url if first_image else None
    
class PriceFileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    
    def get_name(self, obj):
        return os.path.basename(obj.file.name)
    
    class Meta:
        model = PriceFile
        fields = ['id', 'file', 'name', 'is_active', 'uploaded_at']
        read_only_fields = ['uploaded_at', 'name']
    

