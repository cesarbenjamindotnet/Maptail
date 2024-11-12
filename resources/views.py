from django.views.generic.base import View
from django.http import JsonResponse
from .models import Resource


class DynamicPygeoapiConfigView(View):
    def get(self, request, *args, **kwargs):

        config = {
            "metadata": {
                "name": "Dynamic PyGeoAPI",
                "description": "Django-powered dynamic configuration for pygeoapi",
                "api_version": "1.0.0"
            },
            "resources": {}
        }

        for resource in Resource.objects.all():
            config["resources"][resource.title] = {
                "type": "collection",
                "title": resource.title,
                "description": resource.description,
                "keywords": resource.tags.all().values_list('name', flat=True),
                "providers": {
                    "name": "pygeoapi_providers.DjangoResourceProvider",
                    "data": resource.id
                }
            }

        return JsonResponse(config)
mm