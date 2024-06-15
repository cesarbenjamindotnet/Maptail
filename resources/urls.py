from .viewsets import (ResourceViewSet, PointVectorLayerViewSet, RasterLayerViewSet, DataTableViewSet, RemoteWMSViewSet,
                       RemoteWFSViewSet)
from base.urls import drf_default_router

urlpatterns = []

drf_default_router.register('resources', ResourceViewSet, basename='resources')
drf_default_router.register('point-vector-layers', PointVectorLayerViewSet, basename='point-vector-layers')
drf_default_router.register('rasterlayers', RasterLayerViewSet, basename='rasterlayers')
drf_default_router.register('datatables', DataTableViewSet, basename='datatables')
drf_default_router.register('remotewms', RemoteWMSViewSet, basename='remotewms')
drf_default_router.register('remotewfs', RemoteWFSViewSet, basename='remotewfs')
