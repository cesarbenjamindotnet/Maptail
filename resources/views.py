from django.views.generic.base import View
from django.http import JsonResponse
from django.contrib.gis.db.models import Extent
from django.db.models import Min, Max
from .models import Resource


class DynamicPygeoapiResourcesView(View):
    def get(self, request, *args, **kwargs):
        config = {
            "resources": {}
        }

        for resource in Resource.objects.all():
            config["resources"][resource.slug] = {
                "type": "collection",
                "title": resource.title,
                "description": resource.description,
                "keywords": list(resource.tags.all().values_list('name', flat=True)),
                "extents": {
                  "spatial": {
                    "bbox": resource.features.aggregate(Extent('geom'))['geom__extent'],
                    'crs': 'http://www.opengis.net/def/crs/OGC/1.3/CRS84'
                  },
                  "temporal": {
                    "begin": resource.features.aggregate(begin=Min('last_published_at'))['begin'],
                    "end": resource.features.aggregate(end=Max('last_published_at'))['end']
                  }
                },
                "providers": [
                    {
                        "type": "feature",
                        "name": "pygeoapi_wagtail_provider.WagtailProvider",
                        "data": resource.id,
                    },
                    {
                        "type": "tile",
                        "name": "elasticsearch",
                        "data": {
                            "url": "https://8408c9deeb14462e9828caee0f63a531.us-central1.gcp.cloud.es.io/{index}/_mvt/{field}/{z}/{x}/{y}",
                            "index": resource.index_name,
                            "field": "geom"
                        }
                    }
                ]
            }

        return JsonResponse(config)
