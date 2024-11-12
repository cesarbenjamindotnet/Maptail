from django.conf import settings
from django.contrib.gis.db import models
from django.db.models import ForeignKey

from base.mixins import LockableWorkFlowDraftStateRevisionModelBaseMixin
from wagtail.models import RevisionMixin, LockableMixin, DraftStateMixin, Orderable
from modelcluster.fields import ParentalKey
from resources.models import (VectorLayer, PointVectorLayer, LineStringVectorLayer, PolygonVectorLayer,
                              MultiPointVectorLayer, MultiLineStringVectorLayer, MultiPolygonVectorLayer,
                              GeometryCollectionVectorLayer, RasterLayer, DataTable, RemoteWMS, RemoteWFS)
from polymorphic.models import PolymorphicModel

# Create your models here.


class Feature(PolymorphicModel, LockableWorkFlowDraftStateRevisionModelBaseMixin):
    data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"


class Point(Feature):
    geom = models.PointField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(PointVectorLayer, on_delete=models.CASCADE, related_name="features")
    source_file = ParentalKey("resource_files.ResourcePointsFile", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.layer.name}: {self.id}"

    class Meta:
        verbose_name = "Point"
        verbose_name_plural = "Points"


class LineString(Feature):
    geom = models.LineStringField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(LineStringVectorLayer, on_delete=models.CASCADE, related_name="features")
    source_file = ParentalKey("resource_files.ResourceLineStringsFile", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.layer.name}: {self.id}"


class Polygon(Feature):
    geom = models.PolygonField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(PolygonVectorLayer, on_delete=models.CASCADE, related_name="features")
    source_file = ParentalKey("resource_files.ResourcePolygonsFile", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.layer.name}: {self.id}"


class MultiPoint(Feature):
    geom = models.MultiPointField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(MultiPointVectorLayer, on_delete=models.CASCADE, related_name="features")
    source_file = ParentalKey("resource_files.ResourceMultiPointsFile", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.layer.name}: {self.id}"


class MultiLineString(Feature):
    geom = models.MultiLineStringField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(MultiLineStringVectorLayer, on_delete=models.CASCADE, related_name="features")
    source_file = ParentalKey("resource_files.ResourceMultiLineStringsFile", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.layer.name}: {self.id}"


class MultiPolygon(Feature):
    geom = models.MultiPolygonField(srid=settings.DATA_FEATURES_SRID)
    layer = ParentalKey(MultiPolygonVectorLayer, on_delete=models.CASCADE, related_name="features")
    source_file = ParentalKey("resource_files.ResourceMultiPolygonsFile", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.layer.name}: {self.id}"
