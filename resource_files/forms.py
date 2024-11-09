from wagtail.admin.forms.collections import CollectionChoiceField, SelectWithDisabledOptions
from wagtail.models import Collection
from wagtail.admin.forms import WagtailAdminModelForm
from wagtail.snippets.widgets import AdminSnippetChooser
from django import forms
from resources.models import PointVectorLayer
from .models import ResourcePointsFile

#


class NewResourcePointsFileForm(WagtailAdminModelForm):
    collection = CollectionChoiceField(
        queryset=Collection.objects.all(),
        widget=SelectWithDisabledOptions,
    )
    layer = forms.ModelChoiceField(
        queryset=PointVectorLayer.objects.all(),
        widget=AdminSnippetChooser(PointVectorLayer)
    )

    class Meta:
        model = ResourcePointsFile
        fields = ['collection', 'title', 'file', 'layer']


class EditResourcePointsFileForm(WagtailAdminModelForm):
    collection = CollectionChoiceField(
        queryset=Collection.objects.all(),
        widget=SelectWithDisabledOptions,
    )

    class Meta:
        model = ResourcePointsFile
        fields = ['collection', 'title']
