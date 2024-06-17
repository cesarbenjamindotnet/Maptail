from django.db import models
from base.mixins import (LockableWorkFlowDraftStateRevisionModelBaseMixin, LockableRevisionOrderableModelBaseMixin,
                         LockableDraftStateRevisionOrderableModelBaseMixin)
from modelcluster.fields import ParentalKey
from wagtail.models import Orderable
import uuid
from resources.models import PointVectorLayer
from features.models import Point
from wagtail.admin.panels import FieldPanel
from wagtail.models import RevisionMixin, LockableMixin, DraftStateMixin, WorkflowMixin, Orderable
from .utils import validate_point_vector_file, uuid_file_path, store_layer_data
from modelcluster.models import ClusterableModel
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_delete, post_delete, pre_save, post_save
from django.dispatch import receiver
from django.db.models import Q

# Create your models here.


class PointVectorLayerFile(Orderable):
    """
    A point dataset.
    """

    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    file = models.FileField(upload_to=uuid_file_path, validators=[validate_point_vector_file])
    kind = models.CharField(max_length=255, null=True)
    layer = ParentalKey(PointVectorLayer, on_delete=models.CASCADE, related_name="files")

    def __str__(self):
        return f"{self.uuid} - {self.layer.name}"


    @receiver(post_delete, sender='resource_files.PointVectorLayerFile')
    def delete_orphan_pointfiles_post_delete(sender, instance, **kwargs):
        orphans = Point.objects.filter(file_uuid=instance.uuid)
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
        verbose_name_plural = "Resource Files: Point Vector Layer Files"
