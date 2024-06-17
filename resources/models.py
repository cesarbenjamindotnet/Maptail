from django.contrib.gis.db import models
import uuid
from base.mixins import LockableWorkFlowDraftStateRevisionModelBaseMixin
from base.fields import GeoKnotTextField
from polymorphic.models import PolymorphicModel
from .managers import ResourceBaseManager
from metadata.models import ResourceMetadataMixin
from resource_attrs.models import ResourceCategory
from autoslug import AutoSlugField
from base import enumerations
from modelcluster.models import ClusterableModel
from django.core.exceptions import ValidationError
from modelcluster.fields import ParentalKey

# Create your models here.


def is_resourcecategory_live(pk):
    if not ResourceCategory.objects.filter(pk=pk, live=True).exists():
        raise ValidationError('The resource category must be live.')


class ResourceBase(LockableWorkFlowDraftStateRevisionModelBaseMixin, ResourceMetadataMixin):
    """
    Base model for all resources.
    """

    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='name', always_update=True, unique=True, editable=False)
    description = GeoKnotTextField(null=True, blank=True)
    category = models.ForeignKey(ResourceCategory, on_delete=models.PROTECT, validators=[is_resourcecategory_live])
    is_featured = models.BooleanField(default=False)
    is_advertised = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to='resources/thumbnails/', null=True, blank=True)
    popular_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    # rating = models.IntegerField(default=0, null=True, blank=True)
    # state = models.CharField(max_length=255, choices=enumerations.PROCESSING_STATES, default='running', editable=False)

    objects = ResourceBaseManager()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class ResourceBaseRemoteServiceMixin(models.Model):
    """
    Mixin for resources that have a remote URL.
    """

    service_type = models.CharField(max_length=255, choices=enumerations.REMOTE_SERVICE_TYPES, default='wms')
    service_url = models.URLField()

    class Meta:
        abstract = True


class Resource(PolymorphicModel, ResourceBase):
    """
    A resource.
    """

    class Meta:
        verbose_name = "Resource"
        verbose_name_plural = "Resources"


class VectorLayerMixin(ClusterableModel, Resource):
    """
    A dataset.
    """

    class Meta:
        abstract = True
        verbose_name = "Vector Layer"
        verbose_name_plural = "Vector Layers"


class PointVectorLayer(VectorLayerMixin):
    """
    A point dataset.
    """

    class Meta:
        verbose_name = "Point Vector Layer"
        verbose_name_plural = "Resources: Point Vector Layers"


class LineStringVectorLayer(VectorLayerMixin):
    """
    A line dataset.
    """

    class Meta:
        verbose_name = "LineString Vector Layer"
        verbose_name_plural = "LineString Vector Layers"


class PolygonVectorLayer(VectorLayerMixin):
    """
    A polygon dataset.
    """

    class Meta:
        verbose_name = "Polygon Vector Layer"
        verbose_name_plural = "Polygon Vector Layers"


class MultiPointVectorLayer(VectorLayerMixin):
    """
    A multipoint dataset.
    """

    class Meta:
        verbose_name = "MultiPoint Vector Layer"
        verbose_name_plural = "MultiPoint Vector Layers"


class MultiLineStringVectorLayer(VectorLayerMixin):
    """
    A multilinestring dataset.
    """

    class Meta:
        verbose_name = "MultiLineString Vector Layer"
        verbose_name_plural = "MultiLineString Vector Layers"


class MultiPolygonVectorLayer(VectorLayerMixin):
    """
    A multipolygon dataset.
    """

    class Meta:
        verbose_name = "MultiPolygon Vector Layer"
        verbose_name_plural = "MultiPolygon Vector Layers"


class GeometryCollectionVectorLayer(VectorLayerMixin):
    """
    A geometry collection dataset.
    """

    class Meta:
        verbose_name = "GeometryCollection Vector Layer"
        verbose_name_plural = "GeometryCollection Vector Layers"


class RasterLayer(Resource):
    """
    A dataset.
    """

    class Meta:
        verbose_name = "Raster Layer"
        verbose_name_plural = "Raster Layers"


class DataTable(Resource):
    """
    A table.
    """

    class Meta:
        verbose_name = "Data Table"
        verbose_name_plural = "Data Tables"


class RemoteWMS(Resource, ResourceBaseRemoteServiceMixin):
    """
    A WMS service.
    """

    class Meta:
        verbose_name = "WMS Service"
        verbose_name_plural = "WMS Services"


class RemoteWFS(Resource, ResourceBaseRemoteServiceMixin):
    """
    A WFS service.
    """

    class Meta:
        verbose_name = "WFS Service"
        verbose_name_plural = "WFS Services"
