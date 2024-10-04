from wagtail.snippets.models import register_snippet
from .models import PointVectorLayer, LineStringVectorLayer, PolygonVectorLayer, MultiPointVectorLayer, MultiLineStringVectorLayer, MultiPolygonVectorLayer
from wagtail.admin.panels import FieldPanel, InlinePanel, MultipleChooserPanel, MultiFieldPanel, FieldRowPanel, TabbedInterface, ObjectList, AdminPageChooser, TitleFieldPanel
from wagtail.snippets.views.snippets import SnippetViewSet
from django_json_widget.widgets import JSONEditorWidget
from .widgets import CustomOSMWidget


class VectorLayerSnippetViewSet(SnippetViewSet):
    add_to_admin_menu = False
    search_fields = ("name", "description", "category", "abstract", "purpose")
    list_filter = ("category", "topic_category", "license", "language", "date_type", "maintenance_frequency", "regions", "restriction_code_type", "is_featured", "is_advertised")

    main_panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('category'),
    ]

    metadata_panels = [
        FieldPanel('abstract'),
        FieldPanel('purpose'),
        FieldPanel('topic_category'),
        FieldPanel('date'),
        FieldPanel('date_type'),
        FieldPanel('edition'),
        FieldPanel('attribution'),
        FieldPanel('doi'),
        FieldPanel('maintenance_frequency'),
        FieldPanel('regions'),
        FieldPanel('restriction_code_type'),
        FieldPanel('other_constraints'),
        FieldPanel('license'),
        FieldPanel('language'),
        FieldPanel('spatial_representation_type'),
        FieldPanel('supplemental_information'),
        FieldPanel('data_quality_statement'),
    ]

    extra_panels = [
        FieldPanel('is_featured'),
        FieldPanel('is_advertised'),
        FieldPanel('thumbnail'),
    ]


@register_snippet
class PointVectorLayerSnippetViewSet(VectorLayerSnippetViewSet):
    model = PointVectorLayer
    menu_label = "Point Vector Layers"

    features_panels = [
        InlinePanel('points', panels=[
            FieldPanel('id', heading=' '),
            FieldPanel('source_file'),
            FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'data_height': 500})),
            FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
        ], min_num=0),
    ]

    files_panels = [
        InlinePanel('files', panels=[
            FieldPanel('file')
        ], min_num=0),
    ]

    edit_handler = TabbedInterface([
        ObjectList(VectorLayerSnippetViewSet.main_panels, heading='Main'),
        ObjectList(VectorLayerSnippetViewSet.metadata_panels, heading='Metadata'),
        ObjectList(VectorLayerSnippetViewSet.extra_panels, heading='Extra'),
        ObjectList(files_panels, heading='Files'),
        ObjectList(features_panels, heading='Features'),
    ])


@register_snippet
class LineStringVectorLayerSnippetViewSet(VectorLayerSnippetViewSet):
    model = LineStringVectorLayer
    menu_label = "LineString Vector Layers"

    features_panels = [
        InlinePanel('lines', panels=[
            FieldPanel('id', heading=' '),
            FieldPanel('source_file'),
            FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'data_height': 500})),
            FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
        ], min_num=0),
    ]

    files_panels = [
        InlinePanel('files', panels=[
            FieldPanel('file')
        ], min_num=0),
    ]

    edit_handler = TabbedInterface([
        ObjectList(VectorLayerSnippetViewSet.main_panels, heading='Main'),
        ObjectList(VectorLayerSnippetViewSet.metadata_panels, heading='Metadata'),
        ObjectList(VectorLayerSnippetViewSet.extra_panels, heading='Extra'),
        ObjectList(files_panels, heading='Files'),
        ObjectList(features_panels, heading='Features'),
    ])


@register_snippet
class PolygonVectorLayerSnippetViewSet(VectorLayerSnippetViewSet):
    model = PolygonVectorLayer
    menu_label = "Polygons Vector Layers"

    features_panels = [
        InlinePanel('polygons', panels=[
            FieldPanel('id', heading=' '),
            FieldPanel('source_file'),
            FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'data_height': 500})),
            FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
        ], min_num=0),
    ]

    files_panels = [
        InlinePanel('files', panels=[
            FieldPanel('file')
        ], min_num=0),
    ]

    edit_handler = TabbedInterface([
        ObjectList(VectorLayerSnippetViewSet.main_panels, heading='Main'),
        ObjectList(VectorLayerSnippetViewSet.metadata_panels, heading='Metadata'),
        ObjectList(VectorLayerSnippetViewSet.extra_panels, heading='Extra'),
        ObjectList(files_panels, heading='Files'),
        ObjectList(features_panels, heading='Features'),
    ])



@register_snippet
class MultiPointVectorLayerSnippetViewSet(VectorLayerSnippetViewSet):
    model = MultiPointVectorLayer
    menu_label = "MultiPoint Vector Layers"

    features_panels = [
        InlinePanel('multipoints', panels=[
            FieldPanel('id', heading=' '),
            FieldPanel('source_file'),
            FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'data_height': 500})),
            FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
        ], min_num=0),
    ]

    files_panels = [
        InlinePanel('files', panels=[
            FieldPanel('file')
        ], min_num=0),
    ]

    edit_handler = TabbedInterface([
        ObjectList(VectorLayerSnippetViewSet.main_panels, heading='Main'),
        ObjectList(VectorLayerSnippetViewSet.metadata_panels, heading='Metadata'),
        ObjectList(VectorLayerSnippetViewSet.extra_panels, heading='Extra'),
        ObjectList(files_panels, heading='Files'),
        ObjectList(features_panels, heading='Features'),
    ])




@register_snippet
class MultiLineStringVectorLayerSnippetViewSet(VectorLayerSnippetViewSet):
    model = MultiLineStringVectorLayer
    menu_label = "MultiLineString Vector Layers"

    features_panels = [
        InlinePanel('multilines', panels=[
            FieldPanel('id', heading=' '),
            FieldPanel('source_file'),
            FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'data_height': 500})),
            FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
        ], min_num=0),
    ]

    files_panels = [
        InlinePanel('files', panels=[
            FieldPanel('file')
        ], min_num=0),
    ]

    edit_handler = TabbedInterface([
        ObjectList(VectorLayerSnippetViewSet.main_panels, heading='Main'),
        ObjectList(VectorLayerSnippetViewSet.metadata_panels, heading='Metadata'),
        ObjectList(VectorLayerSnippetViewSet.extra_panels, heading='Extra'),
        ObjectList(files_panels, heading='Files'),
        ObjectList(features_panels, heading='Features'),
    ])


@register_snippet
class MultiPolygonVectorLayerSnippetViewSet(VectorLayerSnippetViewSet):
    model = MultiPolygonVectorLayer
    menu_label = "MultiPolygons Vector Layers"

    features_panels = [
        InlinePanel('multipolygons', panels=[
            FieldPanel('id', heading=' '),
            FieldPanel('source_file'),
            FieldPanel('geom', widget=CustomOSMWidget(attrs={'map_width': 800, 'data_height': 500})),
            FieldPanel('data', widget=JSONEditorWidget(options={}, width="800px")),
        ], min_num=0),
    ]

    files_panels = [
        InlinePanel('files', panels=[
            FieldPanel('file')
        ], min_num=0),
    ]

    edit_handler = TabbedInterface([
        ObjectList(VectorLayerSnippetViewSet.main_panels, heading='Main'),
        ObjectList(VectorLayerSnippetViewSet.metadata_panels, heading='Metadata'),
        ObjectList(VectorLayerSnippetViewSet.extra_panels, heading='Extra'),
        ObjectList(files_panels, heading='Files'),
        ObjectList(features_panels, heading='Features'),
    ])
