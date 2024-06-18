from .viewsets import (ResourceViewSet, PointVectorLayerViewSet, RasterLayerViewSet, DataTableViewSet, RemoteWMSViewSet,
                       RemoteWFSViewSet)
from base.router import drf_default_router

urlpatterns = []

drf_default_router.register('rest/v1/resources/resources', ResourceViewSet, basename='resources-resources')
drf_default_router.register('rest/v1/resources/point-vector-layers', PointVectorLayerViewSet, basename='resources-point-vector-layers')
drf_default_router.register('rest/v1/resources/linestring-vector-layers', PointVectorLayerViewSet, basename='resources-linestring-vector-layers')
drf_default_router.register('rest/v1/resources/polygon-vector-layers', PointVectorLayerViewSet, basename='resources-polygon-vector-layers')
drf_default_router.register('rest/v1/resources/multipoint-vector-layers', PointVectorLayerViewSet, basename='resources-multipoint-vector-layers')
drf_default_router.register('rest/v1/resources/multilinestring-vector-layers', PointVectorLayerViewSet, basename='resources-multilinestring-vector-layers')
drf_default_router.register('rest/v1/resources/multipolygon-vector-layers', PointVectorLayerViewSet, basename='resources-multipolygon-vector-layers')
drf_default_router.register('rest/v1/resources/rasterlayers', RasterLayerViewSet, basename='resources-rasterlayers')
drf_default_router.register('rest/v1/resources/datatables', DataTableViewSet, basename='resources-datatables')
drf_default_router.register('rest/v1/resources/remotewms', RemoteWMSViewSet, basename='resources-remotewms')
drf_default_router.register('rest/v1/resources/remotewfs', RemoteWFSViewSet, basename='resources-remotewfs')

if drf_default_router.urls not in urlpatterns:
    urlpatterns += drf_default_router.urls