from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from django.urls import path
import plantapp.views as plan_view
import docapp.views as doc_view
import stockapp.views as stock_view

router = DefaultRouter()
router.register(r'plantapp/plant', plan_view.PlantViewSet, basename='plan')
router.register(r'plantapp/genus', plan_view.GenusViewSet, basename='genus')
router.register(r'plantapp/category',
                plan_view.CategoryViewSet, basename='category')
router.register(r'plantapp/photo', plan_view.PhotoViewSet, basename='photo')

router.register(r'docapp/offer', doc_view.OfferViewSet, basename='offer')
router.register(r'docapp/offeritem', doc_view.OfferItemViewSet,
                basename='offeritem')
router.register(r'docapp/counterparty',
                doc_view.CounterpartyViewSet, basename='counterparty')
router.register(r'docapp/vacancy', doc_view.VacancyViewSet, basename='vacancy')

router.register(r'stockapp/goods', stock_view.GoodsViewSet, basename='goods')
urlpatterns = [path('api/', include(router.urls)),
               path('api/stockapp/pot-sizes/',
                    stock_view.PotSizeListView.as_view(), name='pot-sizes'),
               ]
