# from wagtail.snippets.models import register_snippet
from .models import Feature, Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from django_json_widget.widgets import JSONEditorWidget
from .widgets import CustomOSMWidget
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


class FeatureSnippetViewSet(SnippetViewSet):
    model = Feature
    menu_label = "All Features"
    add_to_admin_menu = False
    search_fields = ("data", "layer",)
    list_filter = ("layer", "source_file",)

    panels = [
        # FieldPanel('layer'),
        # FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'map_height': 500})),
        FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
        FieldPanel('source_file', read_only=True),
    ]


class PointSnippetViewSet(SnippetViewSet):
    model = Point
    menu_label = "Points"
    add_to_admin_menu = False
    search_fields = ("data", "layer",)
    list_filter = ("layer", "source_file",)

    panels = [
        FieldPanel('layer'),
        FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'map_height': 500})),
        FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
        FieldPanel('source_file', read_only=True),
    ]


class LineStringSnippetViewSet(SnippetViewSet):
    model = LineString
    menu_label = "LineStrings"
    add_to_admin_menu = False
    search_fields = ("data", "layer",)
    list_filter = ("layer", "source_file",)

    panels = [
        FieldPanel('layer'),
        FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'map_height': 500})),
        FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
        FieldPanel('source_file', read_only=True),
    ]


class PolygonSnippetViewSet(SnippetViewSet):
    model = Polygon
    menu_label = "Polygons"
    add_to_admin_menu = False
    search_fields = ("data", "layer",)
    list_filter = ("layer", "source_file",)

    panels = [
        FieldPanel('layer'),
        FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'map_height': 500})),
        FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
        FieldPanel('source_file', read_only=True),
    ]


class MultiPointSnippetViewSet(SnippetViewSet):
    model = MultiPoint
    menu_label = "MultiPoints"
    add_to_admin_menu = False
    search_fields = ("data", "layer",)
    list_filter = ("layer", "source_file",)

    panels = [
        FieldPanel('layer'),
        FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'map_height': 500})),
        FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
        FieldPanel('source_file', read_only=True),
    ]


class MultiLineStringSnippetViewSet(SnippetViewSet):
    model = MultiLineString
    menu_label = "MultiLineStrings"
    add_to_admin_menu = False
    search_fields = ("data", "layer",)
    list_filter = ("layer", "source_file",)

    panels = [
        FieldPanel('layer'),
        FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'map_height': 500})),
        FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
        FieldPanel('source_file', read_only=True),
    ]


class MultiPolygonSnippetViewSet(SnippetViewSet):
    model = MultiPolygon
    menu_label = "MultiPolygons"
    add_to_admin_menu = False
    search_fields = ("data", "layer",)
    list_filter = ("layer", "source_file",)

    panels = [
        FieldPanel('layer'),
        FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'map_height': 500})),
        FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
        FieldPanel('source_file', read_only=True),
    ]


class FeaturesSnippetViewSetGroup(SnippetViewSetGroup):
    items = [FeatureSnippetViewSet, PointSnippetViewSet, LineStringSnippetViewSet, PolygonSnippetViewSet,
             MultiPointSnippetViewSet, MultiLineStringSnippetViewSet, MultiPolygonSnippetViewSet]
    menu_icon = "folder-open-inverse"
    menu_label = "Features"
    menu_name = "features"


"""
@register_snippet
class LineStringSnippetViewSet(SnippetViewSet):
    model = LineString
    menu_label = "LineStrings"
    add_to_admin_menu = False
    search_fields = ("data",)
    list_filter = ("id",)

    panels = [
        FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
        FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'map_height': 500})),
    ]


@register_snippet
class PolygonSnippetViewSet(SnippetViewSet):
    model = Polygon
    menu_label = "Polygons"
    add_to_admin_menu = False
    search_fields = ("data",)
    list_filter = ("id",)

    panels = [
        FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
        FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'map_height': 500})),
    ]


@register_snippet
class MultiPointSnippetViewSet(SnippetViewSet):
    model = MultiPoint
    menu_label = "MultiPoints"
    add_to_admin_menu = False
    search_fields = ("data",)
    list_filter = ("id",)

    panels = [
        FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
        FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'map_height': 500})),
    ]


@register_snippet
class MultiLineStringSnippetViewSet(SnippetViewSet):
    model = MultiLineString
    menu_label = "MultiLineStrings"
    add_to_admin_menu = False
    search_fields = ("data",)
    list_filter = ("id",)

    panels = [
        FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
        FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'map_height': 500})),
    ]


@register_snippet
class MultiPolygonSnippetViewSet(SnippetViewSet):
    model = MultiPolygon
    menu_label = "MultiPolygons"
    add_to_admin_menu = False
    search_fields = ("data",)
    list_filter = ("id",)

    panels = [
        FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
        FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'map_height': 500})),
    ]


@register_snippet
class GeometryCollectionSnippetViewSet(SnippetViewSet):
    model = GeometryCollection
    menu_label = "GeometryCollections"
    add_to_admin_menu = False
    search_fields = ("data",)
    list_filter = ("id",)

    panels = [
        FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
        FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'map_height': 500})),
    ]
"""
