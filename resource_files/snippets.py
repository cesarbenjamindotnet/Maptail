from wagtail.snippets.models import register_snippet
from .models import (PointVectorLayerFile, LineStringVectorLayerFile, PolygonVectorLayerFile, MultiPointVectorLayerFile,
                     MultiPolygonVectorLayerFile, MultiLineStringVectorLayerFile)
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, TabbedInterface, ObjectList, AdminPageChooser, TitleFieldPanel
from wagtail.snippets.views.snippets import SnippetViewSet
from django_json_widget.widgets import JSONEditorWidget
from resource_attrs.models import ResourceCategory

from django.utils.functional import cached_property
from wagtail.admin.ui.tables import (
    BulkActionsCheckboxColumn,
    Column,
    DateColumn,
    # InlineActionsTable,
    LiveStatusTagColumn,
    TitleColumn,
    UserColumn,
)


@register_snippet
class PointVectorLayerFileSnippetViewSet(SnippetViewSet):
    model = PointVectorLayerFile
    menu_label = "Point Vector Layer Files"
    # list_display = ("uuid", "layer", "kind", "status_string")
    add_to_admin_menu = False
    search_fields = ("name",)
    list_filter = ("kind",)

    @cached_property
    def list_display(self):
        # list_display = super().list_display.copy()
        list_display = ["uuid", "layer", "kind"]
        if self.draftstate_enabled:
            list_display.append(LiveStatusTagColumn())
        return list_display

    panels = [
        FieldPanel('uuid', read_only=True),
        FieldPanel('file'),
        FieldPanel('kind', read_only=True),
        FieldPanel('layer'),
    ]


@register_snippet
class LineStringVectorLayerFileSnippetViewSet(SnippetViewSet):
    model = LineStringVectorLayerFile
    menu_label = "LineString Vector Layer Files"
    # list_display = ("uuid", "layer", "kind", "status_string")
    add_to_admin_menu = False
    search_fields = ("name",)
    list_filter = ("kind",)

    @cached_property
    def list_display(self):
        # list_display = super().list_display.copy()
        list_display = ["uuid", "layer", "kind"]
        if self.draftstate_enabled:
            list_display.append(LiveStatusTagColumn())
        return list_display

    panels = [
        FieldPanel('uuid', read_only=True),
        FieldPanel('file'),
        FieldPanel('kind', read_only=True),
        FieldPanel('layer'),
    ]


@register_snippet
class PolygonVectorLayerFileSnippetViewSet(SnippetViewSet):
    model = PolygonVectorLayerFile
    menu_label = "Polygon Vector Layer Files"
    # list_display = ("uuid", "layer", "kind", "status_string")
    add_to_admin_menu = False
    search_fields = ("name",)
    list_filter = ("kind",)

    @cached_property
    def list_display(self):
        # list_display = super().list_display.copy()
        list_display = ["uuid", "layer", "kind"]
        if self.draftstate_enabled:
            list_display.append(LiveStatusTagColumn())
        return list_display

    panels = [
        FieldPanel('uuid', read_only=True),
        FieldPanel('file'),
        FieldPanel('kind', read_only=True),
        FieldPanel('layer'),
    ]


@register_snippet
class MultiPointVectorLayerFileSnippetViewSet(SnippetViewSet):
    model = MultiPointVectorLayerFile
    menu_label = "MultiPoint Vector Layer Files"
    # list_display = ("uuid", "layer", "kind", "status_string")
    add_to_admin_menu = False
    search_fields = ("name",)
    list_filter = ("kind",)

    @cached_property
    def list_display(self):
        # list_display = super().list_display.copy()
        list_display = ["uuid", "layer", "kind"]
        if self.draftstate_enabled:
            list_display.append(LiveStatusTagColumn())
        return list_display

    panels = [
        FieldPanel('uuid', read_only=True),
        FieldPanel('file'),
        FieldPanel('kind', read_only=True),
        FieldPanel('layer'),
    ]


@register_snippet
class MultiLineStringVectorLayerFileSnippetViewSet(SnippetViewSet):
    model = MultiLineStringVectorLayerFile
    menu_label = "MultiLineString Vector Layer Files"
    # list_display = ("uuid", "layer", "kind", "status_string")
    add_to_admin_menu = False
    search_fields = ("name",)
    list_filter = ("kind",)

    @cached_property
    def list_display(self):
        # list_display = super().list_display.copy()
        list_display = ["uuid", "layer", "kind"]
        if self.draftstate_enabled:
            list_display.append(LiveStatusTagColumn())
        return list_display

    panels = [
        FieldPanel('uuid', read_only=True),
        FieldPanel('file'),
        FieldPanel('kind', read_only=True),
        FieldPanel('layer'),
    ]


@register_snippet
class MultiPolygonVectorLayerFileSnippetViewSet(SnippetViewSet):
    model = MultiPolygonVectorLayerFile
    menu_label = "MultiPolygon Vector Layer Files"
    # list_display = ("uuid", "layer", "kind", "status_string")
    add_to_admin_menu = False
    search_fields = ("name",)
    list_filter = ("kind",)

    @cached_property
    def list_display(self):
        # list_display = super().list_display.copy()
        list_display = ["uuid", "layer", "kind"]
        if self.draftstate_enabled:
            list_display.append(LiveStatusTagColumn())
        return list_display

    panels = [
        FieldPanel('uuid', read_only=True),
        FieldPanel('file'),
        FieldPanel('kind', read_only=True),
        FieldPanel('layer'),
    ]
