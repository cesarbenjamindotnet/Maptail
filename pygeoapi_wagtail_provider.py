import logging
from pygeoapi.provider.base import BaseProvider, ProviderItemNotFoundError
from resources.models import Resource

LOGGER = logging.getLogger(__name__)

class DynamicProvider(BaseProvider):
    def __init__(self, provider_def):
        super().__init__(provider_def)

    def _get_resources(self):
        return Resource.objects.all()

    def query(self, collection_id=None, offset=0, limit=10, resulttype='results', bbox=[], datetime_=None, properties=[], sortby=[],
              select_properties=[], skip_geometry=False, q=None, **kwargs):
        if not collection_id:
            raise ProviderItemNotFoundError('collection_id is required')

        try:
            resource = Resource.objects.get(id=collection_id)
        except Resource.DoesNotExist:
            raise ProviderItemNotFoundError(f'Resource with id {collection_id} not found')

        features = resource.get_real_instance().features.all()[offset:offset + limit]
        total_count = resource.get_real_instance().features.count()

        feature_list = []
        for feature in features:
            feature_list.append({
                'type': 'Feature',
                'id': feature.id,
                'geometry': feature.geom,  # Asumiendo que cada feature tiene un campo geom
                'properties': {
                    'name': feature.title,
                    'description': feature.description,
                }
            })

        return {
            'type': 'FeatureCollection',
            'features': feature_list,
            'numberMatched': total_count,
            'numberReturned': len(feature_list)
        }

    def get(self, collection_id=None, identifier=None, **kwargs):
        if not collection_id:
            raise ProviderItemNotFoundError('collection_id is required')

        try:
            resource = Resource.objects.get(id=collection_id)
            feature = resource.get_real_instance().features.get(id=identifier)
        except Resource.DoesNotExist:
            raise ProviderItemNotFoundError(f'Resource with id {collection_id} not found')
        except resource.get_real_instance().features.model.DoesNotExist:
            raise ProviderItemNotFoundError(f'Feature with id {identifier} not found')

        return {
            'type': 'Feature',
            'id': feature.id,
            'geometry': feature.geom,  # Asumiendo que cada feature tiene un campo geom
            'properties': {
                'name': feature.title,
                'description': feature.description,
            }
        }

    def get_collections(self):
        resources = self._get_resources()
        collections = []

        for resource in resources:
            collection = {
                'id': resource.id,
                'title': resource.title,
                'description': resource.description,
                'keywords': [resource.category.title],
                'extents': {
                    'spatial': {
                        'bbox': [-180, -90, 180, 90],
                        'crs': 'http://www.opengis.net/def/crs/OGC/1.3/CRS84'
                    }
                }
            }
            collections.append(collection)

        return collections

    def __repr__(self):
        return '<DynamicProvider>'