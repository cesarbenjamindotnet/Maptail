from wagtail.snippets.models import register_snippet
from .models import PointVectorLayerFile
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, TabbedInterface, ObjectList, AdminPageChooser, TitleFieldPanel
from wagtail.snippets.views.snippets import SnippetViewSet
from django_json_widget.widgets import JSONEditorWidget
from resource_attrs.models import ResourceCategory

from django.utils.functional import cached_property
from wagtail.admin.ui.tables import (
    BulkActionsCheckboxColumn,
    Column,
    DateColumn,
    InlineActionsTable,
    LiveStatusTagColumn,
    TitleColumn,
    UserColumn,
)


@register_snippet
class PointVectorLayerSnippetViewSet(SnippetViewSet):
    model = PointVectorLayerFile
    menu_label = "Point Vector Layers"
    # list_display = ("uuid", "layer", "kind", "status_string")
    add_to_admin_menu = False
    search_fields = ("name",)
    list_filter = ("kind",)

    @cached_property
    def list_display(self):
        # list_display = super().list_display.copy()
        list_display = ["id", "uuid", "layer", "kind"]
        if self.draftstate_enabled:
            list_display.append(LiveStatusTagColumn())
        return list_display

    panels = [
        FieldPanel('uuid', read_only=True),
        FieldPanel('file'),
        FieldPanel('kind', read_only=True),
        FieldPanel('layer'),
    ]

