import fiona
from fiona.transform import transform_geom
from django.core.exceptions import ValidationError
import os
from django.conf import settings
from django.contrib.gis.geos import GEOSGeometry
import json
from shapely.geometry import shape


# TODO: Create a function that will take a file and readit using fiona to get the crs and convert the data to data able to store in geom field on geodjango

def get_data_from_file(file):
    pass
    # with fiona.open(file) as src:
    #     crs = src.crs
    #     for feature in src:
    #         feature = feature
    #         break
    #     return crs, feature


# TODO: create a function to store data in a geodjango model


def get_spatial_data_features(file):
    try:
        file_ext = file.split('.').pop()
        if file_ext in ['zip']:
            with open(file, 'rb') as disk_file:
                with fiona.io.ZipMemoryFile(disk_file) as mem_file:
                    layers = mem_file.listlayers()
                    layer = mem_file.open(layer=layers.pop())
                    for feature in layer:
                        yield feature, layer.crs
        elif file_ext in ['gpkg', 'geojson']:
            with fiona.open(file) as layer:
                for feature in layer:
                    yield feature, layer.crs
        else:
            raise ValidationError("Invalid format file")
    except Exception as e:
        if hasattr(e, 'message'):
            raise ValidationError(e.message)
        else:
            raise ValidationError(e)


def store_layer_data(file, layer, model):
    try:
        print("store_layer_data file", file)
        print("store_layer_data layer", layer)
        print("store_layer_data model", model)

        if not model.objects.filter(layer=layer, file_uuid=file.uuid).exists():
            for feature, crs in get_spatial_data_features(file.file.path):
                properties = dict(feature['properties'])
                reprojected_geometry = transform_geom(crs, settings.DATA_FEATURES_SRID, feature['geometry'])
                shapely_geometry = shape(reprojected_geometry)
                print("store_layer_data file", dir(file))

                new_feature = model(layer=layer, file_uuid=file.uuid, geom=shapely_geometry.wkt, data=properties)
                new_feature.save()
                print("new_feature", new_feature)

    except Exception as e:
        if hasattr(e, 'message'):
            raise ValidationError(e.message)
        else:
            raise ValidationError(e)


def uuid_file_path(instance, filename):
    """
    Returns the file path for the FileField upload_to parameter,
    using the UUID of the instance as the filename.
    """
    print("uuid_file_path")
    ext = filename.split('.').pop()
    print("ext", ext)
    if not ext:
        raise ValidationError("El archivo debe tener extensión")
    filename = f"{instance.layer.uuid}--{instance.uuid}.{ext}"
    print("filename", filename)
    file_path = os.path.join('resource_files/', filename)
    print("file_path", file_path)
    return file_path


def validate_point_vector_file(file):
    print("validate_point_vector_file", file)
    try:
        if file.name.split('.').pop() in ['gpkg', 'geojson']:
            with fiona.open(file) as file:
                if file.schema['geometry'] not in ['Point']:
                    raise ValidationError("Invalid geometry")
        elif file.name.split('.').pop() in ['zip']:
            with fiona.io.ZipMemoryFile(file) as memfile:
                layers = memfile.listlayers()
                layer = memfile.open(layer=layers.pop())
                if layer.schema['geometry'] not in ['Point']:
                    raise ValidationError("Invalid geometry")
        else:
            raise ValidationError("Invalid format file")
    except Exception as e:
        if hasattr(e, 'message'):
            raise ValidationError(e.message)
        else:
            raise ValidationError(e)
