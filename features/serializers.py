from rest_framework import serializers
from .models import Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, GeometryCollection

# Register your serializers here.


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = '__all__'


class LineStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineString
        fields = '__all__'


class PolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polygon
        fields = '__all__'


class MultiPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiPoint
        fields = '__all__'


class MultiLineStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiLineString
        fields = '__all__'


class MultiPolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiPolygon
        fields = '__all__'


class GeometryCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeometryCollection
        fields = '__all__'
