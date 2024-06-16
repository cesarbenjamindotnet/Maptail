from wagtail.snippets.models import register_snippet
from .models import PointVectorLayer, RasterLayer, DataTable, RemoteWMS, RemoteWFS
from wagtail.admin.panels import FieldPanel, InlinePanel, MultipleChooserPanel, MultiFieldPanel, FieldRowPanel, TabbedInterface, ObjectList, AdminPageChooser, TitleFieldPanel
from wagtail.snippets.views.snippets import SnippetViewSet
from django_json_widget.widgets import JSONEditorWidget
from .widgets import CustomOSMWidget
from resource_attrs.models import ResourceCategory


@register_snippet
class PointVectorLayerSnippetViewSet(SnippetViewSet):
    model = PointVectorLayer
    menu_label = "Point Vector Layers"

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

    files_panels = [
        InlinePanel('files', panels=[
            FieldPanel('file')
        ], min_num=0),
    ]

    extra_panels = [
        FieldPanel('is_featured'),
        FieldPanel('is_advertised'),
        FieldPanel('thumbnail'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(main_panels, heading='Main'),
        ObjectList(metadata_panels, heading='Metadata'),
        ObjectList(files_panels, heading='Files'),
        ObjectList(extra_panels, heading='Extra'),
    ])
