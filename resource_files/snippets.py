from cgitb import handler

from wagtail.snippets.models import register_snippet
from .models import (ResourcePointsFile, )
# from .models import (ResourcePointsFile, LineStringVectorLayerFile, PolygonVectorLayerFile, MultiPointVectorLayerFile, MultiPolygonVectorLayerFile, MultiLineStringVectorLayerFile)

from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, TabbedInterface, ObjectList, \
    AdminPageChooser, TitleFieldPanel, MultipleChooserPanel
from wagtail.admin.forms.collections import CollectionChoiceField

from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from django_json_widget.widgets import JSONEditorWidget
from resource_attributes.models import ResourceCategory
from django.utils.translation import gettext_lazy as _
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

from resources.models import PointVectorLayer
from wagtail.admin.forms import WagtailAdminModelForm
from .forms import NewResourcePointsFileForm, EditResourcePointsFileForm

#


class ResourcePointsFileSnippetViewSet(SnippetViewSet):
    model = ResourcePointsFile
    menu_label = "Point Vector Layer Files"
    add_to_admin_menu = False
    search_fields = ("title", "layer",)
    list_filter = ("layer", "collection", "uploaded_by_user")

    def get_form_class(self, for_update=False):
        if for_update:
            return EditResourcePointsFileForm
        return NewResourcePointsFileForm

    panels = [
        FieldPanel('collection'),
        FieldPanel('title'),
        FieldPanel('file'),
        FieldPanel('layer'),
    ]


class LayerFilesSnippetViewSetGroup(SnippetViewSetGroup):
    items = [ResourcePointsFileSnippetViewSet]
    menu_icon = "folder-open-inverse"
    menu_label = "Source Data Files"
    menu_name = "data-files"


"""
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
        list_display = ["id", "layer", "kind"]
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
        list_display = ["id", "layer", "kind"]
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
        list_display = ["id", "layer", "kind"]
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
        list_display = ["id", "layer", "kind"]
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
        list_display = ["id", "layer", "kind"]
        if self.draftstate_enabled:
            list_display.append(LiveStatusTagColumn())
        return list_display

    panels = [
        FieldPanel('uuid', read_only=True),
        FieldPanel('file'),
        FieldPanel('kind', read_only=True),
        FieldPanel('layer'),
    ]
"""
