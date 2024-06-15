from django.contrib import admin
from .models import (DatasetMetadataDateType, DatasetMetadataLanguage, DatasetMetadataLicense,
                     DatasetMetadataMaintenanceFrequency, DatasetMetadataRegion, DatasetMetadataRestrictionCodeType,
                     DatasetMetadataSpatialRepresentationType, DatasetMetadataTopicCategory)

# Register your models here.

admin.site.register(DatasetMetadataDateType)
admin.site.register(DatasetMetadataLanguage)
admin.site.register(DatasetMetadataLicense)
admin.site.register(DatasetMetadataMaintenanceFrequency)
admin.site.register(DatasetMetadataRegion)
admin.site.register(DatasetMetadataRestrictionCodeType)
admin.site.register(DatasetMetadataSpatialRepresentationType)
admin.site.register(DatasetMetadataTopicCategory)
