from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import (Resource, PointVectorLayer, LineStringVectorLayer, PolygonVectorLayer, MultiPointVectorLayer,
                     MultiLineStringVectorLayer, MultiPolygonVectorLayer, GeometryCollectionVectorLayer,
                     RasterLayer, DataTable, RemoteWMS, RemoteWFS)
from features.serializers import PointGeoFeatureSerializer, LineStringGeoFeatureSerializer, PolygonGeoFeatureSerializer, MultiPointGeoFeatureSerializer, MultiLineStringGeoFeatureSerializer, MultiPolygonGeoFeatureSerializer, GeometryCollectionGeoFeatureSerializer


# Register your models here.


class ResourceSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(format='hex')
    class Meta:
        model = Resource
        fields = '__all__'


class PointVectorLayerSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(format='hex')
    points = PointGeoFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = PointVectorLayer
        fields = '__all__'


class LineStringVectorLayerSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(format='hex')
    lines = LineStringGeoFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = LineStringVectorLayer
        fields = '__all__'


class PolygonVectorLayerSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(uuid_format='hex')
    polygons = PolygonGeoFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = PolygonVectorLayer
        fields = '__all__'


class MultiPointVectorLayerSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(format='hex')
    multipoints = MultiPointGeoFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = MultiPointVectorLayer
        fields = '__all__'


class MultiLineStringVectorLayerSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(format='hex')
    multilines = MultiLineStringGeoFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = MultiLineStringVectorLayer
        fields = '__all__'


class MultiPolygonVectorLayerSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(format='hex')
    multipolygons = MultiPolygonGeoFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = MultiPolygonVectorLayer
        fields = '__all__'


class GeometryCollectionVectorLayerSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(format='hex')
    geometrycollections = GeometryCollectionGeoFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = GeometryCollectionVectorLayer
        fields = '__all__'


class RasterLayerSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(format='hex')
    class Meta:
        model = RasterLayer
        fields = '__all__'


class DataTableSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(format='hex')
    class Meta:
        model = DataTable
        fields = '__all__'


class RemoteWMSSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(format='hex')
    class Meta:
        model = RemoteWMS
        fields = '__all__'


class RemoteWFSSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(format='hex')
    class Meta:
        model = RemoteWFS
        fields = '__all__'


# GeoFeatureModelSerializer
