from django.contrib.gis.db import models
from wagtail.models import RevisionMixin, LockableMixin, DraftStateMixin, WorkflowMixin, Orderable
from django.conf import settings


class LockableWorkFlowDrafStateRevisionModelBaseAbstract(LockableMixin, WorkflowMixin, DraftStateMixin, RevisionMixin, models.Model):
    class Meta:
        abstract = True


class LockableRevisionOrderableModelBaseAbstract(LockableMixin, RevisionMixin, Orderable):
    class Meta:
        abstract = True


LockableWorkFlowDraftStateRevisionModelBaseMixin = LockableWorkFlowDrafStateRevisionModelBaseAbstract if settings.ENABLE_MODELS_REVISIONS else models.Model
LockableRevisionOrderableModelBaseMixin = LockableRevisionOrderableModelBaseAbstract if settings.ENABLE_MODELS_REVISIONS else Orderable