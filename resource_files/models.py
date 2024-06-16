from django.db import models
from base.mixins import LockableWorkFlowDraftStateRevisionModelBaseMixin, LockableRevisionOrderableModelBaseMixin
from modelcluster.fields import ParentalKey
from wagtail.models import Orderable
import uuid
from resources.models import PointVectorLayer
from wagtail.admin.panels import FieldPanel
from wagtail.models import RevisionMixin, LockableMixin, DraftStateMixin, WorkflowMixin, Orderable

# Create your models here.


class ResourceBaseFileMixin(Orderable):
    """
    A Vector layer file
    """

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to='resources/files/')
    kind = models.CharField(max_length=255, null=True)

    class Meta:
        abstract = True


class PointVectorLayerFile(ResourceBaseFileMixin):
    """
    A point dataset.
    """

    layer = ParentalKey(PointVectorLayer, on_delete=models.CASCADE, related_name="files")

    def __str__(self):
        return f"{self.uuid} - {self.layer.name}"

    def save(self, *args, **kwargs):
        if not self.kind or not self.pk:
            self.kind = "point_vector_file"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Point Vector Layer File"
        verbose_name_plural = "Resource Files: Point Vector Layer Files"
