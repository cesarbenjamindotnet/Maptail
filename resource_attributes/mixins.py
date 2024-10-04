from django.db import models
from base.mixins import LockableWorkFlowDraftStateRevisionModelBaseMixin
from autoslug import AutoSlugField

# Create your mixins here.


class ResourceBaseModelMixin(LockableWorkFlowDraftStateRevisionModelBaseMixin):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', always_update=True, unique=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
