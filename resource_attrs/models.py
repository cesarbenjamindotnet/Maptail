from django.db import models
from base.mixins import LockableWorkFlowDraftStateRevisionModelBaseMixin
from autoslug import AutoSlugField

# Create your models here.


class ResourceBaseModelMixin(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', always_update=True, unique=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class ResourceCategory(ResourceBaseModelMixin):
    """
    Categories for resources.
    """

    class Meta:
        verbose_name = "Resource Category"
        verbose_name_plural = "Resource attrs: Resource Categories"
        ordering = ['name']
