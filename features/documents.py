from elasticsearch_dsl import Document, Text, Keyword, Date, GeoPoint, GeoShape

class PointFeatureDocument(Document):
    data = Text()
    layer = Keyword()
    geom = GeoPoint()
    last_published_at = Date()

    class Index:
        name = 'point_features'

class LineStringFeatureDocument(Document):
    data = Text()
    layer = Keyword()
    geom = GeoShape()
    last_published_at = Date()

    class Index:
        name = 'linestring_features'

class PolygonFeatureDocument(Document):
    data = Text()
    layer = Keyword()
    geom = GeoShape()
    last_published_at = Date()

    class Index:
        name = 'polygon_features'