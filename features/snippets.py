from wagtail.snippets.models import register_snippet
from .models import Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, GeometryCollection
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.views.snippets import SnippetViewSet
from django_json_widget.widgets import JSONEditorWidget
from .widgets import CustomOSMWidget


@register_snippet
class PointSnippetViewSet(SnippetViewSet):
    model = Point
    menu_label = "Points"
    add_to_admin_menu = False
    search_fields = ("data",)
    list_filter = ("id",)

    panels = [
        FieldPanel('layer'),
        FieldPanel('data', widget=JSONEditorWidget(options={})),
        FieldPanel('geom', widget=CustomOSMWidget),
    ]


@register_snippet
class LineStringSnippetViewSet(SnippetViewSet):
    model = LineString
    menu_label = "LineStrings"
    add_to_admin_menu = False
    search_fields = ("data",)
    list_filter = ("id",)

    panels = [
        FieldPanel('data', widget=JSONEditorWidget(options={})),
        FieldPanel('geom', widget=CustomOSMWidget),
    ]


@register_snippet
class PolygonSnippetViewSet(SnippetViewSet):
    model = Polygon
    menu_label = "Polygons"
    add_to_admin_menu = False
    search_fields = ("data",)
    list_filter = ("id",)

    panels = [
        FieldPanel('data', widget=JSONEditorWidget(options={})),
        FieldPanel('geom', widget=CustomOSMWidget),
    ]


@register_snippet
class MultiPointSnippetViewSet(SnippetViewSet):
    model = MultiPoint
    menu_label = "MultiPoints"
    add_to_admin_menu = False
    search_fields = ("data",)
    list_filter = ("id",)

    panels = [
        FieldPanel('data', widget=JSONEditorWidget(options={})),
        FieldPanel('geom', widget=CustomOSMWidget),
    ]


@register_snippet
class MultiLineStringSnippetViewSet(SnippetViewSet):
    model = MultiLineString
    menu_label = "MultiLineStrings"
    add_to_admin_menu = False
    search_fields = ("data",)
    list_filter = ("id",)

    panels = [
        FieldPanel('data', widget=JSONEditorWidget(options={})),
        FieldPanel('geom', widget=CustomOSMWidget),
    ]


@register_snippet
class MultiPolygonSnippetViewSet(SnippetViewSet):
    model = MultiPolygon
    menu_label = "MultiPolygons"
    add_to_admin_menu = False
    search_fields = ("data",)
    list_filter = ("id",)

    panels = [
        FieldPanel('data', widget=JSONEditorWidget(options={})),
        FieldPanel('geom', widget=CustomOSMWidget),
    ]


@register_snippet
class GeometryCollectionSnippetViewSet(SnippetViewSet):
    model = GeometryCollection
    menu_label = "GeometryCollections"
    add_to_admin_menu = False
    search_fields = ("data",)
    list_filter = ("id",)

    panels = [
        FieldPanel('data', widget=JSONEditorWidget(options={})),
        FieldPanel('geom', widget=CustomOSMWidget),
    ]
