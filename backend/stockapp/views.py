from django.shortcuts import render
from plantapp.serializers import PlantSerializer
from plantapp.models import Plant
from rest_framework import viewsets,permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission,IsAuthenticated,DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
# Create your views here.
from rest_framework.decorators import action

from django.shortcuts import render
from django_filters import FilterSet
from django_filters import filters

from django_filters import FilterSet,BooleanFilter,CharFilter,MultipleChoiceFilter,DateFilter
from django.db.models import Q
from stockapp.models import Goods, GalleryImage, GalleryCategory, PriceFile
from stockapp.serializers import GoodsSerializer, PotSizeSerializer, GalleryCategorySerializer, GalleryImageSerializer, PriceFileSerializer


class GoodsSetFilter(FilterSet):
    search = CharFilter(method="get_search")
    pot_size = CharFilter(field_name='pot__size',lookup_expr="exact")
    def get_search(self, queryset, name, value):
        if value:
            queryset =  queryset.filter(Q(plant__sort__icontains=value)|
                                         Q(plant__species__name__icontains=value)|
                                         Q(plant__species__genus__name__icontains=value)
                                         )
        return queryset
    class Meta:
        model = Goods
        fields= '__all__'
        exclude = []

class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    model = Goods
    serializer_class = GoodsSerializer
    filter_backends = (DjangoFilterBackend,OrderingFilter)
    filterset_class  = GoodsSetFilter
    permission_classes = [IsAuthenticated,DjangoModelPermissions]
    
class PotSizeListView(APIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    def get(self, request):
        pot_sizes = Goods.objects.values_list('pot__size', flat=True).distinct()
        data = [{"pot_size": size} for size in pot_sizes]
        serializer = PotSizeSerializer(data, many=True)
        return Response(serializer.data)

class GalleryCategoryViewSet(viewsets.ModelViewSet):
    queryset = GalleryCategory.objects.all()
    serializer_class = GalleryCategorySerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
     

class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer 
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['category']
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    
class PriceFileViewSet(viewsets.ModelViewSet):
    queryset = PriceFile.objects.all()
    serializer_class = PriceFileSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    
    

