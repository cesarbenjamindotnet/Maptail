from django.db import models
from base.mixins import (LockableWorkFlowDraftStateRevisionModelBaseMixin, LockableRevisionOrderableModelBaseMixin,
                         LockableDraftStateRevisionOrderableModelBaseAbstract)
from modelcluster.fields import ParentalKey
from wagtail.models import Orderable
import uuid
from resources.models import PointVectorLayer
from features.models import Point
from wagtail.admin.panels import FieldPanel
from wagtail.models import RevisionMixin, LockableMixin, DraftStateMixin, WorkflowMixin, Orderable
from .utils import validate_point_vector_file, uuid_file_path, store_layer_data

# Create your models here.


class ResourceBaseFileMixin(Orderable):
    """
    A Vector layer file
    """



    class Meta:
        abstract = True


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

    def save(self, *args, **kwargs):
        # TODO: leer el archivo y guardar los features en la capa
        if not self.kind or not self.pk:
            self.kind = "point_vector_file"
            print("saving file")
            print("self.file", self.file)
            print("self.file.path", self.file.path)
            print("self.file.name", self.file.name)
            print("self.layer", self.layer)
            store_layer_data(self.file.path, self.layer, Point)

        super().save(*args, **kwargs)

    # TODO: implementar delete para eliminar los features de la capa que se relacionan con este archivo

    class Meta:
        verbose_name = "Point Vector Layer File"
        verbose_name_plural = "Resource Files: Point Vector Layer Files"
