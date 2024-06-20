from django.db import models
from base.mixins import (LockableWorkFlowDraftStateRevisionModelBaseMixin, LockableRevisionOrderableModelBaseMixin,
                         LockableDraftStateRevisionOrderableModelBaseMixin)
from modelcluster.fields import ParentalKey
from wagtail.models import Orderable
from resources.models import (PointVectorLayer, LineStringVectorLayer, PolygonVectorLayer, MultiPointVectorLayer,
                              MultiLineStringVectorLayer, MultiPolygonVectorLayer)
from features.models import Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon
from wagtail.admin.panels import FieldPanel
from wagtail.models import RevisionMixin, LockableMixin, DraftStateMixin, WorkflowMixin, Orderable
from .utils import (uuid_file_path, store_layer_data, validate_point_vector_file, validate_linestring_vector_file,
                    validate_polygon_vector_file, validate_multipoint_vector_file, validate_multilinestring_vector_file,
                    validate_multipolygon_vector_file)
from modelcluster.models import ClusterableModel
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_delete, post_delete, pre_save, post_save
from django.dispatch import receiver
from django.db.models import Q

# Create your models here.


class PointVectorLayerFile(Orderable):
    # uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    file = models.FileField(upload_to=uuid_file_path, validators=[validate_point_vector_file])
    kind = models.CharField(max_length=50, null=True)
    layer = ParentalKey(PointVectorLayer, on_delete=models.CASCADE, related_name="point_files")

    def __str__(self):
        return f"{self.pk} - {self.layer.name}"

    @receiver(post_delete, sender='resource_files.PointVectorLayerFile')
    def delete_orphan_pointfiles_post_delete(sender, instance, **kwargs):
        orphans = Point.objects.filter(file_id=instance.pk)
        print("delete_orphan_pointfiles_post_delete")
        # orphans.delete()

    @receiver(post_save, sender='resource_files.PointVectorLayerFile')
    def store_layer_data_post_save(sender, instance, created, **kwargs):
        if created:
            print("store_layer_data_post_save")
            instance.kind = "point_vector_file"
            store_layer_data(instance, instance.layer, Point)

    class Meta:
        verbose_name = "Point Vector Layer File"
        verbose_name_plural = "Files: Point Vector Layer Files"


class LineStringVectorLayerFile(Orderable):
    # uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    file = models.FileField(upload_to=uuid_file_path, validators=[validate_linestring_vector_file])
    kind = models.CharField(max_length=50, null=True)
    layer = ParentalKey(LineStringVectorLayer, on_delete=models.CASCADE, related_name="linestring_files")

    def __str__(self):
        return f"{self.id} - {self.layer.name}"

    @receiver(post_delete, sender='resource_files.LineStringVectorLayerFile')
    def delete_orphan_pointfiles_post_delete(sender, instance, **kwargs):
        orphans = Point.objects.filter(file_id=instance.uuid)
        print("delete_orphan_pointfiles_post_delete")
        # orphans.delete()

    @receiver(post_save, sender='resource_files.LineStringVectorLayerFile')
    def store_layer_data_post_save(sender, instance, created, **kwargs):
        if created:
            print("store_layer_data_post_save")
            instance.kind = "linestring_vector_file"
            store_layer_data(instance, instance.layer, LineString)

    class Meta:
        verbose_name = "LineString Vector Layer File"
        verbose_name_plural = "Files: LineString Vector Layer Files"


class PolygonVectorLayerFile(Orderable):
    # uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    file = models.FileField(upload_to=uuid_file_path, validators=[validate_polygon_vector_file])
    kind = models.CharField(max_length=50, null=True)
    layer = ParentalKey(PolygonVectorLayer, on_delete=models.CASCADE, related_name="polygon_files")

    def __str__(self):
        return f"{self.id} - {self.layer.name}"

    @receiver(post_delete, sender='resource_files.PolygonVectorLayerFile')
    def delete_orphan_pointfiles_post_delete(sender, instance, **kwargs):
        orphans = Point.objects.filter(file_id=instance.uuid)
        print("delete_orphan_pointfiles_post_delete")
        # orphans.delete()

    @receiver(post_save, sender='resource_files.PolygonVectorLayerFile')
    def store_layer_data_post_save(sender, instance, created, **kwargs):
        if created:
            print("store_layer_data_post_save")
            instance.kind = "polygon_vector_file"
            store_layer_data(instance, instance.layer, Polygon)

    class Meta:
        verbose_name = "Polygon Vector Layer File"
        verbose_name_plural = "Files: Polygon Vector Layer Files"


class MultiPointVectorLayerFile(Orderable):
    # uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    file = models.FileField(upload_to=uuid_file_path, validators=[validate_multipoint_vector_file])
    kind = models.CharField(max_length=50, null=True)
    layer = ParentalKey(MultiPointVectorLayer, on_delete=models.CASCADE, related_name="multipoint_files")

    def __str__(self):
        return f"{self.id} - {self.layer.name}"

    @receiver(post_delete, sender='resource_files.MultiPointVectorLayerFile')
    def delete_orphan_pointfiles_post_delete(sender, instance, **kwargs):
        orphans = Point.objects.filter(file_id=instance.uuid)
        print("delete_orphan_pointfiles_post_delete")
        orphans.delete()

    @receiver(post_save, sender='resource_files.MultiPointVectorLayerFile')
    def store_layer_data_post_save(sender, instance, created, **kwargs):
        if created:
            print("store_layer_data_post_save")
            instance.kind = "multipoint_vector_file"
            store_layer_data(instance, instance.layer, MultiPoint)

    class Meta:
        verbose_name = "MultiPoint Vector Layer File"
        verbose_name_plural = "Files: MultiPoint Vector Layer Files"


class MultiLineStringVectorLayerFile(Orderable):
    # uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    file = models.FileField(upload_to=uuid_file_path, validators=[validate_multilinestring_vector_file])
    kind = models.CharField(max_length=50, null=True)
    layer = ParentalKey(MultiLineStringVectorLayer, on_delete=models.CASCADE, related_name="multilinestring_files")

    def __str__(self):
        return f"{self.id} - {self.layer.name}"

    @receiver(post_delete, sender='resource_files.MultiLineStringVectorLayerFile')
    def delete_orphan_pointfiles_post_delete(sender, instance, **kwargs):
        orphans = Point.objects.filter(file_id=instance.uuid)
        print("delete_orphan_pointfiles_post_delete")
        # orphans.delete()

    @receiver(post_save, sender='resource_files.MultiLineStringVectorLayerFile')
    def store_layer_data_post_save(sender, instance, created, **kwargs):
        if created:
            print("store_layer_data_post_save")
            instance.kind = "multilinestring_vector_file"
            store_layer_data(instance, instance.layer, MultiLineString)

    class Meta:
        verbose_name = "MultiLineString Vector Layer File"
        verbose_name_plural = "Files: MultiLineString Vector Layer Files"


class MultiPolygonVectorLayerFile(Orderable):
    # uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    file = models.FileField(upload_to=uuid_file_path, validators=[validate_multipolygon_vector_file])
    kind = models.CharField(max_length=50, null=True)
    layer = ParentalKey(MultiPolygonVectorLayer, on_delete=models.CASCADE, related_name="multipolygon_files")

    def __str__(self):
        return f"{self.id} - {self.layer.name}"

    @receiver(post_delete, sender='resource_files.MultiPolygonVectorLayerFile')
    def delete_orphan_pointfiles_post_delete(sender, instance, **kwargs):
        orphans = Point.objects.filter(file_id=instance.uuid)
        print("delete_orphan_pointfiles_post_delete")
        # orphans.delete()

    @receiver(post_save, sender='resource_files.MultiPolygonVectorLayerFile')
    def store_layer_data_post_save(sender, instance, created, **kwargs):
        if created:
            print("store_layer_data_post_save")
            instance.kind = "multipolygon_vector_file"
            store_layer_data(instance, instance.layer, MultiPolygon)

    class Meta:
        verbose_name = "MultiPolygon Vector Layer File"
        verbose_name_plural = "Files: MultiPolygon Vector Layer Files"
