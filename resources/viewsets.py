from rest_framework import viewsets
from .models import (Resource, VectorLayerMixin, PointVectorLayer, RasterLayer, DataTable, RemoteWMS, RemoteWFS)
from .serializers import (ResourceSerializer, VectorLayerSerializer, RasterLayerSerializer, DataTableSerializer,
                          RemoteWMSSerializer, RemoteWFSSerializer)

# Register your models here.


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class PointVectorLayerViewSet(viewsets.ModelViewSet):
    queryset = PointVectorLayer.objects.all()
    serializer_class = VectorLayerSerializer


class RasterLayerViewSet(viewsets.ModelViewSet):
    queryset = RasterLayer.objects.all()
    serializer_class = RasterLayerSerializer


class DataTableViewSet(viewsets.ModelViewSet):
    queryset = DataTable.objects.all()
    serializer_class = DataTableSerializer


class RemoteWMSViewSet(viewsets.ModelViewSet):
    queryset = RemoteWMS.objects.all()
    serializer_class = RemoteWMSSerializer


class RemoteWFSViewSet(viewsets.ModelViewSet):
    queryset = RemoteWFS.objects.all()
    serializer_class = RemoteWFSSerializer
