import logging
import json
from pygeoapi.provider.base import BaseProvider, ProviderItemNotFoundError
from features.models import Point  # Importa tus modelos aquí
from features.serializers import PointGeoFeatureSerializer  # Importa tus serializadores aquí

LOGGER = logging.getLogger(__name__)


class WagtailProvider(BaseProvider):
    def __init__(self, provider_def):
        super().__init__(provider_def)
        self.layer_id = provider_def.get('layer_id')

    def _get_queryset(self):
        # Filtra los datos por el ID de la capa
        return Point.objects.filter(layer_id=self.layer_id)

    def query(self, offset=0, limit=10, resulttype='results', bbox=[], datetime_=None, properties=[], sortby=[], select_properties=[], skip_geometry=False, q=None, **kwargs):
        queryset = self._get_queryset()
        total_count = queryset.count()
        queryset = queryset[offset:offset + limit]
        serializer = PointGeoFeatureSerializer(queryset, many=True)

        serializer.data['numberMatched'] = total_count
        serializer.data['numberReturned'] = len(serializer.data['features'])


        # Convierte los datos a JSON
        json_data = json.dumps(serializer.data)
        print("json_data", json_data)
        return json.loads(json_data)

    def get(self, identifier, **kwargs):
        try:
            instance = Point.objects.get(id=identifier)
            serializer = PointGeoFeatureSerializer(instance)
            return serializer.data
        except Point.DoesNotExist:
            raise ProviderItemNotFoundError(f'Item {identifier} not found')

    def create(self, new_feature):
        serializer = PointGeoFeatureSerializer(data=new_feature)
        if serializer.is_valid():
            serializer.save()
        else:
            raise ValueError('Invalid data')

    def update(self, identifier, new_feature):
        try:
            instance = Point.objects.get(id=identifier)
            serializer = PointGeoFeatureSerializer(instance, data=new_feature)
            if serializer.is_valid():
                serializer.save()
            else:
                raise ValueError('Invalid data')
        except Point.DoesNotExist:
            raise ProviderItemNotFoundError(f'Item {identifier} not found')

    def delete(self, identifier):
        try:
            instance = Point.objects.get(id=identifier)
            instance.delete()
        except Point.DoesNotExist:
            raise ProviderItemNotFoundError(f'Item {identifier} not found')

    def __repr__(self):
        return f'<WagtailProvider> layer_id={self.layer_id}'