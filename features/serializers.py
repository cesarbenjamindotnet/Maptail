from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Point
# from .models import Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, GeometryCollection

# Register your serializers here.


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = '__all__'


class PointGeoFeatureSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Point
        geo_field = 'geom'
        fields = '__all__'


"""
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


# GeoFeatureModelSerializer


class PointGeoFeatureSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Point
        geo_field = 'geom'
        fields = '__all__'


class LineStringGeoFeatureSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LineString
        geo_field = 'geom'
        fields = '__all__'


class PolygonGeoFeatureSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Polygon
        geo_field = 'geom'
        fields = '__all__'


class MultiPointGeoFeatureSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MultiPoint
        geo_field = 'geom'
        fields = '__all__'


class MultiLineStringGeoFeatureSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MultiLineString
        geo_field = 'geom'
        fields = '__all__'


class MultiPolygonGeoFeatureSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MultiPolygon
        geo_field = 'geom'
        fields = '__all__'


class GeometryCollectionGeoFeatureSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = GeometryCollection
        geo_field = 'geom'
        fields = '__all__'
"""
