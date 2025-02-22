from stockapp.models import Goods, GalleryCategory, GalleryImage
from rest_framework import serializers

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
    

