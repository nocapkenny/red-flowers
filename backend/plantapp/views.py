from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from plantapp.serializers import PlantSerializer,GenusSerializer,CategorySerializer,PhotoSerializer
from plantapp.models import Plant,Genus,Category,Photo
from rest_framework import viewsets,permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import BasePermission,IsAuthenticated,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
# Create your views here.
from rest_framework.decorators import action

from django.shortcuts import render
from django_filters import FilterSet
from django_filters import filters

from django_filters import FilterSet,BooleanFilter,CharFilter,MultipleChoiceFilter,DateFilter
from django.db.models import Q
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from stockapp.export_render import PriceRender

class IndexView(LoginRequiredMixin,TemplateView):
    template_name=  "index.html"

class PlantSetFilter(FilterSet):
    name = CharFilter(method="get_name")
    genus = CharFilter(field_name='species',lookup_expr="genus")
    genus__category = CharFilter(field_name='species',lookup_expr="genus__category")
    def get_name(self,queryset,name,value):
        if value:
            queryset =  queryset.filter(Q(sort__icontains=value)|
                                         Q(species__name__icontains=value)|
                                         Q(species__genus__name__icontains=value)
                                         )
        return queryset

    class Meta:
        model = Plant
        fields= '__all__'
        exclude = ['img']

class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    model = Plant
    serializer_class = PlantSerializer
    filter_backends = (DjangoFilterBackend,OrderingFilter)
    filterset_class  = PlantSetFilter
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    permission_classes = [IsAuthenticated,DjangoModelPermissions]
class GenusSetFilter(FilterSet):
    class Meta:
        model = Genus
        fields= '__all__'
        exclude = []

class GenusViewSet(viewsets.ModelViewSet):
    queryset = Genus.objects.all()
    model = Genus
    serializer_class = GenusSerializer
    filter_backends = (DjangoFilterBackend,OrderingFilter)
    filterset_class  = GenusSetFilter
    ordering_fields = ['name']
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    permission_classes = [IsAuthenticated,DjangoModelPermissions]
class CategorySetFilter(FilterSet):
    class Meta:
        model = Category
        fields= '__all__'
        exclude = []

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    model = Category
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend,OrderingFilter)
    filterset_class  = CategorySetFilter
    permission_classes = [IsAuthenticated,DjangoModelPermissions]
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    @action(methods=["GET"],detail=True)
    def price_xls(self,request,pk=None):
        obj = self.get_object()

        render = PriceRender(Plant.objects.filter(species__genus__category=obj),title=obj.name)
        response = HttpResponse(render.get_steam())
        response['Content-Disposition'] = 'attachment; filename=Прайс-лист_%s.xlsx' % str(
            obj.name)

        response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        return response




def getUser(request):
    if request.user.is_authenticated:
        user= {
            'username':request.user.username,
            'permissions':['change_plant']
        }
    else:
        user = {'permissions':[]}
    return JsonResponse(user)

class PhotoSetFilter(FilterSet):
    class Meta:
        model = Photo
        exclude = ['img']

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    model = Photo
    serializer_class = PhotoSerializer
    filter_backends = (DjangoFilterBackend,OrderingFilter)
    filterset_class  = PhotoSetFilter
    permission_classes = [IsAuthenticated,DjangoModelPermissions]
