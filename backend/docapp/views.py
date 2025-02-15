from django.shortcuts import render
from rest_framework import viewsets,permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import BasePermission,IsAuthenticated,DjangoModelPermissions
# Create your views here.
from rest_framework.decorators import action

from django.shortcuts import render
from django_filters import FilterSet
from django_filters import filters



# Create your views here.
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import DetailView
from docapp.models import Offer,OfferItem,Counterparty
from docapp.serializers import OfferItemSerializer,OfferSerializer,CounterpartySerializer

from django.db.models import F,Sum, ExpressionWrapper,DecimalField

class OfferPDFView(PermissionRequiredMixin,DetailView):
    permission_required = 'letterapp.add_outgoingletter'
    context= {'title': 'Hello World!'}
    model = Offer
    template_name= 'offer_tex.tex'
    def latex_render(self, request, *args, **kwargs):
        self.context = self.get_context_data()
        obj =  self.get_object()
        from django_tex.core import render_template_with_context
        from django_tex.shortcuts import render_to_pdf
        obj =  self.get_object()
        item_set = obj.offeritem_set.all().annotate(total=ExpressionWrapper(F('count')*F('goods__price'),output_field=DecimalField(max_digits=12,decimal_places=2)))
        self.context['item_set'] = item_set
        self.context['counterpary'] = obj.counterparty.name
        self.context['total'] = item_set.aggregate(Sum('total'))['total__sum']
        teml= render_template_with_context(self.template_name,self.context)

        f = open('test.tex','w')
        f.write(teml)
        f.close()

        return render_to_pdf(request,self.template_name, self.context, filename='offer_{}.pdf'.format(obj.id))

    def get(self, request, *args, **kwargs):
        obj =  self.get_object()
        self.object=obj
        return self.latex_render(request,*args,**kwargs)
class OfferSetFilter(FilterSet):
    class Meta:
        model = Offer
        fields= '__all__'
        exclude = []

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    model = Offer
    serializer_class = OfferSerializer
    filter_backends = (DjangoFilterBackend,OrderingFilter)
    filterset_class  = OfferSetFilter
    permission_classes = [IsAuthenticated,DjangoModelPermissions]


class OfferItemSetFilter(FilterSet):
    class Meta:
        model = OfferItem
        fields= '__all__'
        exclude = []

class OfferItemViewSet(viewsets.ModelViewSet):
    queryset = OfferItem.objects.all()
    model = OfferItem
    serializer_class = OfferItemSerializer
    filter_backends = (DjangoFilterBackend,OrderingFilter)
    filterset_class  = OfferItemSetFilter
    permission_classes = [IsAuthenticated,DjangoModelPermissions]

class CounterpartySetFilter(FilterSet):
    class Meta:
        model = Counterparty
        fields= '__all__'
        exclude = []

class CounterpartyViewSet(viewsets.ModelViewSet):
    queryset = Counterparty.objects.all()
    model = Counterparty
    serializer_class = CounterpartySerializer
    filter_backends = (DjangoFilterBackend,OrderingFilter)
    filterset_class  = CounterpartySetFilter
    permission_classes = [IsAuthenticated,DjangoModelPermissions]
