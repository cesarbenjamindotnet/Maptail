from rest_framework import serializers
from .models import (Resource, VectorLayerMixin, RasterLayer, DataTable, RemoteWMS, RemoteWFS)

# Register your models here.


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'


class VectorLayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VectorLayerMixin
        fields = '__all__'


class RasterLayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RasterLayer
        fields = '__all__'


class DataTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTable
        fields = '__all__'


class RemoteWMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemoteWMS
        fields = '__all__'


class RemoteWFSSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemoteWFS
        fields = '__all__'

