from .viewsets import (PointViewSet, LineStringViewSet, PolygonViewSet, MultiPointViewSet, MultiLineStringViewSet,
                       MultiPolygonViewSet, GeometryCollectionViewSet)
from base.urls import drf_default_router

urlpatterns = []

drf_default_router.register('rest/v1/features/points', PointViewSet, basename='points')
drf_default_router.register('rest/v1/features/linestrings', LineStringViewSet, basename='linestrings')
drf_default_router.register('rest/v1/features/polygons', PolygonViewSet, basename='polygons')
drf_default_router.register('rest/v1/features/multipoints', MultiPointViewSet, basename='multipoints')
drf_default_router.register('rest/v1/features/multilinestrings', MultiLineStringViewSet, basename='multilinestrings')
drf_default_router.register('rest/v1/features/multipolygons', MultiPolygonViewSet, basename='multipolygons')
drf_default_router.register('rest/v1/features/geometrycollections', GeometryCollectionViewSet, basename='geometrycollections')
