from django.conf import settings
from django.contrib.gis.db import models
from django.db.models import ForeignKey

from base.mixins import LockableWorkFlowDraftStateRevisionModelBaseMixin
from wagtail.models import RevisionMixin, LockableMixin, DraftStateMixin, Orderable
from modelcluster.fields import ParentalKey
from resources.models import (VectorLayer, PointVectorLayer, LineStringVectorLayer, PolygonVectorLayer,
                              MultiPointVectorLayer, MultiLineStringVectorLayer, MultiPolygonVectorLayer,
                              GeometryCollectionVectorLayer, RasterLayer, DataTable, RemoteWMS, RemoteWFS)
from django.core.exceptions import ValidationError

# Create your models here.


class Point(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    data = models.JSONField(null=True, blank=True)
    geom = models.PointField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(PointVectorLayer, on_delete=models.CASCADE, related_name="points")
    source_file = ForeignKey("resource_files.ResourcePointsFile", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.layer.name}: {self.id}"

    class Meta:
        verbose_name = "Point"
        verbose_name_plural = "Points"
        ordering = ["-id"]

"""
class LineString(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    data = models.JSONField(null=True, blank=True)
    geom = models.LineStringField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(LineStringVectorLayer, on_delete=models.CASCADE, related_name="lines")
    source_file = ParentalKey("resource_files.LineStringVectorLayerFile", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.layer.name}: {self.id}"


class Polygon(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    data = models.JSONField(null=True, blank=True)
    geom = models.PolygonField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(PolygonVectorLayer, on_delete=models.CASCADE, related_name="polygons")
    source_file = ParentalKey("resource_files.PolygonVectorLayerFile", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.layer.name}: {self.id}"


class MultiPoint(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    data = models.JSONField(null=True, blank=True)
    geom = models.MultiPointField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(MultiPointVectorLayer, on_delete=models.CASCADE, related_name="multipoints")
    source_file = ParentalKey("resource_files.MultiPointVectorLayerFile", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.layer.name}: {self.id}"


class MultiLineString(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    data = models.JSONField(null=True, blank=True)
    geom = models.MultiLineStringField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(MultiLineStringVectorLayer, on_delete=models.CASCADE, related_name="multilines")
    source_file = ParentalKey("resource_files.MultiLineStringVectorLayerFile", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.layer.name}: {self.id}"


class MultiPolygon(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    data = models.JSONField(null=True, blank=True)
    geom = models.MultiPolygonField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(MultiPolygonVectorLayer, on_delete=models.CASCADE, related_name="multipolygons")
    source_file = ParentalKey("resource_files.MultiPolygonVectorLayerFile", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.layer.name}: {self.id}"


class GeometryCollection(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    data = models.JSONField(null=True, blank=True)
    geom = models.GeometryCollectionField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(GeometryCollectionVectorLayer, on_delete=models.CASCADE, related_name="geometrycollections")

    def __str__(self):
        return f"{self.layer.name}: {self.id}"
"""
