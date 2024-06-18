from rest_framework import viewsets
from .models import Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, GeometryCollection
from .serializers import (PointSerializer, LineStringSerializer, PolygonSerializer, MultiPointSerializer,
                           MultiLineStringSerializer, MultiPolygonSerializer, GeometryCollectionSerializer)

# Register your viewsets here.


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer


class LineStringViewSet(viewsets.ModelViewSet):
    queryset = LineString.objects.all()
    serializer_class = LineStringSerializer


class PolygonViewSet(viewsets.ModelViewSet):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer


class MultiPointViewSet(viewsets.ModelViewSet):
    queryset = MultiPoint.objects.all()
    serializer_class = MultiPointSerializer


class MultiLineStringViewSet(viewsets.ModelViewSet):
    queryset = MultiLineString.objects.all()
    serializer_class = MultiLineStringSerializer


class MultiPolygonViewSet(viewsets.ModelViewSet):
    queryset = MultiPolygon.objects.all()
    serializer_class = MultiPolygonSerializer


class GeometryCollectionViewSet(viewsets.ModelViewSet):
    queryset = GeometryCollection.objects.all()
    serializer_class = GeometryCollectionSerializer
