from django.conf import settings
from django.contrib.gis.db import models
from base.mixins import LockableWorkFlowDraftStateRevisionModelBaseMixin
from modelcluster.fields import ParentalKey
from resources.models import (VectorLayerMixin, PointVectorLayer, LineStringVectorLayer, PolygonVectorLayer,
                              MultiPointVectorLayer, MultiLineStringVectorLayer, MultiPolygonVectorLayer,
                              GeometryCollectionVectorLayer, RasterLayer, DataTable, RemoteWMS, RemoteWFS)

# Create your models here.


class Point(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    data = models.JSONField(null=True, blank=True)
    geom = models.PointField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(PointVectorLayer, on_delete=models.CASCADE, related_name="points")

    def __str__(self):
        return f"{self.layer.name}: {self.id}"


class LineString(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    data = models.JSONField(null=True, blank=True)
    geom = models.LineStringField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(LineStringVectorLayer, on_delete=models.CASCADE, related_name="lines")

    def __str__(self):
        return f"{self.layer.name}: {self.id}"


class Polygon(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    data = models.JSONField(null=True, blank=True)
    geom = models.PolygonField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(PolygonVectorLayer, on_delete=models.CASCADE, related_name="polygons")

    def __str__(self):
        return f"{self.layer.name}: {self.id}"


class MultiPoint(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    data = models.JSONField(null=True, blank=True)
    geom = models.MultiPointField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(MultiPointVectorLayer, on_delete=models.CASCADE, related_name="multi_points")

    def __str__(self):
        return f"{self.layer.name}: {self.id}"


class MultiLineString(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    data = models.JSONField(null=True, blank=True)
    geom = models.MultiLineStringField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(MultiLineStringVectorLayer, on_delete=models.CASCADE, related_name="multilines")

    def __str__(self):
        return f"{self.layer.name}: {self.id}"


class MultiPolygon(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    data = models.JSONField(null=True, blank=True)
    geom = models.MultiPolygonField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(MultiPolygonVectorLayer, on_delete=models.CASCADE, related_name="multipolygons")

    def __str__(self):
        return f"{self.layer.name}: {self.id}"


class GeometryCollection(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    data = models.JSONField(null=True, blank=True)
    geom = models.GeometryCollectionField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(GeometryCollectionVectorLayer, on_delete=models.CASCADE, related_name="geometrycollections")

    def __str__(self):
        return f"{self.layer.name}: {self.id}"
