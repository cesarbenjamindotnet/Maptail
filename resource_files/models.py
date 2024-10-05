from django.contrib.gis.db import models
from modelcluster.fields import ForeignKey
from wagtail.models import Orderable
from resources.models import (PointVectorLayer, LineStringVectorLayer, PolygonVectorLayer, MultiPointVectorLayer,
                              MultiLineStringVectorLayer, MultiPolygonVectorLayer)
from features.models import Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon
from wagtail.admin.panels import FieldPanel
from wagtail.models import RevisionMixin, LockableMixin, DraftStateMixin, WorkflowMixin, ClusterableModel
from .utils import (uuid_file_path, store_layer_data, validate_point_vector_file, validate_linestring_vector_file,
                    validate_polygon_vector_file, validate_multipoint_vector_file, validate_multilinestring_vector_file,
                    validate_multipolygon_vector_file)
from modelcluster.models import ClusterableModel
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_delete, post_delete, pre_save, post_save
from django.dispatch import receiver
from wagtail.documents.models import AbstractDocument
from modelcluster.fields import ParentalKey
from django.utils.translation import gettext_lazy as _


# Create your models here.


class PointVectorLayerFile(AbstractDocument, Orderable):
    file = models.FileField(upload_to=uuid_file_path, validators=[validate_point_vector_file])
    layer = ParentalKey(PointVectorLayer, on_delete=models.CASCADE, related_name="files")

    def __str__(self):
        # return f"{self.pk}: {self.title} ({self.layer.__class__.__name__}: {self.layer.name})"
        return f"{self.pk}: {self.title} ({self.layer.pk}: {self.layer.name})"

    @receiver(post_delete, sender='resource_files.PointVectorLayerFile')
    def delete_orphans_post_delete(sender, instance, **kwargs):
        print("delete_orphans_post_delete instance", instance)
        print("delete_orphans_post_delete instance.pk", instance.pk)
        orphans = Point.objects.filter(source_file=instance)
        print("orphans", orphans)
        print("delete_orphans_post_delete")
        orphans.delete()

    @receiver(post_save, sender='resource_files.PointVectorLayerFile')
    def store_layer_data_post_save(sender, instance, created, **kwargs):
        if created:
            print("store_layer_data_post_save")
            store_layer_data(instance, instance.layer, Point)

    class Meta(AbstractDocument.Meta):
        permissions = [
            ("choose_document", "Can choose document"),
        ]
        verbose_name = "Point Vector Layer File"
        verbose_name_plural = "Point Vector Layer Files"


class LineStringVectorLayerFile(AbstractDocument, ClusterableModel):
    file = models.FileField(upload_to=uuid_file_path, validators=[validate_linestring_vector_file])
    layer = ForeignKey(LineStringVectorLayer, on_delete=models.CASCADE, related_name="files")

    def __str__(self):
        return f"{self.pk} - {self.layer.name}"

    @receiver(post_delete, sender='resource_files.LineStringVectorLayerFile')
    def delete_orphans_post_delete(sender, instance, **kwargs):
        orphans = LineString.objects.filter(file__id=instance.pk)
        orphans.delete()

    @receiver(post_save, sender='resource_files.LineStringVectorLayerFile')
    def store_layer_data_post_save(sender, instance, created, **kwargs):
        if created:
            store_layer_data(instance, instance.layer, LineString)

    class Meta(AbstractDocument.Meta):
        permissions = [
            ("choose_document", "Can choose document"),
        ]
        verbose_name = "LineString Vector Layer File"
        verbose_name_plural = "Files: LineString Vector Layer Files"


class PolygonVectorLayerFile(AbstractDocument, ClusterableModel):
    file = models.FileField(upload_to=uuid_file_path, validators=[validate_polygon_vector_file])
    layer = ForeignKey(PolygonVectorLayer, on_delete=models.CASCADE, related_name="files")

    def __str__(self):
        return f"{self.pk} - {self.layer.name}"

    @receiver(post_delete, sender='resource_files.PolygonVectorLayerFile')
    def delete_orphans_post_delete(sender, instance, **kwargs):
        orphans = Polygon.objects.filter(file__id=instance.pk)
        orphans.delete()

    @receiver(post_save, sender='resource_files.PolygonVectorLayerFile')
    def store_layer_data_post_save(sender, instance, created, **kwargs):
        if created:
            store_layer_data(instance, instance.layer, Polygon)

    class Meta:
        verbose_name = "Polygon Vector Layer File"
        verbose_name_plural = "Files: Polygon Vector Layer Files"


class MultiPointVectorLayerFile(AbstractDocument, ClusterableModel):
    file = models.FileField(upload_to=uuid_file_path, validators=[validate_multipoint_vector_file])
    layer = ForeignKey(MultiPointVectorLayer, on_delete=models.CASCADE, related_name="files")

    def __str__(self):
        return f"{self.pk} - {self.layer.name}"

    @receiver(post_delete, sender='resource_files.MultiPointVectorLayerFile')
    def delete_orphans_post_delete(sender, instance, **kwargs):
        orphans = MultiPoint.objects.filter(file__id=instance.pk)
        orphans.delete()

    @receiver(post_save, sender='resource_files.MultiPointVectorLayerFile')
    def store_layer_data_post_save(sender, instance, created, **kwargs):
        if created:
            store_layer_data(instance, instance.layer, MultiPoint)

    class Meta(AbstractDocument.Meta):
        permissions = [
            ("choose_document", "Can choose document"),
        ]
        verbose_name = "MultiPoint Vector Layer File"
        verbose_name_plural = "Files: MultiPoint Vector Layer Files"


class MultiLineStringVectorLayerFile(AbstractDocument, ClusterableModel):
    file = models.FileField(upload_to=uuid_file_path, validators=[validate_multilinestring_vector_file])
    layer = ForeignKey(MultiLineStringVectorLayer, on_delete=models.CASCADE, related_name="files")

    def __str__(self):
        return f"{self.pk} - {self.layer.name}"

    @receiver(post_delete, sender='resource_files.MultiLineStringVectorLayerFile')
    def delete_orphans_post_delete(sender, instance, **kwargs):
        orphans = MultiLineString.objects.filter(file__id=instance.pk)
        orphans.delete()

    @receiver(post_save, sender='resource_files.MultiLineStringVectorLayerFile')
    def store_layer_data_post_save(sender, instance, created, **kwargs):
        if created:
            store_layer_data(instance, instance.layer, MultiLineString)

    class Meta(AbstractDocument.Meta):
        permissions = [
            ("choose_document", "Can choose document"),
        ]
        verbose_name = "MultiLineString Vector Layer File"
        verbose_name_plural = "Files: MultiLineString Vector Layer Files"


class MultiPolygonVectorLayerFile(AbstractDocument, ClusterableModel):
    file = models.FileField(upload_to=uuid_file_path, validators=[validate_multipolygon_vector_file])
    layer = ForeignKey(MultiPolygonVectorLayer, on_delete=models.CASCADE, related_name="files")

    def __str__(self):
        return f"{self.pk} - {self.layer.name}"

    @receiver(post_delete, sender='resource_files.MultiPolygonVectorLayerFile')
    def delete_orphans_post_delete(sender, instance, **kwargs):
        orphans = MultiPolygon.objects.filter(file__id=instance.pk)
        orphans.delete()

    @receiver(post_save, sender='resource_files.MultiPolygonVectorLayerFile')
    def store_layer_data_post_save(sender, instance, created, **kwargs):
        if created:
            store_layer_data(instance, instance.layer, MultiPolygon)

    class Meta(AbstractDocument.Meta):
        permissions = [
            ("choose_document", "Can choose document"),
        ]
        verbose_name = "MultiPolygon Vector Layer File"
        verbose_name_plural = "Files: MultiPolygon Vector Layer Files"
