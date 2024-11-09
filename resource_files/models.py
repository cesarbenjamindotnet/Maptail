from django.contrib.gis.db import models
from modelcluster.fields import ForeignKey
from wagtail.models import Orderable
from resources.models import (PointVectorLayer, LineStringVectorLayer, PolygonVectorLayer, MultiPointVectorLayer,
                              MultiLineStringVectorLayer, MultiPolygonVectorLayer)
from features.models import Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon
from wagtail.models import RevisionMixin, LockableMixin, DraftStateMixin, ClusterableModel
from .utils import (uuid_file_path, store_layer_data, validate_point_vector_file, validate_linestring_vector_file,
                    validate_polygon_vector_file, validate_multipoint_vector_file, validate_multilinestring_vector_file,
                    validate_multipolygon_vector_file)
from modelcluster.models import ClusterableModel
from django.db.models.signals import pre_delete, post_delete, pre_save, post_save
from django.dispatch import receiver
from wagtail.documents.models import AbstractDocument, Document
from modelcluster.fields import ParentalKey
from django.utils.translation import gettext_lazy as _


# Create your models here.


class ResourcePointsFile(AbstractDocument, ClusterableModel):
    file = models.FileField(upload_to=uuid_file_path, validators=[validate_point_vector_file])
    layer = ParentalKey(PointVectorLayer, on_delete=models.CASCADE, related_name="files")

    # admin_form_fields = ("title", "file", "collection", "layer")

    def __str__(self):
        return f"{self.title}: {self.file.name} ({self.layer.name})"

    @receiver(post_delete, sender='resource_files.ResourcePointsFile')
    def delete_orphans_post_delete(sender, instance, **kwargs):
        print("delete_orphans_post_delete instance", instance)
        orphans = Point.objects.filter(source_file=instance)
        orphans.delete()

    @receiver(post_save, sender='resource_files.ResourcePointsFile')
    def store_layer_data_post_save(sender, instance, created, **kwargs):
        if created:
            print("store_layer_data_post_save")
            store_layer_data(instance, instance.layer, Point)

    class Meta(AbstractDocument.Meta):
        verbose_name = "Point Vector Layer File"
        verbose_name_plural = "Point Vector Layer Files"
        permissions = [
            ("choose_document", "Can choose document"),
        ]


class ResourceLineStringsFile(AbstractDocument, ClusterableModel):
    file = models.FileField(upload_to=uuid_file_path, validators=[validate_linestring_vector_file])
    layer = ForeignKey(LineStringVectorLayer, on_delete=models.CASCADE, related_name="files")

    def __str__(self):
        return f"{self.title}: {self.file.name} ({self.layer.name})"

    @receiver(post_delete, sender='resource_files.ResourceLineStringsFile')
    def delete_orphans_post_delete(sender, instance, **kwargs):
        orphans = LineString.objects.filter(file__id=instance.pk)
        orphans.delete()

    @receiver(post_save, sender='resource_files.ResourceLineStringsFile')
    def store_layer_data_post_save(sender, instance, created, **kwargs):
        if created:
            store_layer_data(instance, instance.layer, LineString)

    class Meta(AbstractDocument.Meta):
        permissions = [
            ("choose_document", "Can choose document"),
        ]
        verbose_name = "LineString Vector Layer File"
        verbose_name_plural = "Files: LineString Vector Layer Files"


class ResourcePolygonsFile(AbstractDocument, ClusterableModel):
    file = models.FileField(upload_to=uuid_file_path, validators=[validate_polygon_vector_file])
    layer = ForeignKey(PolygonVectorLayer, on_delete=models.CASCADE, related_name="files")

    def __str__(self):
        return f"{self.title}: {self.file.name} ({self.layer.name})"

    @receiver(post_delete, sender='resource_files.ResourcePolygonsFile')
    def delete_orphans_post_delete(sender, instance, **kwargs):
        orphans = Polygon.objects.filter(file__id=instance.pk)
        orphans.delete()

    @receiver(post_save, sender='resource_files.ResourcePolygonsFile')
    def store_layer_data_post_save(sender, instance, created, **kwargs):
        if created:
            store_layer_data(instance, instance.layer, Polygon)

    class Meta:
        verbose_name = "Polygon Vector Layer File"
        verbose_name_plural = "Files: Polygon Vector Layer Files"


class ResourceMultiPointsFile(AbstractDocument, ClusterableModel):
    file = models.FileField(upload_to=uuid_file_path, validators=[validate_multipoint_vector_file])
    layer = ForeignKey(MultiPointVectorLayer, on_delete=models.CASCADE, related_name="files")

    def __str__(self):
        return f"{self.title}: {self.file.name} ({self.layer.name})"

    @receiver(post_delete, sender='resource_files.ResourceMultiPointsFile')
    def delete_orphans_post_delete(sender, instance, **kwargs):
        orphans = MultiPoint.objects.filter(file__id=instance.pk)
        orphans.delete()

    @receiver(post_save, sender='resource_files.ResourceMultiPointsFile')
    def store_layer_data_post_save(sender, instance, created, **kwargs):
        if created:
            store_layer_data(instance, instance.layer, MultiPoint)

    class Meta(AbstractDocument.Meta):
        permissions = [
            ("choose_document", "Can choose document"),
        ]
        verbose_name = "MultiPoint Vector Layer File"
        verbose_name_plural = "Files: MultiPoint Vector Layer Files"


class ResourceMultiLineStringsFile(AbstractDocument, ClusterableModel):
    file = models.FileField(upload_to=uuid_file_path, validators=[validate_multilinestring_vector_file])
    layer = ForeignKey(MultiLineStringVectorLayer, on_delete=models.CASCADE, related_name="files")

    def __str__(self):
        return f"{self.title}: {self.file.name} ({self.layer.name})"

    @receiver(post_delete, sender='resource_files.ResourceMultiLineStringsFile')
    def delete_orphans_post_delete(sender, instance, **kwargs):
        orphans = MultiLineString.objects.filter(file__id=instance.pk)
        orphans.delete()

    @receiver(post_save, sender='resource_files.ResourceMultiLineStringsFile')
    def store_layer_data_post_save(sender, instance, created, **kwargs):
        if created:
            store_layer_data(instance, instance.layer, MultiLineString)

    class Meta(AbstractDocument.Meta):
        permissions = [
            ("choose_document", "Can choose document"),
        ]
        verbose_name = "MultiLineString Vector Layer File"
        verbose_name_plural = "Files: MultiLineString Vector Layer Files"


class ResourceMultiPolygonsFile(AbstractDocument, ClusterableModel):
    file = models.FileField(upload_to=uuid_file_path, validators=[validate_multipolygon_vector_file])
    layer = ForeignKey(MultiPolygonVectorLayer, on_delete=models.CASCADE, related_name="files")

    def __str__(self):
        return f"{self.title}: {self.file.name} ({self.layer.name})"

    @receiver(post_delete, sender='resource_files.ResourceMultiPolygonsFile')
    def delete_orphans_post_delete(sender, instance, **kwargs):
        orphans = MultiPolygon.objects.filter(file__id=instance.pk)
        orphans.delete()

    @receiver(post_save, sender='resource_files.ResourceMultiPolygonsFile')
    def store_layer_data_post_save(sender, instance, created, **kwargs):
        if created:
            store_layer_data(instance, instance.layer, MultiPolygon)

    class Meta(AbstractDocument.Meta):
        permissions = [
            ("choose_document", "Can choose document"),
        ]
        verbose_name = "MultiPolygon Vector Layer File"
        verbose_name_plural = "Files: MultiPolygon Vector Layer Files"
